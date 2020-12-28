import urllib.request
import time

# 다운받을 이미지 url
url = "http://sharehub.kr/newShareHub/upload/gongu/18/2018/01/A1420180129113124.jpg"

# time check
start = time.time()

# 이미지 요청 및 다운로드
urllib.request.urlretrieve(url, "test.jpg")

# 이미지 다운로드 시간 체크
print(time.time() - start)

# 저장 된 이미지 확인
img = Image.open("test.jpg")