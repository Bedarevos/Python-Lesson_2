# Считаем кредит
name1 = input("Введите имя первого человека: ")
name2 = input("Введите имя второго человека: ")
name3 = input("Введите имя третьего человека: ")

salary1 = int(input("зп первого: "))
salary2 = int(input("зп второго: "))
salary3 = int(input("зп третьего: "))

credit = int(input("Введите сумму кредита: "))
period = int(input("Введите срок в месяцах: "))
procent = float(input("процент: "))

pay_per_month = credit / period + (credit / 100 * procent) / 12
print("Ежемесячный платеж составит - ", pay_per_month, "рублей")