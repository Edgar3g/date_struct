def inverter_lista(lista):
    tamanho = len(lista)
    limite = tamanho // 2
    for i in range(limite):
        aux = lista[i]
        lista[i] = lista[n - i]
        liata[tamanho] = aux

def inverter_lista2(lista):
    nova_lista = []
    tamanho = len(lista)
    for i in range(tamanho):
        nova_lista.append(lista[tamanho - i])
    return nova_lista


