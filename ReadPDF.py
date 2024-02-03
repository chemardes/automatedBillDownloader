import glob
import os
from PyPDF2 import PdfReader

file_path = r"C:\Users\LEGION\Downloads"


def getting_latest_downloaded_folder(self):
    # function to get the latest downloaded pdf file in folder
    # passes the download folder path as a parameter

    # returns the file path of the pdf file
    file_list = glob.glob(self + "/*.pdf")
    latest_file = max(file_list, key=os.path.getmtime)
    return latest_file


def extracting_text_from_pdf(path):
    reader = PdfReader(path)
    page = reader.pages[0]
    return page.extract_text()

