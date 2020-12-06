import sys

str = sys.argv
n=0
uppercase = False 
EnglishCheck = False
NumberCheck = False
fail = False
try:
    n=len(str[1])
except:
    print("請輸入字串")

if n<8:
    print("長度小於8")
    sys.exit(0)
elif n>16:
    print("長度大於16")
    sys.exit(0)    

list1 =list(str[1])
for i in range(0,n):
    if 65 <= ord(list1[i]) <= 90:
        uppercase = True
        EnglishCheck = True
    if 97 <= ord(list1[i]) <=122:
        EnglishCheck = True
    if 48 <= ord(list1[i]) <=57:
        NumberCheck = True
       
if EnglishCheck == False:
    print("缺少英文")
elif uppercase == False:
    print("請輸入至少一個大寫英文")
    sys.exit(0) 
elif NumberCheck == False:
    print("缺少數字")
    sys.exit(0) 

    
temp = list1[0]
for i in range(1,n):
    if ord(temp)+1 == ord(list1[i]):
        continuous = True
        if 65 <= ord(list1[i]) <=90:
            print("大寫英文不可連續")
            fail = True
        elif 97 <= ord(list1[i]) <=122:
            print("小寫英文不可連續")
            fail = True
        elif 48 <= ord(list1[i]) <=57:
            print("數字不可連續")
            fail = True    
        
    else:
        continuous = False 
    temp = list1[i]
if fail == True:
    sys.exit(0)

if continuous == False and uppercase == True and EnglishCheck == True and NumberCheck == True:
    print("success")
