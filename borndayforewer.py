'''
Данный модуль реализовывает следующую логику:
- Спросить у пользователя год рождения А.С Пушкина
- Если пользователь ввел верный год, вывести 'Верно'
- Если пользователь ошибся, то задаем ему тот же вопрос снова
- После получения верного ответа на вопрос о годе рождения Пушкина задаем вопрос о дне рождения (день месяца).
- Если пользователь ошибся, то задаем ему тот же вопрос снова
- Если пользователь ввел верный день, вывести 'Верно' и завершаем программу

Ответ пользователя приводится к типу int
Проверка на корректность типа вводимых данных НЕ прозводится.

При неправильном ответе пользователю тот же вопрос задается заново, до получения верного ответа.
'''

# переменная типа int с указанием года рождения Пушкина
born_year = 1799
born_day = 6

# запрос ввода от пользователя на год рождения
answer_year = int(input('В каком году родился А.С. Пушкин? Ваш ответ: '))

while answer_year != born_year:
    answer_year = int(input('Неверно. Так в каком году родился А.С. Пушкин? Ваш ответ: '))

print('Верно')

answer_day = int(input('В какой день (число) в июне 1799 года родился А.С. Пушкин? Ваш ответ: '))

while answer_day != born_day:
    answer_day = int(input('Неверно. Так в какой день (число) в июне 1799 года родился А.С. Пушкин? Ваш ответ: '))

print('Верно')
