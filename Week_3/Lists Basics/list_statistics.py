number_iterations = int(input())
negative_list = []
positive_list = []
for iteration in range(number_iterations):
    number = int(input())
    if number < 0:
        negative_list.append(number)
    else:
        positive_list.append(number)

print(f"""
{positive_list}
{negative_list}
Count of positives: {len(positive_list)}
Sum of negatives: {sum(negative_list)}
""")