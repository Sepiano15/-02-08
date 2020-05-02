from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import os.path
import math

## 함수 선언 부분 ##
def loadImage(fname) :
    global window, canvas, paper, filename, XSIZE, YSIZE, inImage

    inImage = []
    fsize = os.path.getsize(fname)  # 파일의 크기
    XSIZE = YSIZE = int(math.sqrt(fsize))   # 정방형으로 가정하고 크기 구함

    fp = open(fname, 'rb')

    for i in range(0, XSIZE) :
        tmpList = []
        for k in range(0, YSIZE) :
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)

    fp.close()

def displayImage(image) :
 
def func_open() :
     global window, canvas, paper, filename, XSIZE, YSIZE, inImage

    filename = askopenfilename(parent = window, filetypes = (("RAW 파일", "*.raw"), ("모든 파일", "*.*")))
    if filename == '' :
        return

    if canvas != None :
        canvas.destroy()

        # 파일 -> 메모리
        loadImage(filename)

        window.geometry(str(XSIZE) + 'x' + str(YSIZE))  # 윈도창 크기
        canvas = Canvas(window, height = XSIZE, width = YSIZE)
        paper = PhotoImage(width = XSIZE, height = YSIZE)
        canvas.create_image((XSIZE / 2, YSIZE / 2), image = paper, state = "normal")

        #메모리 --> 화면
        displayImage(inImage)

        canvas.pack()

        # 파일 -> 메모리
        loadImage(filename)

        window.geometry(str(XSIZE) + 'x' + str(YSIZE))  # 윈도창 크기
        canvas = Canvas(window, height = XSIZE, width = YSIZE)
        paper = PhotoImage(width = XSIZE, height = YSIZE)
        canvas.create_image((XSIZE / 2, YSIZE / 2), image = paper, state = "normal")

        #메모리 --> 화면
        displayImage(inImage)

        canvas.pack()

    else:
        # 파일 -> 메모리
        loadImage(filename)

        window.geometry(str(XSIZE) + 'x' + str(YSIZE))  # 윈도창 크기
        canvas = Canvas(window, height = XSIZE, width = YSIZE)
        paper = PhotoImage(width = XSIZE, height = YSIZE)
        canvas.create_image((XSIZE / 2, YSIZE / 2), image = paper, state = "normal")

        #메모리 --> 화면
        displayImage(inImage)

        canvas.pack()
 
def func_exit() :
    window.quit()
    window.destroy()

def brightPhoto() :


def darkPhoto() :


def reversePhoto() :


## 전역 변수 선언 부분 ##
window = None
canvas = None
paper = None
XSIZE, YSIZE = 0, 0
inImage = []    #2차원 리스트(메모리)
filename = ''   #파일명(전역 변수)

## 메인 코드 부분 ##
if __name__ == "__main__" :
    window = Tk()
    window.title("흑백 사진 보기(메뉴)")

    #메뉴 추가
    mainMenu = Menu(window)
    window.config(menu = mainMenu)
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "파일", menu = fileMenu)
    fileMenu.add_command(label = "파일 열기", command = func_open)
    fileMenu.add_separator()
    fileMenu.add_command(label = "프로그램 종료", command = func_exit)

    photoMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "사진효과", menu = photoMenu)
    photoMenu.add_command(label = "밝게하기", command = brightPhoto)
    photoMenu.add_command(label = "어둡게하기", command = darkPhoto)
    photoMenu.add_command(label = "반전 이미지", command = reversePhoto)

    window.mainloop()
