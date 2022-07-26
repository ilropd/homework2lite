'''
Данный модуль предназначен для проведения мини-викторины. Пользователю необходимо дать ответ на один вопрос:
год рождения А.С. Пушкина. При вводе неверного числа или НЕ числа запрос ответа будет повторяться. После того, как
пользователь введет верный ответ, модуль напишет поздравление и указание количества попыток.
'''

# год рождения А.С. Пушкина
bornyear = 1799

# в этой переменной будет храниться количество попыток
counter = 0

# упаковываем правильный ответ в переменную, чтобы легче было выводить + счетчик попыток
congrats = '---> А ты молодец! И всего каких-то {tries} попыток! Верно, Александр Сергеевич ' \
           'родился 06 июня 1799 года. <---'

# инициируем первый ввод
answer = input('Привет! Сможешь ли ты верно назвать год рождения А.С. Пушкина? Напиши его здесь одним числом: ')

# проверяем тип введенного значения, если это не число, то просим ввести данные снова
while not answer.isdigit():
    print(counter)
    answer = input('Я просил написать год рождения А.С.Пушкина ЧИСЛОМ. Например, 1234. Попробуй еще раз: ')

# если пользователь ввел число, то проверяем, соответствует ли оно правильному
# соответствует - выводим поздравительный текст
# НЕ соответствует или введено НЕ число, то вставляем неверный ответ в текст вывода (для ощущения интерактива)
if answer == bornyear:
    counter += 1
    print('\n', congrats.format(tries=counter), sep='')
else:
    while not answer.isdigit() or (answer.isdigit() and int(answer) != bornyear):
        counter +=1
        answer = input('Не-а. не {wrong}.Попробуй еще раз: '.format(wrong=answer))
    counter = counter+1
    print('\n', congrats.format(tries=counter), sep='')
