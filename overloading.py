
class OverLoading:
    def __init__(self,a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

ob1 = OverLoading(1)
ob2 = OverLoading(2)

ob3 = OverLoading('Hello,')
ob4 = OverLoading("THis is new meeee")

print(ob1 + ob2)


print(ob3 + ob4)




