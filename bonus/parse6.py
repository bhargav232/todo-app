def parse():
    user_input = input("please, enter feet and inch of the child: ")
    l = user_input.split(" ")
    feet = float(l[0])
    inch = float(l[1])
    return {'feet': feet, 'inch': inch}
