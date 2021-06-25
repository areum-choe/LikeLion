```python
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm    # 한글 폰트
import matplotlib
import os, warnings
import pandas as pd
import seaborn as sns

warnings.filterwarnings('ignore')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df1 = pd.read_csv('C:/Users/user/LikeLion_AI/data/CSV/today_corona_edit.csv')    # 90개국의 정보
df2 = pd.read_csv('C:/Users/user/LikeLion_AI/data/CSV/Natl_GDP.csv')             # 90개국의 GDP 정보
```

## 데이터 처리 과정


```python
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>국가</th>
      <th>확진자</th>
      <th>치료중</th>
      <th>사망자</th>
      <th>완치</th>
      <th>치명(%)</th>
      <th>완치(%)</th>
      <th>발생률</th>
      <th>인구수</th>
      <th>국토면적</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>중국</td>
      <td>91629</td>
      <td>512.0</td>
      <td>4636</td>
      <td>86481.0</td>
      <td>5</td>
      <td>94.0</td>
      <td>64</td>
      <td>1439323776</td>
      <td>9640821</td>
    </tr>
    <tr>
      <th>1</th>
      <td>인도</td>
      <td>29977861</td>
      <td>662521.0</td>
      <td>389302</td>
      <td>28926038.0</td>
      <td>1</td>
      <td>97.0</td>
      <td>21723</td>
      <td>1380004385</td>
      <td>3287263</td>
    </tr>
    <tr>
      <th>2</th>
      <td>미국</td>
      <td>34419838</td>
      <td>5034868.0</td>
      <td>617463</td>
      <td>28767507.0</td>
      <td>2</td>
      <td>84.0</td>
      <td>103987</td>
      <td>331002651</td>
      <td>9833517</td>
    </tr>
    <tr>
      <th>3</th>
      <td>인도네시아</td>
      <td>2004445</td>
      <td>147728.0</td>
      <td>54956</td>
      <td>1801761.0</td>
      <td>3</td>
      <td>90.0</td>
      <td>7328</td>
      <td>273523615</td>
      <td>1904569</td>
    </tr>
    <tr>
      <th>4</th>
      <td>파키스탄</td>
      <td>949838</td>
      <td>33452.0</td>
      <td>22034</td>
      <td>894352.0</td>
      <td>2</td>
      <td>94.0</td>
      <td>4300</td>
      <td>220892340</td>
      <td>796095</td>
    </tr>
    <tr>
      <th>5</th>
      <td>브라질</td>
      <td>17969806</td>
      <td>1178597.0</td>
      <td>502817</td>
      <td>16288392.0</td>
      <td>3</td>
      <td>91.0</td>
      <td>84540</td>
      <td>212559417</td>
      <td>8515770</td>
    </tr>
    <tr>
      <th>6</th>
      <td>나이지리아</td>
      <td>167292</td>
      <td>1377.0</td>
      <td>2118</td>
      <td>163797.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>812</td>
      <td>206139589</td>
      <td>923768</td>
    </tr>
    <tr>
      <th>7</th>
      <td>방글라데시</td>
      <td>856304</td>
      <td>57196.0</td>
      <td>13626</td>
      <td>785482.0</td>
      <td>2</td>
      <td>92.0</td>
      <td>5200</td>
      <td>164689383</td>
      <td>143998</td>
    </tr>
    <tr>
      <th>8</th>
      <td>러시아</td>
      <td>5334204</td>
      <td>326070.0</td>
      <td>129801</td>
      <td>4878333.0</td>
      <td>2</td>
      <td>92.0</td>
      <td>36552</td>
      <td>145934462</td>
      <td>17125407</td>
    </tr>
    <tr>
      <th>9</th>
      <td>멕시코</td>
      <td>2478551</td>
      <td>273052.0</td>
      <td>231244</td>
      <td>1974255.0</td>
      <td>9</td>
      <td>80.0</td>
      <td>19224</td>
      <td>128932753</td>
      <td>1964375</td>
    </tr>
    <tr>
      <th>10</th>
      <td>일본</td>
      <td>785969</td>
      <td>22248.0</td>
      <td>14439</td>
      <td>749282.0</td>
      <td>2</td>
      <td>95.0</td>
      <td>6214</td>
      <td>126476461</td>
      <td>377975</td>
    </tr>
    <tr>
      <th>11</th>
      <td>에티오피아</td>
      <td>275318</td>
      <td>15530.0</td>
      <td>4286</td>
      <td>255502.0</td>
      <td>2</td>
      <td>93.0</td>
      <td>2395</td>
      <td>114963588</td>
      <td>1104300</td>
    </tr>
    <tr>
      <th>12</th>
      <td>필리핀</td>
      <td>1364239</td>
      <td>55847.0</td>
      <td>23749</td>
      <td>1284643.0</td>
      <td>2</td>
      <td>94.0</td>
      <td>12450</td>
      <td>109581078</td>
      <td>300000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>이집트</td>
      <td>277797</td>
      <td>55846.0</td>
      <td>15898</td>
      <td>206053.0</td>
      <td>6</td>
      <td>74.0</td>
      <td>2715</td>
      <td>102334404</td>
      <td>1010408</td>
    </tr>
    <tr>
      <th>14</th>
      <td>베트남</td>
      <td>13530</td>
      <td>8008.0</td>
      <td>69</td>
      <td>5453.0</td>
      <td>1</td>
      <td>40.0</td>
      <td>139</td>
      <td>97338579</td>
      <td>331210</td>
    </tr>
    <tr>
      <th>15</th>
      <td>콩고민주공화국</td>
      <td>37926</td>
      <td>9109.0</td>
      <td>879</td>
      <td>27938.0</td>
      <td>2</td>
      <td>74.0</td>
      <td>423</td>
      <td>89561403</td>
      <td>2344858</td>
    </tr>
    <tr>
      <th>16</th>
      <td>터키</td>
      <td>5375593</td>
      <td>88626.0</td>
      <td>49236</td>
      <td>5237731.0</td>
      <td>1</td>
      <td>97.0</td>
      <td>63738</td>
      <td>84339067</td>
      <td>783356</td>
    </tr>
    <tr>
      <th>17</th>
      <td>이란</td>
      <td>3105620</td>
      <td>262290.0</td>
      <td>83101</td>
      <td>2760229.0</td>
      <td>3</td>
      <td>89.0</td>
      <td>36975</td>
      <td>83992949</td>
      <td>1648195</td>
    </tr>
    <tr>
      <th>18</th>
      <td>독일</td>
      <td>3730599</td>
      <td>31492.0</td>
      <td>91007</td>
      <td>3608100.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>44526</td>
      <td>83783942</td>
      <td>357022</td>
    </tr>
    <tr>
      <th>19</th>
      <td>태국</td>
      <td>225365</td>
      <td>35836.0</td>
      <td>1693</td>
      <td>187836.0</td>
      <td>1</td>
      <td>83.0</td>
      <td>3229</td>
      <td>69799978</td>
      <td>513120</td>
    </tr>
    <tr>
      <th>20</th>
      <td>영국</td>
      <td>4640507</td>
      <td>208530.0</td>
      <td>127981</td>
      <td>4303996.0</td>
      <td>3</td>
      <td>93.0</td>
      <td>68357</td>
      <td>67886011</td>
      <td>243610</td>
    </tr>
    <tr>
      <th>21</th>
      <td>프랑스</td>
      <td>5757798</td>
      <td>80626.0</td>
      <td>110778</td>
      <td>5566394.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>88210</td>
      <td>65273511</td>
      <td>640679</td>
    </tr>
    <tr>
      <th>22</th>
      <td>이탈리아</td>
      <td>4253460</td>
      <td>76853.0</td>
      <td>127291</td>
      <td>4049316.0</td>
      <td>3</td>
      <td>95.0</td>
      <td>70350</td>
      <td>60461826</td>
      <td>301340</td>
    </tr>
    <tr>
      <th>23</th>
      <td>탄자니아</td>
      <td>509</td>
      <td>305.0</td>
      <td>21</td>
      <td>183.0</td>
      <td>4</td>
      <td>36.0</td>
      <td>9</td>
      <td>59734218</td>
      <td>947303</td>
    </tr>
    <tr>
      <th>24</th>
      <td>남아프리카 공화국</td>
      <td>1832479</td>
      <td>117004.0</td>
      <td>58795</td>
      <td>1656680.0</td>
      <td>3</td>
      <td>90.0</td>
      <td>30897</td>
      <td>59308690</td>
      <td>1219090</td>
    </tr>
    <tr>
      <th>25</th>
      <td>미얀마</td>
      <td>148617</td>
      <td>11599.0</td>
      <td>3265</td>
      <td>133753.0</td>
      <td>2</td>
      <td>90.0</td>
      <td>2731</td>
      <td>54409800</td>
      <td>676578</td>
    </tr>
    <tr>
      <th>26</th>
      <td>케냐</td>
      <td>179293</td>
      <td>52867.0</td>
      <td>3461</td>
      <td>122965.0</td>
      <td>2</td>
      <td>69.0</td>
      <td>3334</td>
      <td>53771296</td>
      <td>580367</td>
    </tr>
    <tr>
      <th>27</th>
      <td>대한민국</td>
      <td>151901</td>
      <td>6078.0</td>
      <td>2006</td>
      <td>143817.0</td>
      <td>1</td>
      <td>95.0</td>
      <td>2963</td>
      <td>51269185</td>
      <td>100412</td>
    </tr>
    <tr>
      <th>28</th>
      <td>콜롬비아</td>
      <td>3968405</td>
      <td>181876.0</td>
      <td>100582</td>
      <td>3685947.0</td>
      <td>3</td>
      <td>93.0</td>
      <td>77991</td>
      <td>50882891</td>
      <td>1138914</td>
    </tr>
    <tr>
      <th>29</th>
      <td>스페인</td>
      <td>3764651</td>
      <td>123928.0</td>
      <td>80689</td>
      <td>3560034.0</td>
      <td>2</td>
      <td>95.0</td>
      <td>80519</td>
      <td>46754778</td>
      <td>505990</td>
    </tr>
    <tr>
      <th>30</th>
      <td>우간다</td>
      <td>72679</td>
      <td>22205.0</td>
      <td>680</td>
      <td>49794.0</td>
      <td>1</td>
      <td>69.0</td>
      <td>1589</td>
      <td>45741007</td>
      <td>241038</td>
    </tr>
    <tr>
      <th>31</th>
      <td>아르헨티나</td>
      <td>4277395</td>
      <td>277070.0</td>
      <td>89490</td>
      <td>3910835.0</td>
      <td>2</td>
      <td>91.0</td>
      <td>94641</td>
      <td>45195774</td>
      <td>2780400</td>
    </tr>
    <tr>
      <th>32</th>
      <td>알제리</td>
      <td>136294</td>
      <td>37831.0</td>
      <td>3641</td>
      <td>94822.0</td>
      <td>3</td>
      <td>70.0</td>
      <td>3108</td>
      <td>43851044</td>
      <td>2381741</td>
    </tr>
    <tr>
      <th>33</th>
      <td>수단</td>
      <td>36347</td>
      <td>3548.0</td>
      <td>2737</td>
      <td>30062.0</td>
      <td>8</td>
      <td>83.0</td>
      <td>829</td>
      <td>43849260</td>
      <td>1861484</td>
    </tr>
    <tr>
      <th>34</th>
      <td>우크라이나</td>
      <td>2229846</td>
      <td>25674.0</td>
      <td>52032</td>
      <td>2152140.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>50987</td>
      <td>43733762</td>
      <td>603628</td>
    </tr>
    <tr>
      <th>35</th>
      <td>이라크</td>
      <td>1292700</td>
      <td>70911.0</td>
      <td>16910</td>
      <td>1204879.0</td>
      <td>1</td>
      <td>93.0</td>
      <td>32139</td>
      <td>40222493</td>
      <td>438317</td>
    </tr>
    <tr>
      <th>36</th>
      <td>아프가니스탄</td>
      <td>105755</td>
      <td>36391.0</td>
      <td>4293</td>
      <td>65071.0</td>
      <td>4</td>
      <td>62.0</td>
      <td>2717</td>
      <td>38928346</td>
      <td>652230</td>
    </tr>
    <tr>
      <th>37</th>
      <td>폴란드</td>
      <td>2878840</td>
      <td>153363.0</td>
      <td>74829</td>
      <td>2650648.0</td>
      <td>3</td>
      <td>92.0</td>
      <td>76066</td>
      <td>37846611</td>
      <td>312685</td>
    </tr>
    <tr>
      <th>38</th>
      <td>캐나다</td>
      <td>1409607</td>
      <td>11032.0</td>
      <td>26084</td>
      <td>1372491.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>37348</td>
      <td>37742154</td>
      <td>9984670</td>
    </tr>
    <tr>
      <th>39</th>
      <td>모로코</td>
      <td>526737</td>
      <td>3595.0</td>
      <td>9244</td>
      <td>513898.0</td>
      <td>2</td>
      <td>98.0</td>
      <td>14271</td>
      <td>36910560</td>
      <td>446550</td>
    </tr>
    <tr>
      <th>40</th>
      <td>사우디아라비아</td>
      <td>475403</td>
      <td>10584.0</td>
      <td>7691</td>
      <td>457128.0</td>
      <td>2</td>
      <td>96.0</td>
      <td>13656</td>
      <td>34813871</td>
      <td>2149690</td>
    </tr>
    <tr>
      <th>41</th>
      <td>우즈베키스탄</td>
      <td>106452</td>
      <td>3571.0</td>
      <td>718</td>
      <td>102163.0</td>
      <td>1</td>
      <td>96.0</td>
      <td>3181</td>
      <td>33469203</td>
      <td>447400</td>
    </tr>
    <tr>
      <th>42</th>
      <td>페루</td>
      <td>2030611</td>
      <td>NaN</td>
      <td>190645</td>
      <td>NaN</td>
      <td>9</td>
      <td>NaN</td>
      <td>61586</td>
      <td>32971854</td>
      <td>1285216</td>
    </tr>
    <tr>
      <th>43</th>
      <td>앙골라</td>
      <td>37748</td>
      <td>5098.0</td>
      <td>868</td>
      <td>31782.0</td>
      <td>2</td>
      <td>84.0</td>
      <td>1149</td>
      <td>32866272</td>
      <td>1246700</td>
    </tr>
    <tr>
      <th>44</th>
      <td>말레이시아</td>
      <td>701019</td>
      <td>62918.0</td>
      <td>4477</td>
      <td>633624.0</td>
      <td>1</td>
      <td>90.0</td>
      <td>21659</td>
      <td>32365999</td>
      <td>329847</td>
    </tr>
    <tr>
      <th>45</th>
      <td>모잠비크</td>
      <td>72577</td>
      <td>1488.0</td>
      <td>848</td>
      <td>70241.0</td>
      <td>1</td>
      <td>97.0</td>
      <td>2322</td>
      <td>31255435</td>
      <td>801590</td>
    </tr>
    <tr>
      <th>46</th>
      <td>가나</td>
      <td>95059</td>
      <td>1260.0</td>
      <td>794</td>
      <td>93005.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>3059</td>
      <td>31072940</td>
      <td>238533</td>
    </tr>
    <tr>
      <th>47</th>
      <td>예멘</td>
      <td>6889</td>
      <td>1576.0</td>
      <td>1355</td>
      <td>3958.0</td>
      <td>20</td>
      <td>58.0</td>
      <td>231</td>
      <td>29825964</td>
      <td>527968</td>
    </tr>
    <tr>
      <th>48</th>
      <td>네팔</td>
      <td>622640</td>
      <td>53940.0</td>
      <td>8772</td>
      <td>559928.0</td>
      <td>1</td>
      <td>90.0</td>
      <td>21370</td>
      <td>29136808</td>
      <td>147516</td>
    </tr>
    <tr>
      <th>49</th>
      <td>베네수엘라</td>
      <td>262038</td>
      <td>16708.0</td>
      <td>2973</td>
      <td>242357.0</td>
      <td>1</td>
      <td>93.0</td>
      <td>9215</td>
      <td>28435940</td>
      <td>912050</td>
    </tr>
    <tr>
      <th>50</th>
      <td>마다가스카르</td>
      <td>42137</td>
      <td>765.0</td>
      <td>903</td>
      <td>40469.0</td>
      <td>2</td>
      <td>96.0</td>
      <td>1522</td>
      <td>27691018</td>
      <td>587041</td>
    </tr>
    <tr>
      <th>51</th>
      <td>카메룬</td>
      <td>80328</td>
      <td>853.0</td>
      <td>1313</td>
      <td>78162.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>3026</td>
      <td>26545863</td>
      <td>475440</td>
    </tr>
    <tr>
      <th>52</th>
      <td>코트디부아르</td>
      <td>48047</td>
      <td>252.0</td>
      <td>308</td>
      <td>47487.0</td>
      <td>1</td>
      <td>99.0</td>
      <td>1821</td>
      <td>26378274</td>
      <td>322463</td>
    </tr>
    <tr>
      <th>53</th>
      <td>호주</td>
      <td>30366</td>
      <td>184.0</td>
      <td>910</td>
      <td>29272.0</td>
      <td>3</td>
      <td>96.0</td>
      <td>1191</td>
      <td>25499884</td>
      <td>7741220</td>
    </tr>
    <tr>
      <th>54</th>
      <td>니제르</td>
      <td>5469</td>
      <td>98.0</td>
      <td>193</td>
      <td>5178.0</td>
      <td>4</td>
      <td>95.0</td>
      <td>226</td>
      <td>24206644</td>
      <td>1267000</td>
    </tr>
    <tr>
      <th>55</th>
      <td>대만</td>
      <td>14080</td>
      <td>5977.0</td>
      <td>569</td>
      <td>7534.0</td>
      <td>4</td>
      <td>54.0</td>
      <td>591</td>
      <td>23816775</td>
      <td>36197</td>
    </tr>
    <tr>
      <th>56</th>
      <td>스리랑카</td>
      <td>241820</td>
      <td>37798.0</td>
      <td>2633</td>
      <td>201389.0</td>
      <td>1</td>
      <td>83.0</td>
      <td>11293</td>
      <td>21413249</td>
      <td>65610</td>
    </tr>
    <tr>
      <th>57</th>
      <td>부르키나파소</td>
      <td>13469</td>
      <td>9.0</td>
      <td>167</td>
      <td>13293.0</td>
      <td>1</td>
      <td>99.0</td>
      <td>644</td>
      <td>20903273</td>
      <td>274200</td>
    </tr>
    <tr>
      <th>58</th>
      <td>말리</td>
      <td>14385</td>
      <td>3825.0</td>
      <td>524</td>
      <td>10036.0</td>
      <td>4</td>
      <td>70.0</td>
      <td>710</td>
      <td>20250833</td>
      <td>1240192</td>
    </tr>
    <tr>
      <th>59</th>
      <td>루마니아</td>
      <td>1080282</td>
      <td>2684.0</td>
      <td>32391</td>
      <td>1045207.0</td>
      <td>3</td>
      <td>97.0</td>
      <td>56154</td>
      <td>19237691</td>
      <td>238391</td>
    </tr>
    <tr>
      <th>60</th>
      <td>말라위</td>
      <td>34914</td>
      <td>852.0</td>
      <td>1171</td>
      <td>32891.0</td>
      <td>3</td>
      <td>94.0</td>
      <td>1825</td>
      <td>19129952</td>
      <td>118484</td>
    </tr>
    <tr>
      <th>61</th>
      <td>칠레</td>
      <td>1522223</td>
      <td>38470.0</td>
      <td>31645</td>
      <td>1452108.0</td>
      <td>2</td>
      <td>95.0</td>
      <td>79630</td>
      <td>19116201</td>
      <td>756096</td>
    </tr>
    <tr>
      <th>62</th>
      <td>카자흐스탄</td>
      <td>410523</td>
      <td>20147.0</td>
      <td>4249</td>
      <td>386127.0</td>
      <td>1</td>
      <td>94.0</td>
      <td>21863</td>
      <td>18776707</td>
      <td>2724900</td>
    </tr>
    <tr>
      <th>63</th>
      <td>잠비아</td>
      <td>130631</td>
      <td>18490.0</td>
      <td>1691</td>
      <td>110450.0</td>
      <td>1</td>
      <td>85.0</td>
      <td>7106</td>
      <td>18383955</td>
      <td>752618</td>
    </tr>
    <tr>
      <th>64</th>
      <td>과테말라</td>
      <td>280854</td>
      <td>17419.0</td>
      <td>8735</td>
      <td>254700.0</td>
      <td>3</td>
      <td>91.0</td>
      <td>15677</td>
      <td>17915568</td>
      <td>108889</td>
    </tr>
    <tr>
      <th>65</th>
      <td>에콰도르</td>
      <td>446633</td>
      <td>9821.0</td>
      <td>21304</td>
      <td>415508.0</td>
      <td>5</td>
      <td>93.0</td>
      <td>25315</td>
      <td>17643054</td>
      <td>283561</td>
    </tr>
    <tr>
      <th>66</th>
      <td>시리아</td>
      <td>25158</td>
      <td>1563.0</td>
      <td>1848</td>
      <td>21747.0</td>
      <td>7</td>
      <td>86.0</td>
      <td>1438</td>
      <td>17500658</td>
      <td>185180</td>
    </tr>
    <tr>
      <th>67</th>
      <td>네덜란드</td>
      <td>1679542</td>
      <td>NaN</td>
      <td>17727</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>98019</td>
      <td>17134872</td>
      <td>41543</td>
    </tr>
    <tr>
      <th>68</th>
      <td>세네갈</td>
      <td>42437</td>
      <td>365.0</td>
      <td>1158</td>
      <td>40914.0</td>
      <td>3</td>
      <td>96.0</td>
      <td>2534</td>
      <td>16743927</td>
      <td>196722</td>
    </tr>
    <tr>
      <th>69</th>
      <td>캄보디아</td>
      <td>43446</td>
      <td>5002.0</td>
      <td>441</td>
      <td>38003.0</td>
      <td>1</td>
      <td>88.0</td>
      <td>2599</td>
      <td>16718965</td>
      <td>181035</td>
    </tr>
    <tr>
      <th>70</th>
      <td>차드</td>
      <td>4947</td>
      <td>5.0</td>
      <td>174</td>
      <td>4768.0</td>
      <td>4</td>
      <td>96.0</td>
      <td>301</td>
      <td>16425864</td>
      <td>1284000</td>
    </tr>
    <tr>
      <th>71</th>
      <td>소말리아</td>
      <td>14867</td>
      <td>6888.0</td>
      <td>775</td>
      <td>7204.0</td>
      <td>5</td>
      <td>49.0</td>
      <td>935</td>
      <td>15893222</td>
      <td>637657</td>
    </tr>
    <tr>
      <th>72</th>
      <td>짐바브웨</td>
      <td>42195</td>
      <td>3310.0</td>
      <td>1685</td>
      <td>37200.0</td>
      <td>4</td>
      <td>88.0</td>
      <td>2839</td>
      <td>14862924</td>
      <td>390757</td>
    </tr>
    <tr>
      <th>73</th>
      <td>기니</td>
      <td>23535</td>
      <td>1085.0</td>
      <td>168</td>
      <td>22282.0</td>
      <td>1</td>
      <td>95.0</td>
      <td>1792</td>
      <td>13132795</td>
      <td>245857</td>
    </tr>
    <tr>
      <th>74</th>
      <td>르완다</td>
      <td>31435</td>
      <td>4343.0</td>
      <td>388</td>
      <td>26704.0</td>
      <td>1</td>
      <td>85.0</td>
      <td>2427</td>
      <td>12952218</td>
      <td>26338</td>
    </tr>
    <tr>
      <th>75</th>
      <td>베냉</td>
      <td>8140</td>
      <td>58.0</td>
      <td>103</td>
      <td>7979.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>671</td>
      <td>12123200</td>
      <td>112622</td>
    </tr>
    <tr>
      <th>76</th>
      <td>부룬디</td>
      <td>5242</td>
      <td>4461.0</td>
      <td>8</td>
      <td>773.0</td>
      <td>0</td>
      <td>15.0</td>
      <td>441</td>
      <td>11890784</td>
      <td>27834</td>
    </tr>
    <tr>
      <th>77</th>
      <td>튀니지</td>
      <td>385428</td>
      <td>34658.0</td>
      <td>14118</td>
      <td>336652.0</td>
      <td>4</td>
      <td>87.0</td>
      <td>32612</td>
      <td>11818619</td>
      <td>163610</td>
    </tr>
    <tr>
      <th>78</th>
      <td>볼리비아</td>
      <td>422811</td>
      <td>65678.0</td>
      <td>16174</td>
      <td>340959.0</td>
      <td>4</td>
      <td>81.0</td>
      <td>36221</td>
      <td>11673021</td>
      <td>1098581</td>
    </tr>
    <tr>
      <th>79</th>
      <td>벨기에</td>
      <td>1079640</td>
      <td>37925.0</td>
      <td>25141</td>
      <td>1016574.0</td>
      <td>2</td>
      <td>94.0</td>
      <td>93156</td>
      <td>11589623</td>
      <td>30528</td>
    </tr>
    <tr>
      <th>80</th>
      <td>아이티</td>
      <td>17371</td>
      <td>4319.0</td>
      <td>385</td>
      <td>12667.0</td>
      <td>2</td>
      <td>73.0</td>
      <td>1523</td>
      <td>11402528</td>
      <td>27750</td>
    </tr>
    <tr>
      <th>81</th>
      <td>남수단</td>
      <td>10786</td>
      <td>157.0</td>
      <td>115</td>
      <td>10514.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>964</td>
      <td>11193725</td>
      <td>644329</td>
    </tr>
    <tr>
      <th>82</th>
      <td>도미니카 공화국</td>
      <td>317645</td>
      <td>54238.0</td>
      <td>3758</td>
      <td>259649.0</td>
      <td>1</td>
      <td>82.0</td>
      <td>29282</td>
      <td>10847910</td>
      <td>48670</td>
    </tr>
    <tr>
      <th>83</th>
      <td>체코</td>
      <td>1666082</td>
      <td>2640.0</td>
      <td>30280</td>
      <td>1633162.0</td>
      <td>2</td>
      <td>98.0</td>
      <td>155578</td>
      <td>10708981</td>
      <td>78867</td>
    </tr>
    <tr>
      <th>84</th>
      <td>그리스</td>
      <td>418548</td>
      <td>6111.0</td>
      <td>12559</td>
      <td>399878.0</td>
      <td>3</td>
      <td>96.0</td>
      <td>40156</td>
      <td>10423054</td>
      <td>131957</td>
    </tr>
    <tr>
      <th>85</th>
      <td>요르단</td>
      <td>747000</td>
      <td>6498.0</td>
      <td>9671</td>
      <td>730831.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>73213</td>
      <td>10203134</td>
      <td>89342</td>
    </tr>
    <tr>
      <th>86</th>
      <td>포르투갈</td>
      <td>865806</td>
      <td>28657.0</td>
      <td>17068</td>
      <td>820081.0</td>
      <td>2</td>
      <td>95.0</td>
      <td>84910</td>
      <td>10196709</td>
      <td>92090</td>
    </tr>
    <tr>
      <th>87</th>
      <td>아제르바이잔</td>
      <td>335521</td>
      <td>959.0</td>
      <td>4963</td>
      <td>329599.0</td>
      <td>2</td>
      <td>98.0</td>
      <td>33092</td>
      <td>10139177</td>
      <td>86600</td>
    </tr>
    <tr>
      <th>88</th>
      <td>스웨덴</td>
      <td>1084636</td>
      <td>NaN</td>
      <td>14537</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>107398</td>
      <td>10099265</td>
      <td>450295</td>
    </tr>
    <tr>
      <th>89</th>
      <td>온두라스</td>
      <td>254194</td>
      <td>155560.0</td>
      <td>6772</td>
      <td>91862.0</td>
      <td>3</td>
      <td>36.0</td>
      <td>25664</td>
      <td>9904607</td>
      <td>112492</td>
    </tr>
  </tbody>
</table>
</div>




```python
## 위의 두 자료를 합치는 과정
target = list(df1['국가'])
country = list(df2['국가'])

