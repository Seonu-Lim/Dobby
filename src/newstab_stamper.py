import os
import sys
from _stamper import *
#import argparse
#import time
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def stamp_all_files(origin_path, destination_path):
    filelist = [f for f in os.listdir(origin_path) if f[-4:] == '.pdf']
    for f in filelist:
        stamp_document(origin_path, f, destination_path)

def end_program() :
    root.destroy()

def main():
    root = Tk()
    root.title('NEWSTAB STAMPER')
    root.withdraw()
    origin_path = filedialog.askdirectory()
    destination_path = os.path.join(origin_path,'output')
    if not os.path.exists(destination_path) :
        os.makedirs(destination_path)
    stamp_all_files(origin_path, destination_path)
    sys.exit(1)  
    
if __name__ == "__main__":
    main()