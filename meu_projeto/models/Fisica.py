from models.Endereco import Endereco
from models.enums.Genero import Genero
from models.Pessoa import Pessoa
from abc import ABC
import os

os.system("cls || clear")

class Fisica(Pessoa, ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, datanascimento: str, genero: Genero) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf
        self.rg = rg
        self.datanascimento = datanascimento
        self.genero = genero

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\n Cpf: {self.cpf}"
                f"\n Rg: {self.rg}"
                f"\n Data de nascimento: {self.datanascimento}"
                f"\n Gênero - Caractere: {self.genero.caractere}"
                f"\n Gênero - Texto: {self.genero.texto}")