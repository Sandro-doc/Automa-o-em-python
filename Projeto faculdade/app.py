import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração de layout ---
st.set_page_config(page_title='Análise de restaurantes de floripa', layout='wide', page_icon='🍽️')

# --- Carregamento dos dados ---
df = pd.read_csv('Restaurantes.csv')

# Ordenar DataFrame pelas notas de ordem decrescente
df = df.sort_values(by='Nota', ascending=False).reset_index(drop=True)

# Definir cor dos Graficos
colors = px.colors.qualitative.Plotly
st.markdown(f"<style>.stApp {{ background-color: {colors[0]}; }}</style>", unsafe_allow_html=True)