n = int(input())
command_even = 'even'
command_odd = 'odd'
command_negative = 'negative'
command_positive = 'positive'
original_list = []
filtered_list = []
for iteration in range(n):
    number = int(input())
    original_list.append(number)

command = input()

for item in range(len(original_list)):
    if (command == command_even and original_list[item] % 2 == 0) or (command == command_odd and original_list[item] % 2 != 0) or \
            (command == command_positive and original_list[item] > -1) or (command == command_negative and original_list[item] < 0):
        filtered_list.append(original_list[item])
print(filtered_list)