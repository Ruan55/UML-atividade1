from models.Endereco import Endereco
from models.Fisica import Fisica
from models.enums.Genero import Genero
import os

os.system("cls || clear")

class Cliente(Fisica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, datanascimento: str, genero: Genero, protocoloatendimento: int) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, datanascimento, genero)
        self.protocoloatendimento = protocoloatendimento

    def __str__(self) -> str:
        return (f"{super().__str__()}"
            f"\n Protocolo Atendimento: {self.protocoloatendimento}")