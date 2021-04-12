from tkinter import *
import random

root = Tk()
root.title("Roll Dice")
root.geometry("1080x720")
root.wm_minsize(720,480)
root.wm_maxsize(1240,920)

label = Label(root,font=('Algerian',150,'bold'),text='')
label1 = Label(root,font=('Algerian',40),text='')
label2 = Label(root,font=('helvetica',20,'bold'),text='')
label3 = Label(root,font=('Lucida Calligraphy',15,'italic'),text='')

sum_dice1 = 0
count = 0
con = TRUE
sum_dice2 = 0

def rolldice():
    global sum_dice1
    global sum_dice2
    global con
    global count
    if con:

        dice_dict = {'\u2680': 1, '\u2681': 2, '\u2682': 3, '\u2683': 4, '\u2684': 5, '\u2685': 6}
        box = random.choice(list(dice_dict.keys()))
        label.configure(text=box)
        label.pack()

        if count%2 == 0:
            sum_dice1 += dice_dict[box]
        else:
            sum_dice2 += dice_dict[box]

        count += 1

        if dice_dict[box] == 6:
            label3.configure(text="\nCongratulations !! \n You got 6 on Dice\n Plz play your bonus rolll")
            label3.pack()
            count -= 1
        else:
            label3.configure(text="")
            label3.pack()

        label1.configure(text="\n Player1: " + str(sum_dice1) + "\t Player2: " + str(sum_dice2))
        label1.pack()

        if sum_dice1 >= 100:
            player = "Player1"
        elif sum_dice2 >= 100:
            player = "Player2"


        if sum_dice1 >= 100 or sum_dice2 >= 100:
            label2.configure(text="Congratulations!!!! \n " + player + " is a Winner \n Press Exit to leave the game")
            label2.pack()
            button1 = Button(root, font=('Courier10 BT', 25), text='Exit', command=root.destroy, bg="yellow")
            button1.pack()
            con = FALSE



button = Button(root, font=('Forte', 25, 'bold'), text='Roll Dice', command=rolldice, bg="violet")
button.pack()

root.mainloop()
