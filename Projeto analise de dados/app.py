import streamlit as st
import pandas as pd    
import plotly.express as px 

# --- Configuração da página ---
# Define o título da página, ícone e layoutpara ocupar a largura inteira.
st.set_page_config(
    page_title="Análise de Salários na Área de Dados ",
    page_icon="📊",
    layout="wide",
)

# --- Carregamento dos dados ---
df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

# --- Barra Lateral (Filtros) ---
st.sidebar.header("Filtros")

# Filtro de Ano
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect("ano", anos_disponiveis, default=anos_disponiveis)

# Filtro de Senioridade
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionados = st.sidebar.multiselect("senioridades", senioridades_disponiveis, default=senioridades_disponiveis)

# Filtro por Tipo de Contrato
tipos_contrato_disponiveis = sorted(df['contrato'].unique())
tipos_contrato_selecionados = st.sidebar.multiselect("contrato", tipos_contrato_disponiveis, default=tipos_contrato_disponiveis)

# Filtro tamanho da empresa
tamanhos_empresa_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_empresa_selecionados = st.sidebar.multiselect("tamanho_empresa", tamanhos_empresa_disponiveis, default=tamanhos_empresa_disponiveis)

#--- Filtragem do DataFrame ---
# O dataframe principal é filtrado com base nos filtros selecionados na barra lateral.
df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionados)) &
    (df['contrato'].isin(tipos_contrato_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_empresa_selecionados))
]

# --- Conteúdo Principal ---
st.title("Análise de Salários na Área de Análise de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros na barra lateral para personalizar a visualização dos dados.")

# --- Metricas Principais (KPIs) ---
st.subheader("Métricas Principais")

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado['cargo'].mode()[0]
else:
    salario_medio, salario_mediano, salario_maximo, total_registrado, cargo_mais_comum = 0, 0, 0, ""

col1, col2, col3, col4 = st.columns(4)
col1.metric("salário médio", f"${salario_medio:,.0f}")   
col2.metric("salário máximo", f"${salario_maximo:,.0f}")
col3.metric("total de registros", f"{total_registros:,}")
col4.metric("cargo mais frequente", cargo_mais_frequente)

st.markdown("---")

# --- Análises Visuais com plotly ---
st.subheader("Gráficos")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        grafico_cargos = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            title="Top 10 Cargos por Salário Médio",
            labels={'usd': 'Média Salarial (USD)', 'cargo': ''}
        )
        grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível para exibir.")

with col_graf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram(
            df_filtrado,
            x='usd',
            nbins=30,
            title="Distribuição Salarial Anual",
            labels={'usd': 'Faixa de Salário (USD)', 'count': ''}
        )
        grafico_hist.update_layout(title_x=0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível para exibir.")

col_graf3, col_graf4 = st.columns(2)
with col_graf3:
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        grafico_remoto = px.pie(
            remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            title='Distribuição de Trabalho Remoto',
            hole=0.5,
        )
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(title_x=0.1)
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível para exibir.")


with col_graf4:
    if not df_filtrado.empty:
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
        grafico_paises = px.choropleth(media_ds_pais,
            locations='residencia_iso3',
            color='usd',
            color_continuous_scale ='Viridis',
            title='Salário Médio de Data Scientists por País',
            labels={'usd': 'Salário Médio (USD)', 'residencia_iso3': 'País'})
        grafico_paises.update_layout(title_x=0.1)
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível para exibir.")

# --- Tabela de Dados Detalhados ---
st.subheader("Tabela de Dados Detalhados")
st.dataframe(df_filtrado)
        