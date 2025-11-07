import streamlit as st
import time
from view import View


class ConfirmarServicoUI:
    @staticmethod
    def main():
        st.header("Confirmar Serviço")

        profissional = View.profissional_listar_id(st.session_state.get("usuario_id"))
        if profissional is None:
            st.warning("Nenhum profissional logado.")
            return

        horarios = View.horario_listar()
        if not horarios:
            st.info("Nenhum horário cadastrado.")
            return

        horarios_profissional = [
            h for h in horarios
            if h.get_id_profissional() == profissional.get_id()
            and h.get_id_cliente() is not None
        ]

        if not horarios_profissional:
            st.info("Você não possui horários agendados com clientes.")
            return


        op = st.selectbox(
            "Informe o horário",
            horarios_profissional,
            format_func=lambda h: (
                f"{h.get_id()} - {h.get_data().strftime('%d/%m/%Y %H:%M')} - {h.get_confirmado()}"
            )
        )

        
        cliente = View.cliente_listar_id(op.get_id_cliente())
        clientes_op = [cliente] if cliente else []

        cliente_selecionado = st.selectbox(
            "Cliente",
            clientes_op,
            format_func=lambda c: (
                f"{c.get_id()} - {c.get_nome()} - {c.get_email()} - {c.get_fone()}"
            )
        )

        
        if st.button("Confirmar"):
            View.horario_atualizar(
                op.get_id(),
                op.get_data(),
                True,
                op.get_id_cliente(),
                op.get_id_servico(),
                op.get_id_profissional()
            )
            st.success("Serviço confirmado com sucesso!")
            time.sleep(2)
            st.rerun()
