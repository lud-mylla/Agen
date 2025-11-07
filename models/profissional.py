import json

class Profissional:
    def __init__(self, id, nome, email, especialidade, conselho, senha):
        if not nome.strip():
            raise ValueError("O nome do profissional não pode ser vazio.")
        if not email.strip():
            raise ValueError("O e-mail do profissional não pode ser vazio.")
        if not senha.strip():
            raise ValueError("A senha do profissional não pode ser vazia.")

        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__especialidade = especialidade
        self.__conselho = conselho
        self.__senha = senha

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_especialidade(self): return self.__especialidade
    def get_conselho(self): return self.__conselho
    def get_senha(self): return self.__senha

    def set_id(self, id): self.__id = id

    def set_nome(self, nome):
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = nome

    def set_email(self, email):
        if not email.strip():
            raise ValueError("O e-mail não pode ser vazio.")
        self.__email = email

    def set_especialidade(self, especialidade):
        self.__especialidade = especialidade

    def set_conselho(self, conselho):
        self.__conselho = conselho

    def set_senha(self, senha):
        if not senha.strip():
            raise ValueError("A senha não pode ser vazia.")
        self.__senha = senha

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "especialidade": self.__especialidade,
            "conselho": self.__conselho,
            "senha": self.__senha
        }

    @staticmethod
    def from_json(dic):
        return Profissional(
            dic.get("id", 0),
            dic.get("nome", ""),
            dic.get("email", ""),
            dic.get("especialidade", ""),
            dic.get("conselho", ""),
            dic.get("senha", "")
        )

    def __str__(self):
        return f"{self.__id} - {self.__nome}"


class ProfissionalDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        _id = max([p.get_id() for p in cls.objetos], default=0)
        obj.set_id(_id + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux:
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux:
            cls.objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("profissional.json", "r", encoding="utf-8") as arq:
                lista = json.load(arq)
                for dic in lista:
                    cls.objetos.append(Profissional.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("profissional.json", "w", encoding="utf-8") as arq:
            json.dump([p.to_json() for p in cls.objetos], arq, ensure_ascii=False, indent=4)
