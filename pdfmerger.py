from PyPDF2 import PdfFileMerger

class PDFMerger():

    def __init__(self):
        self.pdfMerger = PdfFileMerger()

    def mergePDFs(self, listOfPDFsToMerge, outputFile):
        for pdf in listOfPDFsToMerge:
            self.pdfMerger.append(pdf)

        self.pdfMerger.write(outputFile)
        self.pdfMerger.close()

    

