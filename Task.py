def lfusize(cachesize):
    def lfu(f):
        lfu.cache = {}
        lfu.quantityuse = {}
        def wrapper(a):
            if len(lfu.cache) + 1 > cachesize:
                cachelist = list(lfu.quantityuse.items())
                cachelist.sort(key=lambda i: i[1])
                delval = cachelist[0][0]
                print('deleting from cache :{}'.format(delval))
                lfu.cache.pop(delval)
                lfu.quantityuse.pop(delval)
            if a not in lfu.cache:
                r = f(a)
                lfu.cache[a] = r
                lfu.quantityuse[a] = 1
                print(lfu.cache)
                print(lfu.quantityuse)
            else:
                print('cache use', lfu.cache[a])
                lfu.quantityuse[a] += 1
                print(lfu.cache)
                print(lfu.quantityuse)
            return lfu.cache.get(a)
        return wrapper
    return lfu


@lfusize(3)
def double(a):
    return a + a


double(10)
double(10)
double(10)
double(20)
double(20)
double(30)
double(40)
double(20)
double(30)
double(40)
double(10)
double(20)
double(30)
double(40)
