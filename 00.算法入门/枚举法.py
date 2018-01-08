import time
start_time = time.time()
# for a in range(0,1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a ** 2 + b ** 2 == c ** 2 and a + b + c ==1000:
#                 print(a, b, c)
# end_time = time.time()
# print("use time:", end_time - start_time)

"""
0 500 500
200 375 425
375 200 425
500 0 500
use time: 1697.7197799682617
"""

for a in range(1001):
    for b in range(1001-a):
        c = 1000-a-b
        if a**2 + b**2 == c**2 and a+b+c == 1000:
            print('(a,b,c): {}'.format((a, b, c)))

end_time = time.time()
print('Use time: {}s'.format(end_time-start_time))
