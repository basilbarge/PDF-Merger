import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame): 
    def __init__(self, master=None):
        tk.Frame.__init__(self, master) 
        self.fileNames = []
        self.fileLabels = []
        self.grid(sticky=tk.N+tk.S+tk.W+tk.E)
        self.createWidgets()

    def createWidgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.fileDialogButton = tk.Button(self, text='Browse',command=self.openFileExplorer) 
        self.fileDialogButton.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    def openFileExplorer(self):
        self.fileNames = filedialog.askopenfilenames(defaultextension=".pdf", filetypes={("*.pdf", ".pdf")})
        print(self.fileNames)
        for file in self.fileNames:
            self.fileLabels.append(tk.Label(self, text=file).grid(row=1, column=0))


app = Application() 
app.master.title('PDF Merger') 
app.mainloop()