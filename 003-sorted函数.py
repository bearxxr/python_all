# 排序函数
# 重要的是reverse属性


a = [1, 99, 6, 8, 44, -58, -11, -33]

print(sorted(a, key=abs))
print(sorted(a, reverse=True))

b = ['Lisa', 'Bob', 'Adam', 'Bart']
print(sorted(b))
# 全部忽略首字母大小写
print(sorted(b, key=str.lower))

x = (1,)
print(list(x)[0])
