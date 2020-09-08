# 向内存中写入数据
from io import StringIO

s = StringIO()

s.write('Hello')
s.write(' ')
s.write('World')

print(s.getvalue())
