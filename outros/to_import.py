# - para importar um modulo:

# import sys

# sys.path += ['F:/Dropbox/Arquivos/Estudo/Python']
# - ou
# sys.path.append('F:/Dropbox/Arquivos/Estudo/Python')

# - module_name = 'nome_do_arquivo' - '.py'

# - caso #1:
# import to_import
# - nesse caso para ter acesso ao que foi definido no arquivo
# - deve ser usado: module_name.def
# - exemplo:
# to_import.mod()

# - caso #2:
# from to_import import *
# - nesse caso o acesso as definiÃ§Ãµes Ã© direto
# - exemplo:
# mod()
# - definiÃ§Ãµes comeÃ§adas com '_' nÃ£o sÃ£o importadas diretamente
# - exemplo:
# to_import._mod()
# - por inserir as definiÃ§Ãµes do arquivo diretamente
# - deve-se tomar cuidado com as definiÃ§Ãµes anteriores

# - isso pode ser feito usando os nomes de pastas
# - exemplo:
# sys.path += ['F:/Dropbox/Arquivos/Estudo']
# import Python.to_import
# - isto Ã© equivalente ao caso #1, mas com o uso diferenciado
# - exemplo:
# Python.to_import.mod()
# - o uso pode ser simplificado com o uso de 'as'
# - exemplo:
# import Python.to_import as toimp
# toimp.mod()

# - tambÃ©m podem ser usados '.' e '..' para navegar nos pacotes
# - exemplo:
# sys.path += ['F:/Dropbox/Arquivos/Estudo/Python']
# from . import to_import
# - importa 'to_import' a partir da pasta raiz
# from ..Python import to_import
# - importa 'to_import' voltando uma pasta a partir da raiz
# - e entrando na pasta 'Python'
# - todos equivalentes ao caso #1
