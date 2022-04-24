class A:
    def func(self):
        return 'A.func'


class B(A):
    def func(self):
        return 'B.func'


class C(A):
    def func(self):
        return 'C.func'


class D(B, C):
    pass

if __name__ == '__main__':
    O = D()
    print('working')
