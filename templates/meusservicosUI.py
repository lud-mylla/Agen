import streamlit as st
import pandas as pd
from view import View

class MeusServicosUI:

    @staticmethod
    def main():
        st.header(" Meus Serviços")

        
        id_cliente = st.session_state.get("usuario_id")
        if not id_cliente:
            st.warning("Nenhum cliente logado.")
            return

        cliente = View.cliente_listar_id(id_cliente)
        if not cliente:
            st.warning("Cliente não encontrado.")
            return

  
        horarios = View.horario_listar()
        if not horarios:
            st.info("Nenhum horário cadastrado.")
            return

        horarios_cliente = [h for h in horarios if h.get_id_cliente() == cliente.get_id()]
        if not horarios_cliente:
            st.info("Você ainda não possui serviços agendados.")
            return

        
        dados = []
        for h in horarios_cliente:
            servico = View.servico_listar_id(h.get_id_servico())
            profissional = View.profissional_listar_id(h.get_id_profissional())

            dados.append({
                "ID": h.get_id(),
                "Data": h.get_data(),
                "Confirmado": " Sim" if h.get_confirmado() else "⏳ Não",
                "Serviço": servico.get_descricao() if servico else "-",
                "Profissional": profissional.get_nome() if profissional else "-"
            })

        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, hide_index=True, use_container_width=True)
        else:
            st.info("Nenhum serviço encontrado para exibir.")
