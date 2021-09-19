chave = 'alan'
letrasAdicao = 'luca'.upper()

conjuntoChave = set(chave)
if(len(conjuntoChave) != len(chave)):
    novaChave = []
    for i, v in enumerate(chave):
        totalcount = chave.count(v)
        count = chave[:i].count(v)
        novaChave.append(v + str(count + 1) if totalcount > 1 else v)
    chave = novaChave

frase = 'QUEM LER E VERY GAY DE MAIS DA CONTA'.upper()
frase = frase.replace(' ', '')

if (len(frase)%5 > 0):
    for letra in letrasAdicao:
        frase += letra
        if(len(frase)%5 == 0):
            break

while(len(frase)%len(chave) > 0):
    frase += ' '

matriz = []
listaAuxi = []

for letra in frase:
    listaAuxi.append(letra)
    if(len(listaAuxi) == len(chave)):
        matriz.append(listaAuxi)
        listaAuxi = []

dicionario = {}

for vez in range(len(chave)):
    listaAuxi = []
    for lista in matriz:
        listaAuxi.append(lista[vez])
    dicionario[chave[vez]] = listaAuxi
    listaAuxi = []

chave = sorted(chave)

codigo = ''

for letra in chave:
    for letra in dicionario[letra]:
        codigo += letra

codigo = codigo.replace(' ', '')
codigoFormatado = ''

contador = 1
for letra in codigo:
    codigoFormatado += letra
    if (contador%5 == 0):
        codigoFormatado += '\n'
    contador += 1

print(codigoFormatado)
