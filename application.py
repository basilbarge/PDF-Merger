import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pdfmerger import PDFMerger

class Application(tk.Frame): 
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master) 
        self.fileNames = []
        self.fileLabels = []
        self.outputFileName = ""
        self.pdfMerger = None
        self.progressLabel = None
        self.progressMarker = None
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

    def openFileExplorer(self):
        self.fileNames = filedialog.askopenfilenames(defaultextension=".pdf", filetypes={("*.pdf", ".pdf")})
        
        self.__clearPDFLabelFrame()

        self.__createChosenPDFLabels(self.fileNames)
        
    def mergePDFs(self):
        self.outputFileName = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes={("*.pdf", ".pdf")})

        progressWindow = tk.Toplevel(self)
        progressWindow.wm_title("Merging PDFs...")

        self.progressMarker = ttk.Progressbar(progressWindow, mode='determinate', maximum=100)
        self.progressMarker.grid(row=1, column=0)

        self.progressLabel = ttk.Label(progressWindow, text="Merging PDFs...: 0 %")
        self.progressLabel.grid(row=0, column=0)

        self.pdfMerger = PDFMerger()
        self.pdfMerger.mergePDFs(self.fileNames, self.outputFileName, self.incrementProgressBarBy, self.incrementProgressLabelBy)

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

    def incrementProgressBarBy(self, incrementBy):
        self.progressMarker['value'] += incrementBy

    def incrementProgressLabelBy(self, progressIncrement):
        currentText = self.progressLabel.cget("text")

        currentTextAsList = currentText.split(' ')

        currentProgressPercentage = float(currentTextAsList[len(currentTextAsList) - 2])
        currentProgressPercentage += progressIncrement

        currentTextAsList[len(currentTextAsList) - 2] = str(currentProgressPercentage)

        separator = " " 
        newText = separator.join(currentTextAsList)

        self.progressLabel.configure(text=newText)

app = Application() 
app.master.title('PDF Merger') 
app.mainloop()