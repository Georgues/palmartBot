import requests


def getData():
    orders = 0
    total = 0

    response = requests.get(
        "https://suppliers-stats.wildberries.ru/api/v1/supplier/orders?dateFrom=2021-12-12T08:00:00.000Z&flag=1&key=ODQ0MmFhMzgtMDg2Zi00NzFhLWE0NTMtY2RmMTk0Yzk4ZjIy")
    data = response.json()
    if response.status_code == 429:
        print("Too man request")

    for order in data:
        orders += 1
        price = int(order["totalPrice"]) * int(order["discountPercent"]) / 100
        total += price

    print("Количество заказов за день: " + str(orders))
    print("Сумма заказов за день: " + str(total) + 'руб.')

    answer = "Количество заказов за день: " + str(orders) + "\n" + "Сумма заказов за день: " + str(total) + 'руб.'
    return answer
