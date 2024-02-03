import glob
import os

# file_path = r"C:\Users\LEGION\Downloads"

def getting_latest_downloaded_folder(self):
    file_list = glob.glob(self + "/*.pdf")
    latest_file = max(file_list, key=os.path.getmtime)
    return latest_file


# print(getting_latest_downloaded_folder(file_path))
