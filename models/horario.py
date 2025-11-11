import json
from datetime import datetime

class Horario:
    def __init__(self, id, data):
        self.set_id(id)
        self.set_data(data)
        self.__confirmado = False
        self.__id_cliente = 0
        self.__id_servico = 0
        self.__id_profissional = 0

    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {'Sim' if self.__confirmado else 'Não'}"

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado
    def get_id_cliente(self): return self.__id_cliente
    def get_id_servico(self): return self.__id_servico
    def get_id_profissional(self): return self.__id_profissional

    
    def set_id(self, id): 
        if not isinstance(id, int) or id < 0:
            raise ValueError("O id deve ser um número inteiro positivo.")
        self.__id = id

    def set_data(self, data):
        if not isinstance(data, datetime):
            raise TypeError("O atributo 'data' deve ser um objeto datetime.")
        if data.year < 2025:
            raise ValueError("A data do horário não pode ser anterior ao ano de 2025.")
        self.__data = data

    def set_confirmado(self, confirmado):
        if not isinstance(confirmado, bool):
            raise TypeError("O atributo 'confirmado' deve ser do tipo booleano.")
        self.__confirmado = confirmado

    def set_id_cliente(self, id_cliente):
        if not isinstance(id_cliente, int) or id_cliente < 0:
            raise ValueError("O id do cliente deve ser um número inteiro positivo.")
        self.__id_cliente = id_cliente

    def set_id_servico(self, id_servico):
        if not isinstance(id_servico, int) or id_servico < 0:
            raise ValueError("O id do serviço deve ser um número inteiro positivo.")
        self.__id_servico = id_servico

    def set_id_profissional(self, id_profissional):
        if not isinstance(id_profissional, int) or id_profissional < 0:
            raise ValueError("O id do profissional deve ser um número inteiro positivo.")
        self.__id_profissional = id_profissional


    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data.strftime("%d/%m/%Y %H:%M"),"confirmado": self.__confirmado,"id_cliente": self.__id_cliente,"id_servico": self.__id_servico, "id_profissional": self.__id_profissional
        }

    @staticmethod
    def from_json(dic):
        data = datetime.strptime(dic["data"], "%d/%m/%Y %H:%M")
        h = Horario(dic.get("id", 0), data)
        h.set_confirmado(dic.get("confirmado", False))
        h.set_id_cliente(dic.get("id_cliente", 0))
        h.set_id_servico(dic.get("id_servico", 0))
        h.set_id_profissional(dic.get("id_profissional", 0))
        return h
