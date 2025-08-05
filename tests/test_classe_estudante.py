#Testes para a classe estudante
import pytest
from src.database.materias import materias, Materia, MateriaBase, MateriaSemPreRequisito
from src.estudante.classe_estudante import Estudante

def test_estudante_sucesso():
  estudante = Estudante("Davi", "200000000", "c1")
  assert estudante.nome == "Davi"
  assert estudante.matricula == "200000000"
  assert estudante.materias_em_andamento == "c1"

def test_estudante_sem_campo():
  with pytest.raises(TypeError):
    Estudante() #estudante sem campos preenchidos