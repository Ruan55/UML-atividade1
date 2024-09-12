from models.enums.UnidadeFederativa import UnidadeFederativa

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf
    
    def __str__(self) -> str:
        return(f"\n Logradouro: {self.logradouro}"
               f"\n Numero: {self.numero}"
               f"\n Complemento: {self.complemento}"
               f"\n Cep: {self.cep}"
               f"\n Cidade: {self.cidade}"
               f"\n UF - Nome: {self.uf.nome}"
               f"\n UF - Sigla: {self.uf.sigla}")