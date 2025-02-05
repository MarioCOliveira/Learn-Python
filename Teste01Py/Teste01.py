# Exemplos de listas
# Atribuição da lista L01

L01 = [1,2,3,4,5];

print("Lista01 -",L01)

L02 = [1+2+3+4+5];

print("Lista02 -",L02)

# Acessando dados de listas

cachorros = ["Lulu", "Toby", "Fox", "Luc", 'Rin-Tin-Tin'];

# Forma de acessos à lista

print(len(cachorros))
print('Numero de ocorrências -',len(cachorros))
print(cachorros[:2]) # exibe as duas primeiras posições - ['Lulu', 'Toby']
print(cachorros[1:2]) # exibe as duas primeiras posições começando da posição 1 - ['Toby']
print(cachorros[1:1]) # exibe a primeira posição começando da posição 1 - []
print(cachorros[:]) # exibe todo o conteúdo 
print(cachorros[1:]) # exibe o conteúdo da posição 0 - Lulu
print(cachorros[1:0]) # exibe o conteúdo da posição 0 - Lulu

# Métodos de acesso a Lista
# adicionando um item a lista

#cachorros = cachorros + 'Chiquinho';
#Traceback (most recent call last):
#  File "C:\Users\mario\Desktop\AprendendoPython\Teste01Py\Teste01.py", line 30, in <module>
#    cachorros = cachorros + 'Chiquinho';
#                ~~~~~~~~~~^~~~~~~~~~~~~
#TypeError: can only concatenate list (not "str") to list

cachorros.insert(2,'Cláudia');

print(cachorros)


cachorros.remove('Luc');

print(cachorros)


cachorros.append('Luck');

print(cachorros)

cachorros.pop(2);

print(cachorros)
