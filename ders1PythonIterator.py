liste=[1,1,2,3,4]
#for i in liste: #liste bir iterable objedir. elemanlara tek tek ulasmayi saglar.
    #print(i)

iterator=iter(liste)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

while True:
    try:
        element=next(iterator)
        print(element)
    except StopIteration:
        break
    finally:
        print('dongu calisti')

