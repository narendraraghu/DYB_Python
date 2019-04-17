import requests
r = requests.get("https://google.co.in")
print(r.headers) # headers as a dict
print(r.status_code) # 200
print(r.content) # body
print("Encoding "+r.encoding) # body
r.close()