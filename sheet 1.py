l= [386,462, 47, 418, 907, 344, 236, 375, 823, 566, 597,978,328,615,953,345,399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,742, 717, 958,743, 527]
for x in l:
    if x== 237:
        print()
        break;
    elif x%2==0:
        print(x)
        
## ques 7##


def color_set():    
  a = []
color_list_1 = ["White","Black","Red"]    
color_list_2 = ["Red", "Green"]    
a = set(color_list_1 + color_list_2)           
for n in a:        
  if n in color_list_2:            
     c = set(a - set(color_list_2))       # set of set 'a' - set of list,( color_list_2  )         
print (c)

##ques
n = int(input('enter the value'))
temp =str(n)
t1 = temp +temp
t2 = temp+ temp+temp
l = n+ int(t1)+int(t2)
print(l)
###ques11###
a = input("Input words: ")
a_list = a.split(",")
a_list.sort()
print((', ').join(a_list)
###ques12###
marks = {'Sally': 57, 'Rahul': 87, 'Kishore': 88, 'Vidhya': 67, 'Raakhi': 79}
highest = max(marks.values())
n = [k for k, v in marks.items() if v == highest]

if len(n)==1:
    print(n[0],' got the highest mark')
elif len(n)==2:
    print(n[0],'and',n[1],' got the highest mark')
elif len(n)==3:
    print(n[0],',',n[1],'and',n[2],' got the highest mark')
###ques 13###
s = input("Input a sentence")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)
####ques15####
n = int(input())
a = [i for i in range(0, n) if (i % 7 == 0)]###divisible by 7
print(a)

def b(n):       ###checking the divisibility by 7
    for i in range(n):
        if i % 7 == 0:
            value = True
        else:
            value = False
        print(i, value)

b(n)
####ques16####
    
