from data import question_data


class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer


end_game = 0
score =0
i = 0
while not end_game:
    for new_question in question_data:
        i+=1
        question = Question(new_question["question"],new_question["correct_answer"])
        queans = input(f"Q{i}. {question.text} True or False :- ")

        if queans == question.answer:
            score +=1
            print("Correct answer")
            print(score,"/",i)
        elif  i>10:
            print("Hushhh That's all Your final score is :-",score)
            end_game = 1
            break

        else:
            print("wrong answer")
            print(score,"/",i)




