items = [
  {"название": "Яблоки", "количество": 3},
  {"название": "Хлеб", "количество": 1},
  {"название": "Молоко", "количество": 0}
]


def create_shopping_list(items):
    shoping_list = []
    for item in items:
        name = item['название']
        quantity = item['количество']
        if quantity > 0:
            shoping_list.append((name, quantity))
        else:
            print('Количество товаров не можеты быть ноль')
    return shoping_list


print(create_shopping_list(items))