from PyPDF2 import PdfFileMerger
class PDFMerger():

    def __init__(self):
        self.pdfMerger = PdfFileMerger(strict=False)

    def mergePDFs(self, listOfPDFsToMerge, outputFile, incrementProgressBarBy, incrementProgressLabelBy):
        for pdf in listOfPDFsToMerge:
            self.pdfMerger.append(pdf)
            incrementProgressBarBy((100 / len(listOfPDFsToMerge)))
            incrementProgressLabelBy((100 / len(listOfPDFsToMerge)))
            

        self.pdfMerger.write(outputFile)
        self.pdfMerger.close()