results10=open('file10results.txt','w')

results100=open('file100results.txt','w')

file10=open('10Random.txt','r')
line10=file10.read()
file100=open('100Random.txt','r')
line100=file100.read()
#Range
max=0
min=1000000000000 
for item in line10.split():
    #print("Item: ",item)
    num=int(item)
    if num<min:
        min=int(item)
    if num>max:
        max=int(item)
            
range=(max-min)
print('Range of file 10 is',range)
results10.write('Range:' + str(range)+'\n')   
    
for item in line100.split():
    num=int(item)
    if num<min:
        min=int(item)
    if num>max:
        max=int(item)
            
range=(max-min)
print('Range of file 100 is',range)
results100.write('Range:' + str(range)+'\n')

#Frequency
print('\nFile10:')
numList=[]
allNum10=[]

for item in line10.split():
    #print("Item 2: ",item)
    allNum10.append(int(item))
    if int(item) not in numList: 
        numList.append(int(item))
            
for item in numList:
    results10=open('file10results.txt','a')
    #print('Frequency of',item,':',allNum10.count(item))
    print()
    results10.write('Frequency of ' + str(item) +':' + str(allNum10.count(item))+'\n')

print('\nFile100:')   
numList=[]
allNum100=[]
for item in line100.split():
    allNum100.append(int(item))
    if int(item) not in numList: 
        numList.append(int(item))
        
for item in numList:
    #print('Frequency of',item,':',allNum100.count(item))
    results100.write('Frequency of ' + str(item) +':' + str(allNum100.count(item))+'\n')

#mean
number=[]
addedNum=0
count10=0
    
for item in line10.split():
    addedNum= (addedNum+int(item))
    count10=count10+1

mean= (addedNum/count10)
mean=str(mean)
results10.write('Mean of file10:'+mean)
number=[]
addedNum=0
count100=0
for item in line100.split():
    addedNum= (addedNum+int(item))
    count100=count100+1

mean=(addedNum/count100)
mean=str(mean)
results100.write('Mean of file100:'+mean)
print()
#median
allNum10.sort()
if len(allNum10)%2>0:
    middle=int(len(allNum10)/2)
    results10.write(allNum10[middle])
else:
    middle=int(len(allNum10)/2)
    median=(allNum100[middle]+allNum100[middle-1])/2
    results10.write('\nMedian of file10:'+str(median))
                                                                              
allNum100.sort()
if len(allNum100)%2>0:
    middle=int(len(allNum100)/2)
    results100.write(allNum100[middle])
else:
    middle=int(len(allNum100)/2)
    median=(allNum100[middle]+allNum100[middle-1])/2
    results100.write('\nMedian of file100:'+str(median))

print()   
#mode
current=0
previous=0
highestCount=0
modeList=[]
for number in allNum10:
    if number==previous:
        continue
    count=allNum10.count(number)
    if count>highestCount:
        modeList.clear()
        modeList.append(number)
        highestCount=count
    elif count==highestCount:
        modeList.append(number)         
    previous=number
results10.write('\nMode of file10:'+str(modeList))

current=0
previous=0
highestCount=0
modeList=[]
for number in allNum100:
    if number==previous:
        continue
    count=allNum100.count(number)
    if count>highestCount:
        modeList.clear()
        modeList.append(number)
        highestCount=count
    elif count==highestCount:
        modeList.append(number)         
    previous=number
results100.write('\nMode of file100:'+str(modeList))

results10.close()
results100.close()