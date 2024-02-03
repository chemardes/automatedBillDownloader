import glob
import os
import re
from PyPDF2 import PdfReader

file_path = r"C:\Users\LEGION\Downloads"


def getting_latest_downloaded_folder(self):
    # function to get the latest downloaded pdf file in folder
    # passes the download folder path as a parameter

    # returns the file path of the pdf file
    file_list = glob.glob(self + "/*.pdf")
    latest_file = max(file_list, key=os.path.getmtime)
    return latest_file


def extracting_amount_due_from_pdf(path):
    reader = PdfReader(path)
    text = reader.pages[0].extract_text()

    # checks for the presence of keyword (specified by the RegEx)
    pattern = re.compile(r'(€[\d.,]+) Amount due')
    match = pattern.search(text)

    # returns amount due if keyword is found
    if match:
        amount = match.group(0) # match.group(1) gives the 1st parenthesized value so (€0.75)
        return amount
    else:
        return "No matching amount found in text file."

