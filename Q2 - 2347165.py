#1
Age=[23,55,22,78,80,33,22]
for x in Age:
    if x%3==0:
        print(x,"Is Divisible by 3")
    else:
        print(x,"Is Not Divisble by 3")

#a.
s=[]
for x in Age:
    if x%2==0:
        v=x*x
    else:
        continue
    s.append(v)
print(s)



#b.
sum=0
i=[]
for x in Age:
    if x%2==0:
        sum+=x
print(sum,"Is the Sum of all Even Numbers In the List Age")


#c.
print(str(Age))
l=list(set(Age))
print(str(l))

#2.
t={'Virat Kohli':'5 November 1988','Umesh Yadav':'25 October 1987','Manish Pandey':'10 September 1989','Rohit Sharma':'30 April 1987','Ravindra Jadeja':'6 December 1988','Hardik Pandya':'11 October 1993'}
def birthDate(x):
    g=t.keys()
    if x in g:
        print(t[x])
    else:
        print("Not in Dictionary")
x=str(input("Enter the Name"))
birthDate(x)

