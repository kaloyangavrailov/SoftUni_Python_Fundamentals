numbers_list = list(map(int,input().split(', ')))
positive_numbers = [item for item in numbers_list if item > -1]
negative_numbers = [item for item in numbers_list if item < 0]
even_numbers = [item for item in numbers_list if item % 2 == 0]
odd_numbers = [item for item in numbers_list if item % 2 != 0]
positive_numbers = [str(item) for item in positive_numbers]
negative_numbers = [str(item) for item in negative_numbers]
even_numbers = [str(item) for item in even_numbers]
odd_numbers = [str(item) for item in odd_numbers]

print(f"""Positive: {', '.join(positive_numbers)}
Negative: {', '.join(negative_numbers)}
Even: {', '.join(even_numbers)}
Odd: {', '.join(odd_numbers)}
""")
