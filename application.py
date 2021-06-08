import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame): 



    def __init__(self, master=None):
        tk.Frame.__init__(self, master) 
        self.grid(sticky=tk.E+tk.W) 
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',command=self.quit) 
        self.quitButton.grid(row=0, column=0, sticky=tk.E+tk.W)
        self.fileNames = filedialog.askopenfilenames(defaultextension=".pdf", filetypes={("*.pdf", ".pdf")})
        print(self.fileNames)

app = Application() 
app.master.title('Sample application') 
app.mainloop()