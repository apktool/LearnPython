# farg, *args, **kwargs
def haha1(farg, *args):
    print('arg %s' % (farg))
    for value in args:
        print('another %s' % (value))

haha1(1,'two',3)


print('-----------')


def haha2(farg, **kwargs):
    print('arg: %s' % (farg))
    for key in kwargs:
        print('another key: %s | %s' % (key, kwargs[key]))

haha2(farg=1,myarg2='two',myarg3=3)
