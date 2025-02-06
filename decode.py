from django.conf import settings
from django.core import signing
import requests


host="127.0.0.1:8000"
res=requests.get(f"http://{host}/")

session_cookie=res.cookies['sessionid']
print("session:", session_cookie)

settings.configure(SECRET_KEY="django-insecure-rut0b*&9m+o0-uh&3zp3x9uh_3421og(96+la=x7-ry")

signed_value = (
    session_cookie
)

try:
    # Django의 쿠키 기반 세션 복호화 시, 기본 salt를 함께 지정
    data = signing.loads(signed_value, salt="django.contrib.sessions.backends.signed_cookies")
    print("복호화된 데이터:", data)
except Exception as e:
    print("복호화에 실패:", e)
