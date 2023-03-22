# crawling-project
라프텔 크롤링 프로젝트 (w.강서현, 이하은, 전혜영)


이 저장소의 
파이썬 실행버전은 3.7입니다.

폴더구조<br>
project_root --- crawling_data    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #타이틀 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- crawling_data_2   &nbsp;&nbsp; #카테고리 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- crawling_data_3   &nbsp;&nbsp; #줄거리 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- crawling_data_4   &nbsp;&nbsp; #테스트데이터 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- temp<br>


# <p align = 'center'>  :triangular_flag_on_post: 자연어 크롤링 프로젝트 <br><br> Barcode Recognition & Dangerous Elements Notification </p>

<br>

### Description
-----------------------------------------------------------------------------------------------------------------------------
<div align = 'center'>
  <img style = "width : 850px" src = 'https://i.esdrop.com/d/f/CcSudjZ5R8/9blR74g8SV.png'>
</div>
<br>

<h5>
시중에 판매중인 음료의 점자는 '맥주', '음료', '탄산' 총 세가지로만 표기되어 있을뿐 아니라, 점자가 잘못 되어있는 제품들도 다수 존재합니다.
<br><br>
시각장애인들은 음료를 하나 먹을 때도 이러한 어려움을 겪으며 살아가고 있습니다.
<br><br><br>
시각장애인이 살아가는데 발생하는 문제점들을 해소해 쾌적한 환경을 만들어주기 위해서,
<br><br>
  <ol>
    <li> 바코드를 인식하여 음성으로 해당 제품을 알려주는 프로그램 </li>
    <br>
    <li> 눈앞에 보이는 위험물을 감지하여 사고를 방지하는 프로그램 </li>
  </ol>   
<br><br>
총 2가지를 제작하게 되었습니다.
</h5>
<br><br>
  
### Barcode Recognition
#### <ul> <li> 구축 환경 : Python 3.7 </li> </ul>
-----------------------------------------------------------------------------------------------------------------------------
<div align = 'center'>
  <img style = "width : 850px" src = 'https://i.esdrop.com/d/f/CcSudjZ5R8/j5O5EhWj1l.png'>
</div>
<h4>1. 데이터 셋</h4>
<h6>
  데이터셋은 공공데이터 포털 오픈 API 데이터를 활용했습니다. 바코드 데이터는 약 22만 개 정도이며,<br><br>
  전처리를 통해서 제품명 / 유통바코드 / 식품 유형을 추출하였습니다.
  <br><br>
</h6>

```python
  def parse():
    try:
        row_id = item.find("row id").get_text()
        PRDLST_REPORT_NO = item.find("PRDLST_REPORT_NO").get_text()
        PRMS_DT = item.find("PRMS_DT").get_text()
        PRDLST_NM = item.find("PRDLST_NM").get_text()
        BAR_CD = item.find("BAR_CD").get_text()
        POG_DAYCNT = item.find("POG_DAYCNT").get_text()
        PRDLST_DCNM = item.find("PRDLST_DCNM").get_text()
        BSSH_NM = item.find("BSSH_NM").get_text()

        return {
            "품목보고(신고)번호":PRDLST_REPORT_NO,
            "보고(신고일)":PRMS_DT,
            "제품명":PRDLST_NM,
            "유통바코드":BAR_CD,
            "유통/소비기한":POG_DAYCNT,
            "식품 유형":PRDLST_DCNM,
            "제조사명":BSSH_NM,
            }

    except AttributeError as e:
        return {
            "품목보고(신고)번호": None,
            "보고(신고일)": None,
            "제품명": None,
            "유통바코드": None,
            "유통/소비기한": None,
            "식품 유형": None,
            "제조사명": None,
        }
  ```
  
