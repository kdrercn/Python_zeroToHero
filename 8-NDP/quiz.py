class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[quiz.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text} ')

        for q in question.choices:
            print("-"+ q)

        answer = input("cevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("Score : ",self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNum = self.questionIndex + 1

        if questionNum > totalQuestion:
            print("Quiz bitti. ")
        else:
            print(f"Question {questionNum} of {totalQuestion}".center(50,"*"))
    
q1 = Question("En iyi prog dili hangisidir ?", ["c#", "python", "javas", "java"], "python")
q2 = Question("En popüler prog dili hangisidir ?", ["python", "c#", "javas", "java"], "python")
q3 = Question("En çok kazandıran prog dili hangisidir ?", ["c#", "java", "python", "javas" ], "python")
q4 = Question("En çok sevilen prog dili hangisidir ?", ["c#", "java", "python", "javas" ], "python")
q5 = Question("En çok kolay prog dili hangisidir ?", ["c#", "java", "python", "javas" ], "python")

questions = [q1, q2, q3, q4, q5]


quiz = Quiz(questions)


quiz.loadQuestion()




