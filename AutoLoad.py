import json
import requests
import time
start = True
timeout = 120

url_1 = ""
url_2 = ""

def starting_load():
    response = requests.get(url_1)
    _jso = response.json()
    if(_jso["status"] == 403):
        print("Было запущено в ручную, не могу запустить.")
    else:
        print("Успешно запустил")



def CheckLoad():
    response = requests.get(url_2)
    _jso = response.json()
    if(_jso["status"] == 403):
        print("Импорт не был запущен.")
        print("Запустил импорт.")
        starting_load()
    else:
        print(response.text)
    #Должна быть ещё одна обработка, когда запущено
    #else:
    #    print("Успешно запустил. Ожидание 2 минуты")




while(start):
    CheckLoad()
    print("Ожидание 2 минуты.")
    time.sleep(120)





