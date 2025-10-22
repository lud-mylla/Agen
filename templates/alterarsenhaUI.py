
# templates/alterarsenhaUI.py
import streamlit as st
import time
from view import View  

class AlterarSenhaUI:

    @staticmethod
    def main():
        st.header("Alterar Senha")

     
        try:
            admin = View.admin_get()
        except AttributeError:
            st.error("O método admin_get() não foi encontrado na View. Atualize a View.")
            return

        
        st.text_input("Nome", value=admin["nome"], disabled=True)

        st.text_input("Email", value=admin["email"], disabled=True)

       
        senha_alterada = st.text_input("Digite a nova senha", type="password")

     
        if st.button("Alterar Senha"):
            if not senha_alterada.strip():
                st.error("Digite uma senha válida.")
            else:
             
                View.admin_atualizar(senha_alterada)
                st.success("Senha alterada!")
                time.sleep(2)
                st.rerun() 