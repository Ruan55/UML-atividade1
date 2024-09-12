from models.Endereco import Endereco
from abc import ABC, abstractmethod
import os

os.system("cls || clear")

class Pessoa(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return (f"\n Nome: {self.nome}"
                f"\n Telefone: {self.telefone}"
                f"\n Email: {self.email}"
                f"\n Endereço: {self.endereco}")