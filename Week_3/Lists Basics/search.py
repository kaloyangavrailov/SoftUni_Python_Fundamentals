number_iterations = int(input())
filter = input()
original_list = []
filtered_list = []
for iteration in range(number_iterations):
    word = input()
    original_list.append(word)
    if filter in word:
        filtered_list.append(word)

print(f'{original_list}')
print(f'{filtered_list}')