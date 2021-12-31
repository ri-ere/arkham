#pip install urlopen
#pip install beautifulsoup4
#pip install lxml
#pip install pillow PIL의 다른 이름?
#pip
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://ko.arkhamdb.com/card/01033")#"https://ko.arkhamdb.com/card/__code__" + code 로 검색
bsObject = BeautifulSoup(html, "lxml", from_encoding='utf-8')

#데이터 검색 및 출력
cardData = bsObject.select('div.col-sm-7')
print(cardData)

#HTML코드로 된 데이터 정제
textData = "text"

#크롤한 데이터 텍스트 파일로 저장 - 데이터 정제X
cardTextFile = open('./cardTextData.txt', 'w', encoding = 'utf-8')
cardTextFile.write(textData)
cardTextFile.close()

#텍스트 파일을 이미지 파일로 저장하기 위한 함수 선언부
from PIL import Image, ImageDraw, ImageFont
import textwrap
def makeImage(txt):
    #이미지 크기
    W = 640
    H = 640
    bgColor = 'rgb(214, 230, 245)' #배경 색
    #폰트
    font = ImageFont.truetype('F:/python/Arkham/SCE_2.0.1/Saves/fontClovaNanumGardenofTree.ttf', size=20)#폰트 위치, 폰트 크기
    fontColor = 'rgb(0, 0, 0)' #폰트 색
    image =Image.new('RGB', (W, H), color = bgColor)
    draw = ImageDraw.Draw(image)
    lines = textwrap.wrap(txt, width=40)#텍스트 최대 길이 조정
    #텍스트 시작 지점
    xTxt = 50
    yTxt = 50
    #한줄씩 내용 작성
    for line in lines:
        width, height = font.getsize(line)
        draw.text((xTxt, yTxt), line, font=font, fill=fontColor)
        yTxt += height#글씨 높이 조정 
    image.save('cardImgFile.png'.format(txt))

#텍스트 파일을 이미지 파일로 저장
cardTextFile = open('./cardTextData.txt', 'r', encoding = 'utf-8')
line = cardTextFile.readline()
print(line)
makeImage(line)
cardTextFile.close()
