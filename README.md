# ![icon](img/icon.png)newstab-stamper![icon](img/icon.png)

1. sampledata 폴더의 pdf 파일 상단에 하기와 같은 형태로 스탬프(pdf 텍스트 추가형태) 날인

**3000C-xxx-yyy**

> 3000C 고정

> xxx : 각 pdf 폴더 이름 앞 숫자 (ex. 030. Pricing The next frontier of value creation.pdf 의 경우 xxx=030)

> yyy : 각 pdf폴더의 해당하는 페이지 수 (ex: 030. 파일의 1 페이지 yyy=1)

2. 코드 한번 돌릴 때 여러 파일을 동시에 변환 가능하게

3. 스탬프의 위치는 우측 상단 고정, 크기는 폰트 사이즈 15-20pt 정도로 눈에 잘 들어오는 정도면 된다.

![sampleimage](img/example.png)

## Usage 

Run below command before executing newstab_stamper for installing required packages.

```
pip install -r requirements.txt
```

Input is a path argument, for the original documents.

```
python newstab_stamper.py --origin_path /PATH/OF/ORIGINAL/FILES
```

## Release note

https://www.notion.so/beeb3b510bfd4d14add28acb61fc2ffa
