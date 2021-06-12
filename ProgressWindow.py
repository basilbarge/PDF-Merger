import tkinter as tk
import tkinter.ttk as ttk

class ProgressWindow(ttk.Frame):

    def __init__(self, parent, master=None):
        super().__init__(master)

        self.parent = parent

        self.window = tk.Toplevel(self)
        self.mainApplication = self.parent.parent

        self.progressMarker = ttk.Progressbar(self.window, mode='determinate', maximum=100)
        self.progressMarker.grid(row=1, column=0)

        self.progressLabel = ttk.Label(self.window, text="Merging PDFs...: 0 %")
        self.progressLabel.grid(row=0, column=0)

        self.window.wm_title("Merging PDFs...")

    def incrementProgressBarBy(self, incrementBy):
        self.progressMarker['value'] += incrementBy
        self.mainApplication.master.update()

    def incrementProgressLabelBy(self, progressIncrement):
        currentText = self.progressLabel.cget("text")

        currentTextAsList = currentText.split(' ')

        currentProgressPercentage = float(currentTextAsList[len(currentTextAsList) - 2])
        currentProgressPercentage += progressIncrement

        currentTextAsList[len(currentTextAsList) - 2] = str(currentProgressPercentage)

        separator = " " 
        newText = separator.join(currentTextAsList)

        self.progressLabel.configure(text=newText)
        self.mainApplication.master.update()
