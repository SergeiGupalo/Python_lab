import json
from pprint import pprint
 
 
def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
 
 
text = {
    "Уганда": "Африка, Насиление 44.7 мил., Площа 236 тыс.км.",
    "Канада": "Северная Америка, Насиление 35.1 мил.,чел. Площа 9.9 мил.км.",
    "Монако": "Европа, Насиление 37.3 тыс.,чел. Площа 2 тыс., км.",
    "Австралия": "Австралия, Насиление 25.6 мил.чел Площа 7.6 мил.км.",
    "Мадагаскар": "Африка, Насиление 24.8 мил.чел. Площа 587 тыс.км.",
    "Узбекистан": "Азия, Насиление 35.6 мил.чел. Площа 448 тыс.км.",
    "Япония": "Азия, Насилениие 126 мил.чел. Площа 377 тыс.чел.",
    "Дания": "Европа, Насиление 5.7 мил.чел. Площа 43 тыс.чел.",
    "Франция": "Европа, насиление 66 мил.чел. Площа 551 тыс.км",
    "Украина": "Европа, Насиление 41 мил.чел. Площа 603 тыс.км"
}
 
 
write(text, 'data.json')
 
 
def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

pprint(read('data.json'))
 
d = read('data.json')
 
for k, v in d.items():
    if v.startswith(('Африка', 'Азия')):
        print(k)

while True:
    add = input('Хотите добавать страну?(Да или Нет): ')
    if add == 'Да':
        new_country = input('Введите страну: ')
        new_info = input('Введите информацию: Континетн, Насиление, Площа: ')
        if new_country in d.keys():
            print('Даная страна уже есть!')
        else:
            text[new_country] = new_info
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(text, f, indent=4, ensure_ascii=False)
                print('Страна добавлена!')
    else:
        break

print("\n----- New Dictionary 1 -----")

pprint(read('data.json'))
 
d = read('data.json')
 
for k, v in d.items():
    if v.startswith(('Африка', 'Азия')):
        print(k)

while True:
    lol = input("Хотите удалить страну из словаря(Да или Нет?): ")
    if lol == 'Да':
        lol_country = input("Введите страну которую хотите удалить: ")
        if lol_country in d.keys():
            del text[lol_country]
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(text, f, indent=4, ensure_ascii=False)
                print("Страна удалена!")
        else:
            print("Такой страны нет!")
    else:
        break

print("\n----- New Dictionary 2 -----")

pprint(read('data.json'))
 
d = read('data.json')
 
for k, v in d.items():
    if v.startswith(('Африка', 'Азия')):
        print(k)
