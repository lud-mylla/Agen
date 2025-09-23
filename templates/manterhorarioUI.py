import json

class HorarioDAO:
    __objetos = []


    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id()> id: id= aux.get_id()
            obj.set_id(id+1)
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
            if obj.get_id() == id: return obj
            return None
        

    @classmethod

    def atualizar(cls, obj):
        