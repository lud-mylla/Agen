import streamlit as st
from view import View
import time

class PerfilclientesUI:
    @staticmethod
    def main():
        st.header("Meus Dados")

        if "usuario_id" not in st.session_state:
            st.info("Nenhum usuário logado.")
            return

        uid = st.session_state["usuario_id"]
        tipo = st.session_state.get("usuario_tipo", "cliente")

        if tipo == "cliente":
            obj = View.cliente_listar_id(uid)
            if not obj:
                st.error("Cliente não encontrado.")
                return

            nome = st.text_input("Nome", obj.get_nome())
            email = st.text_input("E-mail", obj.get_email())
            fone = st.text_input("Fone", obj.get_fone())
            senha = st.text_input("Senha", obj.get_senha(), type="password")

            if st.button("Atualizar"):
                try:
                    View.cliente_atualizar(uid, nome, email, fone, senha)
                    st.success("Dados atualizados com sucesso!")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")
