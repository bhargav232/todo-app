content = ['bhargav', 'ravi', 'purvish']
f = ['a.txt', 'b.txt', 'c.txt']
# task is that we need to load the content by mapping!
for i,j in zip(f,content):
    file = open(f"../files/{i}", "w")
    file.write(j)
