import os
import sys
from _stamper import *
from tkinter import *
from tkinter import filedialog


def stamp_all_files(origin_path, code):
    """
    Creating & inserting stamp to the all files in the `origin_path`.
    """
    destination_path = os.path.join(origin_path, code)
    try:
        os.makedirs(destination_path)
    except OSError:
        # TODO: raise this message to the UI.
        raise OSError(f"폴더가 이미 존재합니다. 다른 폴더명을 입력해주세요.")
    filelist = [file_name for file_name in os.listdir(origin_path) if file_name[-4:] == ".pdf"]
    for file_name in filelist:
        # Stamping to the single document.
        stamp_document(code, origin_path, file_name, destination_path)
    sys.exit(1)


def main():
    root = Tk()
    root.title("NEWSTAB STAMPER")
    label = Label(root,text="문서 코드를 입력하세요.")
    label.pack()
    entry = Entry(root)
    entry.pack()
    origin_path = filedialog.askdirectory()
    button = Button(root, text='확인', command=lambda: stamp_all_files(origin_path, entry.get()))
    button.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
