import json
with open("question.json", "r") as file:
    content = file.read()
a = json.loads(content)


for que in a:
    print(que["que_text"])
    for i,j in enumerate(que["Alternatives"]):
        print(f"{i+1} - {j}")
    user_input = int(input("enter your answer?: "))
    que["user_ans"] = user_input

score =0
flag = True
for result in a:
    if result["user_ans"] == result["correct_ans"]:
        score = score+1
    else:
        flag = False
    print(f"{flag}, your ans: {result['user_ans']}, correct ans: {result['correct_ans']}")

print(f" your score is {score} / {len(a)}")
