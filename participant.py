# подключаем модуль json (нужен только для чтения)
import json

# путь к файлу, чтобы он сохранился место, в котором я потом его найду 
put = r'C:\Users\Asus\Desktop\python\participant.json'

# создаём профиль как текст в формате JSON
tekst = '''{
    "Имя": "Алексей",
    "Группа": "КБ-101",
    "Навыки": ["Python", "Excel"],
    "Уведомления": true
}'''

# сохраняем профиль в файл
with open(put, 'w', encoding='utf-8') as f:
    f.write(tekst)

# читаем профиль из файла
with open(put, 'r', encoding='utf-8') as f:
    profil = json.load(f)

# добавляем навык CSV
profil['Навыки'].append('CSV')

# выключаем уведомления
profil['Уведомления'] = False

# снова превращаем словарь в текст
tekst = '''{
    "Имя": "''' + profil['Имя'] + '''",
    "Группа": "''' + profil['Группа'] + '''",
    "Навыки": ["Python", "Excel", "CSV"],
    "Уведомления": false
}'''

# сохраняем обновлённый профиль
with open(put, 'w', encoding='utf-8') as f:
    f.write(tekst)

# читаем ещё раз и выводим
with open(put, 'r', encoding='utf-8') as f:
    profil = json.load(f)

print(profil)