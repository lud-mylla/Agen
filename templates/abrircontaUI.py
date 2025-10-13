import streamlit as st
from views import View
import time

class AbrirContaUI:
    @staticmethod
    def main():
        st.header("Abrir Conta no Sistema")
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o email")
        fone = st.text_input("Informe o telefone")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Inserir"):
            View.cliente_inserir(nome, email, fone, senha)
            st.success("Conta criada com sucesso!")
            time.sleep(1)
            st.rerun()
