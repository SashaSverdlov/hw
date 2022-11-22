from datetime import datetime
def timer(funk):
    def inner(*args, **kwargs):
        start = datetime.now()
        res = funk(*args, **kwargs)
        time = datetime.now() - start
        print(time)
        return res
    return inner

@timer
def funk(n):
   pr = 1
   for i in range (1, n+1):
       pr = pr*i
   print (pr)
funk(19999)

@timer
def myfunk(n):
   if n == 1:
       return n
   else:
       return n*myfunk(n-1)
funk(19999)