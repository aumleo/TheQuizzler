from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375365"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain) : #specify datatype - QuizBrain
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=35, pady= 40, bg = THEME_COLOR)
        
        self.score_label = Label(text = "Score: 0", fg = "white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width = 300, height=250, bg = 'white')
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width = 275, 
            text='', 
            fill=THEME_COLOR,
            font=('Arial', 21, 'italic' )
        )
        self.canvas.grid(row=1, column=0,columnspan=2,pady = 50)

        true_image = PhotoImage(file='images/true.png')
        self.true = Button(image=true_image, highlightthickness=0, command=self.true_press)
        self.true.grid(row =2, column = 0)

        false_image = PhotoImage(file='images/false.png')
        self.false = Button(image=false_image, highlightthickness=0, command=self.false_press)
        self.false.grid(row =2, column = 1)

        self.get_next_q()

        self.window.mainloop()

    def get_next_q (self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'SCORE : {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = 'END OF QUIZ')
            self.true.config(state='disabled')
            self.false.config(state='disabled')

    def true_press(self):
        is_correct = self.quiz.check_answer('True')
        self.feedback(is_correct)

    def false_press(self):
        is_correct = self.quiz.check_answer('False')
        self.feedback(is_correct)

    def feedback(self, right):
        if right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.reset_feedback)


    def reset_feedback(self):
        self.canvas.config(bg='white')
        self.get_next_q()