gdp = list(df2['2021'])
idx_list = []
new_cty = []
gdp_list = []

for i in target:
    for idx, one in enumerate(country):
        if i == one:
            idx_list.append(idx)
        
for i in idx_list:
    new_cty.append(country[i])
    if gdp[i] == 'no data':
        gdp_list.append(0.0)
    else:
        gdp_list.append(float(gdp[i]))
        
for i in range(90):
    print(target[i], gdp_list[i])
```

    중국 16642.318
    인도 3049.704
    미국 22675.271
    인도네시아 1158.783
    파키스탄 0.0
    브라질 1491.772
    나이지리아 514.049
    방글라데시 352.908
    러시아 1710.734
    멕시코 1192.48
    일본 5378.136
    에티오피아 93.966
    필리핀 402.638
    이집트 394.284
    베트남 354.868
    콩고민주공화국 12.022
    터키 794.53
    이란 682.859
    독일 4319.286
    태국 538.735
    영국 3124.65
    프랑스 2938.271
    이탈리아 2106.287
    탄자니아 65.919
    남아프리카 공화국 329.529
    미얀마 76.195
    케냐 106.041
    대한민국 1806.707
    콜롬비아 295.61
    스페인 1461.552
    우간다 41.271
    아르헨티나 418.15
    알제리 151.459
    수단 35.827
    우크라이나 164.593
    이라크 190.733
    아프가니스탄 19.938
    폴란드 642.121
    캐나다 1883.487
    모로코 124.003
    사우디아라비아 804.921
    우즈베키스탄 61.203
    페루 225.918
    앙골라 66.493
    말레이시아 387.093
    모잠비크 13.957
    가나 74.26
    예멘 25.095
    네팔 36.084
    베네수엘라 42.53
    마다가스카르 14.746
    카메룬 44.893
    코트디부아르 70.991
    호주 1617.543
    니제르 15.899
    대만 759.104
    스리랑카 84.532
    부르키나파소 18.853
    말리 19.912
    루마니아 289.13
    말라위 9.268
    칠레 307.938
    카자흐스탄 187.836
    잠비아 18.955
    과테말라 81.402
    에콰도르 100.595
    시리아 0.0
    네덜란드 1012.598
    세네갈 27.927
    캄보디아 27.239
    차드 12.531
    소말리아 5.367
    짐바브웨 26.085
    기니 16.339
    르완다 10.633
    베냉 17.327
    부룬디 3.244
    튀니지 44.265
    볼리비아 43.11
    벨기에 578.996
    아이티 22.431
    남수단 4.461
    도미니카 공화국 83.917
    체코 276.109
    그리스 209.857
    요르단 44.979
    포르투갈 257.391
    아제르바이잔 49.914
    스웨덴 625.948
    온두라스 26.161
    

### 정확한 통계를 위해 중국은 삭제한다 ...!!


```python
gdp_list = pd.DataFrame(gdp_list)
df1['GDP'] = gdp_list
# df1 = df1.drop([0])
df3 = df1.sort_values(by='인구수', ascending=False).head(30)
# df3 = df3.drop([1])
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>국가</th>
      <th>확진자</th>
      <th>치료중</th>
      <th>사망자</th>
      <th>완치</th>
      <th>치명(%)</th>
      <th>완치(%)</th>
      <th>발생률</th>
      <th>인구수</th>
      <th>국토면적</th>
      <th>GDP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>인도</td>
      <td>29977861</td>
      <td>662521.0</td>
      <td>389302</td>
      <td>28926038.0</td>
      <td>1</td>
      <td>97.0</td>
      <td>21723</td>
      <td>1380004385</td>
      <td>3287263</td>
      <td>3049.704</td>
    </tr>
    <tr>
      <th>2</th>
      <td>미국</td>
      <td>34419838</td>
      <td>5034868.0</td>
      <td>617463</td>
      <td>28767507.0</td>
      <td>2</td>
      <td>84.0</td>
      <td>103987</td>
      <td>331002651</td>
      <td>9833517</td>
      <td>22675.271</td>
    </tr>
    <tr>
      <th>3</th>
      <td>인도네시아</td>
      <td>2004445</td>
      <td>147728.0</td>
      <td>54956</td>
      <td>1801761.0</td>
      <td>3</td>
      <td>90.0</td>
      <td>7328</td>
      <td>273523615</td>
      <td>1904569</td>
      <td>1158.783</td>
    </tr>
    <tr>
      <th>4</th>
      <td>파키스탄</td>
      <td>949838</td>
      <td>33452.0</td>
      <td>22034</td>
      <td>894352.0</td>
      <td>2</td>
      <td>94.0</td>
      <td>4300</td>
      <td>220892340</td>
      <td>796095</td>
      <td>0.000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>브라질</td>
      <td>17969806</td>
      <td>1178597.0</td>
      <td>502817</td>
      <td>16288392.0</td>
      <td>3</td>
      <td>91.0</td>
      <td>84540</td>
      <td>212559417</td>
      <td>8515770</td>
      <td>1491.772</td>
    </tr>
    <tr>
      <th>6</th>
      <td>나이지리아</td>
      <td>167292</td>
      <td>1377.0</td>
      <td>2118</td>
      <td>163797.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>812</td>
      <td>206139589</td>
      <td>923768</td>
      <td>514.049</td>
    </tr>
    <tr>
      <th>7</th>
      <td>방글라데시</td>
      <td>856304</td>
      <td>57196.0</td>
      <td>13626</td>
      <td>785482.0</td>
      <td>2</td>
      <td>92.0</td>
      <td>5200</td>
      <td>164689383</td>
      <td>143998</td>
      <td>352.908</td>
    </tr>
    <tr>
      <th>8</th>
      <td>러시아</td>
      <td>5334204</td>
      <td>326070.0</td>
      <td>129801</td>
      <td>4878333.0</td>
      <td>2</td>
      <td>92.0</td>
      <td>36552</td>
      <td>145934462</td>
      <td>17125407</td>
      <td>1710.734</td>
    </tr>
    <tr>
      <th>9</th>
      <td>멕시코</td>
      <td>2478551</td>
      <td>273052.0</td>
      <td>231244</td>
      <td>1974255.0</td>
      <td>9</td>
      <td>80.0</td>
      <td>19224</td>
      <td>128932753</td>
      <td>1964375</td>
      <td>1192.480</td>
    </tr>
    <tr>
      <th>10</th>
      <td>일본</td>
      <td>785969</td>
      <td>22248.0</td>
      <td>14439</td>
      <td>749282.0</td>
      <td>2</td>
      <td>95.0</td>
      <td>6214</td>
      <td>126476461</td>
      <td>377975</td>
      <td>5378.136</td>
    </tr>
    <tr>
      <th>11</th>
      <td>에티오피아</td>
      <td>275318</td>
      <td>15530.0</td>
      <td>4286</td>
      <td>255502.0</td>
      <td>2</td>
      <td>93.0</td>
      <td>2395</td>
      <td>114963588</td>
      <td>1104300</td>
      <td>93.966</td>
    </tr>
    <tr>
      <th>12</th>
      <td>필리핀</td>
      <td>1364239</td>
      <td>55847.0</td>
      <td>23749</td>
      <td>1284643.0</td>
      <td>2</td>
      <td>94.0</td>
      <td>12450</td>
      <td>109581078</td>
      <td>300000</td>
      <td>402.638</td>
    </tr>
    <tr>
      <th>13</th>
      <td>이집트</td>
      <td>277797</td>
      <td>55846.0</td>
      <td>15898</td>
      <td>206053.0</td>
      <td>6</td>
      <td>74.0</td>
      <td>2715</td>
      <td>102334404</td>
      <td>1010408</td>
      <td>394.284</td>
    </tr>
    <tr>
      <th>14</th>
      <td>베트남</td>
      <td>13530</td>
      <td>8008.0</td>
      <td>69</td>
      <td>5453.0</td>
      <td>1</td>
      <td>40.0</td>
      <td>139</td>
      <td>97338579</td>
      <td>331210</td>
      <td>354.868</td>
    </tr>
    <tr>
      <th>15</th>
      <td>콩고민주공화국</td>
      <td>37926</td>
      <td>9109.0</td>
      <td>879</td>
      <td>27938.0</td>
      <td>2</td>
      <td>74.0</td>
      <td>423</td>
      <td>89561403</td>
      <td>2344858</td>
      <td>12.022</td>
    </tr>
    <tr>
      <th>16</th>
      <td>터키</td>
      <td>5375593</td>
      <td>88626.0</td>
      <td>49236</td>
      <td>5237731.0</td>
      <td>1</td>
      <td>97.0</td>
      <td>63738</td>
      <td>84339067</td>
      <td>783356</td>
      <td>794.530</td>
    </tr>
    <tr>
      <th>17</th>
      <td>이란</td>
      <td>3105620</td>
      <td>262290.0</td>
      <td>83101</td>
      <td>2760229.0</td>
      <td>3</td>
      <td>89.0</td>
      <td>36975</td>
      <td>83992949</td>
      <td>1648195</td>
      <td>682.859</td>
    </tr>
    <tr>
      <th>18</th>
      <td>독일</td>
      <td>3730599</td>
      <td>31492.0</td>
      <td>91007</td>
      <td>3608100.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>44526</td>
      <td>83783942</td>
      <td>357022</td>
      <td>4319.286</td>
    </tr>
    <tr>
      <th>19</th>
      <td>태국</td>
      <td>225365</td>
      <td>35836.0</td>
      <td>1693</td>
      <td>187836.0</td>
      <td>1</td>
      <td>83.0</td>
      <td>3229</td>
      <td>69799978</td>
      <td>513120</td>
      <td>538.735</td>
    </tr>
    <tr>
      <th>20</th>
      <td>영국</td>
      <td>4640507</td>
      <td>208530.0</td>
      <td>127981</td>
      <td>4303996.0</td>
      <td>3</td>
      <td>93.0</td>
      <td>68357</td>
      <td>67886011</td>
      <td>243610</td>
      <td>3124.650</td>
    </tr>
    <tr>
      <th>21</th>
      <td>프랑스</td>
      <td>5757798</td>
      <td>80626.0</td>
      <td>110778</td>
      <td>5566394.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>88210</td>
      <td>65273511</td>
      <td>640679</td>
      <td>2938.271</td>
    </tr>
    <tr>
      <th>22</th>
      <td>이탈리아</td>
      <td>4253460</td>
      <td>76853.0</td>
      <td>127291</td>
      <td>4049316.0</td>
      <td>3</td>
      <td>95.0</td>
      <td>70350</td>
      <td>60461826</td>
      <td>301340</td>
      <td>2106.287</td>
    </tr>
    <tr>
      <th>23</th>
      <td>탄자니아</td>
      <td>509</td>
      <td>305.0</td>
      <td>21</td>
      <td>183.0</td>
      <td>4</td>
      <td>36.0</td>
      <td>9</td>
      <td>59734218</td>
      <td>947303</td>
      <td>65.919</td>
    </tr>
    <tr>
      <th>24</th>
      <td>남아프리카 공화국</td>
      <td>1832479</td>
      <td>117004.0</td>
      <td>58795</td>
      <td>1656680.0</td>
      <td>3</td>
      <td>90.0</td>
      <td>30897</td>
      <td>59308690</td>
      <td>1219090</td>
      <td>329.529</td>
    </tr>
    <tr>
      <th>25</th>
      <td>미얀마</td>
      <td>148617</td>
      <td>11599.0</td>
      <td>3265</td>
      <td>133753.0</td>
      <td>2</td>
      <td>90.0</td>
      <td>2731</td>
      <td>54409800</td>
      <td>676578</td>
      <td>76.195</td>
    </tr>
    <tr>
      <th>26</th>
      <td>케냐</td>
      <td>179293</td>
      <td>52867.0</td>
      <td>3461</td>
      <td>122965.0</td>
      <td>2</td>
      <td>69.0</td>
      <td>3334</td>
      <td>53771296</td>
      <td>580367</td>
      <td>106.041</td>
    </tr>
    <tr>
      <th>27</th>
      <td>대한민국</td>
      <td>151901</td>
      <td>6078.0</td>
      <td>2006</td>
      <td>143817.0</td>
      <td>1</td>
      <td>95.0</td>
      <td>2963</td>
      <td>51269185</td>
      <td>100412</td>
      <td>1806.707</td>
    </tr>
    <tr>
      <th>28</th>
      <td>콜롬비아</td>
      <td>3968405</td>
      <td>181876.0</td>
      <td>100582</td>
      <td>3685947.0</td>
      <td>3</td>
      <td>93.0</td>
      <td>77991</td>
      <td>50882891</td>
      <td>1138914</td>
      <td>295.610</td>
    </tr>
    <tr>
      <th>29</th>
      <td>스페인</td>
      <td>3764651</td>
      <td>123928.0</td>
      <td>80689</td>
      <td>3560034.0</td>
      <td>2</td>
      <td>95.0</td>
      <td>80519</td>
      <td>46754778</td>
      <td>505990</td>
      <td>1461.552</td>
    </tr>
    <tr>
      <th>30</th>
      <td>우간다</td>
      <td>72679</td>
      <td>22205.0</td>
      <td>680</td>
      <td>49794.0</td>
      <td>1</td>
      <td>69.0</td>
      <td>1589</td>
      <td>45741007</td>
      <td>241038</td>
      <td>41.271</td>
    </tr>
    <tr>
      <th>31</th>
      <td>아르헨티나</td>
      <td>4277395</td>
      <td>277070.0</td>
      <td>89490</td>
      <td>3910835.0</td>
      <td>2</td>
      <td>91.0</td>
      <td>94641</td>
      <td>45195774</td>
      <td>2780400</td>
      <td>418.150</td>
    </tr>
    <tr>
      <th>32</th>
      <td>알제리</td>
      <td>136294</td>
      <td>37831.0</td>
      <td>3641</td>
      <td>94822.0</td>
      <td>3</td>
      <td>70.0</td>
      <td>3108</td>
      <td>43851044</td>
      <td>2381741</td>
      <td>151.459</td>
    </tr>
    <tr>
      <th>33</th>
      <td>수단</td>
      <td>36347</td>
      <td>3548.0</td>
      <td>2737</td>
      <td>30062.0</td>
      <td>8</td>
      <td>83.0</td>
      <td>829</td>
      <td>43849260</td>
      <td>1861484</td>
      <td>35.827</td>
    </tr>
    <tr>
      <th>34</th>
      <td>우크라이나</td>
      <td>2229846</td>
      <td>25674.0</td>
      <td>52032</td>
      <td>2152140.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>50987</td>
      <td>43733762</td>
      <td>603628</td>
      <td>164.593</td>
    </tr>
    <tr>
      <th>35</th>
      <td>이라크</td>
      <td>1292700</td>
      <td>70911.0</td>
      <td>16910</td>
      <td>1204879.0</td>
      <td>1</td>
      <td>93.0</td>
      <td>32139</td>
      <td>40222493</td>
      <td>438317</td>
      <td>190.733</td>
    </tr>
    <tr>
      <th>36</th>
      <td>아프가니스탄</td>
      <td>105755</td>
      <td>36391.0</td>
      <td>4293</td>
      <td>65071.0</td>
      <td>4</td>
      <td>62.0</td>
      <td>2717</td>
      <td>38928346</td>
      <td>652230</td>
      <td>19.938</td>
    </tr>
    <tr>
      <th>37</th>
      <td>폴란드</td>
      <td>2878840</td>
      <td>153363.0</td>
      <td>74829</td>
      <td>2650648.0</td>
      <td>3</td>
      <td>92.0</td>
      <td>76066</td>
      <td>37846611</td>
      <td>312685</td>
      <td>642.121</td>
    </tr>
    <tr>
      <th>38</th>
      <td>캐나다</td>
      <td>1409607</td>
      <td>11032.0</td>
      <td>26084</td>
      <td>1372491.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>37348</td>
      <td>37742154</td>
      <td>9984670</td>
      <td>1883.487</td>
    </tr>
    <tr>
      <th>39</th>
      <td>모로코</td>
      <td>526737</td>
      <td>3595.0</td>
      <td>9244</td>
      <td>513898.0</td>
      <td>2</td>
      <td>98.0</td>
      <td>14271</td>
      <td>36910560</td>
      <td>446550</td>
      <td>124.003</td>
    </tr>
    <tr>
      <th>40</th>
      <td>사우디아라비아</td>
      <td>475403</td>
      <td>10584.0</td>
      <td>7691</td>
      <td>457128.0</td>
      <td>2</td>
      <td>96.0</td>
      <td>13656</td>
      <td>34813871</td>
      <td>2149690</td>
      <td>804.921</td>
    </tr>
    <tr>
      <th>41</th>
      <td>우즈베키스탄</td>
      <td>106452</td>
      <td>3571.0</td>
      <td>718</td>
      <td>102163.0</td>
      <td>1</td>
      <td>96.0</td>
      <td>3181</td>
      <td>33469203</td>
      <td>447400</td>
      <td>61.203</td>
    </tr>
    <tr>
      <th>42</th>
      <td>페루</td>
      <td>2030611</td>
      <td>NaN</td>
      <td>190645</td>
      <td>NaN</td>
      <td>9</td>
      <td>NaN</td>
      <td>61586</td>
      <td>32971854</td>
      <td>1285216</td>
      <td>225.918</td>
    </tr>
    <tr>
      <th>43</th>
      <td>앙골라</td>
      <td>37748</td>
      <td>5098.0</td>
      <td>868</td>
      <td>31782.0</td>
      <td>2</td>
      <td>84.0</td>
      <td>1149</td>
      <td>32866272</td>
      <td>1246700</td>
      <td>66.493</td>
    </tr>
    <tr>
      <th>44</th>
      <td>말레이시아</td>
      <td>701019</td>
      <td>62918.0</td>
      <td>4477</td>
      <td>633624.0</td>
      <td>1</td>
      <td>90.0</td>
      <td>21659</td>
      <td>32365999</td>
      <td>329847</td>
      <td>387.093</td>
    </tr>
    <tr>
      <th>45</th>
      <td>모잠비크</td>
      <td>72577</td>
      <td>1488.0</td>
      <td>848</td>
      <td>70241.0</td>
      <td>1</td>
      <td>97.0</td>
      <td>2322</td>
      <td>31255435</td>
      <td>801590</td>
      <td>13.957</td>
    </tr>
    <tr>
      <th>46</th>
      <td>가나</td>
      <td>95059</td>
      <td>1260.0</td>
      <td>794</td>
      <td>93005.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>3059</td>
      <td>31072940</td>
      <td>238533</td>
      <td>74.260</td>
    </tr>
    <tr>
      <th>47</th>
      <td>예멘</td>
      <td>6889</td>
      <td>1576.0</td>
      <td>1355</td>
      <td>3958.0</td>
      <td>20</td>
      <td>58.0</td>
      <td>231</td>
      <td>29825964</td>
      <td>527968</td>
      <td>25.095</td>
    </tr>
    <tr>
      <th>48</th>
      <td>네팔</td>
      <td>622640</td>
      <td>53940.0</td>
      <td>8772</td>
      <td>559928.0</td>
      <td>1</td>
      <td>90.0</td>
      <td>21370</td>
      <td>29136808</td>
      <td>147516</td>
      <td>36.084</td>
    </tr>
    <tr>
      <th>49</th>
      <td>베네수엘라</td>
      <td>262038</td>
      <td>16708.0</td>
      <td>2973</td>
      <td>242357.0</td>
      <td>1</td>
      <td>93.0</td>
      <td>9215</td>
      <td>28435940</td>
      <td>912050</td>
      <td>42.530</td>
    </tr>
    <tr>
      <th>50</th>
      <td>마다가스카르</td>
      <td>42137</td>
      <td>765.0</td>
      <td>903</td>
      <td>40469.0</td>
      <td>2</td>
      <td>96.0</td>
      <td>1522</td>
      <td>27691018</td>
      <td>587041</td>
      <td>14.746</td>
    </tr>
    <tr>
      <th>51</th>
      <td>카메룬</td>
      <td>80328</td>
      <td>853.0</td>
      <td>1313</td>
      <td>78162.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>3026</td>
      <td>26545863</td>
      <td>475440</td>
      <td>44.893</td>
    </tr>
    <tr>
      <th>52</th>
      <td>코트디부아르</td>
      <td>48047</td>
      <td>252.0</td>
      <td>308</td>
      <td>47487.0</td>
      <td>1</td>
      <td>99.0</td>
      <td>1821</td>
      <td>26378274</td>
      <td>322463</td>
      <td>70.991</td>
    </tr>
    <tr>
      <th>53</th>
      <td>호주</td>
      <td>30366</td>
      <td>184.0</td>
      <td>910</td>
      <td>29272.0</td>
      <td>3</td>
      <td>96.0</td>
      <td>1191</td>
      <td>25499884</td>
      <td>7741220</td>
      <td>1617.543</td>
    </tr>
    <tr>
      <th>54</th>
      <td>니제르</td>
      <td>5469</td>
      <td>98.0</td>
      <td>193</td>
      <td>5178.0</td>
      <td>4</td>
      <td>95.0</td>
      <td>226</td>
      <td>24206644</td>
      <td>1267000</td>
      <td>15.899</td>
    </tr>
    <tr>
      <th>55</th>
      <td>대만</td>
      <td>14080</td>
      <td>5977.0</td>
      <td>569</td>
      <td>7534.0</td>
      <td>4</td>
      <td>54.0</td>
      <td>591</td>
      <td>23816775</td>
      <td>36197</td>
      <td>759.104</td>
    </tr>
    <tr>
      <th>56</th>
      <td>스리랑카</td>
      <td>241820</td>
      <td>37798.0</td>
      <td>2633</td>
      <td>201389.0</td>
      <td>1</td>
      <td>83.0</td>
      <td>11293</td>
      <td>21413249</td>
      <td>65610</td>
      <td>84.532</td>
    </tr>
    <tr>
      <th>57</th>
      <td>부르키나파소</td>
      <td>13469</td>
      <td>9.0</td>
      <td>167</td>
      <td>13293.0</td>
      <td>1</td>
      <td>99.0</td>
      <td>644</td>
      <td>20903273</td>
      <td>274200</td>
      <td>18.853</td>
    </tr>
    <tr>
      <th>58</th>
      <td>말리</td>
      <td>14385</td>
      <td>3825.0</td>
      <td>524</td>
      <td>10036.0</td>
      <td>4</td>
      <td>70.0</td>
      <td>710</td>
      <td>20250833</td>
      <td>1240192</td>
      <td>19.912</td>
    </tr>
    <tr>
      <th>59</th>
      <td>루마니아</td>
      <td>1080282</td>
      <td>2684.0</td>
      <td>32391</td>
      <td>1045207.0</td>
      <td>3</td>
      <td>97.0</td>
      <td>56154</td>
      <td>19237691</td>
      <td>238391</td>
      <td>289.130</td>
    </tr>
    <tr>
      <th>60</th>
      <td>말라위</td>
      <td>34914</td>
      <td>852.0</td>
      <td>1171</td>
      <td>32891.0</td>
      <td>3</td>
      <td>94.0</td>
      <td>1825</td>
      <td>19129952</td>
      <td>118484</td>
      <td>9.268</td>
    </tr>
    <tr>
      <th>61</th>
      <td>칠레</td>
      <td>1522223</td>
      <td>38470.0</td>
      <td>31645</td>
      <td>1452108.0</td>
      <td>2</td>
      <td>95.0</td>
      <td>79630</td>
      <td>19116201</td>
      <td>756096</td>
      <td>307.938</td>
    </tr>
    <tr>
      <th>62</th>
      <td>카자흐스탄</td>
      <td>410523</td>
      <td>20147.0</td>
      <td>4249</td>
      <td>386127.0</td>
      <td>1</td>
      <td>94.0</td>
      <td>21863</td>
      <td>18776707</td>
      <td>2724900</td>
      <td>187.836</td>
    </tr>
    <tr>
      <th>63</th>
      <td>잠비아</td>
      <td>130631</td>
      <td>18490.0</td>
      <td>1691</td>
      <td>110450.0</td>
      <td>1</td>
      <td>85.0</td>
      <td>7106</td>
      <td>18383955</td>
      <td>752618</td>
      <td>18.955</td>
    </tr>
    <tr>
      <th>64</th>
      <td>과테말라</td>
      <td>280854</td>
      <td>17419.0</td>
      <td>8735</td>
      <td>254700.0</td>
      <td>3</td>
      <td>91.0</td>
      <td>15677</td>
      <td>17915568</td>
      <td>108889</td>
      <td>81.402</td>
    </tr>
    <tr>
      <th>65</th>
      <td>에콰도르</td>
      <td>446633</td>
      <td>9821.0</td>
      <td>21304</td>
      <td>415508.0</td>
      <td>5</td>
      <td>93.0</td>
      <td>25315</td>
      <td>17643054</td>
      <td>283561</td>
      <td>100.595</td>
    </tr>
    <tr>
      <th>66</th>
      <td>시리아</td>
      <td>25158</td>
      <td>1563.0</td>
      <td>1848</td>
      <td>21747.0</td>
      <td>7</td>
      <td>86.0</td>
      <td>1438</td>
      <td>17500658</td>
      <td>185180</td>
      <td>0.000</td>
    </tr>
    <tr>
      <th>67</th>
      <td>네덜란드</td>
      <td>1679542</td>
      <td>NaN</td>
      <td>17727</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>98019</td>
      <td>17134872</td>
      <td>41543</td>
      <td>1012.598</td>
    </tr>
    <tr>
      <th>68</th>
      <td>세네갈</td>
      <td>42437</td>
      <td>365.0</td>
      <td>1158</td>
      <td>40914.0</td>
      <td>3</td>
      <td>96.0</td>
      <td>2534</td>
      <td>16743927</td>
      <td>196722</td>
      <td>27.927</td>
    </tr>
    <tr>
      <th>69</th>
      <td>캄보디아</td>
      <td>43446</td>
      <td>5002.0</td>
      <td>441</td>
      <td>38003.0</td>
      <td>1</td>
      <td>88.0</td>
      <td>2599</td>
      <td>16718965</td>
      <td>181035</td>
      <td>27.239</td>
    </tr>
    <tr>
      <th>70</th>
      <td>차드</td>
      <td>4947</td>
      <td>5.0</td>
      <td>174</td>
      <td>4768.0</td>
      <td>4</td>
      <td>96.0</td>
      <td>301</td>
      <td>16425864</td>
      <td>1284000</td>
      <td>12.531</td>
    </tr>
    <tr>
      <th>71</th>
      <td>소말리아</td>
      <td>14867</td>
      <td>6888.0</td>
      <td>775</td>
      <td>7204.0</td>
      <td>5</td>
      <td>49.0</td>
      <td>935</td>
      <td>15893222</td>
      <td>637657</td>
      <td>5.367</td>
    </tr>
    <tr>
      <th>72</th>
      <td>짐바브웨</td>
      <td>42195</td>
      <td>3310.0</td>
      <td>1685</td>
      <td>37200.0</td>
      <td>4</td>
      <td>88.0</td>
      <td>2839</td>
      <td>14862924</td>
      <td>390757</td>
      <td>26.085</td>
    </tr>
    <tr>
      <th>73</th>
      <td>기니</td>
      <td>23535</td>
      <td>1085.0</td>
      <td>168</td>
      <td>22282.0</td>
      <td>1</td>
      <td>95.0</td>
      <td>1792</td>
      <td>13132795</td>
      <td>245857</td>
      <td>16.339</td>
    </tr>
    <tr>
      <th>74</th>
      <td>르완다</td>
      <td>31435</td>
      <td>4343.0</td>
      <td>388</td>
      <td>26704.0</td>
      <td>1</td>
      <td>85.0</td>
      <td>2427</td>
      <td>12952218</td>
      <td>26338</td>
      <td>10.633</td>
    </tr>
    <tr>
      <th>75</th>
      <td>베냉</td>
      <td>8140</td>
      <td>58.0</td>
      <td>103</td>
      <td>7979.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>671</td>
      <td>12123200</td>
      <td>112622</td>
      <td>17.327</td>
    </tr>
    <tr>
      <th>76</th>
      <td>부룬디</td>
      <td>5242</td>
      <td>4461.0</td>
      <td>8</td>
      <td>773.0</td>
      <td>0</td>
      <td>15.0</td>
      <td>441</td>
      <td>11890784</td>
      <td>27834</td>
      <td>3.244</td>
    </tr>
    <tr>
      <th>77</th>
      <td>튀니지</td>
      <td>385428</td>
      <td>34658.0</td>
      <td>14118</td>
      <td>336652.0</td>
      <td>4</td>
      <td>87.0</td>
      <td>32612</td>
      <td>11818619</td>
      <td>163610</td>
      <td>44.265</td>
    </tr>
    <tr>
      <th>78</th>
      <td>볼리비아</td>
      <td>422811</td>
      <td>65678.0</td>
      <td>16174</td>
      <td>340959.0</td>
      <td>4</td>
      <td>81.0</td>
      <td>36221</td>
      <td>11673021</td>
      <td>1098581</td>
      <td>43.110</td>
    </tr>
    <tr>
      <th>79</th>
      <td>벨기에</td>
      <td>1079640</td>
      <td>37925.0</td>
      <td>25141</td>
      <td>1016574.0</td>
      <td>2</td>
      <td>94.0</td>
      <td>93156</td>
      <td>11589623</td>
      <td>30528</td>
      <td>578.996</td>
    </tr>
    <tr>
      <th>80</th>
      <td>아이티</td>
      <td>17371</td>
      <td>4319.0</td>
      <td>385</td>
      <td>12667.0</td>
      <td>2</td>
      <td>73.0</td>
      <td>1523</td>
      <td>11402528</td>
      <td>27750</td>
      <td>22.431</td>
    </tr>
    <tr>
      <th>81</th>
      <td>남수단</td>
      <td>10786</td>
      <td>157.0</td>
      <td>115</td>
      <td>10514.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>964</td>
      <td>11193725</td>
      <td>644329</td>
      <td>4.461</td>
    </tr>
    <tr>
      <th>82</th>
      <td>도미니카 공화국</td>
      <td>317645</td>
      <td>54238.0</td>
      <td>3758</td>
      <td>259649.0</td>
      <td>1</td>
      <td>82.0</td>
      <td>29282</td>
      <td>10847910</td>
      <td>48670</td>
      <td>83.917</td>
    </tr>
    <tr>
      <th>83</th>
      <td>체코</td>
      <td>1666082</td>
      <td>2640.0</td>
      <td>30280</td>
      <td>1633162.0</td>
      <td>2</td>
      <td>98.0</td>
      <td>155578</td>
      <td>10708981</td>
      <td>78867</td>
      <td>276.109</td>
    </tr>
    <tr>
      <th>84</th>
      <td>그리스</td>
      <td>418548</td>
      <td>6111.0</td>
      <td>12559</td>
      <td>399878.0</td>
      <td>3</td>
      <td>96.0</td>
      <td>40156</td>
      <td>10423054</td>
      <td>131957</td>
      <td>209.857</td>
    </tr>
    <tr>
      <th>85</th>
      <td>요르단</td>
      <td>747000</td>
      <td>6498.0</td>
      <td>9671</td>
      <td>730831.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>73213</td>
      <td>10203134</td>
      <td>89342</td>
      <td>44.979</td>
    </tr>
    <tr>
      <th>86</th>
      <td>포르투갈</td>
      <td>865806</td>
      <td>28657.0</td>
      <td>17068</td>
      <td>820081.0</td>
      <td>2</td>
      <td>95.0</td>
      <td>84910</td>
      <td>10196709</td>
      <td>92090</td>
      <td>257.391</td>
    </tr>
    <tr>
      <th>87</th>
      <td>아제르바이잔</td>
      <td>335521</td>
      <td>959.0</td>
      <td>4963</td>
      <td>329599.0</td>
      <td>2</td>
      <td>98.0</td>
      <td>33092</td>
      <td>10139177</td>
      <td>86600</td>
      <td>49.914</td>
    </tr>
    <tr>
      <th>88</th>
      <td>스웨덴</td>
      <td>1084636</td>
      <td>NaN</td>
      <td>14537</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>107398</td>
      <td>10099265</td>
      <td>450295</td>
      <td>625.948</td>
    </tr>
    <tr>
      <th>89</th>
      <td>온두라스</td>
      <td>254194</td>
      <td>155560.0</td>
      <td>6772</td>
      <td>91862.0</td>
      <td>3</td>
      <td>36.0</td>
      <td>25664</td>
      <td>9904607</td>
      <td>112492</td>
      <td>26.161</td>
    </tr>
  </tbody>
