class Fib:
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for i in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            L = []
            if start is None:
                start = 0
            a, b = 1, 1
            for i in range(stop):
                a, b = b, a + b
                if i >= start:
                    L.append(a)
            return L


a = Fib()
print(a[4])

print(a[2:5])
