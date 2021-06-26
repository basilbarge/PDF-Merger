# PDF Merger 🗃

This is a repository for a small application that can merge multiple PDFs together to provide a simple, quick, and lightweight method as a more robust alternative to a simple online PDF merger.

TODO: ✅

- [x] Fix file name labels so that each time the "Browse" button is pressed old file labels are erased
- [x] Figure out a way to freeze the application or notify the user on the progress of the PDF merging process. Need to figure out a way to get this progress to show and let the user know the operation is complete before closing out.
- [x] Fix the application so that you files that you browse for are appended to the list of PDFs to merge (might have to update the functionalilty of the 'Browse' button and have a different way to clear PDFs you no longer want to merge)
- [ ] Look into StringVars as a way to keep track of text on labels and windows that are updated somewhat frequently.
- [x] Add a button to clear all the PDFs currently selected for merging.
- [x] Add a feature to remove individual PDF files from the ones being merged together.
- [ ] Handle case where a file might not be chosen i.e. potentially lock the merge button until at least 2 files are chosen.
- [ ] Potentially handle a case for duplicate PDFs
- [ ] Add an error case for merging to a PDF file that is already opened
- [ ] Have a scroll wheel or something similar pop-up when the length of the list of PDFs is longer than the application screen.
- [ ] Figure out a nice theming for the application.
- [ ] Package the application to a .exe so that it can be run as a desktop application on devices.
