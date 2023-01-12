class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.correctAnswers = 0
        self.numQuestions = len(questions)

    def run_questions(self):
        qNum = 1
        for question in self.questions:
            answer = input(f"Q {qNum}: {question.text} True or False? ").lower()
            qNum += 1
            if answer == question.answer:
                self.correctAnswers += 1
        
    def get_results(self):
        print(f"You got {self.correctAnswers} out of {self.numQuestions}")