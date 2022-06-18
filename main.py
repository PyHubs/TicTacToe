from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
root.resizable(0,0)
root.attributes('-alpha', 0.87)

# Frame
window = Frame(root, bg='#202020')

# X starts so true
clicked = True
count = 0

def Reset():
	global b1, b2, b3, b4, b5, b6, b7, b8, b9
	global clicked, count
	clicked = True
	count = 0

	#confuring a bg
	b1.configure(text=" ", bg="#202020", borderwidth=0, state="normal")
	b2.configure(text=" ", bg="#202020", borderwidth=0, state="normal")
	b3.configure(text=" ", bg="#202020", borderwidth=0, state="normal")
	b4.configure(text=" ", bg="#202020", borderwidth=0, state="normal")
	b5.configure(text=" ", bg="#202020", borderwidth=0, state="normal")
	b6.configure(text=" ", bg="#202020", borderwidth=0, state="normal")
	b7.configure(text=" ", bg="#202020", borderwidth=0, state="normal")
	b8.configure(text=" ", bg="#202020", borderwidth=0, state="normal")
	b9.configure(text=" ", bg="#202020", borderwidth=0, state="normal")


def disable_all_buttons():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)

#check to see if somone won
def checkifwon():
	global winner
	winner = False

	if b1['text'] == "X" and b4['text'] == 'X' and b7 ['text'] == 'X':
		b1.config(bg="#87A96B")
		b4.config(bg="#87A96B")
		b7.config(bg="#87A96B")
		winner = True
		messagebox.showinfo("Winner", "CONGRATULATIONS!, X wins!")
		disable_all_buttons()

	elif b2['text'] == "X" and b5['text'] == 'X' and b8 ['text'] == 'X':
		b2.config(bg="#87A96B")
		b5.config(bg="#87A96B")
		b8.config(bg="#87A96B")
		winner = True
		messagebox.showinfo("Winner", "CONGRATULATIONS!, X wins!")
		disable_all_buttons()

	elif b3['text'] == "X" and b6['text'] == 'X' and b9 ['text'] == 'X':
		b3.config(bg="#87A96B")
		b6.config(bg="#87A96B")
		b9.config(bg="#87A96B")
		winner = True
		messagebox.showinfo("Winner", "CONGRATULATIONS!, X wins!")
		disable_all_buttons()

	elif b1['text'] == "X" and b5['text'] == 'X' and b9 ['text'] == 'X':
		b1.config(bg="#87A96B")
		b5.config(bg="#87A96B")
		b9.config(bg="#87A96B")
		winner = True
		messagebox.showinfo("Winner", "CONGRATULATIONS!, X wins!")
		disable_all_buttons()

	elif b3['text'] == "X" and b5['text'] == 'X' and b7 ['text'] == 'X':
		b3.config(bg="#87A96B")
		b5.config(bg="#87A96B")
		b7.config(bg="#87A96B")
		winner = True
		messagebox.showinfo("Winner", "CONGRATULATIONS!, X wins!")
		disable_all_buttons()

	elif b1['text'] == "X" and b2['text'] == 'X' and b3 ['text'] == 'X':
		b1.config(bg="#87A96B")
		b2.config(bg="#87A96B")
		b3.config(bg="#87A96B")
		winner = True
		messagebox.showinfo("Winner", "CONGRATULATIONS!, X wins!")
		disable_all_buttons()

	elif b4['text'] == "X" and b5['text'] == 'X' and b6['text'] == 'X':
		b4.config(bg="#87A96B")
		b5.config(bg="#87A96B")
		b6.config(bg="#87A96B")
		winner = True
		messagebox.showinfo("Winner", "CONGRATULATIONS!, X wins!")
		disable_all_buttons()

	elif b7['text'] == "X" and b8['text'] == 'X' and b9['text'] == 'X':
		b7.config(bg="#87A96B")
		b8.config(bg="#87A96B")
		b9.config(bg="#87A96B")
		winner = True
		messagebox.showinfo("Winner", "CONGRATULATIONS!, X wins!")
		disable_all_buttons()

	elif b1['text'] == "O" and b4['text'] == 'O' and b7 ['text'] == 'O':
		b1.config(bg="#87A96B")
		b4.config(bg="#87A96B")
		b7.config(bg="#87A96B")
		winner = True
		messagebox.showinfo("Winner", "CONGRATULATIONS!, O wins!")
		disable_all_buttons()

	elif b2['text'] == "O" and b5['text'] == 'O' and b8 ['text'] == 'O':
		b2.config(bg="#87A96B")
		b5.config(bg="#87A96B")
		b8.config(bg="#87A96B")
		winner = True
		messagebox.showinfo("Winner", "CONGRATULATIONS!, O wins!")
		disable_all_buttons()

	elif b3['text'] == "O" and b6['text'] == 'O' and b9 ['text'] == 'O':
		b3.config(bg="#87A96B")
		b6.config(bg="#87A96B")
		b9.config(bg="#87A96B")
		winner = True
		messagebox.showinfo("Winner", "CONGRATULATIONS!, O wins!")
		disable_all_buttons()

	elif b1['text'] == "O" and b5['text'] == 'O' and b9 ['text'] == 'O':
		b1.config(bg="#87A96B")
		b5.config(bg="#87A96B")
		b9.config(bg="#87A96B")
		winner = True
		messagebox.showinfo("Winner", "CONGRATULATIONS!, O wins!")
		disable_all_buttons()

	elif b3['text'] == "O" and b5['text'] == 'O' and b7 ['text'] == 'O':
		b3.config(bg="#87A96B")
		b5.config(bg="#87A96B")
		b7.config(bg="#87A96B")
		winner = True
		messagebox.showinfo("Winner", "CONGRATULATIONS!, O wins!")
		disable_all_buttons()

	elif b1['text'] == "O" and b2['text'] == 'O' and b3 ['text'] == 'O':
		b1.config(bg="#87A96B")
		b2.config(bg="#87A96B")
		b3.config(bg="#87A96B")
		winner = True
		messagebox.showinfo("Winner", "CONGRATULATIONS!, O wins!")
		disable_all_buttons()

	elif b4['text'] == "O" and b5['text'] == 'O' and b6['text'] == 'O':
		b4.config(bg="#87A96B")
		b5.config(bg="#87A96B")
		b6.config(bg="#87A96B")
		winner = True
		messagebox.showinfo("Winner", "CONGRATULATIONS!, O wins!")
		disable_all_buttons()

	elif b7['text'] == "O" and b8['text'] == 'O' and b9['text'] == 'O`':
		b7.config(bg="#87A96B")
		b8.config(bg="#87A96B")
		b9.config(bg="#87A96B")
		winner = True
		messagebox.showinfo("Winner", "CONGRATULATIONS!, O wins!")
		disable_all_buttons()

	elif count == 9 and winner == False:
			messagebox.showinfo("Winner", "It is a tie!\nno one wins, try starting a new match")
			disable_all_buttons()

