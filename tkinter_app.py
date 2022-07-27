from tkinter import *
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText

class Data:
    def __init__(self):
        self.connectionString = ''

    def list_of_Groups(self):
        list = ['Comp1', 'Comp2','Comp3','Comp4']
        return list

    def list_of_Dates(self):
        list = ['2022/02', '2022/03','2022/04','2022/05']
        return list

class MainGUI(Data):
    spacer = 50

    def __init__(self, win):

        self.GroupLabel=Label(win, text='Group Name')
        self.GroupCB = Combobox(win, values = Data.list_of_Groups(self))
        self.GroupLabel.place(x=100, y=50)
        self.GroupCB.place(x=200, y=50)

        self.ConfDateLabel=Label(win, text='Confirmed date')
        self.ConfDateCB = Combobox(win, values = Data.list_of_Dates(self))
        self.ConfDateLabel.place(x=100, y=100)
        self.ConfDateCB.place(x=200, y=100)

        self.commentLabel=Label(win, text='Insert comments')
        self.commentValue = ScrolledText(win, width = 30, height =5, relief="raised")
        self.commentLabel.place(x=170, y=145)
        self.commentValue.place(x=100, y=170)


        self.b1=Button(win, text='Update in db', command=self.print_smh)
        self.b1.place(x=200, y=300)

    def print_smh(self):

        Val1=str(self.GroupCB.get())
        Val2=str(self.ConfDateCB.get())
        Val3=str(self.commentValue.get("1.0", END))
        result=Val1+Val2+Val3
        print(result)



window=Tk()
mywin= MainGUI(window)
window.title('Hello Python')
window.geometry("430x400+10+10")
window.mainloop()
