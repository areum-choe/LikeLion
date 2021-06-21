{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import time\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\chlal\\\\Documents\\\\GitHub\\\\LikeLion\\\\code'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "driver=webdriver.Chrome('./chromedriver_90.exe')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "url='https:///www.amazon.com/'\n",
    "driver.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "input input\n"
     ]
    }
   ],
   "source": [
    "sel_search = driver.find_element_by_xpath('//*[@id=\"twotabsearchtextbox\"]')\n",
    "sel_btn = driver.find_element_by_xpath('//*[@id=\"nav-search-submit-button\"]')\n",
    "\n",
    "print(sel_search.tag_name,sel_btn.tag_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "sel_search.clear()\n",
    "sel_search.send_keys('samsung tv')\n",
    "sel_btn.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://www.amazon.com/Hisense-40-Inch-Class-Compatibility-40H4F/dp/B084B1T8KK/ref=sr_1_1_sspa?dchild=1&keywords=samsung+tv&qid=1624259326&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTjc5Q1FSS05ERldEJmVuY3J5cHRlZElkPUEwODI2Mzk3MVJSRUdGS01XT0tJViZlbmNyeXB0ZWRBZElkPUEwMDE5MDA2MlE0QUU4RlI0M09EQiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='\n",
    "driver.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<title>Amazon.com: Hisense 40-Inch Class H4 Series LED Roku Smart TV with Alexa Compatibility (40H4F, 2020 Model): Electronics</title>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "page = driver.page_source\n",
    "soup = BeautifulSoup(page, 'html.parser')\n",
    "soup.title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Christine Haas', 'Shok', 'Laura', 'Courtney', 'Jayme', 'CeeKay', 'gregory', 'Richelle']\n",
      "['3', '1', '5', '5', '5', '1', '3', '5']\n",
      "[' March 12, 2020', ' March 12, 2020', ' April 4, 2020', ' February 26, 2020', ' January 22, 2021', ' September 10, 2020', ' May 11, 2020', ' February 29, 2020']\n",
      "['172 people found this helpful', '147 people found this helpful', '110 people found this helpful', '107 people found this helpful', '64 people found this helpful', '71 people found this helpful', '64 people found this helpful', '76 people found this helpful']\n"
     ]
    }
   ],
   "source": [
    "### 닉네임\n",
    "import re \n",
    "all_r=soup.find_all(\"div\",class_=\"a-section celwidget\")\n",
    "all_user=[]\n",
    "all_score=[]\n",
    "all_date=[]\n",
    "all_people=[]\n",
    "\n",
    "for one in all_r:\n",
    "    user_one=one.find(\"span\",class_=\"a-profile-name\").text\n",
    "    all_user.append(user_one) #사용자 추가\n",
    "    \n",
    "    score_one=one.find(\"span\",class_=\"a-icon-alt\").text\n",
    "    nums = re.findall(\"\\d+\", score_one)[0]\n",
    "    all_score.append(nums) #평점\n",
    "    \n",
    "    review_date = one.find(\"span\", class_=\"a-size-base a-color-secondary review-date\")\n",
    "    tmp = review_date.text\n",
    "    texts = tmp.split(\"on\")\n",
    "    all_date.append(texts[1]) #날짜\n",
    "\n",
    "        \n",
    "    review_people = one.find(\"span\", class_=\"a-size-base a-color-tertiary cr-vote-text\")\n",
    "    tmp = review_people.text\n",
    "    all_people.append(tmp) #도움받은 사람 수\n",
    "    \n",
    "\n",
    "\n",
    "    \n",
    "print(all_user)\n",
    "print(all_score)\n",
    "print(all_date)\n",
    "print(all_people)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>사용자</th>\n",
       "      <th>평점</th>\n",
       "      <th>날짜</th>\n",
       "      <th>도움</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Christine Haas</td>\n",
       "      <td>3</td>\n",
       "      <td>March 12, 2020</td>\n",
       "      <td>172 people found this helpful</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Shok</td>\n",
       "      <td>1</td>\n",
       "      <td>March 12, 2020</td>\n",
       "      <td>147 people found this helpful</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Laura</td>\n",
       "      <td>5</td>\n",
       "      <td>April 4, 2020</td>\n",
       "      <td>110 people found this helpful</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Courtney</td>\n",
       "      <td>5</td>\n",
       "      <td>February 26, 2020</td>\n",
       "      <td>107 people found this helpful</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Jayme</td>\n",
       "      <td>5</td>\n",
       "      <td>January 22, 2021</td>\n",
       "      <td>64 people found this helpful</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>CeeKay</td>\n",
       "      <td>1</td>\n",
       "      <td>September 10, 2020</td>\n",
       "      <td>71 people found this helpful</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>gregory</td>\n",
       "      <td>3</td>\n",
       "      <td>May 11, 2020</td>\n",
       "      <td>64 people found this helpful</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Richelle</td>\n",
       "      <td>5</td>\n",
       "      <td>February 29, 2020</td>\n",
       "      <td>76 people found this helpful</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              사용자 평점                   날짜                             도움\n",
       "0  Christine Haas  3       March 12, 2020  172 people found this helpful\n",
       "1            Shok  1       March 12, 2020  147 people found this helpful\n",
       "2           Laura  5        April 4, 2020  110 people found this helpful\n",
       "3        Courtney  5    February 26, 2020  107 people found this helpful\n",
       "4           Jayme  5     January 22, 2021   64 people found this helpful\n",
       "5          CeeKay  1   September 10, 2020   71 people found this helpful\n",
       "6         gregory  3         May 11, 2020   64 people found this helpful\n",
       "7        Richelle  5    February 29, 2020   76 people found this helpful"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dat_r = {\"사용자\":all_user, \"평점\":all_score,\n",
    "         \"날짜\":all_date, '도움':all_people}\n",
    "dat = pd.DataFrame(dat_r)\n",
    "dat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\chlal\\Documents\\GitHub\\LikeLion\\code\n",
      "['.ipynb_checkpoints', '210621_class.ipynb', '210621_실습.ipynb', 'amazonreview.csv', 'AmazonTV_review.csv', 'chromedriver_90.exe', 'chromedriver_win32.zip', '셀레늄.ipynb']\n"
     ]
    }
   ],
   "source": [
    "dat.to_csv(\"AmazonTV_review.csv\", index=False)\n",
    "\n",
    "## 확인\n",
    "print(os.getcwd())  # 현재 위치\n",
    "print(os.listdir(os.getcwd()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
