#importing modules
from time import time
import pandas 
from dateutil import parser
from datetime import datetime

#importing the dataset from the Excel files
df_config = pandas.read_excel("/home/rohith_ubuntu/Desktop/internshala/Savings-config.xlsx")
df_balance= pandas.read_excel("/home/rohith_ubuntu/Desktop/internshala/Account-config.xlsx")

#creating the dictionary to store all the data of the each user

dic={}

for i in range(len(df_config)):
    temp_loop_arr=list(df_config.iloc[i])
    balance=(list(df_balance.iloc[i])[1])
    temp_loop_arr.append(balance)
    dic[temp_loop_arr[0]]=temp_loop_arr[1:]
    print(datetime.timestamp(dic[temp_loop_arr[0]][2]))
print(dic)
flag=True
while(flag):
    print("\n","Input the time interval")
    # inp=input()
    inp="5th march 2022"
    inp=inp.split(" ")
    date=parser.parse("-".join(inp))
    
    for i in dic.keys():
        diff=abs(datetime.timestamp(dic[i][2])-datetime.timestamp(date))
        days_diff=(diff//86400)
        print( str(i) +"   " + str(days_diff))
        fin_modified=dic[i][3]
        change=dic[i][0]
        if(dic[i][1]=='monthly'):
            frequency=30
        if(dic[i][1]=='weekly'):
            frequency=7
        if(dic[i][1]=='daily'):
            frequency=1
        # days_diff-=frequency
        while(dic[i][3]>=change and days_diff>=frequency):
            # print("subtractingg   ",change*(days_diff//frequency))
            dic[i][3]-=change
            days_diff-=frequency
    flag=False
print(dic)