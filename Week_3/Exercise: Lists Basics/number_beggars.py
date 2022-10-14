values_money = input().split(', ')
count_beggars = int(input())
values_money = [int(item) for item in values_money]

list_of_money_beggars_take = []
start_index = 0
while start_index < count_beggars:
    money_beggars_take = 0
    for item in range(start_index,len(values_money),count_beggars):
        money_beggars_take += values_money[item]
    list_of_money_beggars_take.append(money_beggars_take)
    start_index += 1

print(list_of_money_beggars_take)