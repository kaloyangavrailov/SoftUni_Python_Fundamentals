def loading_bar(num):
    if num != 100:
        return print(f"{num}% [{num//10 * '%'}{(10 - num//10) * '.'}]\nStill loading...")
    else:
        print(f'100% Complete!\n[%%%%%%%%%%]')

number = int(input())

loading_bar(number)