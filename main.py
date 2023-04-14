cost = 0
ticket = input("Сколько билетов вы хотите приобрести на мероприятие?")
ticket = int(ticket)
if type(ticket) == int:
    for i in range(ticket):
        i += 1
        age = input(f"Для какого возраста билет №{i}?")
        age = int(age)
        if age < 18:
            cost += 0
        elif 25 > age >= 18:
            cost += 990
        elif age > 25:
            cost += 1390
print(cost)
if ticket > 3:
    cost = cost - ((cost / 100) * 10)
    print(f'Сумма к оплате {cost} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше 3-х человек')
else:
    print(f'Сумма к оплате {cost} руб.')