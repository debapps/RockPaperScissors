import random
from tkinter import *
from tkinter import ttk

#
# This class defines the main GUI and fuctionality of Rock-Paper-Scissors Game.
#
class RockPaperScissors:

    # Declare the common variables.

    CHOICE = ['Rock', 'Paper', 'Scissors']

    # RPSWinDict is the winnablity matrix where the Key is a tuple of user input and Computer choice.
    # The value is the score of the game.

    RPSWinDict = {
        ('Rock', 'Rock') : ('It is a Tie!!\n', 0, 0),
        ('Paper', 'Paper') : ('It is a Tie!!\n', 0, 0),
        ('Scissors', 'Scissors') : ('It is a Tie!!\n', 0, 0),
        ('Rock', 'Paper') : ('Oppss !!! You Lose!\nPaper beats Rock.\n\n', 0, 1),
        ('Rock', 'Scissors') : ('Wow! You WIN !!\nRock beats Scissors.\n\n', 1, 0),
        ('Paper', 'Rock') : ('Wow! You WIN !!\nPaper beats Rock.\n\n', 1, 0),
        ('Paper', 'Scissors') : ('Oppss !!! You Lose!\nScissors beats Paper.\n\n', 0, 1),
        ('Scissors', 'Rock') : ('Oppss !!! You Lose!\nRock beats Scissors.\n\n', 0, 1),
        ('Scissors', 'Paper') : ('Wow! You WIN !!\nScissors beats Paper.\n\n', 1, 0)
    }

    def __init__(self, master):

        # Putting Additional Style.
        self.bgcolor = '#ddfc03'
        self.fgcolor = 'purple'

        master.title('Rock-Paper-Scissors Game')
        master.geometry('400x250+500+200')
        master.resizable(False,False)
        master.configure(background = self.bgcolor)

        self.style = ttk.Style()
        self.style.configure('TButton', font = ('Comic Sans MS', 11, 'bold'), foreground = self.fgcolor)
        self.style.configure('TFrame', background = self.bgcolor)
        self.style.configure('TLabel', background = self.bgcolor, font = ('Comic Sans MS', 11, 'bold'),
                              foreground = self.fgcolor)
        

        # Creating frames
        self.headerFrame = ttk.Frame(master)
        self.buttonFrame = ttk.Frame(master)
        self.scoreFrame = ttk.Frame(master)

        # Geometry Manager Methods
        self.headerFrame.pack()
        self.buttonFrame.pack()
        self.scoreFrame.pack()

        # Creating Heder Label.
        ttk.Label(self.headerFrame, text = 'Rock-Paper-Scissors Game').pack()

        # Creating input Buttons
        ttk.Button(self.buttonFrame, text = 'Rock',
        command = lambda: self.RPSGameProcess('Rock')).grid(row = 0, column = 0, padx = 10, pady = 10)
        ttk.Button(self.buttonFrame, text = 'Paper',
        command = lambda: self.RPSGameProcess('Paper')).grid(row = 0, column = 1, padx = 10, pady = 10)
        ttk.Button(self.buttonFrame, text = 'Scissors',
        command = lambda: self.RPSGameProcess('Scissors')).grid(row = 0, column = 2, padx = 10, pady = 10)

        # Creating the score Text Area.
        self.scoreBoard = Text(self.scoreFrame, width = 50, height = 10, wrap = 'word', 
                               font = ('Courier New', 10), bg = '#eaf984', fg = self.fgcolor)
        # Geometry Manager Method.
        self.scoreBoard.pack(fill = BOTH, expand = True, padx = 10, pady = 10)

        # Showing the initial score.
        self.scoreStr = 'Press Rock/Paper/Scissors Button to START.\n'
        self.userScoreInt = 0
        self.compScoreInt = 0
        self.showScore([self.scoreStr, self.userScoreInt, self.compScoreInt])

    #
    # This method clears the Text Area Score Board.
    #
    def clearScore(self):
        self.scoreBoard.delete(1.0, END)
        self.scoreBoard.delete(2.0, END)
        self.scoreBoard.delete(3.0, END)
        self.scoreBoard.delete(4.0, END)
        self.scoreBoard.delete(5.0, END)
        self.scoreBoard.delete(6.0, END)
        self.scoreBoard.delete(7.0, END)
        self.scoreBoard.delete(8.0, END)
        self.scoreBoard.delete(9.0, END)

    #
    # This method shows the score board in the Text Area.
    #
    def showScore(self, scoreTuple, drawTup = ()):
        # Get the Draws.
        if drawTup:
            self.userInput = drawTup[0]
            self.compInput = drawTup[1]
        else:
            self.userInput = ''
            self.compInput = ''

        # Get the score.
        self.scoreStr = scoreTuple[0]
        self.userScoreInt += scoreTuple[1]
        self.compScoreInt += scoreTuple[2]

        # Clear the previous score.
        self.clearScore()

        # Update the new score.
        self.scoreBoard.insert(1.0, 'Rock-Paper-Scissors Score Board\n')
        self.scoreBoard.insert(2.0, '-------------------------------\n\n\n')
        self.scoreBoard.insert(3.0, self.scoreStr)
        self.scoreBoard.insert(6.0, 'Your Draw = {} \t Computer Draw = {}\n'.format(self.userInput, self.compInput))
        self.scoreBoard.insert(7.0, 'Your Score       Computer Score\n')
        self.scoreBoard.insert(8.0, '----------       --------------\n')
        self.scoreBoard.insert(9.0, '     {}                 {}'.format(self.userScoreInt, self.compScoreInt))

    #
    # This method takes the user input from the Buttons and gets the Computer random choice and declares
    # the winner in the score board.
    #
    def RPSGameProcess(self, userInput):
        # Get the Computer random Choice.
        self.compInput = random.choice(RockPaperScissors.CHOICE)

        # Create the tuple with user input and computer input.
        self.drawTuple = tuple([userInput, self.compInput])

        # Get the game score tuple.
        self.scoreTup = RockPaperScissors.RPSWinDict[self.drawTuple]

        # show the score in Text Area scoreBoard.
        self.showScore(self.scoreTup, self.drawTuple)


def main():
    root = Tk()
    RPSApp = RockPaperScissors(root)
    root.mainloop()

if __name__ == '__main__':
    main()
