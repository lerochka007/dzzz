# подключаем модуль для работы с csv (нужен только для чтения)
import csv

# это я написала полный путь к файлу, потому что почему-то он у меня сохраняется непонятно куда и я не могу его потом найти
# может можно как-то иначе решить эту проблему, но я не знаю как 
put = r'C:\Users\Asus\Desktop\python\purchases.csv'

# создаём файл и записываем данные обычным способом
with open(put, 'w', encoding='utf-8') as f:
    # пишем заголовок
    f.write('Товар,Цена за штуку,Количество')
    # пишем товары
    f.write('Тетрадь,2.50,4')
    f.write('Ручка,1.20,3')
    f.write('Папка,4.00,2')
    f.write('Маркер,3.30,1')

# теперь читаем файл обратно
with open(put, 'r', encoding='utf-8') as f:
    chitatel = csv.reader(f)
    # пропускаем заголовок
    next(chitatel)
    
    # переменная для общей суммы
    itogo = 0
    
    # идём по каждой строке
    for stroka in chitatel:
        # достаём данные
        nazvanie = stroka[0]
        cena = float(stroka[1])
        kolichestvo = int(stroka[2])
        
        # считаем стоимость
        stoimost = cena * kolichestvo
        
        # прибавляем к общей сумме
        itogo += stoimost
        
        # выводим информацию о товаре
        print(nazvanie, cena, kolichestvo)
        print('Стоимость:', stoimost)

# выводим итоговую сумму
print('Общая сумма покупок:', itogo)