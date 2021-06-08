from os import defpath
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class Application(tk.Frame): 
    def __init__(self, master=None):
        tk.Frame.__init__(self, master) 
        self.fileNames = []
        self.fileLabels = []
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.filePathEntry = ttk.Entry(self)
        self.filePathEntry.grid(row=0, column=0)

        self.enterButton = ttk.Button(self, text="Enter")
        self.enterButton.grid(row=0, column=1)

        self.fileDialogButton = ttk.Button(self, text='Browse',command=self.openFileExplorer) 
        self.fileDialogButton.grid(row=0, column=2, columnspan=2, padx=5, pady=5)


    def openFileExplorer(self):
        self.fileNames = tk.filedialog.askopenfilenames(defaultextension=".pdf", 
                                                        filetypes={("*.pdf", ".pdf")})
        for index in range(len(self.fileNames)):
            currentFileName = self.fileNames[index]
            self.fileLabels.append(ttk.Label(self, text=currentFileName).grid(row=index + 1, column=0))


app = Application() 
app.master.title('PDF Merger') 
app.mainloop()