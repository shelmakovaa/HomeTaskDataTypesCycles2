# Задание 4
# Дана переменная, в которой хранится статистика рекламных каналов по объемам продаж
# (пример структуры данных приведен ниже).
# Напишите программу, которая возвращает название канала с максимальным объемом продаж.

stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
result = ''
max_sales = max(stats.values())

for company, data in stats.items():
    if data == max_sales:
        result = company
        break

print(f"Максимальный объем продаж на рекламном канале: {result}")