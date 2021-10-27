import re

s = (input())
s = int(s)
s_list = list()

for i in range(s):
    s_list.append(input())

n = int(input())
i = 0
while i < n:
    st = str(input())
    for j in range(s):
        if re.match(s_list[j], st):
            print('YES,', j + 1)
            break
        if j == s - 1:
            print('NO,', 0)
    i = i + 1
