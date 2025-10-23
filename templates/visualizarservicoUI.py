import streamlit as st
import pandas as pd


def visualizarservico_UI():
    st.set_page_config(page_title="Visualizar Meus Serviços", layout="wide")

    st.title("Meus Serviços")
    st.write("Aqui você pode visualizar seus agendamentos e atendimentos realizados.")

    dados = [
        {"id": 1, "data": "2025-10-07 08:00:00", "confirmado": True,  "serviço": "Consulta", "profissional": "James"},
        {"id": 4, "data": "2025-10-07 13:00:00", "confirmado": False, "serviço": "Consulta", "profissional": "Eduardo"},
        {"id": 5, "data": "2025-10-10 09:00:00", "confirmado": False, "serviço": "Consulta", "profissional": "Eduardo"},
        {"id": 11,"data": "2025-10-14 09:00:00", "confirmado": False, "serviço": "Consulta", "profissional": "Valéria"},
    ]

 
    df = pd.DataFrame(dados)

    st.dataframe(df, use_container_width=True)

  
    st.divider()

    total = len(df)
    confirmados = df["confirmado"].sum()
    pendentes = total - confirmados

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Serviços", total)
    with col2:
        st.metric("Confirmados", confirmados)
    with col3:
        st.metric("Pendentes", pendentes)

  
    st.divider()
    profs = df["profissional"].unique().tolist()
    prof_selecionado = st.selectbox("Filtrar por profissional:", ["Todos"] + profs)

    if prof_selecionado != "Todos":
        df_filtrado = df[df["profissional"] == prof_selecionado]
        st.dataframe(df_filtrado, use_container_width=True)
    else:
        st.dataframe(df, use_container_width=True)



if __name__ == "__main__":
    visualizarservico_UI()
