def run_quiz():
    questions = [
        "What is the capital of India?\na) Mumbai\nb) Delhi\nc) Goa\n",
        "Which language is used for AI?\na) Python\nb) HTML\nc) CSS\n"
    ]
    answers = ["b", "a"]
    score = 0
    
    for i in range(len(questions)):
        print(questions[i])
        user_ans = input("Your answer: ").lower()
        if user_ans == answers[i]:
            score += 1
            print("Correct!\n")
        else:
            print("Wrong Answer!\n")
            
    print("Quiz finished! Your final score is:", score, "/", len(questions))

def main():
    run_quiz()

main()
