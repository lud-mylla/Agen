import streamlit as st
from datetime import datetime

from view import View  # Certifique-se que a View tem os métodos para Profissional

class ManterProfissionalUI:
    @staticmethod
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            ManterProfissionalUI.listar()
        with tab2:
            ManterProfissionalUI.inserir()
        with tab3:
            ManterProfissionalUI.atualizar()
        with tab4:
            ManterProfissionalUI.excluir()

    @staticmethod
    def listar():
        profissionais = View.profissional_listar()
        if not profissionais:
            st.write("Nenhum profissional cadastrado.")
            return

        for prof in profissionais:
            st.markdown(f"## Profissional ID: {prof.get_id()}")
            st.write("Nome:", prof.get_nome())
            st.write("Email:", prof.get_email())
            st.write("Telefone:", prof.get_fone())
            st.markdown("---")

    @staticmethod
    def inserir():
        nome = st.text_input("Nome do profissional")
        email = st.text_input("Email")
        fone = st.text_input("Telefone")

        if st.button("Inserir"):
            if not nome.strip():
                st.error("Nome é obrigatório.")
                return
            View.profissional_inserir(nome, email, fone)
            st.success("Profissional inserido com sucesso.")

    @staticmethod
    def atualizar():
        profissionais = View.profissional_listar()
        if not profissionais:
            st.write("Nenhum profissional cadastrado.")
            return

        op = st.selectbox(
            "Selecione um profissional para atualizar",
            profissionais,
            format_func=lambda p: f"{p.get_id()} - {p.get_nome()}"
        )

        nome = st.text_input("Novo nome", op.get_nome())
        email = st.text_input("Novo email", op.get_email())
        fone = st.text_input("Novo telefone", op.get_fone())

        if st.button("Atualizar"):
            if not nome.strip():
                st.error("Nome é obrigatório.")
                return
            View.profissional_atualizar(op.get_id(), nome, email, fone)
            st.success("Profissional atualizado com sucesso.")

    @staticmethod
    def excluir():
        profissionais = View.profissional_listar()
        if not profissionais:
            st.write("Nenhum profissional cadastrado.")
            return

        op = st.selectbox(
            "Selecione um profissional para excluir",
            profissionais,
            format_func=lambda p: f"{p.get_id()} - {p.get_nome()}"
        )

        if st.button("Excluir"):
            View.profissional_excluir(op.get_id())
            st.success("Profissional excluído com sucesso.")
            # Opcional: pausa para mostrar mensagem e recarregar
            import time
            time.sleep(2)
            st.experimental_rerun()
