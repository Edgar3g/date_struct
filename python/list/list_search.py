
"""
Neste List_search se usou a Busca linear.
"""

def search(list, element):
    """Return the Indece element if is in list or None if don't exist"""
    for i in range(len(list)):
        if list[i] == element:
            return i
    return None

Random_list = [12, 'python', 1, "Edgar", 33, 100, 32, True, 0.5, 'Test']
element = False

# indece = search(Random_list, element)
# if indece is not None:
#     print(f'O Índece do elemnto {element} é {indece}')
# else:
#     print(f'o Elemento "{element}" não foi encontrado !')


def duplicate(list):
    for i in range(len(list) -1):
        for j in range(i + 1,len(list)):
            if list[i] == list[j]:
                print(f'I find this: {list[i]} {list[j]} ')
                return True

    return False

test = 'Edgar'

print(duplicate(test))