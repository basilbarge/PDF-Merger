import tkinter.ttk as ttk

class PDFLabels(ttk.Frame):

    def __init__(self, parent, master=None):
        super().__init__(master)
        self.grid()

        self.fileNames = []

        self.PDFLabelFrame = ttk.Labelframe(self, text="PDFs to Merge")
        self.PDFLabelFrame.grid(row=1, column=0, columnspan=2)

    def createChosenPDFLabels(self, pdfList):
        for index in range(len(pdfList)):
            currentFilePath = pdfList[index]
            currentFilePath = currentFilePath.split("/")

            lastSplitItemIndex = len(currentFilePath) - 1
            currentFileName = currentFilePath[lastSplitItemIndex]

            ttk.Label(self.PDFLabelFrame, text=currentFileName).grid(row=index, column=0, columnspan=2)
