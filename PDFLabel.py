import tkinter.ttk as ttk
import tkinter as tk

class PDFLabel(ttk.Frame):

    def __init__(self, parent, PDFName, row, master=None):
        super().__init__(master)
        self.parent= parent
        
        self.name = PDFName

        self.row = row

        self.trashIcon = tk.PhotoImage(file="trash.png")

        self.grid(row=0, column=0, columnspan=2)

        self.PDFFileLabel = ttk.Label(self.parent, text=self.name)
        self.PDFFileLabel.grid(row=row, column=0)

        self.deleteButton = ttk.Button(self.parent, image=self.trashIcon, command=self.deleteSelfFromPDFList)
        self.deleteButton.grid(row=row, column=1)

    def deleteSelfFromPDFList(self):
        self.parent.master.updateLabelFrame(self)

    def destroy(self):
        self.PDFFileLabel.destroy()
        self.deleteButton.destroy()



