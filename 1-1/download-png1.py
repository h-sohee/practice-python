# 라이브러리 읽어 들이기 --- (※1)
import urllib.request

# URL 과 저장 경로 저장하기
url = "http://uta.pw/shodou/img/28/214.png"
savename = 'test.png'

# 다운로드 --- (※2)
urllib.request.urlretrieve(url, savename)
print('저장되었습니다...!')


