import json

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
      
        if not nome.strip():
            raise ValueError("O nome do cliente não pode ser vazio.")
        if not email.strip():
            raise ValueError("O e-mail do cliente não pode ser vazio.")
        if not senha.strip():
            raise ValueError("A senha do cliente não pode ser vazia.")

        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
        self.__senha = senha

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
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

    def set_fone(self, fone):
        self.__fone = fone

    def set_senha(self, senha):
        if not senha.strip():
            raise ValueError("A senha não pode ser vazia.")
        self.__senha = senha

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone,
            "senha": self.__senha
        }

    @staticmethod
    def from_json(dic):
        return Cliente(
            dic.get("id", 0),
            dic.get("nome", ""),
            dic.get("email", ""),
            dic.get("fone", ""),
            dic.get("senha", "")
        )

    def __str__(self):
        return f"{self.__id} - {self.__nome}"


class ClienteDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        _id = max([c.get_id() for c in cls.objetos], default=0)
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
            with open("clientes.json", "r", encoding="utf-8") as arq:
                lista = json.load(arq)
                for dic in lista:
                    cls.objetos.append(Cliente.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("clientes.json", "w", encoding="utf-8") as arq:
            json.dump(
                [c.to_json() for c in cls.objetos],
                arq,
                ensure_ascii=False,
                indent=4
            )
