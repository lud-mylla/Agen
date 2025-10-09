from models.servico import Servico, ServicoDAO
from models.cliente import Cliente, ClienteDAO
from models.horarios import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO

class View:
    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()

    @staticmethod
    def cliente_inserir(nome, email, fone):
        cliente = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(cliente)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "")
        ClienteDAO.excluir(cliente)

    @staticmethod
    def servico_listar():
        return ServicoDAO.listar()

    @staticmethod
    def servico_inserir(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)

    @staticmethod
    def servico_excluir(id):
        servico = Servico(id, "", 0.0)
        ServicoDAO.excluir(servico)

    @staticmethod
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        horario = Horario(0, data)
        horario.set_confirmado(confirmado)
        horario.set_id_cliente(id_cliente)
        horario.set_id_servico(id_servico)
        horario.set_id_profissional(id_profissional)
        HorarioDAO.inserir(horario)

    @staticmethod
    def horario_listar():
        return HorarioDAO.listar()

    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        horario = Horario(id, data)
        horario.set_confirmado(confirmado)
        horario.set_id_cliente(id_cliente)
        horario.set_id_servico(id_servico)
        horario.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(horario)

    @staticmethod
    def horario_excluir(id):
        horario = HorarioDAO.listar_id(id)
        if horario:
            HorarioDAO.excluir(horario)

    @staticmethod
    def profissional_listar():
        return ProfissionalDAO.listar()

    @staticmethod
    def profissional_inserir(nome, email, fone):
        profissional = Profissional(0, nome, email, fone)
        ProfissionalDAO.inserir(profissional)

    @staticmethod
    def profissional_atualizar(id, nome, email, fone):
        profissional = Profissional(id, nome, email, fone)
        ProfissionalDAO.atualizar(profissional)

    @staticmethod
    def profissional_excluir(id):
        profissional = Profissional(id, "", "", "")
        ProfissionalDAO.excluir(profissional)