<br>
<h4>2. 바코드 인식 과정</h4>
<h6>
  바코드 인식 과정은 OpenCV로 QR코드/바코드를 인식하는 방식으로 진행되는데, 인식 과정에서 총 3가지 결과가 발생합니다.<br><br>
  바코드가 아닌 QR코드가 인식 될 경우, 예외 처리를 하고 바코드를 인식해달라는 TTS를 넣었습니다. <br><br>
 </h6>
 
  ```python
     except:
       cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
       TTS_text = '바코드를 정확하게 인식시켜 주세요'
       threading.Thread(target=say, args=(TTS_text,)).start()
       continue
  ```
  <br>
 <h6> 
  등록되지 않은 바코드가 인식될 경우, 등록되지 않은 제품이라는 TTS를 넣어 처리했습니다. <br><br>
 </h6>
 
  ```python
     except:
       TTS_text = '해당 제품은 등록되지 않은 제품입니다'
       threading.Thread(target=say, args=(TTS_text,)).start()
       continue
  
  ```
  <br>
 <h6>  
  등록된 바코드가 인식될 경우, 데이터셋에서 인식된 바코드 일련번호와 동일한 제품의 인덱스를 찾아, 해당 인덱스의 1번째, 3번째 Column에 해당되는 값을 추출하여, <br><br>
  해당 메세지를 출력하는 방식으로 진행됩니다. <br><br>
 </h6>
 
  ```python
     try:
        df = pd.read_csv('./datasets/barcode_final.csv')
        product_idx = df[df['유통바코드'] == barcode_int].index[0]
        print(product_idx)

        TTS_data = df.iloc[product_idx, :]
        TTS_text = '이 제품은 {}이고, {}카테고리의 제품입니다.'.format(TTS_data[0], TTS_data[2])
        threading.Thread(target=say, args=(TTS_text,)).start()
  ```
  <br>
  
<h6>    
  위에 언급한 3가지 코드를 중심으로 바코드 인식이 진행되며, 인식되는 상황에 맞게 TTS를 넣어 시각장애인들이 인식된 물건의 정보를 귀로 들을 수 있도록 설정했습니다.  
</h6>
<br><br>
  
  
### Dangerous Elements Notification
#### <ul> <li> 구축 환경 : Python 3.7 </li> </ul>
-----------------------------------------------------------------------------------------------------------------------------
<div align = 'center'>
  <img style = "width : 850px" src = 'https://i.esdrop.com/d/f/CcSudjZ5R8/yYsoH7Qx2C.png'>
</div>
<h6>
  위험물 감지는 'Yolov7'을 기반으로 제작되었습니다. <br><br>
  실시간 감지를 위해 Pre-Trained Model 중에서 'Yolov7s.pt' 모델을 사용하여 감지를 실시하였으며,<br><br>
</h6>
  
  ```python
  def Distance_Measurement(w, h):
    distance_inch = round((((2 * 3.14 * 180) / ((w + h) * 360)) * 1000) + 3, 1)
    distance_cm = round(distance_inch / 2.54)
    return distance_cm
  ```
   ```python
    if save_img or view_img:  # Add bbox to image
        width = round(int(xyxy[2] - xyxy[0]) / 18, 1)
        height = round(int(xyxy[3] - xyxy[1]) / 18, 1)
        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
        print(xywh[:])
        dist = Distance_Measurement(width, height)
        label = f'{names[int(cls)]} {conf:.2f} {dist:.1f}cm'
        plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=1)
        if dist <= 100:
            overlist.append(names[int(cls)])
 ```
 <br>
<h6>
  단측카메라를 사용하기 때문에, 깊이 데이터에 대한 정보 습득과 학습을 진행할 수 없어 물체의 크기의 변화를 기준으로 거리를 예측하는 계산식을 넣어,<br><br>
  감지된 물체가 어느 정도의 거리에 있는지를 판단할 수 있도록 했습니다.<br><br>
</h6>
<br><br>

- - -
<div align = "center">
<h4> 💽Tech Stack 💽 </h4>
🚋 Plaforms & Languages 💬
<br><br>
<img src = "https://img.shields.io/static/v1?label=Python&message=v3.7&color=red">
<img src = "https://img.shields.io/static/v1?label=Matplotlib&message=3.5.3&color=yellow">
<br>
<img src = "https://img.shields.io/static/v1?label=Numpy&message=1.21.6&color=green">
<img src = "https://img.shields.io/static/v1?label=opencv&message=4.5.5.628&color=blue">
<img src = "https://img.shields.io/static/v1?label=Pandas&message=1.1.5&color=navy">
<img src = "https://img.shields.io/static/v1?label=Torch&message=1.13.1&color=purple">
</div>
