# /usr/bin/env python3

# 라이브러리를 읽어 들입니다. --- (※1)
import sys
import urllib.request as request
import urllib.parse as parse

# 명령줄 매개변수 추출 --- (※2)
if len(sys.argv) <= 1:
    print("USAGE: download-forecast-arvg <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]

# 매개변수를 URL 인코딩합니다. --- (※3)
API = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stdId': regionNumber
}

params = parse.urlencode(values)
url = API + "?" + params
print('url=', url)

# 다운로드합니다. --- (※4)
data = request.urlopen(url).read()
text = data.decode('utf-8')
print(text)

