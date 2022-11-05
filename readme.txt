Noughts and Crosses(tic tac toe) is a simple game played by two people.

 

The object of Noughts and Crosses is to get a winning line of three Noughts or three Crosses in either a horizontal, vertical or diagonal row.

 

The Noughts and Crosses board is a square grid containing nine squares arranged in threes.

 

The game is played by two people who either play as Noughts (Os) or Crosses ( Xs)


Though Simple it never fails to cheer up a person from boredom



Here is a program to create this game using Python


Let us run you through our code


First we have some libraries imported namely Tkinter and the random.

In Tkinter the Font,Simple dialoguebox,message box functions are imported which are used to enhance the program


######Step 1
We create The window 1
This is an opening window Wherein the users(or players) input their Names for the game
Win.title used to give the window a title and win.state zoom to open the window full screne
A background image is chosen and applied using PhotoImage Function


There is a simple start button in the window
on pressing it the interface asks the user to input his names.This is achieved by the SimpleDialogueBox command
On entering the names The button Changes its text to Lets Play and the ShowFrame fuction is invoked
What the Showframe function does is simple, It Just Withdraws the window thus closing it using the win.withdraw command

Various fonts and colours are added to the text to make it eye catching.


#######Step 2
Creating the Game window

First a function is created named button to create a basic button which is used further in the program
The button is created using the Button function
and its length ,Width ,colour,font to be used inside the button are all specified within this function itself


Second, A Change function is created which toggles the value of the click between X and O alternatively
This is achieved by an if statement

Next, The Reset function, This function creates the 3X3 grids required to play the game
This function serves the purpose of resetting the grids once the game is over, back to its narmal state
The grids are created using 2 nested for loops each with a range of 3
It also decides as to which player is assigned with an x and an o and who gets to play first Randomly using Random function

Check Function:
This is the main algorihm of the program which decides as to who won or if the game is a draw
The function is invoked after every move and it checks if a certain player has won using the series of if and elif functions
This if function checks if there is any line of three along vertical horizontal or diagonal of any player
There are 8 possibilities for each player to win which is checked using the grid name in each if statement

If the first if statement satisfies , this means that the first player has won and this is displayed using the messagebox and the reset function is called here
If not the elif statement is checked for the victory of the second player
If none of them satisfy then the else statement is used to mention that the game has ended in a draw and the board is reset


Lastly the click function :
This function defines what has to be done on a click by the user. Here the change function is called to decide as to what is displayed in that particular button
The click function ensures that a button once clicked cannot be clicked again by mentioning its state to be disabled after the click
It also displays as to whose chance it is to play using the lable.config function


These are the functions used in the window 2
Now a window is created using tkinter and a title is added
The Choice as to who is assigned x and o is decided randomly
Again various colours and fonts are input to display the text in an attractive manner
The root.mainloop plays an integral role to keep the function open


The end