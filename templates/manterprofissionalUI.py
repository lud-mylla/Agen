import streamlit as st
import pandas as pd
import time
from view import View

class ManterProfissionalUI:
    @staticmethod
    def main():
        st.header("Gerenciar Profissionais")

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    @staticmethod
    def listar():
        profissionais = View.profissional_listar()
        if not profissionais:
            st.info("Nenhum profissional cadastrado.")
            return
        df = pd.DataFrame([p.to_json() for p in profissionais])
        st.dataframe(df)

    @staticmethod
    def inserir():
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        especialidade = st.text_input("Especialidade")
        conselho = st.text_input("Conselho")
        senha = st.text_input("Senha", type="password")

        if st.button("Inserir"):
            try:
                View.profissional_inserir(nome, email, especialidade, conselho, senha)
                st.success("Profissional inserido com sucesso!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {e}")

    @staticmethod
    def atualizar():
        profissionais = View.profissional_listar()
        if not profissionais:
            st.info("Nenhum profissional cadastrado.")
            return

        op = st.selectbox("Selecione o profissional", profissionais, format_func=lambda p: p.get_nome())
        nome = st.text_input("Nome", op.get_nome())
        email = st.text_input("E-mail", op.get_email())
        especialidade = st.text_input("Especialidade", op.get_especialidade())
        conselho = st.text_input("Conselho", op.get_conselho())
        senha = st.text_input("Senha", op.get_senha(), type="password")

        if st.button("Atualizar"):
            try:
                View.profissional_atualizar(op.get_id(), nome, email, especialidade, conselho, senha)
                st.success("Profissional atualizado com sucesso!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {e}")

    @staticmethod
    def excluir():
        profissionais = View.profissional_listar()
        if not profissionais:
            st.info("Nenhum profissional cadastrado.")
            return

        op = st.selectbox("Selecione o profissional para excluir", profissionais, format_func=lambda p: p.get_nome())

        if st.button("Excluir"):
            try:
                View.profissional_excluir(op.get_id())
                st.success("Profissional excluído com sucesso!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {e}")
