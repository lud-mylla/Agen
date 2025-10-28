import time
from datetime import datetime, date, timedelta

import pandas as pd
import streamlit as st

from view import View


class AbrirAgendaUI:
    @staticmethod
    def main():
       
        st.header("Agenda")

        tab_listar, tab_inserir = st.tabs(["Listar", "Inserir"])
        with tab_listar:
            AbrirAgendaUI.listar()
        with tab_inserir:
            AbrirAgendaUI.inserir()

    
    @staticmethod
    def listar():
        usuario_id = st.session_state.get("usuario_id")
        profissional = View.profissional_listar_id(usuario_id)

        if not profissional:
            st.warning("Nenhum profissional logado.")
            return

        horarios_profissional = View.horario_listar_por_profissional(profissional.get_id())
        if not horarios_profissional:
            st.info("Você ainda não abriu horários na sua agenda.")
            return

        dados = []
        for obj in horarios_profissional:
            cliente = View.cliente_listar_id(obj.get_id_cliente())
            servico = View.servico_listar_id(obj.get_id_servico())

            dados.append({
                "ID": obj.get_id(),
                "Data": obj.get_data(),
                "Confirmado": obj.get_confirmado(),
                "Cliente": cliente.get_nome() if cliente else "-",
                "Serviço": servico.get_descricao() if servico else "-"
            })

        df = pd.DataFrame(dados)
        st.dataframe(df, hide_index=True)
    @staticmethod
    def inserir():
        usuario_id = st.session_state.get("usuario_id")
        profissional = View.profissional_listar_id(usuario_id)

        if not profissional:
            st.warning("Nenhum profissional logado.")
            return

        
        data_atendimento = st.date_input("Informe o dia do atendimento", date.today())
        hora_inicial = st.time_input("Hora inicial do atendimento")
        hora_final = st.time_input("Hora final do atendimento")
        intervalo = st.number_input(
            "Intervalo entre atendimentos",
            min_value=5,
            step=5
        )

        
        inicio_dt = datetime.combine(data_atendimento, hora_inicial)
        fim_dt = datetime.combine(data_atendimento, hora_final)
        if inicio_dt >= fim_dt:
            st.error("Hora final deve ser maior que hora inicial.")
            return

        
        if st.button("Gerar horários"):
            horarios_gerados = []
            inicio = inicio_dt
            while inicio < fim_dt:
                View.horario_inserir(inicio, False, None, None, profissional.get_id())
                horarios_gerados.append(inicio.strftime("%H:%M"))
                inicio += timedelta(minutes=intervalo)

            st.success(f"Foram inseridos {len(horarios_gerados)} horários na agenda")
            time.sleep(2)
            st.rerun()
