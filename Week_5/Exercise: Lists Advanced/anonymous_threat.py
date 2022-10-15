def merge_function(start, end, list_of_strings):
    merged_element = ''
    copy_list = list_of_strings.copy()
    if int(end) > len(list_of_strings):
        if int(start) > len(list_of_strings):
            return list_of_strings
        for index in range(int(start), len(copy_list) + 1):
            if index > len(list_of_strings)+1:
                break
            merged_element += copy_list[index]
            list_of_strings.remove(list_of_strings[int(start)])
    else:
        for index in range(int(start),int(end)+1):
            merged_element += copy_list[index]
            list_of_strings.remove(list_of_strings[int(start)])
    list_of_strings.insert(int(start),merged_element)
    return list_of_strings


def divide_function(position_index,partition, list_of_strings):
    if len(list_of_strings[int(position_index)]) % int(partition) == 0:
        word = list_of_strings[int(position_index)]
        list_of_strings.remove(word)
        step = len(word) / int(partition)
        for char in range(0,len(word),int(step)):
            list_of_strings.append(word[char:char+2])
        return list_of_strings
    else:
        word = list_of_strings[int(position_index)]
        list_of_strings.remove(word)
        word = [item for item in word]
        word_list = []
        for index in range(partition):
            if index == partition-1:
                word_list.append(''.join(word))
            else:
                word_list.append(word[0])
                word.remove(word[0])
        word_list = word_list[::-1]
        for index in range(0,int(partition)):
            list_of_strings.insert(index,word_list.pop())
        return list_of_strings


array_data_list = input().split()
list_strings = []
while True:
    command = input()
    if command == '3:1':
        break
    else:
        command,index_1,index_2 = command.split()
        if command == 'merge':
            list_strings = merge_function(index_1,index_2,array_data_list)
        elif command == 'divide':
            list_strings = divide_function(index_1,index_2,array_data_list)

print(' '.join(list_strings))