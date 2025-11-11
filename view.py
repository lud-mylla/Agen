from models.cliente import Cliente, ClienteDAO
from models.profissional import Profissional, ProfissionalDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
import json

class View:
    
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        if email.lower() == "admin":
            raise ValueError("O e-mail 'admin' é reservado ao administrador.")

        for c in ClienteDAO.listar():
            if c.get_email().lower() == email.lower():
                raise ValueError("Já existe um cliente com este e-mail.")
        for p in ProfissionalDAO.listar():
            if p.get_email().lower() == email.lower():
                raise ValueError("Já existe um profissional com este e-mail.")

        c = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(c)

    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar() or []

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        if email.lower() == "admin":
            raise ValueError("O e-mail 'admin' é reservado ao administrador.")

        for c in ClienteDAO.listar():
            if c.get_email().lower() == email.lower() and c.get_id() != id:
                raise ValueError("Já existe outro cliente com este e-mail.")
        for p in ProfissionalDAO.listar():
            if p.get_email().lower() == email.lower():
                raise ValueError("Já existe um profissional com este e-mail.")

        c = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(c)

    @staticmethod
    def cliente_excluir(id):
        for h in HorarioDAO.listar():
            if h.get_id_cliente() == id:
                raise ValueError("Não é possível excluir um cliente com horários agendados.")
        c = ClienteDAO.listar_id(id)
        if c:
            ClienteDAO.excluir(c)

    @staticmethod
    def cliente_autenticar(email, senha):
        for c in ClienteDAO.listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome(), "tipo": "cliente"}
        return None

    @staticmethod
    def profissional_inserir(nome, email, especialidade, conselho, senha):
       
        if not nome.strip() or not email.strip() or not senha.strip():
            raise ValueError("Nome, e-mail e senha são obrigatórios.")
        
        if email.lower() == "admin":
            raise ValueError("O e-mail 'admin' é reservado ao administrador.")

        for p in ProfissionalDAO.listar():
            if p.get_email().lower() == email.lower():
                raise ValueError("Já existe um profissional com este e-mail.")
        for c in ClienteDAO.listar():
            if c.get_email().lower() == email.lower():
                raise ValueError("Já existe um cliente com este e-mail.")

        p = Profissional(0, nome, email, especialidade, conselho, senha)
        ProfissionalDAO.inserir(p)

    @staticmethod
    def profissional_listar():
        return ProfissionalDAO.listar() or []

    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)

    @staticmethod
    def profissional_atualizar(id, nome, email, especialidade, conselho, senha):
       
        if not nome.strip() or not email.strip() or not senha.strip():
            raise ValueError("Nome, e-mail e senha são obrigatórios.")

        if email.lower() == "admin":
            raise ValueError("O e-mail 'admin' é reservado ao administrador.")

        for p in ProfissionalDAO.listar():
            if p.get_email().lower() == email.lower() and p.get_id() != id:
                raise ValueError("Já existe outro profissional com este e-mail.")
        for c in ClienteDAO.listar():
            if c.get_email().lower() == email.lower():
                raise ValueError("Já existe um cliente com este e-mail.")

        p = Profissional(id, nome, email, especialidade, conselho, senha)
        ProfissionalDAO.atualizar(p)

    @staticmethod
    def profissional_excluir(id):
        
        for h in HorarioDAO.listar():
            if h.get_id_profissional() == id:
                raise ValueError("Não é possível excluir um profissional com horários cadastrados.")

        p = ProfissionalDAO.listar_id(id)
        if p:
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
        return ServicoDAO.listar() or []

    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        s = Servico(id, descricao, valor)
        ServicoDAO.atualizar(s)

    @staticmethod
    def servico_excluir(id):
        s = ServicoDAO.listar_id(id)
        if s:
            ServicoDAO.excluir(s)

    
    @staticmethod
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        for h in HorarioDAO.listar():
            if h.get_id_profissional() == id_profissional and h.get_data() == data:
                raise ValueError("Já existe um horário cadastrado com essa data e hora para este profissional")
        h = Horario(0, data)
        h.set_confirmado(confirmado)
        h.set_id_cliente(id_cliente)
        h.set_id_servico(id_servico)
        h.set_id_profissional(id_profissional)
        HorarioDAO.inserir(h)

    @staticmethod
    def horario_listar():
        return HorarioDAO.listar() or []
    

    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        # Validação 1 também no atualizar
        for h in HorarioDAO.listar():
            if (
                h.get_id_profissional() == id_profissional
                and h.get_data() == data
                and h.get_id() != id
            ):
                raise ValueError("Já existe outro horário com essa data e hora para este profissional.")
            
        h = Horario(id, data)
        h.set_confirmado(confirmado)
        h.set_id_cliente(id_cliente)
        h.set_id_servico(id_servico)
        h.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(h)



    @staticmethod
    def horario_excluir(id):
        h = HorarioDAO.listar_id(id)
        if not h:
            return
        if h.get_id_cliente() is not None and h.get_id_cliente() != 0:
            raise ValueError("Não é posível escluir um horário que ja foi agendado por um cliente")
        

        HorarioDAO.excluir(h)

    @staticmethod
    def admin_get():
        try:
            with open("admin.json", "r", encoding="utf-8") as arq:
                return json.load(arq)
        except FileNotFoundError:
            return {"senha": "1234"}

    @staticmethod
    def admin_atualizar(nova_senha):
        with open("admin.json", "w", encoding="utf-8") as arq:
            json.dump({"senha": nova_senha}, arq, ensure_ascii=False, indent=4)
            