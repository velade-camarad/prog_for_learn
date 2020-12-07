#достаю файл в режиме чтения
import os
import codecs
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'files/test.txt')
file = codecs.open(filename, 'r', 'utf_8_sig')

#shitкод, который я не хочу объяснять, потому что сам хз как работает, но важно то, что он разбивает файл с тестом на массив
inner_massive = []
for i in file:
    inner_massive.append(i)
    
massive = [[0 for j in range(0)] for i in range(1000)]

end = 7
start = 0

for i in range(len(inner_massive)-1993):
    for j in range(start, end):
        massive[i].append(inner_massive[j])
    start+=7
    end+=7
#shitкод закончился



