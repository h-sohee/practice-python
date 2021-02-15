import urllib.request as request
import urllib.parse as parse
API = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

# 매개변수를 URL 인코딩합니다. --- (※1)
values = {
    'stdId': '108'
}
params = parse.urlencode(values)

# 요천 전용 URL 을 생성합니다. --- (※2)
url = API + "?" + params
print('url=', url)

# 다운로드합니다. --- (※3)
data = request.urlopen(url).read()
text = data.decode('utf-8')
print(text)


