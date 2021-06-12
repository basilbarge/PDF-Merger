
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog

from pdfmerger import PDFMerger

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

        progressWindow = tk.Toplevel(self)
        progressWindow.wm_title("Merging PDFs...")

        self.progressMarker = ttk.Progressbar(progressWindow, mode='determinate', maximum=100)
        self.progressMarker.grid(row=1, column=0)

        self.progressLabel = ttk.Label(progressWindow, text="Merging PDFs...: 0 %")
        self.progressLabel.grid(row=0, column=0)

        self.pdfMerger = PDFMerger()
        self.pdfMerger.mergePDFs(self.parent.PDFLabels.fileNames, self.outputFileName, self.incrementProgressBarBy, self.incrementProgressLabelBy)

        progressWindow.destroy()

    def incrementProgressBarBy(self, incrementBy):
        self.progressMarker['value'] += incrementBy
        self.master.update()

    def incrementProgressLabelBy(self, progressIncrement):
        currentText = self.progressLabel.cget("text")

        currentTextAsList = currentText.split(' ')

        currentProgressPercentage = float(currentTextAsList[len(currentTextAsList) - 2])
        currentProgressPercentage += progressIncrement

        currentTextAsList[len(currentTextAsList) - 2] = str(currentProgressPercentage)

        separator = " " 
        newText = separator.join(currentTextAsList)

        self.progressLabel.configure(text=newText)
        self.master.update()