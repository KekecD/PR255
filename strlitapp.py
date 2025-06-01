import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pyaxis import pyaxis
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

@st.cache_data
def load_data():
    data1 = pyaxis.parse('podatki/brezaposleneCetrtletno.PX', encoding='cp1250')
    data2 = pyaxis.parse('podatki/delovnaMestaCetrtletno.PX', encoding='cp1250')
    df1 = data1['DATA']
    df2 = data2['DATA']
    return df1, df2

df, delovna_df = load_data()

st.title("Trendi brezposelnosti in prostih delovnih mest v Sloveniji")
st.markdown("Vir: SURS, četrtletni podatki (2008–2024)")

st.sidebar.header("Nastavitve")

quarters = sorted(df['ČETRTLETJE'].unique())
selected_genders = st.sidebar.multiselect("Izberi spol:", ['Moški', 'Ženske'], default=['Moški', 'Ženske'])
quarter_range = st.sidebar.slider("Izberi obdobje:", min_value=0, max_value=len(quarters)-1, value=(0, len(quarters)-1))
filtered_quarters = quarters[quarter_range[0]:quarter_range[1]+1]

st.sidebar.markdown("---") 

graph_type = st.sidebar.radio("Izberi tip grafa:", ['Črtni graf', 'Stolpčni graf'])
selected_regions = st.sidebar.multiselect("Izberi regije:", ['Vzhodna Slovenija', 'Zahodna Slovenija'], default=['Vzhodna Slovenija', 'Zahodna Slovenija'])

st.sidebar.markdown("---") 

vac = delovna_df[
    (delovna_df["MERITVE"] == "Število prostih delovnih mest  - SKUPAJ") &
    (delovna_df["SKD DEJAVNOST"] != "SKD Dejavnost - SKUPAJ [B do S]")
].copy()

vac['ČETRTLETJE'] = pd.PeriodIndex(vac['ČETRTLETJE'], freq='Q').to_timestamp()
vac["DATA"] = pd.to_numeric(vac["DATA"], errors="coerce")
vac_pivot = vac.pivot_table(index="ČETRTLETJE", columns="SKD DEJAVNOST", values="DATA")

available_industries = sorted(vac['SKD DEJAVNOST'].unique())
top_industries = vac_pivot.mean().sort_values(ascending=False).head(5).index.tolist()
selected_industries = st.sidebar.multiselect("Izberi industrije:", available_industries, default=top_industries)

st.header("1. Brezposelnost po spolu")

df_gender = df[
    (df['KOHEZIJSKA REGIJA'] == 'SLOVENIJA') &
    (df['BREZPOSELNE OSEBE'] == 'Brezposelni - SKUPAJ') &
    (df['MERITVE'] == 'Število v 1000') &
    (df['SPOL'].isin(selected_genders)) &
    (df['ČETRTLETJE'].isin(filtered_quarters))
].copy()

df_gender['ČETRTLETJE'] = pd.PeriodIndex(df_gender['ČETRTLETJE'], freq='Q').to_timestamp()
df_gender['DATA'] = pd.to_numeric(df_gender['DATA'], errors='coerce')
pivot_gender = df_gender.pivot_table(index='ČETRTLETJE', columns='SPOL', values='DATA')

fig, ax = plt.subplots(figsize=(10, 5))
pivot_gender.plot(ax=ax, title='Število brezposelnih po spolu v Sloveniji') 
ax.set_ylabel("Število oseb (v 1000)")
ax.set_xlabel("Četrtletje") 
ax.grid(True)
st.pyplot(fig)

img_buffer = io.BytesIO()
fig.savefig(img_buffer, format='png')
img_buffer.seek(0)

st.download_button("Prenesi graf kot PNG", img_buffer, file_name="brezposelnost_spol.png", mime="image/png")
st.download_button("Prenesi podatke kot CSV", df_gender.to_csv(index=False).encode('utf-8'), file_name="brezposelnost_spol.csv", mime="text/csv")

def generate_pdf():
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    flow = []

    flow.append(Paragraph("Trendi brezposelnosti po spolu", styles['Heading1']))
    flow.append(Spacer(1, 12))

    chart_path = "brezposelnost_spol.png"
    fig.savefig(chart_path)
    flow.append(Image(chart_path, width=400, height=200))

    doc.build(flow)
    buffer.seek(0)
    return buffer

if st.button("Prenesi PDF poročilo"):
    pdf = generate_pdf()
    st.download_button("Prenesi PDF", data=pdf, file_name="porocilo.pdf", mime="application/pdf")

st.header("2. Primerjava regij")

def prep_region(region):
    d = df[
        (df['KOHEZIJSKA REGIJA'] == region) &
        (df['BREZPOSELNE OSEBE'] == 'Brezposelni - SKUPAJ') &
        (df['MERITVE'] == 'Število v 1000') &
        (df['SPOL'] == 'Spol - SKUPAJ')
    ].copy()

    d['ČETRTLETJE'] = pd.PeriodIndex(d['ČETRTLETJE'], freq='Q').to_timestamp()
    d['DATA'] = pd.to_numeric(d['DATA'], errors='coerce')
    return d.pivot_table(index='ČETRTLETJE', values='DATA')

region_data = {}
for region in selected_regions:
    region_data[region] = prep_region(region)

fig, ax = plt.subplots(figsize=(12, 6))
for region, data in region_data.items():
    if graph_type == 'Črtni graf':
        ax.plot(data.index, data.values, label=region)
    else:
        ax.bar(data.index, data.values.flatten(), label=region, alpha=0.7)

ax.set_title("Brezposelnost po regijah")
ax.set_ylabel("Število (v 1000)")
ax.set_xlabel("Četrtletje")
ax.legend()
ax.grid(True)
st.pyplot(fig)

st.subheader("Povprečna brezposelnost (2008–2024)")

cols = st.columns(len(region_data))
for col, (region, data) in zip(cols, region_data.items()):
    col.metric(label=region, value=f"{data.mean().values[0]:.2f} tisoč")

st.header("3. Prosta delovna mesta po industriji")

if selected_industries:
    fig, ax = plt.subplots(figsize=(12, 6))
    vac_pivot[selected_industries].plot(ax=ax, title="Prosta delovna mesta po izbranih industrijah")
    ax.set_ylabel("Št. prostih mest")
    ax.set_xlabel("Četrtletje")
    ax.grid(True)
    ax.legend(title="Industrija")
    st.pyplot(fig)

    vac_csv = vac[vac['SKD DEJAVNOST'].isin(selected_industries)].to_csv(index=False).encode('utf-8')
    st.download_button("Prenesi CSV", vac_csv, file_name="delovna_mesta_po_industriji.csv", mime="text/csv")
else:
    st.warning("Izberi vsaj eno industrijo za prikaz.")