</table>
</div>




```python
%matplotlib inline 
```


```python
# 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처
matplotlib.rcParams['axes.unicode_minus'] = False
```


```python
## 한글 폰트 적용 ( 안하면 한글 깨짐 )
f_name = fm.FontProperties(fname="C:/Windows/Fonts/malgunbd.ttf").get_name()
plt.rc('font', family=f_name)
```

## 인구수 하위 30개국 확진자 비율

### 인도의 인구수가 다른 나라들에 비해 매우 많으므로 일시적으로 제외시켰습니다.


```python
fig = plt.figure(figsize=(10, 8))
fig.patch.set_facecolor('xkcd:white')

sns.set_color_codes('pastel')
sns.barplot(x='인구수', y='국가', data=df3, label='인구수', color='b')

sns.set_color_codes('muted')
sns.barplot(x='확진자', y='국가', data=df3, label='확진자', color='b')

fig.legend(ncol=1, loc="upper right")

sns.despine()
```


    
![png](output_11_0.png)
    


### 데이터 해석 : 
이 데이터에서는 확진자가 눈에 띄게 보이는 몇몇 국가들이 있습니다.

- 미국의 경우에는 전 세계적으로 GDP가 가장 높으면서 확진자가 가장 많습니다. 도심지를 주변으로 사람들이 매우 밀집해있으며, 몇몇 보수적인 시민들의 단체행동으로 인해 확진자가 크게 늘어나게 되었습니다.
- 브라질의 경우에는 대통령이 적극적으로 방역활동을 지시하지 않은 것이 큰 문제점이었습니다. 심지어 대면활동과 경제활동을 장려하기까지 했고, 이로 인해 수많은 사람들이 죽어나갔습니다.
- 그리고 여러 유럽국가에서, 우선 처음으로 변이바이러스가 발생한 곳이 영국이었고, 그를 중심으로 코로나 바이러스가 크게 확산하기도 하였습니다.

