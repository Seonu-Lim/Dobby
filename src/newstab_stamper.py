import os
import sys
from _stamper import *
from tkinter import *
from tkinter import filedialog

def stamp_all_files(code, origin_path, destination_path):
    filelist = [f for f in os.listdir(origin_path) if f[-4:] == '.pdf']
    for f in filelist:
        stamp_document(code, origin_path, f, destination_path)

def get_and_run(origin_path,code) :
    destination_path = os.path.join(origin_path,code)
    if not os.path.exists(destination_path) :
        os.makedirs(destination_path)
    stamp_all_files(code,origin_path,destination_path)
    sys.exit(1)


def main():
    origin_path = filedialog.askdirectory()
    root = Tk()
    root.title('NEWSTAB STAMPER')
    lab = Label(root,text="문서 코드를 입력하세요.")
    lab.pack()
    entry = Entry(root)
    entry.pack()
    button = Button(root,text='확인',command=lambda:get_and_run(origin_path,entry.get()))
    button.pack()
    root.mainloop()
      
    
if __name__ == "__main__":
    main()