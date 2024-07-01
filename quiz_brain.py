class QuizBrain:
    def __init__(self, quiz_data:list)->None:
        """Construct"""
        self.question_number =0
        self.quiz_data = quiz_data
        self.score=0
    def still_has_question(self)->bool:
        """Return True if still there is question"""
        return self.question_number< len(self.quiz_data)
    def next_question(self):
        """Give you the next question"""
        answer = input(f"Q.{self.question_number+1}:{self.quiz_data[self.question_number].txt} (True/False): ")
        self.question_number+=1
        self.check_answer(answer=answer,corect_anwser=self.quiz_data[self.question_number-1].ans)
    def check_answer(self, answer:str,corect_anwser:str):
        """Check if the answer is correct"""
        if answer.lower() == corect_anwser.lower():
            print("Correct!")
            self.score+=1
        else:
            print(f"Wrong! The correct answer is: {corect_anwser}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")