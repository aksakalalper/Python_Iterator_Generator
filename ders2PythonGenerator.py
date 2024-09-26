
#bellek uzerinde yer isgal etmeyen bir yapi insa edilir. tek seferlik goruntuleme yapilir.
def cube():
    for i in range(5):
        yield i**3

generator=cube()
iterator=iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


for i in cube():
    print (i)

