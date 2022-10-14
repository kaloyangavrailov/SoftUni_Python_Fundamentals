list_of_words = input().split()
palindrome = input()
list_of_palindromes = [item for item in list_of_words if item == item[::-1]]

print(list_of_palindromes)
print(f'Found palindrome {list_of_palindromes.count(palindrome)} times')
