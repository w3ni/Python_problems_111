#  *args function

def summ_all(*args):
    print(args)
    for i in args:
        print(i*2)
    return sum(args)

print(summ_all(1,2,3,4,5,6)) 
