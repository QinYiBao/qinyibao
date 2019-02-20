#daydayupq3.py
dayup=1
dayfactor=0.01
for i in range(365):
    if i % 7 in [0,6]:
       dayup=dayup*(1-dayfactor)
    else:
       dayup=dayup*(1+dayfactor)
print("工作日的力量是:{:.2f}".format(dayup))
