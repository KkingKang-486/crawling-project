# <p align = 'center'>  :triangular_flag_on_post: 라프텔 장르 분류 모델 <br><br> Laftel_Genre_Classification_Model </p>
자연어처리 기반의 장르 분류 모델 개발 프로젝트 입니다 (w.강서현, 이하은, 전혜영)

이 저장소의 
파이썬 실행버전은 3.7입니다.

<br>

### 프로젝트 개요
-----------------------------------------------------------------------------------------------------------------------------
<div align = 'center'>
  <img style = "width : 850px" src = 'https://i.esdrop.com/d/f/NXl6YkfhTU/DKCNmwGYtI.jpg'>
</div>
<br>

### 프로젝트 목적
<br>
애니메이션은 주로 독특한 줄거리로 소개되곤 한다. 비교적 관련성이 떨어지는 줄거리 내용으로 해당 애니메이션의 장르를 예측할 수 있을 지, 애니메이션 OTT플랫폼인 라프텔 데이터를 활용해 알아보고자 한다.
<br><br>

---------------------------------------------------
### 구축 환경 : Python 3.7
--------------------------------------------------- 

### 데이터셋(크롤링/전처리)

  <ol>
    <li> 라프텔 (애니메이션 ott 플랫폼) </li>
    <li> 네이버 줄거리 </li>
  </ol>   

* eval_set : 애니플러스 카테고리
* test_data : 특정 애니메이션의 네이버 검색 결과 줄거리
* 폴더구조<br>
project_root --- crawling_data    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #타이틀 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- crawling_data_2   &nbsp;&nbsp; #카테고리 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- crawling_data_3   &nbsp;&nbsp; #줄거리 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- crawling_data_4   &nbsp;&nbsp; #테스트데이터 <br>

----------------------------------------------------

### 프로젝트 과정

  <ol>
    <li> 데이터수집 (selemium / BeautifulSoup) </li>
    <div align = 'center'>
  <img style = "width : 850px" src = 'https://i.esdrop.com/d/f/NXl6YkfhTU/AMiKnxoZs2.jpg'>
</div>
<br>
    <li> 전처리 (KoNLPy / re / sklearn) </li>
    <li> 모델학습 : Numpy, metaplotlib, keras, sklearn </li>
    <li> 모델예측 : Pandas, Numpy, sklearn, KoNLPy, keras, pickle  </li>
  </ol>  


----------------------------------------------------


### 프로젝트 결과 - 어플리케이션 실행
<!-- <div align = 'left'>
  <img style = "width : 200px" src = 'https://i.esdrop.com/d/f/NXl6YkfhTU/nR2lHRkgr9.png'>
  </div>
  <div align = 'right'>
  <img style = "width : 400px" src = 'https://i.esdrop.com/d/f/NXl6YkfhTU/1HbUiAZ4e3.png'>
</div> -->
<div>
  <img style = "width : 300px" src = 'https://i.esdrop.com/d/f/NXl6YkfhTU/nR2lHRkgr9.png'>
  <img style = "width : 300px" src = 'https://i.esdrop.com/d/f/NXl6YkfhTU/1HbUiAZ4e3.png'>
</div>

----------------------------------------------------

### 기대효과
1) 애니메이션 컨텐츠를 다루는 OTT플랫폼의 컨텐츠 분류모델 제작과 제작한 모델의 예측률을 검증
2) 애니메이션 이외에도 영화, 드라마, 웹툰 등에서도 줄거리를 통해 장르 분류 가능



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
