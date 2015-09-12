import sys,getopt,os,math

py=sys.argv[0]
ansfile=sys.argv[1]
testfile=sys.argv[2]
target=sys.argv[3]

ans=open(ansfile)
test=open(testfile)

line1=ans.readline()
myline=line1.split('\t')
line1=myline[0]
#print(line1)
line2=test.readline()

precision=0.0
recall=0.0

count_p=0
count_right=0

count_r=0
count_all=0

counts=1

while line1:
   # line1=line1.split('\t')[0]
    if line2==target+'\n':
        if line1==target:
            count_p+=1
            count_right+=1
        else:
            count_p+=1
    if line1==target:
        if line2==target+'\n':
            count_r+=1
            count_all+=1
        else:
            count_all+=1
    
    line1=ans.readline()
    #print(line1)
    try:
        myline=line1.split('\t')
        line1=myline[0]
    except:
        line1=line1
    line2=test.readline()
    counts+=1

count_right=float(count_right)
count_p=float(count_p)
count_all=float(count_all)
precision=count_right/count_p
recall=count_r/count_all
print('For '+str(counts)+'rows:')
print('We thinks'+' '+ str(count_p) + ' is '+ str(target)+', while '+ str(count_right)+' is right')
print('All have ' + str(count_all) + ' '+target+' we recalled '+ str(count_r))
print('precision is '+ str(precision))
print('recall reate is ' + str(recall))
print(2*precision*recall/(precision+recall))


    
