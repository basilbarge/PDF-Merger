
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog

from PDFMerger import PDFMerger
from ProgressWindow import ProgressWindow

class ControlsBar(ttk.Frame):

    def __init__(self, parent, master=None):
        super().__init__(master)
        self.grid()
        self.parent = parent

        self.fileDialogButton = ttk.Button(self, text='Browse',command=self.openFileExplorer) 
        self.fileDialogButton.grid(row=0, column=0, padx=5, pady=5)

        self.mergePDFButton = ttk.Button(self, text="Merge", command=self.mergePDFs)
        self.mergePDFButton.grid(row=0, column=1, padx=5, pady=5)

    def openFileExplorer(self):
        self.parent.PDFLabels.fileNames.extend(tk.filedialog.askopenfilenames(defaultextension=".pdf", filetypes={("*.pdf", ".pdf")}))
        
        # self.__clearPDFLabelFrame()

        self.parent.PDFLabels.createChosenPDFLabels(self.parent.PDFLabels.fileNames)
        
    def mergePDFs(self):
        self.outputFileName = tkinter.filedialog.asksaveasfilename(defaultextension=".pdf", filetypes={("*.pdf", ".pdf")})

        progressWindow = ProgressWindow(self)

        self.pdfMerger = PDFMerger()
        self.pdfMerger.mergePDFs(self.parent.PDFLabels.fileNames, self.outputFileName, progressWindow.incrementProgressBarBy, progressWindow.incrementProgressLabelBy)

        progressWindow.destroy()