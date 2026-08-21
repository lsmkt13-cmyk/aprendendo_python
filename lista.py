componentes = ['teclado', 'mouse', 'monitor']

print(componentes)
print(componentes[0])
print(componentes[-1])

componentes. append ("gabinete")

print(componentes)
print(componentes[0])
print(componentes[-1])

componentes.remove("mouse")

print(componentes)
print(componentes[0])
print(componentes[-1])

for i in range(3):
    if i == 0:
        print(componentes[i])