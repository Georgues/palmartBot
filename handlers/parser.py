import requests
import datetime

now = datetime.datetime.now()


def getData():
    orders = 0
    total = 0
    wbtimeformatted = str(now.year) + '-' + str(now.month) + '-' + str(now.day) + 'T00:30:00.000Z'

    try:
        response = requests.get('https://suppliers-stats.wildberries.ru/api/v1/supplier/orders',
                                params={
                                    'dateFrom': wbtimeformatted,
                                    'flag': 1,
                                    'key': 'ODQ0MmFhMzgtMDg2Zi00NzFhLWE0NTMtY2RmMTk0Yzk4ZjIy'
                                })
        data = response.json()
        status_code = response.status_code

        if status_code == 200:
            for order in data:
                orders += 1
                price = int(order["totalPrice"]) * int(order["discountPercent"]) / 100
                total += price
            answer = "Статистика на " + str(now.day) + "-" + str(now.month) + "-" + str(now.year) \
                     + "\nКоличество заказов за день: " + str(orders) \
                     + "\nСумма заказов за день: " + str(total) + 'руб.'
            print(answer)
            return answer

        elif status_code == 429:
            answer = "Превышено количество допустимых запросов, чутка подожди"
            print(answer)
            return answer

        else:
            answer = "У ВБ очередная беда с башкой, апишка не бом-бом" \
                     "\nstatus code = " + str(response.status_code)
            print(answer)
            return answer

    except requests.exceptions.RequestException as e:
        print(e)
        return "Какая-то ебейшая ошибка, если не пройдет спустя 5 минут - чекни логи хироку"

getData()
