# def foo(s):
#     n = int(s)
#     print(' >>> n =%d' % n)
#     return 10 / n


# def main():
#     foo('0')


# main()

# 断言
def foo(s):
    n = int(s)
    # 如果是False,就会抛出'n is zero!'
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('0')

main()


