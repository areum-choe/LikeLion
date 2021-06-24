# 1)tkinker 프로그램 만들기

하나의 라이브러리 (파이썬에서 가져와서 사용하는)

엑셀 파일에 파일을 불러와 그 안에 단어들을 가지고 검색을 하면 해당되는 def를 보여줍니다.

```python
#둘의 차이 
from tkinter import plot, abc  
#사용할 때
plot
abc
#단점 어디에서 불러왔는지 모른다.
import tkinter 
#사용할 때
tkinter.plot
tkinter.abc
단점=메모리를 많이 잡아 먹는다
```

- 디렉터리랑 폴더 차이

디렉터리(윈도우에서의 폴더와 같은 의미.)

폴더(리눅스와 맥에서는 디렉터리라고 한다.)

- ..은 상위폴더        /        .은 현재 폴더

[tkinter - Python interface to Tcl/Tk - Python 3.9.5 documentation](https://docs.python.org/ko/3/library/tkinter.html)

[Posts | 076923](https://076923.github.io/posts/#Python-Tkinter)

- 내 코드

```python
from tkinter import *
import pandas as pd
import os   #폴더를 만들고 삭제...현재 폴더 위치.

print(os.getcwd()) #작업폴더의 위치를 가져오는 것

#파일 불러오기
dat=pd.read_excel("./dic_excel.xlsx")

#기능 추가(제풀 버튼 클릭시, 동작하는 기능)
def click():
    pass
window=Tk()
window.title("Areum Dictionary")

#01 입력 상자 설명 레이블
label=Label(window,text="원하는 단어 입력 후, 엔터 키 누르기")
label.grid(row=0,column=0,sticky=W)

#02 텍스트 입력이 가능한 상자(Entry)
entry=Entry(window,width=15,bg="light yellow")
entry.grid(row=1, column=0, sticky=W) #sticky 위치 w동쪽  좌, 우

#03 제출버튼
button=Button(window,width=5,text="제출")
button.grid(row=2, column=0, sticky=W)

#04 설명 레이블 - 의미
label2=Label(window,text="\n입력한 단어의 의미")
label2.grid(row=3,column=0,sticky=W)

#05 텍스트 박스 입력 상자
# columnspan=2 는 (4,0)~(4,1) 위치까지 분포
output = Text(window, width=50, height=6, **wrap=WORD,** background="light yellow") #wrap
output.grid(row=4, column=0, columnspan=2, sticky=W)

#메인 반복문 실행
window.mainloop()
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/241fcfec-f019-4c17-b87a-c9ed8948baf5/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/241fcfec-f019-4c17-b87a-c9ed8948baf5/Untitled.png)

# 2)GitHub 가입 및 설치해 보기

# 3)HTML 기본 이해

```html
<html>
<head>
<title>my web page</title>
</head>

<body>
               <P>단락1</P>
	 <P>단락2</P>
	 <P>단락3</P>
	 단락1<br>
	 단락2<br>
	 <a href="https://www.naver.com/">네이버</a>
	 <a href="https://www.daum.net/">다음</a>
</body>
</html>
```
