print('Welcome the Math Exam! You must answer 5 question and you must get minimum 60 points for pass the exam! Good luck :)')

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer

class Exam:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question =self.getQuestion()
        self.displayProgress()
        print(f'Soru {self.questionIndex +1}: {question.text}')
        
        myChoices = ['A', 'B', 'C', 'D']
        for q in range(len(myChoices)):
            print((myChoices[q]) + '-' + question.choices[q])
            
        answer = (input('Your Answer: ')).upper()
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer) -> str:
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 20
        else:
            self.score -= 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
            print("Exam has finished!")
        else:
            self.displayQuestion()
            
    def showScore(self) ->int:
        print(f'Score: {self.score}')

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            pass
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(60,'*'))


q1 = Question('85-27 = ?', ['58', '45', '60', '68'], 'A')
q2 = Question('55/11 = ?', ['15', '5', '11', '0'], 'B')
q3 = Question('8x8 = ?', ['16', '48', '64', '88'], 'C')
q4 = Question('56/7 = ?', ['9', '7', '0', '8'], 'D')
q5 = Question('42/21+8 =?', ['20', '0', '24', '10'], 'D')
questions = [q1,q2,q3,q4,q5]
exam = Exam(questions)
exam.displayQuestion()

input("Press Enter to continue...")