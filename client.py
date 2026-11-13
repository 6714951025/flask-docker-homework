import requests

URL = "http://localhost:5000/"

# ทดสอบ GET: ขอหน้าเว็บฟอร์ม
r = requests.get(URL)
print("GET status:", r.status_code)
print(r.text)

# ทดสอบ POST: ส่งข้อความไปที่ server (ชื่อ 'message' ต้องตรงกับใน app.py)
r = requests.post(URL, data={"message": "Hello from client.py"})
print("POST status:", r.status_code)
print(r.text)
