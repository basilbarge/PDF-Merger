import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pdfmerger import PDFMerger
import time

class Application(tk.Frame): 
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master) 
        self.fileNames = []
        self.fileLabels = []
        self.outputFileName = ""
        self.pdfMerger = None
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

        self.mergePDFButton = ttk.Button(self, text="Merge", command=self.mergePDFs)
        self.mergePDFButton.grid(row=0, column=1, padx=5, pady=5)
        
        self.PDFLabelFrame = ttk.Labelframe(self, text="PDFs to Merge")
        self.PDFLabelFrame.grid(row=1, column=0, columnspan=2)

        self.progressMarker = None


    def openFileExplorer(self):
        self.fileNames = filedialog.askopenfilenames(defaultextension=".pdf", filetypes={("*.pdf", ".pdf")})
        
        self.__clearPDFLabelFrame()

        self.__createChosenPDFLabels(self.fileNames)
        
    def mergePDFs(self):
        self.outputFileName = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes={("*.pdf", ".pdf")})

        self.progressMarker = ttk.Progressbar(self, mode='determinate', maximum=100)
        self.progressMarker.grid()
        self.pdfMerger = PDFMerger()
        self.pdfMerger.mergePDFs(self.fileNames, self.outputFileName, self.progressMarker)

    def __clearPDFLabelFrame(self):
        PDFLabelFrameChildren = self.PDFLabelFrame.winfo_children()

        for child in PDFLabelFrameChildren:
            child.destroy()
    
    def __createChosenPDFLabels(self, pdfList):
        for index in range(len(pdfList)):
            currentFilePath = pdfList[index]
            currentFilePath = currentFilePath.split("/")

            lastSplitItemIndex = len(currentFilePath) - 1
            currentFileName = currentFilePath[lastSplitItemIndex]

            ttk.Label(self.PDFLabelFrame, text=currentFileName).grid(row=index, column=0, columnspan=2)


app = Application() 
app.master.title('PDF Merger') 
app.mainloop()