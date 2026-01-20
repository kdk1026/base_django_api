# Python Django API
#### [Python 유틸] (https://github.com/kdk1026/python_util)

## 가상환경 생성
```
python -m venv venv
```

<br />

## 가상환경 활성화
```
(Windows)
venv\Scripts\activate

(Linux/Mac)
source venv/bin/activate
```

<br />

## VS Code 인터프리터 설정 (자동으로 가상환경 켜기)
1. `Ctrl + Shift + P` -> `Python: Select Interpreter` 선택
2. 리스트에서 `./venv/Scripts/activate` 선택
3. 터미널 새로 열기 `Ctrl + Shift + ~`

<br />

## 설치된 라이브러리 목록 추출
#### - Git에 올리는 경우
```
pip freeze > requirements.txt
```

<br />

## 라이브러리 한 번에 설치
#### - Git에서 내려받는 경우
```
pip install -r requirements.txt
```

<br /><br />

## Django 설치
```
pip instal django
```

<br />

## 프로젝트 만들기
```
django-admin startproject config .
```

<br />

## 서버 실행
```
python manage.py runserver
```

<br />

## 앱 생성
```
mkdir apps/sample
python manage.py startapp sample ./apps/sample
```

## apps\sample\apps.py 수정
```
# 수정 전
class SampleConfig(AppConfig):
    name = 'sample'

# 수정 후 (경로를 포함해야 함)
class SampleConfig(AppConfig):
    name = 'apps.sample'
```