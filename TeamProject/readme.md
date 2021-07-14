## Main Subject : 건강검진 정보 데이터 분석 및 시각화

### [ 황금 시바견 팀 소개 ]

- 이예준(팀장) : 전체 프로젝트 진행 총괄

👾 Github  : [https://github.com/yejun-lee](https://github.com/yejun-lee)

- 최수연(팀원) : 데이터 수집, 데이터 전처리 및 분석, 데이터 시각화(Matplot), 시각화 자료 해석.

👻 Github : [https://github.com/devpixelchoi](https://github.com/devpixelchoi)

- 최아름(팀원) : 데이터 주제 선정, 데이터 전처리 및 분석, 데이터 시각화(Seaborn), 시각화 자료 해석.

👽 Github : [https://github.com/areummy](https://github.com/areummy)

### [ 주제 선정 동기 ]

- 국민건강보험공단에서 제공하는 건강검진정보를 이용하여 지역 및 성별 등 데이터의 여러 범주들의 상관관계를 분석함으로써 다양한 결과를 예측 및 시각화합니다.
- 이렇게 분석한 자료를 바탕으로 연령대 별 건강정보에 대해 공유하고, 이상치를 가진 사람의 프로필을 분석함으로써 경각심을 가지게 함을 목표로 합니다.
- 그리고 앞으로 분석하게 될 주요 parameter들 중 생소한 것들에 대해 설명하고, 연관성이 없을 것 같았던 요소들 중 상관관계가 있는 것들의 이유를 분석합니다.
- 자료출처 : 국민 건강 보험 공단_건강검진 정보

[국민건강보험공단_건강검진정보_20191231](https://www.data.go.kr/data/15007122/fileData.do)

[[ 사용 Module ] ](https://www.notion.so/d994a0928847417cbc6f92bc189212dd)

## 목차

**1. 주요 parameter 설명**

- 개요
- parameter

-총 콜레스테롤

-혈압

-식전혈당 (공복)

-트리글리세라이드

-혈색소

-요단백

-혈청크레아티닌

-혈청지오티(AST/ALT)

-감마지티피

**2. 데이터 전처리**

- 이슈 사항
- 결측치 처리

**3. 데이터 시각화**

- 지역별 인구/연령대 비율 시각화 (Pieplot, Boxplot, Plot)
- 지역별 parameter 평균 시각화 (Plot)
- 연령대별 parameter 상관관계 비교 시각화 (Heatmap)
- 연령대별 신장/체중 밀집도 시각화 (Jointplot)
- parameter별 연령대 수치 비교
- parameter별 상위/하위 표본 간의 수치 비교분석
- 이상치를 가진 표본의 profile 분석

**4. 데이터 분석**

- 콜레스테롤과 체중의 관계
- 콜레스테롤과 혈압의 관계
- 혈당과 단백뇨의 관계
- 연령대, 지역에 따른 트리글리세라이드 수치 비교
- 혈색소와 혈압의 관계
- 혈색소와 연령대의 관계
- 음주상태에 따른 혈청지오티, 혈청지피티 수치 비교

**5. 결론 및 소감**

- 좋았던 점(Good)
- 스스로 피드백(Problem)
- 추후 발전계획(Try)

## 1. 주요 parameter 설명🖌️

### 개요

- 데이터 규모는 2016년 ~ 2019년까지 연간 100만 건, 총 400만 건입니다.
- 각 연도별 진료 및 건강검진 수진 환자를 매년 100만명 씩 무작위로 추출하며, 재식별 가능성이 존재하는 데이터는 대상에서 제외되었습니다.
- 저희들이 사용하게 된 국민건강보험공단의 건강검진 정보는 총 31가지의 Column을 가집니다.
- 주요 parameter : 성별 코드, 연령대 코드, 시도 코드, 신장, 체중, 허리둘레, 시력, 청력, 수축기혈압, 이완기혈압, 식전혈당, 콜레스테롤, 트리글리 세라이드, HDL콜레스테롤, LDL콜레스테롤, 혈색소, 요단백, 혈청크레아티닌, AST, ALT, 감마 지티피, 흡연여부, 음주여부, 구강검진 수검여부, 치석유무
- 데이터를 분석하기에 앞서 parameter에 대한 이해도가 필요하므로 간단하게 설명하겠습니다.

### Parameter (하나씩 열어보세요)

- 총 콜레스테롤

    📔 설명 

    지질의 한 종류로 생체 내에서 여러 가지 중요한 역할을 하는 물질이다. 

    💫 주요 기능

    - 모든 세포막을 만들고 유지하는 데 사용되기 때문에 신진대사에 꼭 필요하다.
    - 담즙의 구성요소이고 남은 콜레스테롤은 담낭에 저장되어 배출된다.
    - 햇빛을 받으면 콜레스테롤에서 비타민 D를 생산한다.
    - 콜레스테롤은 우리 혈액에서 HDL, LDL 콜레스테롤 두 가지 형태로 존재한다. (일반적으로 LDL 콜레스테롤은 그 수치가 낮을수록, HDL 콜레스테롤은 높을수록 좋다)

    → **고밀도 저단백(HDL) 콜레스테롤** 

    작은 입자의 콜레스테롤로 세포에 이끌려간 콜레스테롤을 간으로 돌려주고 혈관 벽에 쌓인 나쁜 콜레스테롤을 없애는 역할을 하는 성분

    → **저밀도 저단백(LDL) 콜레스테롤** 

    입자가 매우 큰 콜레스테롤로 양이 과도하게 증가할 경우, 혈관벽에 쌓여서 동맥경화나 각종 질병을 야기 하는 성분

    🖊️ 정상 수치 범위

    - 총 콜레스테롤

    **높음 : 240 mg/dL 이상**

    경계 : 200 ~ 239 mg/dL

    **적정 수치 : 200 mg/dL 미만**

    - HDL 콜레스테롤

    **높음 : 60 mg/dL 이상**

    **낮음 : 40 mg/dL 미만**

    - LDL 콜레스테롤

    매우 높음 : 190 mg/dL 이상

    **높음 : 160 ~ 189 mg/dL**

    경계 수치 : 130 ~ 159 mg/dL

    정상 : 100 ~ 129 mg/dL

    **적정 : 100 mg/dL 미만**

    👾 이상치를 띌 경우 생길 수 있는 질병

    - [고콜레스테롤혈증(Pure hypercholesterolemia)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=32081)
    - [이상지질혈증(Dyslipidemia)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=31326)

    [🖊️ 데이터 분석](https://www.notion.so/_-8d876e84b954473eafeea8b27c3ed8c0)

- 혈압💉

    📔 설명 

    - 혈압은 심장 수축에 의하여 만들어지며 혈액이 혈관을 흐를 수 있게 하는 힘이다.
    - 심장혈관계의 압력을 나타내는 단위는 mmHg이며, 해수면에서 정상적인 대기압인 60 mmHg과 비교하여 표현한다.
    - 즉 혈압이 0 mmHg이면 실제 압력은 대기압과 같고, 혈압이 100 mmHg라면 대기압보다 100 mmHg 높다는 것이다. 혈압은 측정하는 신체 부위와 심장 박동 주기의 시점에 따라 다르다.

    수축기(최고) 혈압 : 혈액이 좌심실로부터 대동맥으로 박출된 직후의 수축기 혈압.

    이완기(최저) 혈압 : 혈액이 좌심실로 유입되는 중의 확장기 압력.

    🖊️ 정상 수치 범위

    [혈압분류표](https://www.notion.so/3fba25357c7045fda1984913d1bd33ae)

    👾 이상치를 띌 경우 생길 수 있는 질병

    - [고혈압(Essential (primary) hypertension)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=31322)
    - [임신성 고혈압(Pregnancy-induced hypertension)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=31846)
    - [저혈압(Hypotension)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=32144)

- 식전혈당 (공복)

- 트리글리세라이드(중성지방)

    📔 설명

    - 글리세롤에 3분자의 지방산이 에스테르 합한 것으로, 자연계에서 찾아낼 수 있는 지방산유도체 가운데서 가장 분포가 넓다.
    - 생체에 있어서의 에너지의 운반과 저장, 피하지방으로서 보온이나 생체의 보호를 맡고 있다.
    - 혈장 중의 트리글리세라이드는 보통 100mg/dl 전후이지만, 지질대사이상인에서는 3,000~5,000mg/dl 에 이르는 일도 있어서 그 변동은 다른 지질에 비해서 몹시 크다.

    🖊️ 정상 수치 & 변동

    - 트리글리세라이드 정상치 : 30~135mg/dl
    - 생활환경의 영향이 크며, 대도시에 비해서 어촌이나 시골에서는 그 수치가 낮다.
    - 여자에 비해서 남자가 높고 개인차도 크다.
    - 임부에 대해서는 임신이 진행됨에 따라서 상승하고 분만 후 저하된다.
    - 나이에 대해서는 60대 전후로 하강하기 시작하며, 그 이전까지는 상승한다.

    👾 이상치를 띌 경우 생길 수 있는 질병

    - [비만(Obesity)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=31809)
    - [허혈성 심질환(Ischemic heart disease)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=30275)
    - [협심증(Angina pectoris)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=32179)

- 혈색소

    📔 설명

    - 적혈구의 주요 성분으로 산소와 이산화탄소를 운반하는 역할을 수행한다.
    - 혈중 혈색소의 양을 측정함으로써 혈액의 산소운반 능력을 알 수 있는데, 체내의 적혈구 생산 감소, 파괴 증가 또는 출혈로 인해 혈색소 수치가 낮아지면 조직에 산소운반이 제대로 이루어지지 않을 수 있다.

    🖊️ 정상 수치 & 변동

    - 남성 : 13.0 ~ 17.0 g/dL
    - 여성 : 12.0 ~ 16.0 g/dL
    - 철분, 비타민 B12 또는 엽산 결핍, 유전질환, 간경변, 과다출혈, 과도한 적혈구 파괴, 신장질환, 만성질환, 혈액종양 등의 경우에 혈색소 수치가 낮을 수 있다.
    - 어린이와 노인의 경우 일반 성인보다 혈색소 수치가 낮으며, 정상적으로 임신이나 월경, 다이어트 중에도 혈색소 수치가 감소할 수 있다.
    - 혈색소 수치가 8g/dL 이하일 경우 단순 빈혈보다는 출혈을 뜻하므로 원인질환을 확인하기 위한 추가적인 검사가 필요할 수 있다.

    👾 이상치를 띌 경우 생길 수 있는 질병

    - [재생불량빈혈(Aplastic anemia)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=31786)
    - [철결핍빈혈(Iron deficiency anemia)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=31629)
    - [용혈빈혈(Hemolytic anemia)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=31048)
    - 위 질병 외 관련 질병 링크 참조 >> [🌐](http://www.amc.seoul.kr/asan/healthinfo/management/managementDetail.do?managementId=119&tabIndex=1)

    [🖋️ 데이터 분석](https://www.notion.so/_-8d876e84b954473eafeea8b27c3ed8c0)

- 요단백

    📔 설명

    - 소변 안에는 평상시에는 거의 알아볼 수 없을 만큼 극소량의 단백질이 배출되기도 하는데, 하루동안 배출되는 소변 안에 300mg 이상의 단백질이 섞여 배출되는 것을 요단백이라 한다.
    - 월경, 과격한 운동, 근육운동 스트레스, 컨디션 난조, 정신적 스트레스를 받은 사람에게서 일시적으로 나타나기도 한다.
    - 기능성 단백뇨 이외의 단백뇨는 대부분 신장에 심각한 질병이 있음을 의미한다.

    🖌️ 측정 단위

    - 단백뇨를 진단하기 위한 시험지 검사법은 시험지에 소변을 적신 후 60초 이내에 초록색으로 변색하는 정도를 아래와 같이 판정한다.
    - 1 (-1), 2 (±), 3(+1) , 4(+2) , 5(+3) , 6(+4)
    - +1 : 30mg/dL  ,  +2 : 100mg/dL  ,  +3 : 300mg/dL  ,  +4 : 1000mg/dL

    👾 이상치를 띌 경우 생길 수 있는 질병

    - [만성 신부전(Chronic renal failure)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=31973)
    - [급성 신부전(Acute renal failure)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=31971)
    - [당뇨병(Diabetes mellitus)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=31596)
    - 위 질병 외 관련 질병 링크 참조 >> [🌐](http://www.amc.seoul.kr/asan/healthinfo/management/managementDetail.do?managementId=87&tabIndex=1)

    🖊️ [데이터분석](https://www.notion.so/_-8d876e84b954473eafeea8b27c3ed8c0)

     참조 : [http://www.amc.seoul.kr/asan/healthinfo/management/managementDetail.do?managementId=87](http://www.amc.seoul.kr/asan/healthinfo/management/managementDetail.do?managementId=87) 

- 혈청크레아티닌

- 혈청지오티/지피티 (AST/ALT)

    *AST : 아스파테이트아미노전달효소

    *ALT : 알라닌아미노전달효소

    📔 설명

    혈청지오티(AST) 🍎

    - 간 기능을 나타내는 혈액검사상의 수치, 간세포 이외에 심장, 신장, 뇌 , 근육 등에도 존재하는 효소로 이러한 세포들이 손상을 받는 경우 농도가 증가함
    - AST의 경우 음주경력에 굉장히 영향을 많이 받음.
    - 음주경력이 없는데 AST가 크게 증가했다면 다른 사유로 수치가 증가했을 가능성이 높다.
    - 근육운동을 많이하는 사람들에게서 근육 손상으로 인해 AST 수치가 높아지는 경향이 있다.
    - 정상치 0~40 IU/L

    혈청지피티(ALT) 🍌

    - 간 기능을 나타내는 혈액검사상의 수치, ALT는 주로 간세포 안에 존재하는 효소로, 간세포가 손상을 받는 경우 농도가 증가함
    - AST / ALT 비율이 2 이상인 경우 간 세포가 파괴되었을 가능성이 높다.
    - 정상치 0~40 IU/L

    👾 이상치를 띌 경우 생길 수 있는 질병

    - [간경화(Liver cirrhosis)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=30480)
    - [간염(Hepatitis)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=31687)
    - [급성 C형 간염(Acute hepatitis C)](http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=32096)
    - 위 질병 외 관련 질병 링크 참조 >> [🌐](http://www.amc.seoul.kr/asan/healthinfo/management/managementDetail.do?managementId=108&tabIndex=1&pageIndex=2)

    [🖊️ 데이터 분석](https://www.notion.so/_-8d876e84b954473eafeea8b27c3ed8c0)

- 감마지티피