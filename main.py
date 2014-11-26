__author__ = 'Java'
i = 0
mathSum = 0
physicSum = 0
rusSum = 0

with open('data8.txt') as source:
    for line in source:
        line = line.strip()
        arr = line.split(';')
        i += 1
        mathSum += int(arr[1])
        physicSum += int(arr[2])
        rusSum += int(arr[3])
        print((int(arr[1])+int(arr[2])+int(arr[3]))/3)
print(mathSum/i,physicSum/i,rusSum/i)



