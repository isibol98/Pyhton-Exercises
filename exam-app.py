
print('Welcome the English Tense Exam! You must answer 10 question and you must get minimum 60 points for pass the exam! Good luck :)')

class Question:
    def __init__(self,text,choices,answer):
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
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-'+ q)
        answer = input('Your Answer: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 10
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
            print('Exam has finished.')
        else:         
            self.displayProgress()  
            self.displayQuestion()

    def showScore(self):
        print('score: ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Exam has finished.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(60,'*'))


q1 = Question("Why do you live in Turkey?", ["present perfect", "present continous", "present simple"],"present simple")
q2 = Question("I am visiting my family.", ["present perfect", "present continous", "past simple"], "present continous")
q3 = Question("I haven't had breakfast yet.", ["present perfect", "past simple", "present continous"],"present perfect")
q4 = Question("I will study at home.", ["present simple", "future simple", "past simple"], "future simple")
q5 = Question("Did Petra call you yesterday?", ["present continous", "past simple", "present simple"],"past simple")
q6 = Question("The train had already gone.", ["past simple", "present perfect", "past perfect"], "past perfect")
q7 = Question("We will have finished by 6 p.m", ["future perfect", "future simple", "present simple"], "future perfect")
q8 = Question("Will he still be travelling this evening?", ["future simple", "past continous", "future continous"], "future continous")
q9 = Question("I wake up at 9 a.m", ["present simple", "present continous", "future simple"], "present simple")
q10 = Question("We are playing Warframe.", ["present simple", "past continous", "present continous"],"present continous") 

questions=[q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

quiz = Quiz(questions)

quiz.loadQuestion()

input("Press Enter to continue...")