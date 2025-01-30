import os
import pyaes

# Nome do arquivo criptografado e chave de descriptografia
file_name = "teste.txt.ransomwaretroll"
key = b"testeransomwares"

# Verifica se o arquivo existe antes de tentar abrir
if os.path.exists(file_name):
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Descriptografando os dados
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    # Criando o arquivo descriptografado
    new_file = "teste.txt"
    with open(new_file, "wb") as file:
        file.write(decrypt_data)

    # Removendo o arquivo criptografado
    os.remove(file_name)
    print(f"Arquivo {file_name} descriptografado com sucesso como {new_file}.")
else:
    print(f"Erro: O arquivo {file_name} não foi encontrado.")
