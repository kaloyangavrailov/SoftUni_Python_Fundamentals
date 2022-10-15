software_version = input().split('.')
software_version = [int(item) for item in software_version]

for index in range(len(software_version)-1,-1,-1):
    software_version[index] += 1
    if software_version[index] > 9:
        software_version[index] = 0
        software_version[index-1] += 1
        if software_version[index-1] > 9:
            software_version[index - 1] = 0
            software_version[index-2] += 1
    break
print('.'.join(str(item) for item in software_version))