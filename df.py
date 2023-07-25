import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Education dashboard",page_icon="",layout="wide")

df=pd.read_excel(
io="Dashboard actuel.xlsx",
engine='openpyxl',
sheet_name='Elev_effec',
skiprows=0,
usecols='A:J',
nrows=631,
)

st.dataframe(df)

st.sidebar.header("Filtrer ici:")

annees=st.sidebar.multiselect(
	"Selectionner une région",
	options=df["ANNEE_SCOLAIRE"].unique(),
	default=df["ANNEE_SCOLAIRE"].unique()
	)

Régions=st.sidebar.multiselect(
	"Selectionner une région",
	options=df["REGIONS"].unique()
	)

Zones=st.sidebar.multiselect(
	"Selectionner une zone",
	options=df["ZONES"].unique()
	)

SS=st.sidebar.multiselect(
	"Selectionner un sous-système",
	options=df["SOUS_SYSTEME"].unique()
	)

OD=st.sidebar.multiselect(
	"Selectionner un ordre d'enseignement",
	options=df["ORDRE_ENSEIGENEMENT"].unique()
	)

SOD=st.sidebar.multiselect(
	"Selectionner un sous-ordre d'enseignement",
	options=df["SOUS_ORDRE_ENSEIGENEMENT"].unique()
	)

classe=st.sidebar.multiselect(
	"Selectionner une classe",
	options=df["CLASSE"].unique()
	)

filtre1=st.sidebar.multiselect(
	"Selectionner un filtre",
	options=df["FILTRE_1"].unique()
	)

genre=st.sidebar.multiselect(
	"Selectionner un genre",
	options=df["CRITERES_1"].unique()
	)

df_selection = df.query(
	"(ANNEE_SCOLAIRE==@annees) or (REGIONS==@Régions) or (ZONES==@Zones) or (SOUS_SYSTEME==@SS) or (ORDRE_ENSEIGENEMENT==@OD) or (SOUS_ORDRE_ENSEIGENEMENT==@SOD) or (CLASSE==@classe) or (FILTRE_1==@filtre1) or (CRITERES_1==@genre)"
)

st.dataframe(df_selection)

st.markdown("---")

df_selection.groupby(by=["CRITERES_1"]).sum()[["PRESCOLAIRE"]]













