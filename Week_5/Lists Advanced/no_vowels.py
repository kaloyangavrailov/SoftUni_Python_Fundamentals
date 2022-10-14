vowels = ['a', 'o', 'u', 'e', 'i']
word = input()
vowels_removed = [letter for letter in word if letter.lower() not in vowels]
print(''.join(vowels_removed))