import base64
import re
import zlib

def func(code):
    return zlib.decompress(base64.b64decode(code[::-1]))


code = b"exec((_)(b'ERJZpiLQ4NBZLYYZRi5t9puZ6'))"


regex = re.compile(rb"^exec\(\(_\)\(b'(.+)'\)\)$")
while True:
    result = regex.search(code)
    if not result:
        break 
    code = func(result.group(1))
print(code.decode('utf-8'))
