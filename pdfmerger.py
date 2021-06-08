from PyPDF2 import PdfFileMerger
from math import ceil
class PDFMerger():

    def __init__(self):
        self.pdfMerger = PdfFileMerger()

    def mergePDFs(self, listOfPDFsToMerge, outputFile, relativeProgress):
        for pdf in listOfPDFsToMerge:
            self.pdfMerger.append(pdf)
            relativeProgress['value'] += ceil(100 / len(listOfPDFsToMerge))

        self.pdfMerger.write(outputFile)
        self.pdfMerger.close()