## 인구수 하위 30개국 확진자 비율


```python
df4 = df1.sort_values(by='인구수', ascending=False).tail(30)

fig = plt.figure(figsize=(10, 8))
fig.patch.set_facecolor('xkcd:white')

sns.set_color_codes('pastel')
sns.barplot(x='인구수', y='국가', data=df4, label='인구수', color='b')

sns.set_color_codes('muted')
sns.barplot(x='확진자', y='국가', data=df4, label='확진자', color='b')

fig.legend(ncol=1, loc="upper right")

sns.despine()
```


    
![png](output_14_0.png)
    



```python
df1['인구밀도'] = df1['인구수']/df1['국토면적']   # 인구밀도 Column 추가
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>국가</th>
      <th>확진자</th>
      <th>치료중</th>
      <th>사망자</th>
      <th>완치</th>
      <th>치명(%)</th>
      <th>완치(%)</th>
      <th>발생률</th>
      <th>인구수</th>
      <th>국토면적</th>
      <th>GDP</th>
      <th>인구밀도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>인도</td>
      <td>29977861</td>
      <td>662521.0</td>
      <td>389302</td>
      <td>28926038.0</td>
      <td>1</td>
      <td>97.0</td>
      <td>21723</td>
      <td>1380004385</td>
      <td>3287263</td>
      <td>3049.704</td>
      <td>419.803461</td>
    </tr>
    <tr>
      <th>2</th>
      <td>미국</td>
      <td>34419838</td>
      <td>5034868.0</td>
      <td>617463</td>
      <td>28767507.0</td>
      <td>2</td>
      <td>84.0</td>
      <td>103987</td>
      <td>331002651</td>
      <td>9833517</td>
      <td>22675.271</td>
      <td>33.660658</td>
    </tr>
    <tr>
      <th>3</th>
      <td>인도네시아</td>
      <td>2004445</td>
      <td>147728.0</td>
      <td>54956</td>
      <td>1801761.0</td>
      <td>3</td>
      <td>90.0</td>
      <td>7328</td>
      <td>273523615</td>
      <td>1904569</td>
      <td>1158.783</td>
      <td>143.614442</td>
    </tr>
    <tr>
      <th>4</th>
      <td>파키스탄</td>
      <td>949838</td>
      <td>33452.0</td>
      <td>22034</td>
      <td>894352.0</td>
      <td>2</td>
      <td>94.0</td>
      <td>4300</td>
      <td>220892340</td>
      <td>796095</td>
      <td>0.000</td>
      <td>277.469825</td>
    </tr>
    <tr>
      <th>5</th>
      <td>브라질</td>
      <td>17969806</td>
      <td>1178597.0</td>
      <td>502817</td>
      <td>16288392.0</td>
      <td>3</td>
      <td>91.0</td>
      <td>84540</td>
      <td>212559417</td>
      <td>8515770</td>
      <td>1491.772</td>
      <td>24.960681</td>
    </tr>
    <tr>
      <th>6</th>
      <td>나이지리아</td>
      <td>167292</td>
      <td>1377.0</td>
      <td>2118</td>
      <td>163797.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>812</td>
      <td>206139589</td>
      <td>923768</td>
      <td>514.049</td>
      <td>223.150823</td>
    </tr>
    <tr>
      <th>7</th>
      <td>방글라데시</td>
      <td>856304</td>
      <td>57196.0</td>
      <td>13626</td>
      <td>785482.0</td>
      <td>2</td>
      <td>92.0</td>
      <td>5200</td>
      <td>164689383</td>
      <td>143998</td>
      <td>352.908</td>
      <td>1143.692155</td>
    </tr>
    <tr>
      <th>8</th>
      <td>러시아</td>
      <td>5334204</td>
      <td>326070.0</td>
      <td>129801</td>
      <td>4878333.0</td>
      <td>2</td>
      <td>92.0</td>
      <td>36552</td>
      <td>145934462</td>
      <td>17125407</td>
      <td>1710.734</td>
      <td>8.521518</td>
    </tr>
    <tr>
      <th>9</th>
      <td>멕시코</td>
      <td>2478551</td>
      <td>273052.0</td>
      <td>231244</td>
      <td>1974255.0</td>
      <td>9</td>
      <td>80.0</td>
      <td>19224</td>
      <td>128932753</td>
      <td>1964375</td>
      <td>1192.480</td>
      <td>65.635509</td>
    </tr>
    <tr>
      <th>10</th>
      <td>일본</td>
      <td>785969</td>
      <td>22248.0</td>
      <td>14439</td>
      <td>749282.0</td>
      <td>2</td>
      <td>95.0</td>
      <td>6214</td>
      <td>126476461</td>
      <td>377975</td>
      <td>5378.136</td>
      <td>334.615943</td>
    </tr>
    <tr>
      <th>11</th>
      <td>에티오피아</td>
      <td>275318</td>
      <td>15530.0</td>
      <td>4286</td>
      <td>255502.0</td>
      <td>2</td>
      <td>93.0</td>
      <td>2395</td>
      <td>114963588</td>
      <td>1104300</td>
      <td>93.966</td>
      <td>104.105395</td>
    </tr>
    <tr>
      <th>12</th>
      <td>필리핀</td>
      <td>1364239</td>
      <td>55847.0</td>
      <td>23749</td>
      <td>1284643.0</td>
      <td>2</td>
      <td>94.0</td>
      <td>12450</td>
      <td>109581078</td>
      <td>300000</td>
      <td>402.638</td>
      <td>365.270260</td>
    </tr>
    <tr>
      <th>13</th>
      <td>이집트</td>
      <td>277797</td>
      <td>55846.0</td>
      <td>15898</td>
      <td>206053.0</td>
      <td>6</td>
      <td>74.0</td>
      <td>2715</td>
      <td>102334404</td>
      <td>1010408</td>
      <td>394.284</td>
      <td>101.280279</td>
    </tr>
    <tr>
      <th>14</th>
      <td>베트남</td>
      <td>13530</td>
      <td>8008.0</td>
      <td>69</td>
      <td>5453.0</td>
      <td>1</td>
      <td>40.0</td>
      <td>139</td>
      <td>97338579</td>
      <td>331210</td>
      <td>354.868</td>
      <td>293.887802</td>
    </tr>
    <tr>
      <th>15</th>
      <td>콩고민주공화국</td>
      <td>37926</td>
      <td>9109.0</td>
      <td>879</td>
      <td>27938.0</td>
      <td>2</td>
      <td>74.0</td>
      <td>423</td>
      <td>89561403</td>
      <td>2344858</td>
      <td>12.022</td>
      <td>38.194809</td>
    </tr>
    <tr>
      <th>16</th>
      <td>터키</td>
      <td>5375593</td>
      <td>88626.0</td>
      <td>49236</td>
      <td>5237731.0</td>
      <td>1</td>
      <td>97.0</td>
      <td>63738</td>
      <td>84339067</td>
      <td>783356</td>
      <td>794.530</td>
      <td>107.663779</td>
    </tr>
    <tr>
      <th>17</th>
      <td>이란</td>
      <td>3105620</td>
      <td>262290.0</td>
      <td>83101</td>
      <td>2760229.0</td>
      <td>3</td>
      <td>89.0</td>
      <td>36975</td>
      <td>83992949</td>
      <td>1648195</td>
      <td>682.859</td>
      <td>50.960565</td>
    </tr>
    <tr>
      <th>18</th>
      <td>독일</td>
      <td>3730599</td>
      <td>31492.0</td>
      <td>91007</td>
      <td>3608100.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>44526</td>
      <td>83783942</td>
      <td>357022</td>
      <td>4319.286</td>
      <td>234.674451</td>
    </tr>
    <tr>
      <th>19</th>
      <td>태국</td>
      <td>225365</td>
      <td>35836.0</td>
      <td>1693</td>
      <td>187836.0</td>
      <td>1</td>
      <td>83.0</td>
      <td>3229</td>
      <td>69799978</td>
      <td>513120</td>
      <td>538.735</td>
      <td>136.030515</td>
    </tr>
    <tr>
      <th>20</th>
      <td>영국</td>
      <td>4640507</td>
      <td>208530.0</td>
      <td>127981</td>
      <td>4303996.0</td>
      <td>3</td>
      <td>93.0</td>
      <td>68357</td>
      <td>67886011</td>
      <td>243610</td>
      <td>3124.650</td>
      <td>278.666767</td>
    </tr>
    <tr>
      <th>21</th>
      <td>프랑스</td>
      <td>5757798</td>
      <td>80626.0</td>
      <td>110778</td>
      <td>5566394.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>88210</td>
      <td>65273511</td>
      <td>640679</td>
      <td>2938.271</td>
      <td>101.881771</td>
    </tr>
    <tr>
      <th>22</th>
      <td>이탈리아</td>
      <td>4253460</td>
      <td>76853.0</td>
      <td>127291</td>
      <td>4049316.0</td>
      <td>3</td>
      <td>95.0</td>
      <td>70350</td>
      <td>60461826</td>
      <td>301340</td>
      <td>2106.287</td>
      <td>200.643214</td>
    </tr>
    <tr>
      <th>23</th>
      <td>탄자니아</td>
      <td>509</td>
      <td>305.0</td>
      <td>21</td>
      <td>183.0</td>
      <td>4</td>
      <td>36.0</td>
      <td>9</td>
      <td>59734218</td>
      <td>947303</td>
      <td>65.919</td>
      <td>63.057140</td>
    </tr>
    <tr>
      <th>24</th>
      <td>남아프리카 공화국</td>
      <td>1832479</td>
      <td>117004.0</td>
      <td>58795</td>
      <td>1656680.0</td>
      <td>3</td>
      <td>90.0</td>
      <td>30897</td>
      <td>59308690</td>
      <td>1219090</td>
      <td>329.529</td>
      <td>48.649968</td>
    </tr>
    <tr>
      <th>25</th>
      <td>미얀마</td>
      <td>148617</td>
      <td>11599.0</td>
      <td>3265</td>
      <td>133753.0</td>
      <td>2</td>
      <td>90.0</td>
      <td>2731</td>
      <td>54409800</td>
      <td>676578</td>
      <td>76.195</td>
      <td>80.419109</td>
    </tr>
    <tr>
      <th>26</th>
      <td>케냐</td>
      <td>179293</td>
      <td>52867.0</td>
      <td>3461</td>
      <td>122965.0</td>
      <td>2</td>
      <td>69.0</td>
      <td>3334</td>
      <td>53771296</td>
      <td>580367</td>
      <td>106.041</td>
      <td>92.650506</td>
    </tr>
    <tr>
      <th>27</th>
      <td>대한민국</td>
      <td>151901</td>
      <td>6078.0</td>
      <td>2006</td>
      <td>143817.0</td>
      <td>1</td>
      <td>95.0</td>
      <td>2963</td>
      <td>51269185</td>
      <td>100412</td>
      <td>1806.707</td>
      <td>510.588227</td>
    </tr>
    <tr>
      <th>28</th>
      <td>콜롬비아</td>
      <td>3968405</td>
      <td>181876.0</td>
      <td>100582</td>
      <td>3685947.0</td>
      <td>3</td>
      <td>93.0</td>
      <td>77991</td>
      <td>50882891</td>
      <td>1138914</td>
      <td>295.610</td>
      <td>44.676675</td>
    </tr>
    <tr>
      <th>29</th>
      <td>스페인</td>
      <td>3764651</td>
      <td>123928.0</td>
      <td>80689</td>
      <td>3560034.0</td>
      <td>2</td>
      <td>95.0</td>
      <td>80519</td>
      <td>46754778</td>
      <td>505990</td>
      <td>1461.552</td>
      <td>92.402573</td>
    </tr>
    <tr>
      <th>30</th>
      <td>우간다</td>
      <td>72679</td>
      <td>22205.0</td>
      <td>680</td>
      <td>49794.0</td>
      <td>1</td>
      <td>69.0</td>
      <td>1589</td>
      <td>45741007</td>
      <td>241038</td>
      <td>41.271</td>
      <td>189.766788</td>
    </tr>
    <tr>
      <th>31</th>
      <td>아르헨티나</td>
      <td>4277395</td>
      <td>277070.0</td>
      <td>89490</td>
      <td>3910835.0</td>
      <td>2</td>
      <td>91.0</td>
      <td>94641</td>
      <td>45195774</td>
      <td>2780400</td>
      <td>418.150</td>
      <td>16.255134</td>
    </tr>
    <tr>
      <th>32</th>
      <td>알제리</td>
      <td>136294</td>
      <td>37831.0</td>
      <td>3641</td>
      <td>94822.0</td>
      <td>3</td>
      <td>70.0</td>
      <td>3108</td>
      <td>43851044</td>
      <td>2381741</td>
      <td>151.459</td>
      <td>18.411340</td>
    </tr>
    <tr>
      <th>33</th>
      <td>수단</td>
      <td>36347</td>
      <td>3548.0</td>
      <td>2737</td>
      <td>30062.0</td>
      <td>8</td>
      <td>83.0</td>
      <td>829</td>
      <td>43849260</td>
      <td>1861484</td>
      <td>35.827</td>
      <td>23.556077</td>
    </tr>
    <tr>
      <th>34</th>
      <td>우크라이나</td>
      <td>2229846</td>
      <td>25674.0</td>
      <td>52032</td>
      <td>2152140.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>50987</td>
      <td>43733762</td>
      <td>603628</td>
      <td>164.593</td>
      <td>72.451513</td>
    </tr>
    <tr>
      <th>35</th>
      <td>이라크</td>
      <td>1292700</td>
      <td>70911.0</td>
      <td>16910</td>
      <td>1204879.0</td>
      <td>1</td>
      <td>93.0</td>
      <td>32139</td>
      <td>40222493</td>
      <td>438317</td>
      <td>190.733</td>
      <td>91.765761</td>
    </tr>
    <tr>
      <th>36</th>
      <td>아프가니스탄</td>
      <td>105755</td>
      <td>36391.0</td>
      <td>4293</td>
      <td>65071.0</td>
      <td>4</td>
      <td>62.0</td>
      <td>2717</td>
      <td>38928346</td>
      <td>652230</td>
      <td>19.938</td>
      <td>59.684998</td>
    </tr>
    <tr>
      <th>37</th>
      <td>폴란드</td>
      <td>2878840</td>
      <td>153363.0</td>
      <td>74829</td>
      <td>2650648.0</td>
      <td>3</td>
      <td>92.0</td>
      <td>76066</td>
      <td>37846611</td>
      <td>312685</td>
      <td>642.121</td>
      <td>121.037501</td>
    </tr>
    <tr>
      <th>38</th>
      <td>캐나다</td>
      <td>1409607</td>
      <td>11032.0</td>
      <td>26084</td>
      <td>1372491.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>37348</td>
      <td>37742154</td>
      <td>9984670</td>
      <td>1883.487</td>
      <td>3.780010</td>
    </tr>
    <tr>
      <th>39</th>
      <td>모로코</td>
      <td>526737</td>
      <td>3595.0</td>
      <td>9244</td>
      <td>513898.0</td>
      <td>2</td>
      <td>98.0</td>
      <td>14271</td>
      <td>36910560</td>
      <td>446550</td>
      <td>124.003</td>
      <td>82.657172</td>
    </tr>
    <tr>
      <th>40</th>
      <td>사우디아라비아</td>
      <td>475403</td>
      <td>10584.0</td>
      <td>7691</td>
      <td>457128.0</td>
      <td>2</td>
      <td>96.0</td>
      <td>13656</td>
      <td>34813871</td>
      <td>2149690</td>
      <td>804.921</td>
      <td>16.194833</td>
    </tr>
    <tr>
      <th>41</th>
      <td>우즈베키스탄</td>
      <td>106452</td>
      <td>3571.0</td>
      <td>718</td>
      <td>102163.0</td>
      <td>1</td>
      <td>96.0</td>
      <td>3181</td>
      <td>33469203</td>
      <td>447400</td>
      <td>61.203</td>
      <td>74.808232</td>
    </tr>
    <tr>
      <th>42</th>
      <td>페루</td>
      <td>2030611</td>
      <td>NaN</td>
      <td>190645</td>
      <td>NaN</td>
      <td>9</td>
      <td>NaN</td>
      <td>61586</td>
      <td>32971854</td>
      <td>1285216</td>
      <td>225.918</td>
      <td>25.654718</td>
    </tr>
    <tr>
      <th>43</th>
      <td>앙골라</td>
      <td>37748</td>
      <td>5098.0</td>
      <td>868</td>
      <td>31782.0</td>
      <td>2</td>
      <td>84.0</td>
      <td>1149</td>
      <td>32866272</td>
      <td>1246700</td>
      <td>66.493</td>
      <td>26.362615</td>
    </tr>
    <tr>
      <th>44</th>
      <td>말레이시아</td>
      <td>701019</td>
      <td>62918.0</td>
      <td>4477</td>
      <td>633624.0</td>
      <td>1</td>
      <td>90.0</td>
      <td>21659</td>
      <td>32365999</td>
      <td>329847</td>
      <td>387.093</td>
      <td>98.124279</td>
    </tr>
    <tr>
      <th>45</th>
      <td>모잠비크</td>
      <td>72577</td>
      <td>1488.0</td>
      <td>848</td>
      <td>70241.0</td>
      <td>1</td>
      <td>97.0</td>
      <td>2322</td>
      <td>31255435</td>
      <td>801590</td>
      <td>13.957</td>
      <td>38.991798</td>
    </tr>
    <tr>
      <th>46</th>
      <td>가나</td>
      <td>95059</td>
      <td>1260.0</td>
      <td>794</td>
      <td>93005.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>3059</td>
      <td>31072940</td>
      <td>238533</td>
      <td>74.260</td>
      <td>130.266839</td>
    </tr>
    <tr>
      <th>47</th>
      <td>예멘</td>
      <td>6889</td>
      <td>1576.0</td>
      <td>1355</td>
      <td>3958.0</td>
      <td>20</td>
      <td>58.0</td>
      <td>231</td>
      <td>29825964</td>
      <td>527968</td>
      <td>25.095</td>
      <td>56.491992</td>
    </tr>
    <tr>
      <th>48</th>
      <td>네팔</td>
      <td>622640</td>
      <td>53940.0</td>
      <td>8772</td>
      <td>559928.0</td>
      <td>1</td>
      <td>90.0</td>
      <td>21370</td>
      <td>29136808</td>
      <td>147516</td>
      <td>36.084</td>
      <td>197.516256</td>
    </tr>
    <tr>
      <th>49</th>
      <td>베네수엘라</td>
      <td>262038</td>
      <td>16708.0</td>
      <td>2973</td>
      <td>242357.0</td>
      <td>1</td>
      <td>93.0</td>
      <td>9215</td>
      <td>28435940</td>
      <td>912050</td>
      <td>42.530</td>
      <td>31.178049</td>
    </tr>
    <tr>
      <th>50</th>
      <td>마다가스카르</td>
      <td>42137</td>
      <td>765.0</td>
      <td>903</td>
      <td>40469.0</td>
      <td>2</td>
      <td>96.0</td>
      <td>1522</td>
      <td>27691018</td>
      <td>587041</td>
      <td>14.746</td>
      <td>47.170501</td>
    </tr>
    <tr>
      <th>51</th>
      <td>카메룬</td>
      <td>80328</td>
      <td>853.0</td>
      <td>1313</td>
      <td>78162.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>3026</td>
      <td>26545863</td>
      <td>475440</td>
      <td>44.893</td>
      <td>55.834307</td>
    </tr>
    <tr>
      <th>52</th>
      <td>코트디부아르</td>
      <td>48047</td>
      <td>252.0</td>
      <td>308</td>
      <td>47487.0</td>
      <td>1</td>
      <td>99.0</td>
      <td>1821</td>
      <td>26378274</td>
      <td>322463</td>
      <td>70.991</td>
      <td>81.802483</td>
    </tr>
    <tr>
      <th>53</th>
      <td>호주</td>
      <td>30366</td>
      <td>184.0</td>
      <td>910</td>
      <td>29272.0</td>
      <td>3</td>
      <td>96.0</td>
      <td>1191</td>
      <td>25499884</td>
      <td>7741220</td>
      <td>1617.543</td>
      <td>3.294039</td>
    </tr>
    <tr>
      <th>54</th>
      <td>니제르</td>
      <td>5469</td>
      <td>98.0</td>
      <td>193</td>
      <td>5178.0</td>
      <td>4</td>
      <td>95.0</td>
      <td>226</td>
      <td>24206644</td>
      <td>1267000</td>
      <td>15.899</td>
      <td>19.105481</td>
    </tr>
    <tr>
      <th>55</th>
      <td>대만</td>
      <td>14080</td>
      <td>5977.0</td>
      <td>569</td>
      <td>7534.0</td>
      <td>4</td>
      <td>54.0</td>
      <td>591</td>
      <td>23816775</td>
      <td>36197</td>
      <td>759.104</td>
      <td>657.976490</td>
    </tr>
    <tr>
      <th>56</th>
      <td>스리랑카</td>
      <td>241820</td>
      <td>37798.0</td>
      <td>2633</td>
      <td>201389.0</td>
      <td>1</td>
      <td>83.0</td>
      <td>11293</td>
      <td>21413249</td>
      <td>65610</td>
      <td>84.532</td>
      <td>326.371727</td>
    </tr>
    <tr>
      <th>57</th>
      <td>부르키나파소</td>
      <td>13469</td>
      <td>9.0</td>
      <td>167</td>
      <td>13293.0</td>
      <td>1</td>
      <td>99.0</td>
      <td>644</td>
      <td>20903273</td>
      <td>274200</td>
      <td>18.853</td>
      <td>76.233673</td>
    </tr>
    <tr>
      <th>58</th>
      <td>말리</td>
      <td>14385</td>
      <td>3825.0</td>
      <td>524</td>
      <td>10036.0</td>
      <td>4</td>
      <td>70.0</td>
      <td>710</td>
      <td>20250833</td>
      <td>1240192</td>
      <td>19.912</td>
      <td>16.328789</td>
    </tr>
    <tr>
      <th>59</th>
      <td>루마니아</td>
      <td>1080282</td>
      <td>2684.0</td>
      <td>32391</td>
      <td>1045207.0</td>
      <td>3</td>
      <td>97.0</td>
      <td>56154</td>
      <td>19237691</td>
      <td>238391</td>
      <td>289.130</td>
      <td>80.698059</td>
    </tr>
    <tr>
      <th>60</th>
      <td>말라위</td>
      <td>34914</td>
      <td>852.0</td>
      <td>1171</td>
      <td>32891.0</td>
      <td>3</td>
      <td>94.0</td>
      <td>1825</td>
      <td>19129952</td>
      <td>118484</td>
      <td>9.268</td>
      <td>161.455994</td>
    </tr>
    <tr>
      <th>61</th>
      <td>칠레</td>
      <td>1522223</td>
      <td>38470.0</td>
      <td>31645</td>
      <td>1452108.0</td>
      <td>2</td>
      <td>95.0</td>
      <td>79630</td>
      <td>19116201</td>
      <td>756096</td>
      <td>307.938</td>
      <td>25.282770</td>
    </tr>
    <tr>
      <th>62</th>
      <td>카자흐스탄</td>
      <td>410523</td>
      <td>20147.0</td>
      <td>4249</td>
      <td>386127.0</td>
      <td>1</td>
      <td>94.0</td>
      <td>21863</td>
      <td>18776707</td>
      <td>2724900</td>
      <td>187.836</td>
      <td>6.890788</td>
    </tr>
    <tr>
      <th>63</th>
      <td>잠비아</td>
      <td>130631</td>
      <td>18490.0</td>
      <td>1691</td>
      <td>110450.0</td>
      <td>1</td>
      <td>85.0</td>
      <td>7106</td>
      <td>18383955</td>
      <td>752618</td>
      <td>18.955</td>
      <td>24.426675</td>
    </tr>
    <tr>
      <th>64</th>
      <td>과테말라</td>
      <td>280854</td>
      <td>17419.0</td>
      <td>8735</td>
      <td>254700.0</td>
      <td>3</td>
      <td>91.0</td>
      <td>15677</td>
      <td>17915568</td>
      <td>108889</td>
      <td>81.402</td>
      <td>164.530559</td>
    </tr>
    <tr>
      <th>65</th>
      <td>에콰도르</td>
      <td>446633</td>
      <td>9821.0</td>
      <td>21304</td>
      <td>415508.0</td>
      <td>5</td>
      <td>93.0</td>
      <td>25315</td>
      <td>17643054</td>
      <td>283561</td>
      <td>100.595</td>
      <td>62.219607</td>
    </tr>
    <tr>
      <th>66</th>
      <td>시리아</td>
      <td>25158</td>
      <td>1563.0</td>
      <td>1848</td>
      <td>21747.0</td>
      <td>7</td>
      <td>86.0</td>
      <td>1438</td>
      <td>17500658</td>
      <td>185180</td>
      <td>0.000</td>
      <td>94.506199</td>
    </tr>
    <tr>
      <th>67</th>
      <td>네덜란드</td>
      <td>1679542</td>
      <td>NaN</td>
      <td>17727</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>98019</td>
      <td>17134872</td>
      <td>41543</td>
      <td>1012.598</td>
      <td>412.461113</td>
    </tr>
    <tr>
      <th>68</th>
      <td>세네갈</td>
      <td>42437</td>
      <td>365.0</td>
      <td>1158</td>
      <td>40914.0</td>
      <td>3</td>
      <td>96.0</td>
      <td>2534</td>
      <td>16743927</td>
      <td>196722</td>
      <td>27.927</td>
      <td>85.114664</td>
    </tr>
    <tr>
      <th>69</th>
      <td>캄보디아</td>
      <td>43446</td>
      <td>5002.0</td>
      <td>441</td>
      <td>38003.0</td>
      <td>1</td>
      <td>88.0</td>
      <td>2599</td>
      <td>16718965</td>
      <td>181035</td>
      <td>27.239</td>
      <td>92.352114</td>
    </tr>
    <tr>
      <th>70</th>
      <td>차드</td>
      <td>4947</td>
      <td>5.0</td>
      <td>174</td>
      <td>4768.0</td>
      <td>4</td>
      <td>96.0</td>
      <td>301</td>
      <td>16425864</td>
      <td>1284000</td>
      <td>12.531</td>
      <td>12.792729</td>
    </tr>
    <tr>
      <th>71</th>
      <td>소말리아</td>
      <td>14867</td>
      <td>6888.0</td>
      <td>775</td>
      <td>7204.0</td>
      <td>5</td>
      <td>49.0</td>
      <td>935</td>
      <td>15893222</td>
      <td>637657</td>
      <td>5.367</td>
      <td>24.924406</td>
    </tr>
    <tr>
      <th>72</th>
      <td>짐바브웨</td>
      <td>42195</td>
      <td>3310.0</td>
      <td>1685</td>
      <td>37200.0</td>
      <td>4</td>
      <td>88.0</td>
      <td>2839</td>
      <td>14862924</td>
      <td>390757</td>
      <td>26.085</td>
      <td>38.036232</td>
    </tr>
    <tr>
      <th>73</th>
      <td>기니</td>
      <td>23535</td>
      <td>1085.0</td>
      <td>168</td>
      <td>22282.0</td>
      <td>1</td>
      <td>95.0</td>
      <td>1792</td>
      <td>13132795</td>
      <td>245857</td>
      <td>16.339</td>
      <td>53.416397</td>
    </tr>
    <tr>
      <th>74</th>
      <td>르완다</td>
      <td>31435</td>
      <td>4343.0</td>
      <td>388</td>
      <td>26704.0</td>
      <td>1</td>
      <td>85.0</td>
      <td>2427</td>
      <td>12952218</td>
      <td>26338</td>
      <td>10.633</td>
      <td>491.769231</td>
    </tr>
    <tr>
      <th>75</th>
      <td>베냉</td>
      <td>8140</td>
      <td>58.0</td>
      <td>103</td>
      <td>7979.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>671</td>
      <td>12123200</td>
      <td>112622</td>
      <td>17.327</td>
      <td>107.645043</td>
    </tr>
    <tr>
      <th>76</th>
      <td>부룬디</td>
      <td>5242</td>
      <td>4461.0</td>
      <td>8</td>
      <td>773.0</td>
      <td>0</td>
      <td>15.0</td>
      <td>441</td>
      <td>11890784</td>
      <td>27834</td>
      <td>3.244</td>
      <td>427.203564</td>
    </tr>
    <tr>
      <th>77</th>
      <td>튀니지</td>
      <td>385428</td>
      <td>34658.0</td>
      <td>14118</td>
      <td>336652.0</td>
      <td>4</td>
      <td>87.0</td>
      <td>32612</td>
      <td>11818619</td>
      <td>163610</td>
      <td>44.265</td>
      <td>72.236532</td>
    </tr>
    <tr>
      <th>78</th>
      <td>볼리비아</td>
      <td>422811</td>
      <td>65678.0</td>
      <td>16174</td>
      <td>340959.0</td>
      <td>4</td>
      <td>81.0</td>
      <td>36221</td>
      <td>11673021</td>
      <td>1098581</td>
      <td>43.110</td>
      <td>10.625544</td>
    </tr>
    <tr>
      <th>79</th>
      <td>벨기에</td>
      <td>1079640</td>
      <td>37925.0</td>
      <td>25141</td>
      <td>1016574.0</td>
      <td>2</td>
      <td>94.0</td>
      <td>93156</td>
      <td>11589623</td>
      <td>30528</td>
      <td>578.996</td>
      <td>379.639118</td>
    </tr>
    <tr>
      <th>80</th>
      <td>아이티</td>
      <td>17371</td>
      <td>4319.0</td>
      <td>385</td>
      <td>12667.0</td>
      <td>2</td>
      <td>73.0</td>
      <td>1523</td>
      <td>11402528</td>
      <td>27750</td>
      <td>22.431</td>
      <td>410.901910</td>
    </tr>
    <tr>
      <th>81</th>
      <td>남수단</td>
      <td>10786</td>
      <td>157.0</td>
      <td>115</td>
      <td>10514.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>964</td>
      <td>11193725</td>
      <td>644329</td>
      <td>4.461</td>
      <td>17.372685</td>
    </tr>
    <tr>
      <th>82</th>
      <td>도미니카 공화국</td>
      <td>317645</td>
      <td>54238.0</td>
      <td>3758</td>
      <td>259649.0</td>
      <td>1</td>
      <td>82.0</td>
      <td>29282</td>
      <td>10847910</td>
      <td>48670</td>
      <td>83.917</td>
      <td>222.886994</td>
    </tr>
    <tr>
      <th>83</th>
      <td>체코</td>
      <td>1666082</td>
      <td>2640.0</td>
      <td>30280</td>
      <td>1633162.0</td>
      <td>2</td>
      <td>98.0</td>
      <td>155578</td>
      <td>10708981</td>
      <td>78867</td>
      <td>276.109</td>
      <td>135.785322</td>
    </tr>
    <tr>
      <th>84</th>
      <td>그리스</td>
      <td>418548</td>
      <td>6111.0</td>
      <td>12559</td>
      <td>399878.0</td>
      <td>3</td>
      <td>96.0</td>
      <td>40156</td>
      <td>10423054</td>
      <td>131957</td>
      <td>209.857</td>
      <td>78.988261</td>
    </tr>
    <tr>
      <th>85</th>
      <td>요르단</td>
      <td>747000</td>
      <td>6498.0</td>
      <td>9671</td>
      <td>730831.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>73213</td>
      <td>10203134</td>
      <td>89342</td>
      <td>44.979</td>
      <td>114.203107</td>
    </tr>
    <tr>
      <th>86</th>
      <td>포르투갈</td>
      <td>865806</td>
      <td>28657.0</td>
      <td>17068</td>
      <td>820081.0</td>
      <td>2</td>
      <td>95.0</td>
      <td>84910</td>
      <td>10196709</td>
      <td>92090</td>
      <td>257.391</td>
      <td>110.725475</td>
    </tr>
    <tr>
      <th>87</th>
      <td>아제르바이잔</td>
      <td>335521</td>
      <td>959.0</td>
      <td>4963</td>
      <td>329599.0</td>
      <td>2</td>
      <td>98.0</td>
      <td>33092</td>
      <td>10139177</td>
      <td>86600</td>
      <td>49.914</td>
      <td>117.080566</td>
    </tr>
    <tr>
      <th>88</th>
      <td>스웨덴</td>
      <td>1084636</td>
      <td>NaN</td>
      <td>14537</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>107398</td>
      <td>10099265</td>
      <td>450295</td>
      <td>625.948</td>
      <td>22.428108</td>
    </tr>
    <tr>
      <th>89</th>
      <td>온두라스</td>
      <td>254194</td>
      <td>155560.0</td>
      <td>6772</td>
      <td>91862.0</td>
      <td>3</td>
      <td>36.0</td>
      <td>25664</td>
      <td>9904607</td>
      <td>112492</td>
      <td>26.161</td>
      <td>88.047212</td>
    </tr>
  </tbody>
</table>
</div>



### GDP 정보가 없는 하위 2개국 삭제하기 !


```python
df5 = df1.sort_values(by='GDP', ascending=False)
# df5 = df5.drop([4])
# df5 = df5.drop([66])

