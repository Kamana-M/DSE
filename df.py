import pandas as pd
import plotly.express as px
import streamlit as st
import openpyxl

st.set_page_config(page_title="Education dashboard",page_icon="",layout="wide")

fl = st.file_uploader(":file_folder: Télécharger un fichier",type=(["csv","txt","xlsx","xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding = "ISO-8859-1")
else:
    df=pd.read_excel(
	io="Dashboard actuel.xlsx",
	engine='openpyxl',
	sheet_name='Elev_effec',
	skiprows=0,
	usecols='A:J',
	nrows=631,
)	
	
st.sidebar.header("Filtrer ici:")

annees=st.sidebar.multiselect("Selectionner une région",options=df["ANNEE_SCOLAIRE"].unique(),default=df["ANNEE_SCOLAIRE"].unique())

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

#Filtrer les données
if not annees and not Régions and not Zones and not SS and not OD and not SOD and not classe and not filtre1 and not genre:
	df_selection = df
elif not Régions and not Zones and not SS and not OD and not SOD and not classe and not filtre1 and not genre:
	df_selection = df.query("(ANNEE_SCOLAIRE==@annees)")
elif not Zones and not SS and not OD and not SOD and not classe and not filtre1 and not genre:
	df_selection = df.query("(ANNEE_SCOLAIRE==@annees) and (REGIONS==@Régions)")

st.dataframe(df_selection)

st.markdown("---")

df_selection.groupby(by=["CRITERES_1"]).sum()[["PRESCOLAIRE"]]














