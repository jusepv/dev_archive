def test(t):
    assert type(t) is int, '정수가 아닌 값이 있네'

list = [1,3,4,5,3.3, 5,7,8.6]

for i in list:
    test(i)

