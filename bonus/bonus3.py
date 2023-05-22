# take password from the user and check weather its strong or not based on 3 conditions:
# 1) contain atlest 8 characters
# 2) must contain numbers
# 3) atleast have one upper case letter
while True:
    result = {}
    pwd = input('please enter a password : \n ')
    l = len(pwd)

    p = False
    if l >= 8:
         p = True

    result['length'] = p

    digit = False
    for i in pwd:
        if i.isdigit():
            digit = True
    result['digit'] = digit

    upper = False
    for j in pwd:
        if j.isupper():
            upper = True
    result['upper_case'] = upper

    print(result)

    if all(result.values()):
        print('strong password')
    else:
        print('weak password! ')

