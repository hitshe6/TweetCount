#CODE BY HITESH PRAJAPAI

from collections import Counter

x = int(input("Enter number of InputSet:"))
cnt = 0
tweet_list = []

while cnt < x:
	num = int(input("Number Of tweets:"))
	count = 0
	while count <num:
		t_name = str(input())
		tweet_list.append(t_name)
		count +=1
	cnt +=1

new_name=[]
cnt_name = []
for i in tweet_list:
	new_name.append(i.split()[0])
print(new_name)

x = Counter(new_name)
y = x.values()
z = x.keys()

for key, value in sorted(x.items(),key=lambda item: item[1]):
	if value == 1:
		continue
	print(key,'',value)



	
