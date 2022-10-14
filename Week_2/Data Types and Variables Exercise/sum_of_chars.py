number_of_lines = int(input())
sum = 0
for letter in range(number_of_lines):
    sum += ord(input())
print(f'The sum equals: {sum}')
