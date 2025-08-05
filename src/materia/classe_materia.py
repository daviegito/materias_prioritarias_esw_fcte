from abc import ABC, abstractmethod


#classe abstrata
class MateriaBase(ABC):
    @abstractmethod
    def descricao(self):
        pass
    
    
class Materia(MateriaBase):
    def __init__(self, nome, codigo, creditos, pre_requisito, status):
        self.nome = nome
        self.codigo = codigo #código da matéria
        self.creditos = creditos
        self.pre_requisito = pre_requisito #numero de creditos de materias que ela desbloqueia
        self.status = status #0 para não cursada, 1 para cursada ou cursando

    @property #aqui ocorre o encapsulamento dos atributos
    def nome(self):
        return self._nome

    @nome.setter #o setter também ajuda no encapsulamento
    def nome(self, value):
        self._nome = value

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def creditos(self):
        return self._creditos

    @creditos.setter
    def creditos(self, value):
        self._creditos = value

    @property
    def pre_requisito(self):
        return self._pre_requisito

    @pre_requisito.setter
    def pre_requisito(self, value):
        self._pre_requisito = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def descricao(self):
        return f"{self.nome} ({self.codigo}) - Créditos: {self.creditos}, Pré-requisitos: {self.pre_requisito}"


#Para matérias que não trancam outras
class MateriaSemPreRequisito(MateriaBase):
    def __init__(self, nome, codigo, creditos, status):
        self.nome = nome
        self.codigo = codigo
        self.creditos = creditos
        self.status = status

    @property #encapsulamento novamente :)
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def creditos(self):
        return self._creditos

    @creditos.setter
    def creditos(self, value):
        self._creditos = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    #isso serve para o menu de matérias - quando um usuário quiser verificar alguma matéria individual
    def descricao(self):
        return f"{self.nome} ({self.codigo}) - Créditos: {self.creditos}, Sem pré-requisitos"