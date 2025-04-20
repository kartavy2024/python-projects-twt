que_ans = {
    "what does CPU stands for?":"central processing unit",
    "what does GPU stands for?":"graphics processing unit",
    "what does RAM stands for?":"random access memory",
    "what does PSU stands for?":"power supply"
}

question_number = 0
# function to fetch the quesions
def fetch_ans(question):
    ans = que_ans[question]
    return ans
def calculate_score(correct):
    percentage = (correct/len(que_ans))*100
    return percentage
score = 0
for question in que_ans:
    answer = input(f"{question} ")
    if answer.lower() == que_ans[question]:
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")

print(f"You Gave correct answers of {score} questions and your score is {calculate_score(score)}%")