df5
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>국가</th>
      <th>확진자</th>
      <th>치료중</th>
      <th>사망자</th>
      <th>완치</th>
      <th>치명(%)</th>
      <th>완치(%)</th>
      <th>발생률</th>
      <th>인구수</th>
      <th>국토면적</th>
      <th>GDP</th>
      <th>인구밀도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>미국</td>
      <td>34419838</td>
      <td>5034868.0</td>
      <td>617463</td>
      <td>28767507.0</td>
      <td>2</td>
      <td>84.0</td>
      <td>103987</td>
      <td>331002651</td>
      <td>9833517</td>
      <td>22675.271</td>
      <td>33.660658</td>
    </tr>
    <tr>
      <th>10</th>
      <td>일본</td>
      <td>785969</td>
      <td>22248.0</td>
      <td>14439</td>
      <td>749282.0</td>
      <td>2</td>
      <td>95.0</td>
      <td>6214</td>
      <td>126476461</td>
      <td>377975</td>
      <td>5378.136</td>
      <td>334.615943</td>
    </tr>
    <tr>
      <th>18</th>
      <td>독일</td>
      <td>3730599</td>
      <td>31492.0</td>
      <td>91007</td>
      <td>3608100.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>44526</td>
      <td>83783942</td>
      <td>357022</td>
      <td>4319.286</td>
      <td>234.674451</td>
    </tr>
    <tr>
      <th>20</th>
      <td>영국</td>
      <td>4640507</td>
      <td>208530.0</td>
      <td>127981</td>
      <td>4303996.0</td>
      <td>3</td>
      <td>93.0</td>
      <td>68357</td>
      <td>67886011</td>
      <td>243610</td>
      <td>3124.650</td>
      <td>278.666767</td>
    </tr>
    <tr>
      <th>1</th>
      <td>인도</td>
      <td>29977861</td>
      <td>662521.0</td>
      <td>389302</td>
      <td>28926038.0</td>
      <td>1</td>
      <td>97.0</td>
      <td>21723</td>
      <td>1380004385</td>
      <td>3287263</td>
      <td>3049.704</td>
      <td>419.803461</td>
    </tr>
    <tr>
      <th>21</th>
      <td>프랑스</td>
      <td>5757798</td>
      <td>80626.0</td>
      <td>110778</td>
      <td>5566394.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>88210</td>
      <td>65273511</td>
      <td>640679</td>
      <td>2938.271</td>
      <td>101.881771</td>
    </tr>
    <tr>
      <th>22</th>
      <td>이탈리아</td>
      <td>4253460</td>
      <td>76853.0</td>
      <td>127291</td>
      <td>4049316.0</td>
      <td>3</td>
      <td>95.0</td>
      <td>70350</td>
      <td>60461826</td>
      <td>301340</td>
      <td>2106.287</td>
      <td>200.643214</td>
    </tr>
    <tr>
      <th>38</th>
      <td>캐나다</td>
      <td>1409607</td>
      <td>11032.0</td>
      <td>26084</td>
      <td>1372491.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>37348</td>
      <td>37742154</td>
      <td>9984670</td>
      <td>1883.487</td>
      <td>3.780010</td>
    </tr>
    <tr>
      <th>27</th>
      <td>대한민국</td>
      <td>151901</td>
      <td>6078.0</td>
      <td>2006</td>
      <td>143817.0</td>
      <td>1</td>
      <td>95.0</td>
      <td>2963</td>
      <td>51269185</td>
      <td>100412</td>
      <td>1806.707</td>
      <td>510.588227</td>
    </tr>
    <tr>
      <th>8</th>
      <td>러시아</td>
      <td>5334204</td>
      <td>326070.0</td>
      <td>129801</td>
      <td>4878333.0</td>
      <td>2</td>
      <td>92.0</td>
      <td>36552</td>
      <td>145934462</td>
      <td>17125407</td>
      <td>1710.734</td>
      <td>8.521518</td>
    </tr>
    <tr>
      <th>53</th>
      <td>호주</td>
      <td>30366</td>
      <td>184.0</td>
      <td>910</td>
      <td>29272.0</td>
      <td>3</td>
      <td>96.0</td>
      <td>1191</td>
      <td>25499884</td>
      <td>7741220</td>
      <td>1617.543</td>
      <td>3.294039</td>
    </tr>
    <tr>
      <th>5</th>
      <td>브라질</td>
      <td>17969806</td>
      <td>1178597.0</td>
      <td>502817</td>
      <td>16288392.0</td>
      <td>3</td>
      <td>91.0</td>
      <td>84540</td>
      <td>212559417</td>
      <td>8515770</td>
      <td>1491.772</td>
      <td>24.960681</td>
    </tr>
    <tr>
      <th>29</th>
      <td>스페인</td>
      <td>3764651</td>
      <td>123928.0</td>
      <td>80689</td>
      <td>3560034.0</td>
      <td>2</td>
      <td>95.0</td>
      <td>80519</td>
      <td>46754778</td>
      <td>505990</td>
      <td>1461.552</td>
      <td>92.402573</td>
    </tr>
    <tr>
      <th>9</th>
      <td>멕시코</td>
      <td>2478551</td>
      <td>273052.0</td>
      <td>231244</td>
      <td>1974255.0</td>
      <td>9</td>
      <td>80.0</td>
      <td>19224</td>
      <td>128932753</td>
      <td>1964375</td>
      <td>1192.480</td>
      <td>65.635509</td>
    </tr>
    <tr>
      <th>3</th>
      <td>인도네시아</td>
      <td>2004445</td>
      <td>147728.0</td>
      <td>54956</td>
      <td>1801761.0</td>
      <td>3</td>
      <td>90.0</td>
      <td>7328</td>
      <td>273523615</td>
      <td>1904569</td>
      <td>1158.783</td>
      <td>143.614442</td>
    </tr>
    <tr>
      <th>67</th>
      <td>네덜란드</td>
      <td>1679542</td>
      <td>NaN</td>
      <td>17727</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>98019</td>
      <td>17134872</td>
      <td>41543</td>
      <td>1012.598</td>
      <td>412.461113</td>
    </tr>
    <tr>
      <th>40</th>
      <td>사우디아라비아</td>
      <td>475403</td>
      <td>10584.0</td>
      <td>7691</td>
      <td>457128.0</td>
      <td>2</td>
      <td>96.0</td>
      <td>13656</td>
      <td>34813871</td>
      <td>2149690</td>
      <td>804.921</td>
      <td>16.194833</td>
    </tr>
    <tr>
      <th>16</th>
      <td>터키</td>
      <td>5375593</td>
      <td>88626.0</td>
      <td>49236</td>
      <td>5237731.0</td>
      <td>1</td>
      <td>97.0</td>
      <td>63738</td>
      <td>84339067</td>
      <td>783356</td>
      <td>794.530</td>
      <td>107.663779</td>
    </tr>
    <tr>
      <th>55</th>
      <td>대만</td>
      <td>14080</td>
      <td>5977.0</td>
      <td>569</td>
      <td>7534.0</td>
      <td>4</td>
      <td>54.0</td>
      <td>591</td>
      <td>23816775</td>
      <td>36197</td>
      <td>759.104</td>
      <td>657.976490</td>
    </tr>
    <tr>
      <th>17</th>
      <td>이란</td>
      <td>3105620</td>
      <td>262290.0</td>
      <td>83101</td>
      <td>2760229.0</td>
      <td>3</td>
      <td>89.0</td>
      <td>36975</td>
      <td>83992949</td>
      <td>1648195</td>
      <td>682.859</td>
      <td>50.960565</td>
    </tr>
    <tr>
      <th>37</th>
      <td>폴란드</td>
      <td>2878840</td>
      <td>153363.0</td>
      <td>74829</td>
      <td>2650648.0</td>
      <td>3</td>
      <td>92.0</td>
      <td>76066</td>
      <td>37846611</td>
      <td>312685</td>
      <td>642.121</td>
      <td>121.037501</td>
    </tr>
    <tr>
      <th>88</th>
      <td>스웨덴</td>
      <td>1084636</td>
      <td>NaN</td>
      <td>14537</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>107398</td>
      <td>10099265</td>
      <td>450295</td>
      <td>625.948</td>
      <td>22.428108</td>
    </tr>
    <tr>
      <th>79</th>
      <td>벨기에</td>
      <td>1079640</td>
      <td>37925.0</td>
      <td>25141</td>
      <td>1016574.0</td>
      <td>2</td>
      <td>94.0</td>
      <td>93156</td>
      <td>11589623</td>
      <td>30528</td>
      <td>578.996</td>
      <td>379.639118</td>
    </tr>
    <tr>
      <th>19</th>
      <td>태국</td>
      <td>225365</td>
      <td>35836.0</td>
      <td>1693</td>
      <td>187836.0</td>
      <td>1</td>
      <td>83.0</td>
      <td>3229</td>
      <td>69799978</td>
      <td>513120</td>
      <td>538.735</td>
      <td>136.030515</td>
    </tr>
    <tr>
      <th>6</th>
      <td>나이지리아</td>
      <td>167292</td>
      <td>1377.0</td>
      <td>2118</td>
      <td>163797.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>812</td>
      <td>206139589</td>
      <td>923768</td>
      <td>514.049</td>
      <td>223.150823</td>
    </tr>
    <tr>
      <th>31</th>
      <td>아르헨티나</td>
      <td>4277395</td>
      <td>277070.0</td>
      <td>89490</td>
      <td>3910835.0</td>
      <td>2</td>
      <td>91.0</td>
      <td>94641</td>
      <td>45195774</td>
      <td>2780400</td>
      <td>418.150</td>
      <td>16.255134</td>
    </tr>
    <tr>
      <th>12</th>
      <td>필리핀</td>
      <td>1364239</td>
      <td>55847.0</td>
      <td>23749</td>
      <td>1284643.0</td>
      <td>2</td>
      <td>94.0</td>
      <td>12450</td>
      <td>109581078</td>
      <td>300000</td>
      <td>402.638</td>
      <td>365.270260</td>
    </tr>
    <tr>
      <th>13</th>
      <td>이집트</td>
      <td>277797</td>
      <td>55846.0</td>
      <td>15898</td>
      <td>206053.0</td>
      <td>6</td>
      <td>74.0</td>
      <td>2715</td>
      <td>102334404</td>
      <td>1010408</td>
      <td>394.284</td>
      <td>101.280279</td>
    </tr>
    <tr>
      <th>44</th>
      <td>말레이시아</td>
      <td>701019</td>
      <td>62918.0</td>
      <td>4477</td>
      <td>633624.0</td>
      <td>1</td>
      <td>90.0</td>
      <td>21659</td>
      <td>32365999</td>
      <td>329847</td>
      <td>387.093</td>
      <td>98.124279</td>
    </tr>
    <tr>
      <th>14</th>
      <td>베트남</td>
      <td>13530</td>
      <td>8008.0</td>
      <td>69</td>
      <td>5453.0</td>
      <td>1</td>
      <td>40.0</td>
      <td>139</td>
      <td>97338579</td>
      <td>331210</td>
      <td>354.868</td>
      <td>293.887802</td>
    </tr>
    <tr>
      <th>7</th>
      <td>방글라데시</td>
      <td>856304</td>
      <td>57196.0</td>
      <td>13626</td>
      <td>785482.0</td>
      <td>2</td>
      <td>92.0</td>
      <td>5200</td>
      <td>164689383</td>
      <td>143998</td>
      <td>352.908</td>
      <td>1143.692155</td>
    </tr>
    <tr>
      <th>24</th>
      <td>남아프리카 공화국</td>
      <td>1832479</td>
      <td>117004.0</td>
      <td>58795</td>
      <td>1656680.0</td>
      <td>3</td>
      <td>90.0</td>
      <td>30897</td>
      <td>59308690</td>
      <td>1219090</td>
      <td>329.529</td>
      <td>48.649968</td>
    </tr>
    <tr>
      <th>61</th>
      <td>칠레</td>
      <td>1522223</td>
      <td>38470.0</td>
      <td>31645</td>
      <td>1452108.0</td>
      <td>2</td>
      <td>95.0</td>
      <td>79630</td>
      <td>19116201</td>
      <td>756096</td>
      <td>307.938</td>
      <td>25.282770</td>
    </tr>
    <tr>
      <th>28</th>
      <td>콜롬비아</td>
      <td>3968405</td>
      <td>181876.0</td>
      <td>100582</td>
      <td>3685947.0</td>
      <td>3</td>
      <td>93.0</td>
      <td>77991</td>
      <td>50882891</td>
      <td>1138914</td>
      <td>295.610</td>
      <td>44.676675</td>
    </tr>
    <tr>
      <th>59</th>
      <td>루마니아</td>
      <td>1080282</td>
      <td>2684.0</td>
      <td>32391</td>
      <td>1045207.0</td>
      <td>3</td>
      <td>97.0</td>
      <td>56154</td>
      <td>19237691</td>
      <td>238391</td>
      <td>289.130</td>
      <td>80.698059</td>
    </tr>
    <tr>
      <th>83</th>
      <td>체코</td>
      <td>1666082</td>
      <td>2640.0</td>
      <td>30280</td>
      <td>1633162.0</td>
      <td>2</td>
      <td>98.0</td>
      <td>155578</td>
      <td>10708981</td>
      <td>78867</td>
      <td>276.109</td>
      <td>135.785322</td>
    </tr>
    <tr>
      <th>86</th>
      <td>포르투갈</td>
      <td>865806</td>
      <td>28657.0</td>
      <td>17068</td>
      <td>820081.0</td>
      <td>2</td>
      <td>95.0</td>
      <td>84910</td>
      <td>10196709</td>
      <td>92090</td>
      <td>257.391</td>
      <td>110.725475</td>
    </tr>
    <tr>
      <th>42</th>
      <td>페루</td>
      <td>2030611</td>
      <td>NaN</td>
      <td>190645</td>
      <td>NaN</td>
      <td>9</td>
      <td>NaN</td>
      <td>61586</td>
      <td>32971854</td>
      <td>1285216</td>
      <td>225.918</td>
      <td>25.654718</td>
    </tr>
    <tr>
      <th>84</th>
      <td>그리스</td>
      <td>418548</td>
      <td>6111.0</td>
      <td>12559</td>
      <td>399878.0</td>
      <td>3</td>
      <td>96.0</td>
      <td>40156</td>
      <td>10423054</td>
      <td>131957</td>
      <td>209.857</td>
      <td>78.988261</td>
    </tr>
    <tr>
      <th>35</th>
      <td>이라크</td>
      <td>1292700</td>
      <td>70911.0</td>
      <td>16910</td>
      <td>1204879.0</td>
      <td>1</td>
      <td>93.0</td>
      <td>32139</td>
      <td>40222493</td>
      <td>438317</td>
      <td>190.733</td>
      <td>91.765761</td>
    </tr>
    <tr>
      <th>62</th>
      <td>카자흐스탄</td>
      <td>410523</td>
      <td>20147.0</td>
      <td>4249</td>
      <td>386127.0</td>
      <td>1</td>
      <td>94.0</td>
      <td>21863</td>
      <td>18776707</td>
      <td>2724900</td>
      <td>187.836</td>
      <td>6.890788</td>
    </tr>
    <tr>
      <th>34</th>
      <td>우크라이나</td>
      <td>2229846</td>
      <td>25674.0</td>
      <td>52032</td>
      <td>2152140.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>50987</td>
      <td>43733762</td>
      <td>603628</td>
      <td>164.593</td>
      <td>72.451513</td>
    </tr>
    <tr>
      <th>32</th>
      <td>알제리</td>
      <td>136294</td>
      <td>37831.0</td>
      <td>3641</td>
      <td>94822.0</td>
      <td>3</td>
      <td>70.0</td>
      <td>3108</td>
      <td>43851044</td>
      <td>2381741</td>
      <td>151.459</td>
      <td>18.411340</td>
    </tr>
    <tr>
      <th>39</th>
      <td>모로코</td>
      <td>526737</td>
      <td>3595.0</td>
      <td>9244</td>
      <td>513898.0</td>
      <td>2</td>
      <td>98.0</td>
      <td>14271</td>
      <td>36910560</td>
      <td>446550</td>
      <td>124.003</td>
      <td>82.657172</td>
    </tr>
    <tr>
      <th>26</th>
      <td>케냐</td>
      <td>179293</td>
      <td>52867.0</td>
      <td>3461</td>
      <td>122965.0</td>
      <td>2</td>
      <td>69.0</td>
      <td>3334</td>
      <td>53771296</td>
      <td>580367</td>
      <td>106.041</td>
      <td>92.650506</td>
    </tr>
    <tr>
      <th>65</th>
      <td>에콰도르</td>
      <td>446633</td>
      <td>9821.0</td>
      <td>21304</td>
      <td>415508.0</td>
      <td>5</td>
      <td>93.0</td>
      <td>25315</td>
      <td>17643054</td>
      <td>283561</td>
      <td>100.595</td>
      <td>62.219607</td>
    </tr>
    <tr>
      <th>11</th>
      <td>에티오피아</td>
      <td>275318</td>
      <td>15530.0</td>
      <td>4286</td>
      <td>255502.0</td>
      <td>2</td>
      <td>93.0</td>
      <td>2395</td>
      <td>114963588</td>
      <td>1104300</td>
      <td>93.966</td>
      <td>104.105395</td>
    </tr>
    <tr>
      <th>56</th>
      <td>스리랑카</td>
      <td>241820</td>
      <td>37798.0</td>
      <td>2633</td>
      <td>201389.0</td>
      <td>1</td>
      <td>83.0</td>
      <td>11293</td>
      <td>21413249</td>
      <td>65610</td>
      <td>84.532</td>
      <td>326.371727</td>
    </tr>
    <tr>
      <th>82</th>
      <td>도미니카 공화국</td>
      <td>317645</td>
      <td>54238.0</td>
      <td>3758</td>
      <td>259649.0</td>
      <td>1</td>
      <td>82.0</td>
      <td>29282</td>
      <td>10847910</td>
      <td>48670</td>
      <td>83.917</td>
      <td>222.886994</td>
    </tr>
    <tr>
      <th>64</th>
      <td>과테말라</td>
      <td>280854</td>
      <td>17419.0</td>
      <td>8735</td>
      <td>254700.0</td>
      <td>3</td>
      <td>91.0</td>
      <td>15677</td>
      <td>17915568</td>
      <td>108889</td>
      <td>81.402</td>
      <td>164.530559</td>
    </tr>
    <tr>
      <th>25</th>
      <td>미얀마</td>
      <td>148617</td>
      <td>11599.0</td>
      <td>3265</td>
      <td>133753.0</td>
      <td>2</td>
      <td>90.0</td>
      <td>2731</td>
      <td>54409800</td>
      <td>676578</td>
      <td>76.195</td>
      <td>80.419109</td>
    </tr>
    <tr>
      <th>46</th>
      <td>가나</td>
      <td>95059</td>
      <td>1260.0</td>
      <td>794</td>
      <td>93005.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>3059</td>
      <td>31072940</td>
      <td>238533</td>
      <td>74.260</td>
      <td>130.266839</td>
    </tr>
    <tr>
      <th>52</th>
      <td>코트디부아르</td>
      <td>48047</td>
      <td>252.0</td>
      <td>308</td>
      <td>47487.0</td>
      <td>1</td>
      <td>99.0</td>
      <td>1821</td>
      <td>26378274</td>
      <td>322463</td>
      <td>70.991</td>
      <td>81.802483</td>
    </tr>
    <tr>
      <th>43</th>
      <td>앙골라</td>
      <td>37748</td>
      <td>5098.0</td>
      <td>868</td>
      <td>31782.0</td>
      <td>2</td>
      <td>84.0</td>
      <td>1149</td>
      <td>32866272</td>
      <td>1246700</td>
      <td>66.493</td>
      <td>26.362615</td>
    </tr>
    <tr>
      <th>23</th>
      <td>탄자니아</td>
      <td>509</td>
      <td>305.0</td>
      <td>21</td>
      <td>183.0</td>
      <td>4</td>
      <td>36.0</td>
      <td>9</td>
      <td>59734218</td>
      <td>947303</td>
      <td>65.919</td>
      <td>63.057140</td>
    </tr>
    <tr>
      <th>41</th>
      <td>우즈베키스탄</td>
      <td>106452</td>
      <td>3571.0</td>
      <td>718</td>
      <td>102163.0</td>
      <td>1</td>
      <td>96.0</td>
      <td>3181</td>
      <td>33469203</td>
      <td>447400</td>
      <td>61.203</td>
      <td>74.808232</td>
    </tr>
    <tr>
      <th>87</th>
      <td>아제르바이잔</td>
      <td>335521</td>
      <td>959.0</td>
      <td>4963</td>
      <td>329599.0</td>
      <td>2</td>
      <td>98.0</td>
      <td>33092</td>
      <td>10139177</td>
      <td>86600</td>
      <td>49.914</td>
      <td>117.080566</td>
    </tr>
    <tr>
      <th>85</th>
      <td>요르단</td>
      <td>747000</td>
      <td>6498.0</td>
      <td>9671</td>
      <td>730831.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>73213</td>
      <td>10203134</td>
      <td>89342</td>
      <td>44.979</td>
      <td>114.203107</td>
    </tr>
    <tr>
      <th>51</th>
      <td>카메룬</td>
      <td>80328</td>
      <td>853.0</td>
      <td>1313</td>
      <td>78162.0</td>
      <td>2</td>
      <td>97.0</td>
      <td>3026</td>
      <td>26545863</td>
      <td>475440</td>
      <td>44.893</td>
      <td>55.834307</td>
    </tr>
    <tr>
      <th>77</th>
      <td>튀니지</td>
      <td>385428</td>
      <td>34658.0</td>
      <td>14118</td>
      <td>336652.0</td>
      <td>4</td>
      <td>87.0</td>
      <td>32612</td>
      <td>11818619</td>
      <td>163610</td>
      <td>44.265</td>
      <td>72.236532</td>
    </tr>
    <tr>
      <th>78</th>
      <td>볼리비아</td>
      <td>422811</td>
      <td>65678.0</td>
      <td>16174</td>
      <td>340959.0</td>
      <td>4</td>
      <td>81.0</td>
      <td>36221</td>
      <td>11673021</td>
      <td>1098581</td>
      <td>43.110</td>
      <td>10.625544</td>
    </tr>
    <tr>
      <th>49</th>
      <td>베네수엘라</td>
      <td>262038</td>
      <td>16708.0</td>
      <td>2973</td>
      <td>242357.0</td>
      <td>1</td>
      <td>93.0</td>
      <td>9215</td>
      <td>28435940</td>
      <td>912050</td>
      <td>42.530</td>
      <td>31.178049</td>
    </tr>
    <tr>
      <th>30</th>
      <td>우간다</td>
      <td>72679</td>
      <td>22205.0</td>
      <td>680</td>
      <td>49794.0</td>
      <td>1</td>
      <td>69.0</td>
      <td>1589</td>
      <td>45741007</td>
      <td>241038</td>
      <td>41.271</td>
      <td>189.766788</td>
    </tr>
    <tr>
      <th>48</th>
      <td>네팔</td>
      <td>622640</td>
      <td>53940.0</td>
      <td>8772</td>
      <td>559928.0</td>
      <td>1</td>
      <td>90.0</td>
      <td>21370</td>
      <td>29136808</td>
      <td>147516</td>
      <td>36.084</td>
      <td>197.516256</td>
    </tr>
    <tr>
      <th>33</th>
      <td>수단</td>
      <td>36347</td>
      <td>3548.0</td>
      <td>2737</td>
      <td>30062.0</td>
      <td>8</td>
      <td>83.0</td>
      <td>829</td>
      <td>43849260</td>
      <td>1861484</td>
      <td>35.827</td>
      <td>23.556077</td>
    </tr>
    <tr>
      <th>68</th>
      <td>세네갈</td>
      <td>42437</td>
      <td>365.0</td>
      <td>1158</td>
      <td>40914.0</td>
      <td>3</td>
      <td>96.0</td>
      <td>2534</td>
      <td>16743927</td>
      <td>196722</td>
      <td>27.927</td>
      <td>85.114664</td>
    </tr>
    <tr>
      <th>69</th>
      <td>캄보디아</td>
      <td>43446</td>
      <td>5002.0</td>
      <td>441</td>
      <td>38003.0</td>
      <td>1</td>
      <td>88.0</td>
      <td>2599</td>
      <td>16718965</td>
      <td>181035</td>
      <td>27.239</td>
      <td>92.352114</td>
    </tr>
    <tr>
      <th>89</th>
      <td>온두라스</td>
      <td>254194</td>
      <td>155560.0</td>
      <td>6772</td>
      <td>91862.0</td>
      <td>3</td>
      <td>36.0</td>
      <td>25664</td>
      <td>9904607</td>
      <td>112492</td>
      <td>26.161</td>
      <td>88.047212</td>
    </tr>
    <tr>
      <th>72</th>
      <td>짐바브웨</td>
      <td>42195</td>
      <td>3310.0</td>
      <td>1685</td>
      <td>37200.0</td>
      <td>4</td>
      <td>88.0</td>
      <td>2839</td>
      <td>14862924</td>
      <td>390757</td>
      <td>26.085</td>
      <td>38.036232</td>
    </tr>
    <tr>
      <th>47</th>
      <td>예멘</td>
      <td>6889</td>
      <td>1576.0</td>
      <td>1355</td>
      <td>3958.0</td>
      <td>20</td>
      <td>58.0</td>
      <td>231</td>
      <td>29825964</td>
      <td>527968</td>
      <td>25.095</td>
      <td>56.491992</td>
    </tr>
    <tr>
      <th>80</th>
      <td>아이티</td>
      <td>17371</td>
      <td>4319.0</td>
      <td>385</td>
      <td>12667.0</td>
      <td>2</td>
      <td>73.0</td>
      <td>1523</td>
      <td>11402528</td>
      <td>27750</td>
      <td>22.431</td>
      <td>410.901910</td>
    </tr>
    <tr>
      <th>36</th>
      <td>아프가니스탄</td>
      <td>105755</td>
      <td>36391.0</td>
      <td>4293</td>
      <td>65071.0</td>
      <td>4</td>
      <td>62.0</td>
      <td>2717</td>
      <td>38928346</td>
      <td>652230</td>
      <td>19.938</td>
      <td>59.684998</td>
    </tr>
    <tr>
      <th>58</th>
      <td>말리</td>
      <td>14385</td>
      <td>3825.0</td>
      <td>524</td>
      <td>10036.0</td>
      <td>4</td>
      <td>70.0</td>
      <td>710</td>
      <td>20250833</td>
      <td>1240192</td>
      <td>19.912</td>
      <td>16.328789</td>
    </tr>
    <tr>
      <th>63</th>
      <td>잠비아</td>
      <td>130631</td>
      <td>18490.0</td>
      <td>1691</td>
      <td>110450.0</td>
      <td>1</td>
      <td>85.0</td>
      <td>7106</td>
      <td>18383955</td>
      <td>752618</td>
      <td>18.955</td>
      <td>24.426675</td>
    </tr>
    <tr>
      <th>57</th>
      <td>부르키나파소</td>
      <td>13469</td>
      <td>9.0</td>
      <td>167</td>
      <td>13293.0</td>
      <td>1</td>
      <td>99.0</td>
      <td>644</td>
      <td>20903273</td>
      <td>274200</td>
      <td>18.853</td>
      <td>76.233673</td>
    </tr>
    <tr>
      <th>75</th>
      <td>베냉</td>
      <td>8140</td>
      <td>58.0</td>
      <td>103</td>
      <td>7979.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>671</td>
      <td>12123200</td>
      <td>112622</td>
      <td>17.327</td>
      <td>107.645043</td>
    </tr>
    <tr>
      <th>73</th>
      <td>기니</td>
      <td>23535</td>
      <td>1085.0</td>
      <td>168</td>
      <td>22282.0</td>
      <td>1</td>
      <td>95.0</td>
      <td>1792</td>
      <td>13132795</td>
      <td>245857</td>
      <td>16.339</td>
      <td>53.416397</td>
    </tr>
    <tr>
      <th>54</th>
      <td>니제르</td>
      <td>5469</td>
      <td>98.0</td>
      <td>193</td>
      <td>5178.0</td>
      <td>4</td>
      <td>95.0</td>
      <td>226</td>
      <td>24206644</td>
      <td>1267000</td>
      <td>15.899</td>
      <td>19.105481</td>
    </tr>
    <tr>
      <th>50</th>
      <td>마다가스카르</td>
      <td>42137</td>
      <td>765.0</td>
      <td>903</td>
      <td>40469.0</td>
      <td>2</td>
      <td>96.0</td>
      <td>1522</td>
      <td>27691018</td>
      <td>587041</td>
      <td>14.746</td>
      <td>47.170501</td>
    </tr>
    <tr>
      <th>45</th>
      <td>모잠비크</td>
      <td>72577</td>
      <td>1488.0</td>
      <td>848</td>
      <td>70241.0</td>
      <td>1</td>
      <td>97.0</td>
      <td>2322</td>
      <td>31255435</td>
      <td>801590</td>
      <td>13.957</td>
      <td>38.991798</td>
    </tr>
    <tr>
      <th>70</th>
      <td>차드</td>
      <td>4947</td>
      <td>5.0</td>
      <td>174</td>
      <td>4768.0</td>
      <td>4</td>
      <td>96.0</td>
      <td>301</td>
      <td>16425864</td>
      <td>1284000</td>
      <td>12.531</td>
      <td>12.792729</td>
    </tr>
    <tr>
      <th>15</th>
      <td>콩고민주공화국</td>
      <td>37926</td>
      <td>9109.0</td>
      <td>879</td>
      <td>27938.0</td>
      <td>2</td>
      <td>74.0</td>
      <td>423</td>
      <td>89561403</td>
      <td>2344858</td>
      <td>12.022</td>
      <td>38.194809</td>
    </tr>
    <tr>
      <th>74</th>
      <td>르완다</td>
      <td>31435</td>
      <td>4343.0</td>
      <td>388</td>
      <td>26704.0</td>
      <td>1</td>
      <td>85.0</td>
      <td>2427</td>
      <td>12952218</td>
      <td>26338</td>
      <td>10.633</td>
      <td>491.769231</td>
    </tr>
    <tr>
      <th>60</th>
      <td>말라위</td>
      <td>34914</td>
      <td>852.0</td>
      <td>1171</td>
      <td>32891.0</td>
      <td>3</td>
      <td>94.0</td>
      <td>1825</td>
      <td>19129952</td>
      <td>118484</td>
      <td>9.268</td>
      <td>161.455994</td>
    </tr>
    <tr>
      <th>71</th>
      <td>소말리아</td>
      <td>14867</td>
      <td>6888.0</td>
      <td>775</td>
      <td>7204.0</td>
      <td>5</td>
      <td>49.0</td>
      <td>935</td>
      <td>15893222</td>
      <td>637657</td>
      <td>5.367</td>
      <td>24.924406</td>
    </tr>
    <tr>
      <th>81</th>
      <td>남수단</td>
      <td>10786</td>
      <td>157.0</td>
      <td>115</td>
      <td>10514.0</td>
      <td>1</td>
      <td>98.0</td>
      <td>964</td>
      <td>11193725</td>
      <td>644329</td>
      <td>4.461</td>
      <td>17.372685</td>
    </tr>
    <tr>
      <th>76</th>
      <td>부룬디</td>
      <td>5242</td>
      <td>4461.0</td>
      <td>8</td>
      <td>773.0</td>
      <td>0</td>
      <td>15.0</td>
      <td>441</td>
      <td>11890784</td>
      <td>27834</td>
      <td>3.244</td>
      <td>427.203564</td>
    </tr>
  </tbody>
