# Laftel_Genre_Classification_Project
라프텔 장르 분류 프로젝트 (w.강서현, 이하은, 전혜영)

eval_set : 애니플러스 카테고리

test_data : 특정 애니메이션의 네이버 검색 결과 줄거리




이 저장소의 
파이썬 실행버전은 3.7입니다.

폴더구조<br>
project_root --- crawling_data    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #타이틀 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- crawling_data_2   &nbsp;&nbsp; #카테고리 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- crawling_data_3   &nbsp;&nbsp; #줄거리 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- crawling_data_4   &nbsp;&nbsp; #테스트데이터 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- temp<br>


# <p align = 'center'>  :triangular_flag_on_post: 라프텔 장르 분류 프로젝트 <br><br> Natural Language Processing Genre Classification Model </p>

<br>

### 프로젝트 개요
-----------------------------------------------------------------------------------------------------------------------------
<div align = 'center'>
  <img style = "width : 850px" src = 'https://i.esdrop.com/d/f/NXl6YkfhTU/DKCNmwGYtI.jpg'>
</div>
<br>

### 프로젝트 목적
<br>
주로 줄거리나 전개가 독특한 애니메이션. 관련성이 떨어지는 내용으로 장르를 예측할 수 있을 지, 애니메이션 OTT플랫폼인 라프텔 데이터를 활용해 알아본다
<br><br>

---------------------------------------------------
### 구축 환경 : Python 3.7
--------------------------------------------------- 

### 데이터셋(크롤링/전처리)
<br><br>
  <ol>
    <li> 라프텔 (애니메이션 ott 플랫폼) </li>
    <li> 네이버 줄거리 </li>
  </ol>   
<br><br>

----------------------------------------------------

### 프로젝트 과정
1) 데이터수집 (selemium/ BeautifulSoup)
2) 전처리 (konlpy/ re / sklearn)
3) 모델학습 : Numpy, metaplotlib, keras, sklearn
4) 모델예측 : Pandas, Numpy, sklearn, KoNLPy, keras, pickle(토큰?) Okt (한글 형태소)

  <ol>
    <li> 데이터수집 (selemium/ BeautifulSoup) </li>
    <li> 전처리 (konlpy/ re / sklearn) </li>
    <li> 모델학습 : Numpy, metaplotlib, keras, sklearn </li>
    <li> 모델예측 : Pandas, Numpy, sklearn, KoNLPy, keras, pickle  </li>
  </ol>  

- - -
<div align = "center">
<h4> 💽Tech Stack 💽 </h4>
🚋 Plaforms & Languages 💬
<br><br>
<img src = "https://img.shields.io/static/v1?label=Python&message=v3.7&color=red">
<img src = "https://img.shields.io/static/v1?label=Matplotlib&message=3.5.3&color=yellow">
<br>
<img src = "https://img.shields.io/static/v1?label=Numpy&message=1.21.6&color=green">
<img src = "https://img.shields.io/static/v1?label=Pandas&message=1.1.5&color=navy">

<img src = "https://img.shields.io/static/v1?label=keras&message=2.9.0&color=blue">
<img src = "https://img.shields.io/static/v1?label=tensorflow&message=2.9.2&color=pink">
<img src = "https://img.shields.io/static/v1?label=scikit-learn&message=1.0.2&color=orange">
<img src = "https://img.shields.io/static/v1?label=konlpy&message=0.6.0&color=purple">
</div>
