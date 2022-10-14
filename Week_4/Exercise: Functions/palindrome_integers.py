def palindrome_or_not(item):
        if item == item[::-1]:
            return True
        else:
            return False


list_integers = input().split(', ')

for number in list_integers:
    print(palindrome_or_not(number))
