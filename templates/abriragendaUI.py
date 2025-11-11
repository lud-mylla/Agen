import streamlit as st
from datetime import datetime, timedelta
from view import View 

class AbrirAgendaUI:
    @staticmethod
    def main():
        st.header("Abrir Minha Agenda")
        st.write("Preencha os campos para inserir horários de atendimento na sua agenda.")

        if "usuario_tipo" not in st.session_state or st.session_state["usuario_tipo"] != "profissional":
            st.warning("Acesso permitido apenas a profissionais.")
            return

        data = st.date_input("Dia do atendimento", datetime.now())
        hora_inicial = st.time_input("Hora inicial", value=datetime.now().time())
        hora_final = st.time_input("Hora final", value=(datetime.now() + timedelta(hours=1)).time())
        intervalo = st.number_input("Intervalo entre horários (minutos)", min_value=5, max_value=120, value=30, step=5)

        
        servicos = View.servico_listar()
        if not servicos:
            st.warning("Nenhum serviço cadastrado. Cadastre um serviço antes de abrir a agenda.")
            return

        servico = st.selectbox("Serviço oferecido", servicos, format_func=lambda s: s.get_descricao() if s else "")

        if st.button("Inserir horários na agenda"):
            profissional_id = st.session_state.get("usuario_id")

            dt_inicial = datetime.combine(data, hora_inicial)
            dt_final = datetime.combine(data, hora_final)

            if dt_inicial >= dt_final:
                st.error("A hora inicial deve ser menor que a hora final.")
                return

            horarios_criados = 0
            while dt_inicial < dt_final:
                View.horario_inserir(
                    dt_inicial,
                    False,          
                    0,              
                    servico.get_id(),
                    profissional_id
                )
                horarios_criados += 1
                dt_inicial += timedelta(minutes=intervalo)

            st.success(f"{horarios_criados} horários inseridos na agenda com sucesso!")
            if dt_inicial >= dt_final:
                st.error("A hora inicial deve ser menor que a hora final.")
                return

            horarios_criados = 0

            try:
                while dt_inicial < dt_final:
                    View.horario_inserir(
                        dt_inicial,
                        False,  # confirmado
                        0,      # id_cliente
                        servico.get_id(),
                        profissional_id
                    )
                    horarios_criados += 1
                    dt_inicial += timedelta(minutes=intervalo)

                st.success(f"{horarios_criados} horários inseridos com sucesso!")

            except ValueError as e:
                st.error(f"Erro ao inserir horários: {e}")
            except Exception as e:
                st.error(f"Ocorreu um erro inesperado: {e}")
