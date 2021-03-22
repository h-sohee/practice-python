import pandas as pd

# 키, 몸무게, 유현 데이터프레임 생성하기
tbl = pd.DataFrame({
    "weight": [80.0, 60.4, 65.6, 45.9, 51.2],
    "height": [170, 180, 155, 143, 154],
    "type": ["f", "n", "n", "t", "t"]
})

# 몸무게 목록 추출하기 -> Series
print("몸무게 목록")
print(tbl["weight"])

# 몸무게와 키 목록 추가하기 -> DataFrame
print("키와 몸무게 목록")
print(tbl[["weight", "height"]])

