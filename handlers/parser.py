import requests
import datetime
import config


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
            answer = "Превышено количество допустимых запросов, подождите"
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
            total += int(price)
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
    ordersDetailed = {}
    for item in config.items.keys():
        ordersDetailed.update({item: 0})

    if success:
        orders = 0
        total = 0
        for order in data:
            orders += 1
            price = int(order["totalPrice"]) * (100 - int(order["discountPercent"])) / 100
            total += int(price)
            answer = "Статистика на " + str(date.day) + "-" + str(date.month) + "-" + str(date.year) \
                 + "\nКоличество заказов за день: " + str(orders) \
                 + "\nСумма заказов за день: " + str(total) + 'руб.'
            for item in config.items:
                barcode = order['barcode']
                if item == barcode:
                    ordersDetailed[barcode] += 1
    else:
        return data

    answer += '\n\nДетализация заказов:\n'

    for item in ordersDetailed:
        if ordersDetailed[item] != 0:
            answer += config.items[item] + ': ' + str(ordersDetailed[item]) + ' шт.\n'

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
