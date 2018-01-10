from timeit import Timer


def da_yin():
    print('hello ')
timer = Timer('da_yin()', 'from __main__ import da_yin')
use_time = timer.timeit(number=5)
print('Use time: ', use_time)

