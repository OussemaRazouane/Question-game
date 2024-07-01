class QuizBrain:
    def __init__(self, quiz_data:list)->None:
        """Construct"""
        self.question_number =0
        self.quiz_data = quiz_data
    
    def next_question(self):
        """Give you the next question if the question_number is correct"""
        if self.question_number < len(self.quiz_data):
            answer = input(f"Q.{self.question_number+1}:{self.quiz_data[self.question_number].txt} (True/False): ")
            self.question_number = self.question_number +1
        else:
            print("Question are terminated")