def b_click(b):
	global clicked, count

	if b["text"] == " " and clicked == True:
		b["text"] = 'X'
		clicked = False
		count += 1
		checkifwon()
	elif b["text"] == " " and clicked == False:
		b["text"] = 'O'
		clicked = True
		count += 1
		checkifwon()
	else:
		messagebox.showerror("Error", "That box has already been used \nUse another box")

#buttons
b1= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#202020",command= lambda: b_click(b1))
b2= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#202020",command= lambda: b_click(b2))
b3= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#202020",command= lambda: b_click(b3))

b4= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#202020",command= lambda: b_click(b4))
b5= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#202020",command= lambda: b_click(b5))
b6= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#202020",command= lambda: b_click(b6))

b7= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#202020",command= lambda: b_click(b7))
b8= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#202020",command= lambda: b_click(b8))
b9= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#202020",command= lambda: b_click(b9))

def about_command():
	messagebox.showinfo("About", 'Well you know how to make tic tac toe lol')

def show_help_command():
	messagebox.showinfo('Help', "Mail izooizkaan@outlook.com to get any help")

# Bottom frame
btframe = Frame(root, bg='#5A7988', bd=1, height=2)
btframe.pack(fill='x', side='top')

# Button
RESET_BTN = Button(btframe, activebackground='#5A7988', activeforeground='lightgrey', bg='#5A7988', font=("Helvetica", 11), fg='white', text=' Reset ', anchor=W, borderwidth=0, command=Reset)
RESET_BTN.grid(row=0, column=0)

# About
ABOUT_BTN = Button(btframe, activebackground='#5A7988', activeforeground='lightgrey', bg='#5A7988', font=("Helvetica", 11), fg='white', text='About ', anchor=W, borderwidth=0, command=about_command)
ABOUT_BTN.grid(row=0, column=1)

# Help
HELP_BTN = Button(btframe, activebackground='#5A7988', activeforeground='lightgrey', bg='#5A7988', font=("Helvetica", 11), fg='white', text='Help ', anchor=W, borderwidth=0, command=show_help_command)
HELP_BTN.grid(row=0, column=2)

# Quit
QUIT_BTN = Button(btframe, activebackground='#5A7988', activeforeground='lightgrey', bg='#5A7988', font=("Helvetica", 11), fg='white', text='Quit ', anchor=W, borderwidth=0, command=lambda:root.quit())
QUIT_BTN.grid(row=0, column=3)

#grid buttons
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

#confuring a bg
b1.configure(bg="#202020", fg='white', borderwidth=0, activebackground='#202020', activeforeground='red')
b2.configure(bg="#202020", fg='white', borderwidth=0, activebackground='#202020', activeforeground='red')
b3.configure(bg="#202020", fg='white', borderwidth=0, activebackground='#202020', activeforeground='red')
b4.configure(bg="#202020", fg='white', borderwidth=0, activebackground='#202020', activeforeground='red')
b5.configure(bg="#202020", fg='white', borderwidth=0, activebackground='#202020', activeforeground='red')
b6.configure(bg="#202020", fg='white', borderwidth=0, activebackground='#202020', activeforeground='red')
b7.configure(bg="#202020", fg='white', borderwidth=0, activebackground='#202020', activeforeground='red')
b8.configure(bg="#202020", fg='white', borderwidth=0, activebackground='#202020', activeforeground='red')
b9.configure(bg="#202020", fg='white', borderwidth=0, activebackground='#202020', activeforeground='red')

window.pack()

root.mainloop()
