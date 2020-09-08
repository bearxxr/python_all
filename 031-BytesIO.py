# 以字节形式编写代码
from io import BytesIO

b = BytesIO()

b.write('中文'.encode('utf-8'))


print(b.getvalue())
