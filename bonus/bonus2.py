date = input('enter a date: ')
mood = input("rate your today's mood from 0 to 10: ")
idea = input("Enter today's quote:\n")
with open(f"../files/{date}.txt", 'w') as file:
    file.writelines(mood + 2*'\n')
    file.writelines(idea)