</table>
</div>



## GDP 상위 10개국, 하위 10개국 parameter 별 상관계수 비교  ( Heatmap )

### < 확진자, 인구수, 국토면적, 사망자, GDP, 완치, 인구밀도 > 


```python
gdp_top10 = df5.sort_values(by='GDP', ascending=False).head(10)
gdp_low10 = df5.sort_values(by='GDP', ascending=False).tail(10)

corr_1 = gdp_top10.loc[:, ['확진자', '인구수', '국토면적', '사망자', 'GDP', '완치', '인구밀도']].corr(method='pearson')
corr_2 = gdp_low10.loc[:, ['확진자', '인구수', '국토면적', '사망자', 'GDP', '완치', '인구밀도']].corr(method='pearson')
```


```python
fig = plt.figure(figsize=(20, 8))
fig.patch.set_facecolor('xkcd:white')

axis1 = fig.add_subplot(1, 2, 1)
axis1 = sns.heatmap(corr_1, annot=True, annot_kws={'size':12}, fmt='.4f', cmap='Blues')
plt.title('< Top 10 >')
axis1.plot()

axis2 = fig.add_subplot(1, 2, 2)
axis2 = sns.heatmap(corr_2, annot=True, annot_kws={'size':12}, fmt='.4f', cmap='Blues')
plt.title('< Low 10 >')
axis2.plot()

plt.show()
```


    
![png](output_21_0.png)
    


