word_list = input().split()
[print(item) for item in word_list if len(item) % 2 == 0]
