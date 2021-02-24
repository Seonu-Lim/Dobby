import os
import sys
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.ttk as ttk
from _stamper import *

class Dobby(Frame) :
    def __init__(self,master) :
        self.master = master
        self.origin_path = filedialog.askdirectory()
        self.destination_path = None
        self.ask_code()

    def ask_code(self) :
        root = Toplevel()
        label = Label(root,text="문서 코드를 입력하세요.")
        entry = Entry(root)
        button = Button(root, text='확인',command=lambda: self.check_dir(root,entry.get()))
        label.pack()
        entry.pack()
        button.pack()

    def check_dir(self,frame,input_text) :
        code = input_text
        frame.destroy()
        self.destination_path = os.path.join(self.origin_path, code)
        if os.path.exists(self.destination_path) :
            msgbox = messagebox.askyesno('Dobby','해당 경로에 같은 코드의 폴더가 이미 존재합니다. 덮어쓰시겠습니까?')
            if msgbox == True :
                shutil.rmtree(self.destination_path)
                os.makedirs(self.destination_path)
                self.stamp_all(code,self.destination_path)
                self.done_stamping()
            else :
                self.ask_code()
        else :
            os.makedirs(self.destination_path)
            self.stamp_all(code,self.destination_path)
            self.done_stamping()
    
    def stamp_all(self,code,destination_path) :
        filelist = [file_name for file_name in os.listdir(self.origin_path) if file_name[-4:] == ".pdf"]
        root = Toplevel()
        var = DoubleVar()
        i = 0
        var.set(i)
        progressbar = ttk.Progressbar(root,maximum=len(filelist),variable=var)
        for file_name in filelist:
            stamp_document(code, self.origin_path, file_name, destination_path)
            i += 1
            var.set(i)
            progressbar.update()
        root.destroy()
        
    def done_stamping(self) :
        root = Toplevel()
        label = Label(root,text='도장 다 찍었어요!')
        button = Button(root, text='나가기',command=lambda:sys.exit(1))
        label.pack()
        button.pack()


def main () :
    root = Tk()
    root.title('Dobby')
    Dobby(root)
    root.mainloop()

if __name__ == '__main__' :
    main()
