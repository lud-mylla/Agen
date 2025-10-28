ADMIN_SENHA = "1234"

from models.cliente import Cliente, ClienteDAO
from models.profissional import Profissional, ProfissionalDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO


class View:

    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        c = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(c)

    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(c)

    @staticmethod
    def cliente_excluir(id):
        c = Cliente(id, "", "", "", "")
        ClienteDAO.excluir(c)

    @staticmethod
    def cliente_autenticar(email, senha):
        for c in ClienteDAO.listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome(), "tipo": "cliente"}

        if email == "admin" and senha == ADMIN_SENHA:
            return {"id": 0, "nome": "Administrador", "tipo": "admin"}

        return None

    @staticmethod
    def profissional_inserir(nome, email, especialidade, conselho, senha):
        p = Profissional(0, nome, email, especialidade, conselho, senha)
        ProfissionalDAO.inserir(p)

    @staticmethod
    def profissional_listar():
        return ProfissionalDAO.listar()

    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)

    @staticmethod
    def profissional_atualizar(id, nome, email, especialidade, conselho, senha):
        p = Profissional(id, nome, email, especialidade, conselho, senha)
        ProfissionalDAO.atualizar(p)

    @staticmethod
    def profissional_excluir(id):
        p = Profissional(id, "", "", "", "", "")
        ProfissionalDAO.excluir(p)

    @staticmethod
    def profissional_autenticar(email, senha):
        for p in ProfissionalDAO.listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id": p.get_id(), "nome": p.get_nome(), "tipo": "profissional"}
        return None

    
    @staticmethod
    def servico_inserir(descricao, valor):
        s = Servico(0, descricao, valor)
        ServicoDAO.inserir(s)

    @staticmethod
    def servico_listar():
        return ServicoDAO.listar()

    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        s = Servico(id, descricao, valor)
        ServicoDAO.atualizar(s)

    @staticmethod
    def servico_excluir(id):
        s = Servico(id, "", 0)
        ServicoDAO.excluir(s)

   
    @staticmethod
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        """Insere um novo horário na agenda."""
        h = Horario(
            0,
            data,
            confirmado=confirmado,
            id_cliente=id_cliente,
            id_servico=id_servico,
            id_profissional=id_profissional
        )
        HorarioDAO.inserir(h)

    @staticmethod
    def horario_listar():
        return HorarioDAO.listar()

    @staticmethod
    def horario_listar_id(id):
        return HorarioDAO.listar_id(id)

    @staticmethod
    def horario_listar_por_profissional(id_profissional):
        """Retorna todos os horários de um profissional específico."""
        return [h for h in HorarioDAO.listar() if h.get_id_profissional() == id_profissional]

    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        h = Horario(id, data)
        h.set_confirmado(confirmado)
        h.set_id_cliente(id_cliente)
        h.set_id_servico(id_servico)
        h.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(h)

    @staticmethod
    def horario_excluir(id):
        h = HorarioDAO.listar_id(id)
        if h is not None:
            HorarioDAO.excluir(h)

    
    @staticmethod
    def admin_get():
        return {"id": 0, "nome": "Administrador", "email": "admin", "senha": ADMIN_SENHA}

    @staticmethod
    def admin_atualizar(nova_senha):
        global ADMIN_SENHA
        ADMIN_SENHA = nova_senha

    @staticmethod
    def visualizar_meus_servicos(id_cliente):
        horarios = HorarioDAO.listar()
        servicos_cliente = []

        for h in horarios:
            if h.get_id_cliente() == id_cliente:
                servico = ServicoDAO.listar_id(h.get_id_servico())
                profissional = ProfissionalDAO.listar_id(h.get_id_profissional())

                servicos_cliente.append({
                    "id": h.get_id(),
                    "data": h.get_data(),
                    "confirmado": h.get_confirmado(),
                    "serviço": servico.get_descricao() if servico else "",
                    "profissional": profissional.get_nome() if profissional else ""
                })
        return servicos_cliente
