import operator
def most_frequent(s):
    d={}
    for i in s:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    d=dict(sorted(d.items(),key=operator.itemgetter(0)))
    return d
s=input("please enter a string")
new=most_frequent(s)
print(new)
