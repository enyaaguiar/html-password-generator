import random 
import string

def gerar_senha(tamanho):
    todos_caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))
    return senha
tamanho = int(input("Digite o tamanho da senha: "))
senha_gerada = gerar_senha(tamanho)
print("Senha gerada:", senha_gerada)