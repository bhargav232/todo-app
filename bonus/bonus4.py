# we need to write a code which ask user to enter width and length of the retengle
# and check if the entered value is number or not and also check if the width and length are same
# or not (because if they are same its seems as square)
while 1:
    try:
        length = float(input('Enter the length of the rectangle: '))
        width = float(input('Enter the width of the rectangle: '))
        if length == width:
            print('Soory, but it seems like square enter other value!')
            continue
        area = (length) * (width)
        print(f"Area of rectangle is {area}")
    except ValueError:
        print('Enter a valid number!')
