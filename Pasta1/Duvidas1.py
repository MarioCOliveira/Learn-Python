# a definição não fixa o tipo na variável
x = int(3);
print(x)

x = 'Mário';
print(x)

# escopo de variável

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()