import requests
import datetime


def getData():
    date = datetime.datetime.now()
    wbtimeformatted = str(date.year) + '-' + str(date.month) + '-' + str(date.day) + 'T00:30:00.000Z'
    response = requests.get('https://suppliers-stats.wildberries.ru/api/v1/supplier/orders',
                            params={
                                'dateFrom': wbtimeformatted,
                                'flag': 1,
                                'key': 'ODQ0MmFhMzgtMDg2Zi00NzFhLWE0NTMtY2RmMTk0Yzk4ZjIy'
                            })

    try:
        status_code = response.status_code

        if status_code == 200:
            data = response.json()
            print(data)
            return data, True, date

        elif status_code == 429:
            answer = "Превышено количество допустимых запросов, чутка подожди"
            print(answer)
            return answer, False, date

        else:
            answer = "У ВБ очередная беда с башкой, апишка не бом-бом" \
                     "\nstatus code = " + str(response.status_code)
            print(answer)
            return answer, False, date

    except requests.exceptions.RequestException as e:
        print(e)
        return "Какая-то ебейшая ошибка, если не пройдет спустя 5 минут - чекни логи хироку", False, date


def getOrders():
    data, success, date = getData()

    if success:
        orders = 0
        total = 0
        for order in data:
            orders += 1
            price = int(order["totalPrice"]) * (100 - int(order["discountPercent"])) / 100
            total += price
        answer = "Статистика на " + str(date.day) + "-" + str(date.month) + "-" + str(date.year) \
                 + "\nКоличество заказов за день: " + str(orders) \
                 + "\nСумма заказов за день: " + str(total) + 'руб.'
        print(answer)
        return answer
    else:
        print(data)
        return data


def getOrdersDetailed():
    data, success, date = getData()
    answer = ''
    items = {'2011444477004':'Дозатор', '2009914145003':'Фотик голубой', '2009914234004':'Фотик розовый', '2008783268004':'Штопор красный',
             '2007020176003':'Щетки для стекол', '2007020015005':'Мельница', '2007019712007':'Штопор черный', '2006969380007':'Лоток',
             '2004297522007':'Швабра', '2004297824002':'Таз'}
    ordersDetailed = {'2011444477004':0, '2009914145003':0, '2009914234004':0, '2008783268004':0,
             '2007020176003':0, '2007020015005':0, '2007019712007':0, '2006969380007':0,
             '2004297522007':0, '2004297824002':0}

    if success:
        orders = 0
        total = 0
        for order in data:
            orders += 1
            price = int(order["totalPrice"]) * (100 - int(order["discountPercent"])) / 100
            total += price
            answer = "Статистика на " + str(date.day) + "-" + str(date.month) + "-" + str(date.year) \
                 + "\nКоличество заказов за день: " + str(orders) \
                 + "\nСумма заказов за день: " + str(total) + 'руб.'
            for item in items:
                barcode = order['barcode']
                if item == barcode:
                    ordersDetailed[barcode] += 1
    else:
        return data

    answer += '\nДетализация заказов:\n'

    for item in ordersDetailed:
        if ordersDetailed[item] != 0:
            answer += items[item] + ': ' + str(ordersDetailed[item]) + ' шт.\n'

    print(answer)
    return answer

# def printJson():
#     wbtimeformatted = str(now.year) + '-' + str(now.month) + '-' + str(now.day) + 'T00:30:00.000Z'
#     response = requests.get('https://suppliers-stats.wildberries.ru/api/v1/supplier/orders',
#                             params={
#                                 'dateFrom': wbtimeformatted,
#                                 'flag': 1,
#                                 'key': 'ODQ0MmFhMzgtMDg2Zi00NzFhLWE0NTMtY2RmMTk0Yzk4ZjIy'
#                             })
#
#     data = response.json()
#     print(data)
#     return str(data)
