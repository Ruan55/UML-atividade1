from models.Endereco import Endereco
from models.enums.Genero import Genero
from models.enums.Setor import Setor
from models.Funcionario import Funcionario
import os

os.system("cls || clear")

class Motoboy(Funcionario):
    BONIFICACAO = 1.1

    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, datanascimento: str, genero: Genero, matricula: str, setor: Setor, salario: float, cnh: str) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, datanascimento, genero, matricula, setor, salario)
        self.cnh = cnh

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Oab: {self.cnh}")