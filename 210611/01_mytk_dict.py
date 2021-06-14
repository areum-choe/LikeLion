from tkinter import *
import pandas as pd
import os   #폴더를 만들고 삭제...현재 폴더 위치.

print(os.getcwd()) #작업폴더의 위치를 가져오는 것

#파일 불러오기
dat=pd.read_excel("./areum_excel.xlsx")

window=Tk()
window.title("Areum Dictionary")

#기능 추가(제풀 버튼 클릭시, 동작하는 기능)
def click():
    print("버튼이 클릭되었습니다.")
    word=entry.get() #아래 엔트리 상자의 내용을 text 넣는다
    # END로 지정하면 문자열이 입력된 최종 입력 지점을 의미.
    # 특정 시작 지점부터 텍스트 엔트리 위젯의 끝까지 모두 지우기 위해 END를 쓴다.
    output.delete(0.0, END)  # 텍스트 박스 내용을 지운다.
    try:
        def_word = dat.loc[dat['word'] == word, 'def'].values[0]
    except:
        def_word = "단어를 뜻을 찾을 수 없음."
    output.insert(END, def_word)



#01 입력 상자 설명 레이블
label=Label(window,text="나에 대해 물어보기")
label.grid(row=0,column=0,sticky=W) #장착 시킴

#02 텍스트 입력이 가능한 상자(Entry)
entry=Entry(window,width=15,bg="light yellow")
entry.grid(row=1, column=0, sticky=W) #sticky 위치 w동쪽  좌, 우

#03 제출버튼
button=Button(window,width=5,text="Click",command=click)
button.grid(row=2, column=0, sticky=W)
command=click

#04 설명 레이블 - 의미
label2=Label(window,text="\n입력한 단어의 의미")
label2.grid(row=3,column=0,sticky=W)

#05 텍스트 박스 입력 상자
# columnspan=2 는 (4,0)~(4,1) 위치까지 분포
output = Text(window, width=50, height=6, wrap=WORD, background="light yellow") #wrap
output.grid(row=4, column=0, columnspan=2, sticky=W)

#메인 반복문 실행
window.mainloop()

