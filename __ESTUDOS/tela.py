from tkinter import *


class MinhaTela(Canvas):
    def __init__(self, master=None):


        self.widget1 =Frame(master,)

        self.widget1.pack(side=RIGHT)

        self.msg = Label(self.widget1, text='Ola mundo')
        self.msg.pack()

        self.btn = Button(self.widget1, text='OK')
        self.btn.pack()

        self.label1 = Label(self.widget1, text='Falaaaaa Magrão')
        self.label1.pack()



root = Tk()

MinhaTela(root)




root.mainloop()