### 데이터 해석 : 
우선, 기본적으로 7개의 parameter 간의 상관관계를 분석하는 것이기 때문에 Heatmap으로 표현하긴 했지만 조금 복잡하게 보이긴합니다. 그래서 이 Heatmap은 훑어보듯이 넘어가고 대충 어떤 느낌인지만 설명하려고 합니다.

---

#### Top 10 나라의 경우
인구밀도를 제외한 나머지의 Parameter에서 매우 높은 상관관계를 보이거나 낮은 정도의 상관관계를 보입니다. 인구밀도 기준으로 보았을 때, 인구수를 제외하고는 다 상관관계가 음수(-)의 값을 가집니다. 왜냐하면 ```인구밀도 = 인구수 / 국토면적``` 이기 때문에 당연한 결과라고 볼 수 있겠습니다. 같은 원리로, 인구밀도와 국토면적은 반비례관계이기 때문에 상관계수가 -0.7로 상당히 낮은 것을 볼 수 있습니다. 나머지 parameter 간의 관계는 다음 축소된 Heatmap을 보면서 추가적으로 설명해보겠습니다.

---

#### GDP가 낮은 하위 10개 나라의 경우
Low 10 국가의 경우 Top 10 국가와 비교해서 parameter 간의 관계가 극명하게 나뉜 것을 볼 수 있습니다. 아무래도 경제상황이 좋지 못하다 보니 이런 상관관계를 보이는 것이 아닐까 예상해볼 수 있습니다. 다음 Heatmap을 보면서 Top 10 국가와 어떻게 차이가 나는지 살펴보도록 하겠습니다.

