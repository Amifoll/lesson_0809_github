import random


# Чтение слов из файла
def file_unpacking():
    with open('world.txt', 'r') as worlds:
        for world in worlds:
            world_all.append(world.strip())


# вхождене в топ
def top_entry(user_name, count):
    with open('history.txt', 'a', encoding='utf-8') as file:
        file.write(f'{user_name} - количество очков: {count}\n')


world_all = []
file_unpacking()
world_dict = dict()


# чтение из топа
def read_top(line, score):
    with open('history.txt', 'r', encoding='utf-8') as file:
        a = len(file.readline())
        for i in file:
            line += 1
            score.append(*(int(score) for score in str.split(i) if score.isdigit()))
    print(f'Всего игр сыграно: {line}')


# создание словоря ключ значение\верно - не верно
for i, word in enumerate(map(list, world_all)):
    random.shuffle(word)
    world_dict[world_all[i]] = ''.join(word)

print('Программа : введите ваше имя')
user_name = input('Пользователь:')
count = 0
for word, world_random in world_dict.items():
    print(f'Угадайте слово: {world_random}')
    user_answer = input('Пользователь: ')
    if user_answer == word:
        print('Верно! Вы получаете 10 очков.')
        count += 10
    else:
        print(f'{user_answer} неверно! Верный ответ - {word}.')
print(f'Вы заработали {count} очков')

# body
top_entry(user_name, count)
line = 0
score = []
read_top(line, score)
max_score = max(score)
print(f'Максимальный рекорд: {max_score}')
