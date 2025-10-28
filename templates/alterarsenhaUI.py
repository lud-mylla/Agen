
import streamlit as st
from view import View

class AlterarSenhaUI:
    @staticmethod
    def main():
        st.header("Alterar Senha (Admin)")

        if "usuario_id" not in st.session_state or st.session_state.get("usuario_tipo") != "admin":
            st.info("Apenas o admin pode acessar esta página.")
            return

        atual = st.text_input("Senha atual", type="password")
        nova = st.text_input("Nova senha", type="password")
        repete = st.text_input("Repita a nova senha", type="password")

        if st.button("Alterar senha"):
            admin = View.admin_get()
            if atual != admin["senha"]:
                st.error("Senha atual inválida.")
                return
            if nova.strip() == "":
                st.error("Senha nova não pode ser vazia.")
                return
            if nova != repete:
                st.error("As senhas não conferem.")
                return
            View.admin_atualizar(nova)
            st.success("Senha do admin atualizada com sucesso.")
