#python中的yield
#Python中带有yield的函数会被解释器视为一个generator，在迭代的过程之中会自动继承上一次迭代的的值
#功能上还有点类似于return
# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b  # 使用 yield
#         # print b
#         a, b = b, a + b
#         n = n + 1
#
#
# for n in fab(5):
#     print(n)
def pluse(num):
    n,a,b = 0,1,0
    while n<num:
        yield b
        b+=a
        a+=1
        n+=1


for n in pluse(5):
    print(n)
