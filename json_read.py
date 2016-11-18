'''
Проверка корректности выгрузки анкет в формат JSON. Берем полученный JSON, преобразуем обратно в объект Python
и производим раазличные манипуляции.
Обращаем внимание, что все нестандартные символы - т.е. все, кроме стандартной латиницы,
представлены в JSON-выводе в виде кодов.
Преобразованию подверглись русские буквы, буквы с диакритикой во французском и польском языках.
В процессе обратного преобразования они были корректно восприняты.
'''
import json
json_string = '''
{"form1117108": {"Age": "21", "Language": "\u0430\u043d\u0433\u043b", "Kettle": "\u0432", "Sex": "male", "Television": "\u0432", "Smartphone": "\u044b", "Lastname": "\u0432\u0432", "Name": "\u0432\u0432\u0432", "Iron": "\u044b", "Coffee": "\u0443", "Residence": "village"},
"form11161625": {"Language": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "Kettle": "\u0447\u0430\u0439\u043d\u0438\u043a", "Sex": "male", "Television": "\u043d\u0435\u0437\u043d\u0430\u044e", "Residence": "village", "Lastname": "\u041f\u0435\u0440\u0435\u043f\u0435\u043b\u0438\u0446\u0430", "Name": "\u041c\u0430\u043a\u0441\u0438\u043c", "Coffee": "\u043d\u0435\u0437\u043d\u0430\u044e", "Age": "20"},
"form1117102": {"Age": "150", "Language": "Deutsch", "Kettle": "Kessel", "Sex": "male", "Television": "Fernsehger\u00e4t", "Iron": "Pl\u00e4tteisen", "Residence": "city", "Lastname": "Marx", "Name": "Karl", "Coffee": "Kaffeemaschine", "Smartphone": "Mobiltelefon"}, "form11161738": {"Language": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "Kettle": "\u0447\u0430\u0439\u043d\u0438\u043a", "Sex": "male", "Television": "\u0442\u0435\u043b\u0435\u0432\u0438\u0437\u043e\u0440\u041a\u0412\u041d", "Residence": "city", "Lastname": "\u0428\u0430\u0440\u0430\u043f\u043e\u0432", "Name": "\u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440", "Coffee": "\u043a\u043e\u0444\u0435\u0432\u0430\u0440\u043a\u0430", "Age": "26"},
"form11161735": {"Age": "35", "Kettle": "\u0447\u0438\u0444\u0438\u0440\u043d\u0438\u043a", "Language": "\u0444\u0435\u043d\u044f", "Sex": "female", "Television": "\u043a\u0438\u043d\u043e\u0448\u043a\u0430", "Residence": "city", "Lastname": "\u041e\u0431\u043b\u0438\u0433\u0430\u0446\u0438\u044f", "Name": "\u041c\u0430\u043d\u044c\u043a\u0430", "Coffee": "\u0432\u0430\u0440\u0438\u043b\u043e"},
"form11161618": {"Language": "\u0431\u0435\u043b\u043e\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "Kettle": "\u0447\u044f\u0439\u043d\u0438\u043a", "Sex": "male", "Television": "\u0442\u044f\u043b\u044f\u0432\u0438\u0437\u0430\u0440", "Age": "44", "Lastname": "\u041f\u0443\u043f\u043a\u0438\u043d", "Name": "\u0412\u0430\u0441\u044f", "Coffee": "\u043a\u0430\u0444\u044f\u0440\u043d\u044f", "Residence": "city"},
"form11171010": {"Age": "200", "Kettle": "bouilloire", "Language": "Francaise", "Sex": "male", "Coffee": "machine \u00e0 caf\u00e9", "Iron": "fer \u00e0 repasser", "Smartphone": "t\u00e9l\u00e9phone portable", "Lastname": "Bonaparte", "Name": "Napoleon", "Television": "poste de t\u00e9l\u00e9vision", "Residence": "city"}, "form11161715": {"Language": "english", "Kettle": "tea-pot", "Sex": "male", "Television": "neverseensuchthing", "Age": "46", "Lastname": "Holmes", "Name": "Sherlock", "Coffee": "coffe-maker", "Residence": "city"},
"form11171017": {"Iron": "prasowa\u0107", "Age": "140", "Language": "polski", "Kettle": "czajnik", "Sex": "male", "Television": "telewizor", "Residence": "city", "Lastname": "J\u00f3zef", "Name": "J\u00f3zef", "Coffee": "Maszyna do kawy", "Smartphone": "telefon kom\u00f3rkowy"}, "form11161636": {"Language": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "Kettle": "\u0447\u0430\u0439\u043d\u0438\u043a", "Sex": "female", "Television": "\u043d\u0435\u0432\u0438\u0434\u0435\u043b\u0430", "Residence": "city", "Lastname": "\u041a\u043b\u0438\u043c\u043e\u0432\u0430", "Name": "\u041c\u0430\u0440\u0443\u0441\u044f", "Coffee": "\u043d\u0435\u0437\u043d\u0430\u044e\u0442\u0430\u043a\u043e\u0433\u043e", "Age": "35"},
"form11161622": {"Language": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "Kettle": "\u0447\u0430\u0439\u043d\u0438\u043a", "Sex": "male", "Television": "\u0442\u0435\u043b\u0435\u0432\u0438\u0437\u043e\u0440", "Age": "66", "Lastname": "\u041f\u0438\u0442\u0435\u0440\u0441\u043a\u0438\u0439", "Name": "\u041d\u0438\u043a\u043e\u043b\u0430", "Coffee": "\u043a\u043e\u0444\u0435\u043a\u043e\u0440\u044b\u0442\u043e", "Residence": "village"},
"form11161615": {"Language": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "Kettle": "\u0447\u0430\u0439\u043d\u0438\u043a", "Sex": "female", "Television": "\u0442\u0435\u043b\u0435\u0432\u0438\u0437\u043e\u0440", "Residence": "village", "Lastname": "\u041f\u0435\u0440\u0435\u043a\u0438\u0434\u044b\u0448\u0438\u043d\u0441\u043a\u0430\u044f", "Name": "\u041c\u0430\u0448\u0430", "Coffee": "\u043a\u043e\u0444\u0435\u0432\u0430\u0440\u043a\u0430", "Age": "33"},
"form1117107": {"Iron": "\u0443\u0442\u044e\u0433", "Language": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "Kettle": "\u0447\u0430\u0439\u043d\u0438\u043a", "Sex": "female", "Television": "\u0442\u0435\u043b\u0435\u0432\u0438\u0437\u043e\u0440", "Residence": "city", "Lastname": "\u041a\u0430\u043c\u0438\u043b\u043e\u0432\u0430", "Name": "\u0410\u0439\u043d\u0430", "Coffee": "\u043a\u043e\u0444\u0435\u0432\u0430\u0440\u043a\u0430", "Smartphone": "\u0442\u0435\u043b\u0435\u0444\u043e\u043d", "Age": "19"},
"form11161723": {"Age": "20", "Language": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "Kettle": "\u0447\u0430\u0439\u043d\u0438\u043a", "Sex": "female", "Television": "\u043d\u0435\u0432\u0438\u0434\u0435\u043b\u0430", "Residence": "city", "Lastname": "\u0421\u0438\u043d\u0438\u0446\u043a\u0430\u044f", "Name": "\u0417\u043e\u0441\u044f", "Coffee": "\u043d\u0438\u043a\u043e\u0433\u0434\u0430\u0442\u0430\u043a\u043e\u0433\u043e\u043d\u0435\u0432\u0438\u0434\u0435\u043b\u0430"},
"form11161613": {"Language": "", "Kettle": "", "Sex": "male", "Television": "", "Residence": "city", "Lastname": "", "Name": "", "Coffee": "", "Age": ""}, "form11161616": {"Language": "", "Kettle": "", "Sex": "male", "Television": "", "Residence": "city", "Lastname": "", "Name": "", "Coffee": "", "Age": ""}}
'''

alldict = json.loads(json_string)

print(alldict)
print('-------')
print(alldict['form11171010'])
print('-------')
print(alldict['form11171010']['Name'], alldict['form11171010']['Lastname'] )
print('-------')
for key in alldict.keys():
    print(key, end=' ')
print('-------')
for value in alldict.values():
    print(value)
print('-------')
