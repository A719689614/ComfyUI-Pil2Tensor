import base64
f = open(r'D:\AC Center\Button.png','rb')
res = f.read()
s = base64.b64encode(res)
f.close()

print(s)