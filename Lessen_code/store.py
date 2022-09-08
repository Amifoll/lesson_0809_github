#  Для этого нужно создать два списка: магазин и покупатель. В каждом списке - монетки по 1,2,5 руб. Ваша задача - организовать покупку товаров из магазина, т.е. сделать так, чтобы покупатель, который имеет достаточное количество монет, мог забрать товар.
#   Товары хранятся в словаре (ключ - товар, значение - стоимость). В программе необходимо предусмотреть возможность сдачи. Покупка товаров возможна до слова “stop”.
#   Шаг 0. Создать два списка.
#   Шаг 1. Добавить в список пользователя монетки 1, 1, 2, 5, 5, 5.
#   Шаг 2. Добавить в список магазина монетки 1, 1, 2, 2, 2, 1.
#   Шаг 3. Вывести список возможных товаров.
#   Шаг 4. Организовать цикл.
#   В цикле - ввод пользователя. Если хватает на товар, он отдается.
#   Вводится слово с консоли (название товара), программа проверяет, что такое слово есть в файле, и выводит его цену.

buy_list = [1, 1, 2, 5, 5, 5]
store_list = [1, 1, 2, 2, 2, 1]

store = {'колбаса': 2, 'курица': 5, 'вафли': 3}
summ_buy_list = 0
hight_token_buy_list = ''
for key, value in store.items():
    print(f'{key} : {value} монет(а) ')

while True:
    zapros = input('Введите название товара').lower()
    if zapros in store:
        if store[zapros] in buy_list:
            print('Покупка выполнена')
            buy_list.remove(store[zapros])
            print('У вас в кошельке:', buy_list)
            del store[zapros]
            print(f'Витрина в магазине : {store}')
            if len(store) == 0:  # Если словарь пуст, Len () возвращает 0
                break
            continue
        elif store[zapros] not in buy_list:
            for i in buy_list:
                summ_buy_list += buy_list[i]
            if summ_buy_list < store[zapros]:
                print('Деньги кончились')
                break
            else:
                for i in buy_list:
                    if i > store[zapros]:
                        hight_token_buy_list = i - store[zapros]
                        buy_list.remove(
                            i)  # remove() — удаляет первый встреченный элемент в списке, который соответствует условию.
                        buy_list.append(hight_token_buy_list)
                        del store[zapros]
                        store_list.remove(hight_token_buy_list)
                        continue
    print('Ошибка')
    continue
