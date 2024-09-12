from models.Endereco import Endereco
from models.Fisica import Fisica
from abc import ABC, abstractmethod
from models.enums.Genero import Genero
from models.enums.Setor import Setor
import os

os.system("cls || clear")

class Funcionario(Fisica, ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, datanascimento: str, genero: Genero, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, datanascimento, genero)
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Matricula: {self.matricula}"
                f"\n Setor: {self.setor.value}"
                f"\n Salario: {self.salario}"
                f"\n Salario Final: {self.salario_final()}")