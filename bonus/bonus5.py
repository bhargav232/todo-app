def get_temp():
    with open('../files/temp.txt', 'r') as f:
       t = f.readlines()[1:]
    return t

li = get_temp()
p = len(li)
sum = 0
for i in li:
    sum = sum+int(i)
avg = sum/p
print(f'Average temp is: {avg}')


