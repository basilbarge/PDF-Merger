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

        self.fileDialogButton = ttk.Button(self, text='Browse',command=self.openFileExplorer) 
        self.fileDialogButton.grid(row=0, column=0, padx=5, pady=5)

        self.mergePDFButton = ttk.Button(self, text="Merge")
        self.mergePDFButton.grid(row=0, column=1, padx=5, pady=5)


    def openFileExplorer(self):
        self.fileNames = tk.filedialog.askopenfilenames(defaultextension=".pdf", 
                                                        filetypes={("*.pdf", ".pdf")})
        for index in range(len(self.fileNames)):
            currentFilePath = self.fileNames[index]
            currentFilePath = currentFilePath.split("/")

            lastSplitItemIndex = len(currentFilePath) - 1
            currentFileName = currentFilePath[lastSplitItemIndex]

            self.fileLabels.append(ttk.Label(self, text=currentFileName).grid(row=index + 1, column=0, columnspan=2))


app = Application() 
app.master.title('PDF Merger') 
app.mainloop()