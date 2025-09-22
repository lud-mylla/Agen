import json


class Servico:
    def __init__(self, id, descricao, valor):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)

    def __str__(self):
        return f"\n{self.__id} - {self.__descricao} - R$ {self.__valor:.2f}"

    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor

    def set_id(self, id): self.__id = id
    def set_descricao(self, descricao): self.__descricao = descricao
    def set_valor(self, valor): self.__valor = valor

    def to_json(self):
        return {
            "id": self.__id,
            "descricao": self.__descricao,
            "valor": self.__valor
        }

    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["descricao"], dic["valor"])



class ServicoDAO:
    __objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id:
                id = aux.get_id()
        obj.set_id(id + 1)
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("servicos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Servico.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("servicos.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default=Servico.to_json)


class ManterServicoUI:
    @staticmethod
    def menu():
        while True:
            print("\n=== Manter Serviços ===")
            print("1 - Inserir serviço")
            print("2 - Listar serviços")
            print("3 - Atualizar serviço")
            print("4 - Excluir serviço")
            print("0 - Voltar")
            opc = input("Escolha uma opção: ")
            if opc == "1":
                ManterServicoUI.inserir()
            elif opc == "2":
                ManterServicoUI.listar()
            elif opc == "3":
                ManterServicoUI.atualizar()
            elif opc == "4":
                ManterServicoUI.excluir()
            elif opc == "0":
                break
            else:
                print("Opção inválida.")

    @staticmethod
    def inserir():
        descricao = input("Descrição: ")
        valor = float(input("Valor: "))
        obj = Servico(0, descricao, valor)
        ServicoDAO.inserir(obj)
        print("✔ Serviço inserido com sucesso!")

    @staticmethod
    def listar():
        lista = ServicoDAO.listar()
        if lista:
            for obj in lista:
                print(obj)
        else:
            print("Nenhum serviço cadastrado.")

    @staticmethod
    def atualizar():
        id = int(input("ID do serviço a atualizar: "))
        obj = ServicoDAO.listar_id(id)
        if obj:
            descricao = input(f"Nova descrição [{obj.get_descricao()}]: ") or obj.get_descricao()
            valor_str = input(f"Novo valor [{obj.get_valor()}]: ")
            valor = float(valor_str) if valor_str else obj.get_valor()
            novo = Servico(id, descricao, valor)
            ServicoDAO.atualizar(novo)
            print("✔ Serviço atualizado!")
        else:
            print("✘ Serviço não encontrado.")

    @staticmethod
    def excluir():
        id = int(input("ID do serviço a excluir: "))
        obj = ServicoDAO.listar_id(id)
        if obj:
            ServicoDAO.excluir(obj)
            print("✔ Serviço excluído!")
        else:
            print("✘ Serviço não encontrado.")



class ManterClienteUI:
    @staticmethod
    def menu():
        print(">> Menu de clientes não implementado aqui.")

class IndexUI:
    @staticmethod
    def main():
        while True:
            print("\n=== Sistema de Agendamento ===")
            print("1 - Manter Clientes")
            print("2 - Manter Serviços")
            print("0 - Sair")
            opc = input("Escolha uma opção: ")
            if opc == "1":
                ManterClienteUI.menu()
            elif opc == "2":
                ManterServicoUI.menu()
            elif opc == "0":
                print("Encerrando o sistema.")
                break
            else:
                print("Opção inválida.")
