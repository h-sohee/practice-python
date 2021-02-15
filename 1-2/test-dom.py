from bs4 import BeautifulSoup

html = """
<html><body>
    <p><a href='a.html'>test</a></p>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")

# 분석이 제대로 됐는지 확인하기 --- (※1)
soup.prettify()

# <a> 태그를 변수 a에 할당
a = soup.p.a

# attrs 속성의 자료형 확인 --- (※2)
print(type(a.attrs))

# href 속성이 있는지 확인
print('href' in a.attrs)

# href 속성값 확인
print(a['href'])


