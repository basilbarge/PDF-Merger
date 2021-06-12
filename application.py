from ProgressWindow import ProgressWindow
from tkinter.ttk import Frame
from ControlsBar import ControlsBar
from PDFLabels import PDFLabels

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master) 

        self.outputFileName = ""
        self.pdfMerger = None
        self.progressLabel = None
        self.progressMarker = None
        self.buttonControls = ControlsBar(self)
        self.PDFLabels = PDFLabels(self)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)        


    def __clearPDFLabelFrame(self):
        PDFLabelFrameChildren = self.PDFLabelFrame.winfo_children()

        for child in PDFLabelFrameChildren:
            child.destroy()
    
    # def __createChosenPDFLabels(self, pdfList):
    #     for index in range(len(pdfList)):
    #         currentFilePath = pdfList[index]
    #         currentFilePath = currentFilePath.split("/")

    #         lastSplitItemIndex = len(currentFilePath) - 1
    #         currentFileName = currentFilePath[lastSplitItemIndex]

    #         Label(self.PDFLabelFrame, text=currentFileName).grid(row=index, column=0, columnspan=2)



app = Application() 
app.master.title('PDF Merger') 
app.mainloop()