from models.Endereco import Endereco
from models.Pessoa import Pessoa
import os

os.system("cls || clear")

class Juridica(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoestadual: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricaoestadual = inscricaoestadual

    def __str__(self) -> str:
        return (f"\n Cnpj: {self.cnpj}"
                f"\n Inscrição Estadual: {self.inscricaoestadual}")