### 상관관계를 시각화 하기 위한 ScatterPlot, 회귀직선


```python
fig = plt.figure(figsize=(6,6), facecolor='white')

plt.scatter(x='확진자',y='사망자',data=gdp_top10)
plt.show()

sns.set_style("darkgrid", {"axes.facecolor": ".9"})
sns.lmplot(x='확진자',y='사망자',data=gdp_top10)
```


    
![png](output_24_0.png)
    





    <seaborn.axisgrid.FacetGrid at 0x188c1f7a880>




    
![png](output_24_2.png)
    


### < 확진자, 인구수, 국토면적, 사망자, GDP, 완치 > 


```python
gdp_top10 = df5.sort_values(by='GDP', ascending=False).head(10)
gdp_low10 = df5.sort_values(by='GDP', ascending=False).tail(10)

corr_1 = gdp_top10.loc[:, ['확진자', '인구수', '국토면적', '사망자', 'GDP', '완치']].corr(method='pearson')
corr_2 = gdp_low10.loc[:, ['확진자', '인구수', '국토면적', '사망자', 'GDP', '완치']].corr(method='pearson')
```


```python
fig = plt.figure(figsize=(20, 8))
fig.patch.set_facecolor('xkcd:white')

axis1 = fig.add_subplot(1, 2, 1)
axis1 = sns.heatmap(corr_1, annot=True, annot_kws={'size':11}, fmt='.4f', cmap='Blues')
plt.title('< Top 10 >')
axis1.plot()

axis2 = fig.add_subplot(1, 2, 2)
axis2 = sns.heatmap(corr_2, annot=True, annot_kws={'size':11}, fmt='.4f', cmap='Blues')
plt.title('< Low 10 >')
axis2.plot()

plt.show()
```


    
![png](output_27_0.png)
    


### 데이터 해석 : 
인구밀도 parameter를 제거하고 나니 Heatmap이 더 명확해지면서 parameter 간의 상관관계를 더욱 파악하기 쉬워졌습니다.

---

#### Top 10 나라의 경우
국토면적이 다른 parameter들과 비교해서 약한 상관관계를 가지는 것을 알 수 있습니다. 즉, 국토면적의 넓고 좁음이 확진자에 끼치는 영향이 크지 않다고 해석할 수 있을 것 같습니다. 

그리고 `국토면적 - 인구수`, `인구수 - GDP`의 관계가 약한 것을 볼 수 있는데 그렇다고 `국토면적 - GDP`의 관계는 그렇게 약하지는 않구나라는 것을 알 수 있습니다. 

추가적으로, 국토면적이 넓다고 꼭 인구수가 많은 것은 아니며(상관계수 = 0.0405), GDP가 높다고 꼭 인구수가 많은 것은 아니라고(상관계수 = 0.0930) 판단할 수 있습니다.

---

#### Low 10 나라의 경우
Low 10 국가와 Top 10 국가와의 차이가 극명하게 보이는 것 같습니다. 대표적으로, GDP와 다른 parameter와의 상관관계가 크지 않다는 점을 뽑을 수 있습니다. 세부적인 내용들을 설명해보겠습니다.

1. GDP와 Covid-19 환자(확진자, 사망자, 완치자)와의 관계 :
Top 10 나라에서는 비교적 높은 상관관계를 가지는 것에 비해 Low 10 나라에서는 오히려 약한 음의 상관관계를 가지는 것을 알 수 있습니다. 조금 과장해서 말하면 반비례 관계를 가지므로, 이 나라들 사이에서는 GDP가 높을 수록 그렇지 않은 나라들에 비해 확진자가 더 적다고 판단할 수 있습니다. 
\
이러한 결과가 나오는 이유는, GDP가 높은 선진국의 경우에 크게 발달한 도심지와 사람들의 높은 소비수준으로 인해 사람들 간의 전염이 빠르고 치명적이었습니다. 반면에 GDP가 낮은 나라의 경우에는 사람들이 한 지역에 많이 밀집해 있을 가능성이 낮고, 이러한 나라들에 있어서 GDP가 높은 것이 사람들 간의 적극적인 소비활동과 직접적인 접촉이 많이 생긴다는 것을 의미하지 않기 때문으로 해석할 수 있습니다.
\
\
2. GDP와 국토면적의 관계 : 
Top 10 나라의 상관계수(0.2368)에 비해 Low 10 나라의 상관계수(0.4237)가 조금 더 의미있는 수치를 가지는 것을 알 수 있습니다. 즉, Top 10 나라에 비해 국토면적이 넓을 수록 GDP가 더 높을 수 있다는 것을 판단할 수 있습니다.
\
\
3. 국토면적과 인구수의 관계 : 
Top 10 나라의 상관계수(0.0405)에 비해 Low 10 나라의 상관계수(0.3500)가 비교적 더 높습니다. 즉, 이 카테고리에서는 국토면적이 넓을수록 인구 수가 더 많을 수 있다는 것을 알 수 있습니다.
\
\
4. 인구수와 Covid-19 환자(확진자, 사망자, 완치자)와의 관계 : 
Top 10 나라에 비해 인구수 대비 Covid-19 환자의 상관계수가 상당히 높은 것을 알 수 있습니다(거의 1의 상관관계). 즉, 인구 수가 많을수록 그에 비례해 확진자도 많다는 뜻입니다. 
\
이 수치가 의미하는 것은 GDP가 높은 나라에서는 인구가 많아도 감염을 예방할 수 있는 수 많은 인적자원과 물자, 개인이 비축할 수 있는 보급품들이 많아 어느정도 예방이 가능했다는 뜻입니다. 반면에, GDP가 낮은 나라의 경우에는 이러한 물자들이 부족하기 때문에 Covid-19를 예방할 수 있는 시민들의 경제적인 능력과 국가적 능력이 부족하다고 해석할 수 있습니다.

### < 확진자, 인구수, 사망자, GDP, 완치 > : 마지막으로 국토면적 항목을 삭제하고 출력해보았습니다.


```python
gdp_top10 = df5.sort_values(by='GDP', ascending=False).head(10)
gdp_low10 = df5.sort_values(by='GDP', ascending=False).tail(10)

corr_1 = gdp_top10.loc[:, ['확진자', '인구수', '사망자', '완치', 'GDP']].corr(method='pearson')
corr_2 = gdp_low10.loc[:, ['확진자', '인구수', '사망자', '완치', 'GDP']].corr(method='pearson')
```


```python
fig = plt.figure(figsize=(20, 8))
fig.patch.set_facecolor('xkcd:white')

axis1 = fig.add_subplot(1, 2, 1)
axis1 = sns.heatmap(corr_1, annot=True, annot_kws={'size':11}, fmt='.4f', cmap='Blues')
plt.title('< Top 10 >')
axis1.plot()

axis2 = fig.add_subplot(1, 2, 2)
axis2 = sns.heatmap(corr_2, annot=True, annot_kws={'size':11}, fmt='.4f', cmap='Blues')
plt.title('< Low 10 >')
axis2.plot()

plt.show()
```


    
![png](output_31_0.png)
    


## GDP 상위 10개국, 하위 10개국 parameter 별 수치 비교 ( 중국 제외 )

위에서 parameter 간의 상관관계를 비교했다면 이제는 `수치`를 비교해보자!

### < GDP 비교 >


```python
gdp_list = df5.sort_values(by='GDP', ascending=False)

top_names = list(gdp_list['국가'].head(10))
top_values = list(gdp_list['GDP'].head(10))
top_values = list(map(float, top_values))

low_names = list(gdp_list['국가'].tail(10))
low_values = list(gdp_list['GDP'].tail(10))
low_values = list(map(float, low_values))

fig = plt.figure(figsize=(20, 12), facecolor='white')

axis1 = fig.add_subplot(2, 1, 1)
plt.plot(top_names, top_values, 'go-')
plt.title('< Top 10 GDP >')
plt.xlabel('국가')
plt.ylabel('GDP [10억 달러]')

axis2 = fig.add_subplot(2, 1, 2)
plt.plot(low_names, low_values, 'ro-')
plt.title('< Low 10 GDP >')
plt.xlabel('국가')
plt.ylabel('GDP [10억 달러]')

plt.show()
```


    
![png](output_34_0.png)
    


#### 상위 10개국과 하위 10개국의 수치 차이가 상당히 심한 것을 볼 수 있습니다.

### < 확진자 & 인구수 비교 >


```python
top_names = list(gdp_list['국가'].head(10))
top_values_1 = list(gdp_list['확진자'].head(10))
top_values_1 = list(map(float, top_values_1))
top_values_2 = list(gdp_list['인구수'].head(10))
top_values_2 = list(map(float, top_values_2))

low_names = list(gdp_list['국가'].tail(10))
low_values_1 = list(gdp_list['확진자'].tail(10))
low_values_1 = list(map(float, low_values_1))
low_values_2 = list(gdp_list['인구수'].tail(10))
low_values_2 = list(map(float, low_values_2))

fig = plt.figure(figsize=(20, 12), facecolor='white')

axis1 = fig.add_subplot(2, 1, 1)
plt.plot(top_names, top_values_1, 'go-')
plt.plot(top_names, top_values_2, 'bo-.')
plt.title('< Top 10 GDP >')
plt.legend(['확진자', '인구수'])
plt.xlabel('국가')
plt.ylabel('10억 명')

axis2 = fig.add_subplot(2, 1, 2)
plt.plot(low_names, low_values_1, 'go-')
plt.plot(low_names, low_values_2, 'bo-.')
plt.title('< Low 10 GDP >')
plt.legend(['확진자', '인구수'])
plt.xlabel('국가')
plt.ylabel('1천만 명')

plt.show()

print('Top 10 인구수 :', top_values_2)
print('Top 10 확진자수 :', top_values_1)
print('Low 10 인구수 :', low_values_2)
print('Low 10 확진자수 :', low_values_1)
```


    
![png](output_37_0.png)
    


    Top 10 인구수 : [331002651.0, 126476461.0, 83783942.0, 67886011.0, 1380004385.0, 65273511.0, 60461826.0, 37742154.0, 51269185.0, 145934462.0]
    Top 10 확진자수 : [34419838.0, 785969.0, 3730599.0, 4640507.0, 29977861.0, 5757798.0, 4253460.0, 1409607.0, 151901.0, 5334204.0]
    Low 10 인구수 : [24206644.0, 27691018.0, 31255435.0, 16425864.0, 89561403.0, 12952218.0, 19129952.0, 15893222.0, 11193725.0, 11890784.0]
    Low 10 확진자수 : [5469.0, 42137.0, 72577.0, 4947.0, 37926.0, 31435.0, 34914.0, 14867.0, 10786.0, 5242.0]
    

#### 확진자 비율이 낮은 관계로 확진자만 다시 출력


```python
top_names = list(gdp_list['국가'].head(10))
top_values = list(gdp_list['확진자'].head(10))
top_values = list(map(float, top_values))

low_names = list(gdp_list['국가'].tail(10))
low_values = list(gdp_list['확진자'].tail(10))
low_values = list(map(float, low_values))

fig = plt.figure(figsize=(20, 12), facecolor='white')

axis1 = fig.add_subplot(2, 1, 1)
plt.plot(top_names, top_values, 'ro-')
plt.title('< Top 10 GDP >')
plt.xlabel('국가')
plt.ylabel('확진자 [1000만 명]')

axis2 = fig.add_subplot(2, 1, 2)
plt.plot(low_names, low_values, 'ro-')
plt.title('< Low 10 GDP >')
plt.xlabel('국가')
plt.ylabel('확진자 [명]')

plt.show()
```


    
![png](output_39_0.png)
    


### < 사망자 비교 >


```python
top_names = list(gdp_list['국가'].head(10))
top_values = list(gdp_list['사망자'].head(10))
top_values = list(map(float, top_values))

low_names = list(gdp_list['국가'].tail(10))
low_values = list(gdp_list['사망자'].tail(10))
low_values = list(map(float, low_values))

fig = plt.figure(figsize=(20, 12), facecolor='white')

axis1 = fig.add_subplot(2, 1, 1)
plt.plot(top_names, top_values, 'ko-')
plt.title('< Top 10 GDP >')
plt.xlabel('국가')
plt.ylabel('사망자 [명]')

axis2 = fig.add_subplot(2, 1, 2)
plt.plot(low_names, low_values, 'ko-')
plt.title('< Low 10 GDP >')
plt.xlabel('국가')
plt.ylabel('사망자 [명]')

plt.show()
```


    
![png](output_41_0.png)
    


### < 완치자 비교 >


```python
top_names = list(gdp_list['국가'].head(10))
top_values = list(gdp_list['완치'].head(10))
top_values = list(map(float, top_values))

low_names = list(gdp_list['국가'].tail(10))
low_values = list(gdp_list['완치'].tail(10))
low_values = list(map(float, low_values))

fig = plt.figure(figsize=(20, 12), facecolor='white')

axis1 = fig.add_subplot(2, 1, 1)
plt.plot(top_names, top_values, 'go-')
plt.title('< Top 10 GDP >')
plt.xlabel('국가')
plt.ylabel('완치자 [1000만 명]')

axis2 = fig.add_subplot(2, 1, 2)
plt.plot(low_names, low_values, 'go-')
plt.title('< Low 10 GDP >')
plt.xlabel('국가')
plt.ylabel('완치자 [명]')

plt.show()
```


    
![png](output_43_0.png)
    


### < 인구밀도 비교 >


```python
top_names = list(gdp_list['국가'].head(10))
top_values = list(gdp_list['인구밀도'].head(10))
top_values = list(map(float, top_values))

low_names = list(gdp_list['국가'].tail(10))
low_values = list(gdp_list['인구밀도'].tail(10))
low_values = list(map(float, low_values))

fig = plt.figure(figsize=(20, 12), facecolor='white')

axis1 = fig.add_subplot(2, 1, 1)
plt.plot(top_names, top_values, 'bo-')
plt.title('< Top 10 GDP >')
plt.xlabel('국가')
plt.ylabel('인구밀도 [명/$km^2$]')

axis2 = fig.add_subplot(2, 1, 2)
plt.plot(low_names, low_values, 'bo-')
plt.title('< Low 10 GDP >')
plt.xlabel('국가')
plt.ylabel('인구밀도 [명/$km^2$]')

plt.show()
```


    
![png](output_45_0.png)
    


### < 치명율 비교 >


```python
gdp_list_1 = df5.sort_values(by='GDP', ascending=False)

gdp_list_1['치명율'] = gdp_list_1['사망자']/gdp_list_1['확진자']   # 치명율 Column 추가

top_names = list(gdp_list_1['국가'].head(10))
top_values = list(gdp_list_1['치명율'].head(10))
top_values = list(map(float, top_values))

low_names = list(gdp_list_1['국가'].tail(10))
low_values = list(gdp_list_1['치명율'].tail(10))
low_values = list(map(float, low_values))

fig = plt.figure(figsize=(20, 12), facecolor='white')

axis1 = fig.add_subplot(2, 1, 1)
plt.plot(top_names, top_values, 'bo-')
plt.title('< Top 10 GDP >')
plt.xlabel('국가')
plt.ylabel('치명율 [%]')

axis2 = fig.add_subplot(2, 1, 2)
plt.plot(low_names, low_values, 'bo-')
plt.title('< Low 10 GDP >')
plt.xlabel('국가')
plt.ylabel('치명율 [%]')

plt.show()
```


    
![png](output_47_0.png)
    



```python

```
