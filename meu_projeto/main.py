from models.enums.Genero import Genero
from models.enums.UnidadeFederativa import UnidadeFederativa
from models.enums.Setor import Setor
from models.Cliente import Cliente
from models.Endereco import Endereco
from models.Motoboy import Motoboy
from models.Medico import Medico
from models.Advogado import Advogado
import os

os.system("cls || clear")

motoboy1 = Motoboy("Ruan", "3333-4444", "Ru21@gmail.com", Endereco("Rua K", "5", "N/A", "31323", "Salvador", UnidadeFederativa.BAHIA), "31233", "56464", "04/08/2002", Genero.MASCULINO, "32134", Setor.OPERACOES, 1500, "432444")
medico1 = Medico("Maiara", "4343-6546", "Maa@gmail.com", Endereco("Rua C", "43", "N/A", "323312", "São Paulo", UnidadeFederativa.SAO_PAULO), "33213", "47565", "17/09/1977", Genero.FEMININO, "98082", Setor.SAUDE, 5600, "32434")
advogado1 = Advogado("Nilton", "9933-3444", "Nilton543@gmail.com", Endereco("Rua I", "45E", "N/A", "3232", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO), "32123", "54353", "14/01/1988", Genero.MASCULINO, "332335", Setor.JURIDICO, 4500, "325466")
cliente1 = Cliente("Renata", "9900-2371", "Rere@gmail.com", Endereco("Rua H", "34", "N/A", "32343", "Camaçari", UnidadeFederativa.BAHIA), "32132", "44343", "09/11/1999", Genero.FEMININO, 2333)

print(motoboy1)
print(medico1)
print(advogado1)
print(cliente1)