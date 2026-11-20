# это я написала полный путь к файлу, потому что почему-то он у меня сохраняется непонятно куда и я не могу его потом найти
# может можно как-то иначе решить эту проблему, но я не знаю как 
put = r'C:\Users\Asus\Desktop\python\diary.txt'

# создаём файл и пишем первые три строки
with open(put, 'w', encoding='utf-8') as f:
    f.write('Сегодня мы работали с файлами Python.'\n)
    f.write('Научились сохранять текст.'\n)
    f.write('Узнали, как читать данные обратно.'\n)

# дописываем четвёртую строку
with open(put, 'a', encoding='utf-8') as f:
    f.write('Следующее занятие – CSV и JSON'\n)

# читаем файл
with open(put, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# выводим все записи
for line in lines:
    print(line.strip())

# выводим количество
print('Количество записей:', len(lines))

print('Файл сохранён сюда:')
print(put)
# создаём файл и записываем первые три строки
with open('diary.txt', 'w', encoding='utf-8') as f:
    f.write('Сегодня мы работали с файлами Python.')
    f.write('Научились сохранять текст.')
    f.write('Узнали, как читать данные обратно.')

# открываем файл ещё раз, чтобы дописать четвёртую строку
with open('diary.txt', 'a', encoding='utf-8') as f:
    f.write('Следующее занятие – CSV и JSON')

# читаем весь файл
with open('diary.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# выводим все записи
for line in lines:
    print(line.strip())

# выводим количество записей
print('Количество записей:', len(lines))

