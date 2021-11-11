# add_cascade

import tkinter as tk
import tkinter.messagebox as ms # get standard dialogs

class App():
    def __init__(self, root):
        # Tk8.0 style top-level window menus
        top = tk.Menu(root)  # σύνδεση του μενού top με το παράθυρο root
        root.geometry('800x400')
        root.config(menu=top)  # επίσης σύνδεσε το παράθυρο με το μενού

###################################################################
        for i, name in enumerate(['Εσπεριδοειδή', 'Μουροειδή', 'Εμπύρηνοι καρποί', 'Τροπικά φρούτα', 'Πεπονοειδή', 'Σαρκώδη φρούτα', 'Φρουτώδη λαχανικά']):

            menu = 'menu' + str(i)
            menu = tk.Menu(top, tearoff=False)

            top.add_cascade(label=name, menu=menu, underline=0)
            frouto1 = tk.Menu(menu, tearoff=True)
            menu.add_cascade(label='Φρούτο1', menu=frouto1, underline=0)
            frouto1.add_command(label='Φώτο', command=root.quit, underline=0)
            frouto1.add_command(label='Περιγραφή', command=self.notdone, underline=0)

            frouto2 = tk.Menu(menu, tearoff=True)
            menu.add_cascade(label='Φρούτο2', menu=frouto2, underline=0)
            frouto2.add_command(label='Φώτο', command=root.quit, underline=0)
            frouto2.add_command(label='Περιγραφή', command=self.notdone, underline=0)

    def notdone(self):
        ms.showerror('Not implemented', 'Not yet available')

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()