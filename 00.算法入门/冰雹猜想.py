# 70年代中期，美国各所名牌大学校园内，人们都像发疯一般，
# 夜以继日，废寝忘食地玩弄一种数学游戏。这个游戏十分简单
# ：任意写出一个自然数N，并且按照以下的规律进行变换：
# 如果是个奇数，则下一步变成3N+1。
# 如果是个偶数，则下一步变成N/2。


def ice_boll(num):
    if num == 1:
        print('-------->Finally number is 1')
        return 1
    elif not num % 2:
        print('-------->even number: %d' % (num/2))
        return ice_boll(num/2)
    else:
        print('-------->odd number: %d' % (3*num+1))
        return ice_boll(3*num+1)
# ice_boll(9)


# 27 max_num
def tributary(num):
    str1 = str((num-1)/3)
    if str1.isdigit():
        return print('FInd max number： %d' % num)
    else:
        print("-------->Number can't been exact division :%s" % str1)
        return tributary(2*num)

tributary(27)
