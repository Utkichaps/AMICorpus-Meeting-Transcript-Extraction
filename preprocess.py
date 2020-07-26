import re
mydict = {}

'''
Make sure the file_list size and speakers size is the same. The speaker list should also have the same order of the speakers
that is being defined in the file_list list.
'''
file_list = ['EN2001a/EN2001aA.txt','EN2001a/EN2001aB.txt','EN2001a/EN2001aC.txt','EN2001a/EN2001aD.txt','EN2001a/EN2001aE.txt']
speakers = ['A','B','C','D','E']

'''
Here the preprocessing of the text is done according to the timestamp and it is
added to a dictionary. This contains the timestamp as the key and the dialogue
as the item.
'''

for n in range(len(file_list)):

	file = open(file_list[n], 'r')
	lines = file.readlines()

	for i in lines:
		i = i.split()
		if len(i) != 0 and i[0] == '<w' and len(i) == 4:
			poi = i[3]
			num = poi[poi.find('\"')+1:]
			num = num[:num.find('\"')]
			key = float(num)		
			value = poi[poi.find('>')+1:poi.find('<')]	
			value = speakers[n]+':'+value
			mydict[key] = value
		file.close()

'''
Once the preprocessing is done, this formats it into a conversational style
discourse.
'''

mydict_sort = sorted(mydict)

insert_lines = []

for i in mydict_sort:
	first = mydict[i].split(':')[0]
	break

input_str = first+":"
for i in mydict_sort:
	spl = mydict[i].split(':')
	if spl[0] == first:
		input_str += " " + spl[1]
	else:
		first = spl[0]
		insert_lines.append(input_str + ".\n")
		input_str = first+":"+spl[1]

'''
As lot of cross talk is happening on alternate lines I eliminate the cross talk existing on those lines

By increasing the following split_parameter variable, you will reduce the chances of cross talk but will 
increase the chances of longer sentences for each speaker which could, in context, be different sentences.
'''
split_parameter = 4  
i = 0  
j = 0
while i != len(insert_lines)-3:
	a = re.split('\.|\:',insert_lines[i])
	b = re.split('\.|\:',insert_lines[i+2])
	if a[0] == b[0]:		
		if len(a[1].split(' ')) <= split_parameter and len(b[1].split(' ')) <= split_parameter:
			insert_lines[i] = a[0] + ':' + a[1] + ' ' + b[1] + '.\n'
			del insert_lines[i+2]
	i+=1
	
	#This code is to eliminate secondary cross-talk but it sometimes negates primary cross-talk	
	a = re.split('\.|\:',insert_lines[j])
	b = re.split('\.|\:',insert_lines[j+1])
	if a[0] == b[0]:
		if len(a[1].split(' ')) <= split_parameter and len(b[1].split(' ')) <= split_parameter:
			insert_lines[i] = a[0] + ':' + a[1] + ' ' + b[1] + '.\n'
			del insert_lines[j+1]
	j+=1
	
	




#The output file you want to write the final conversation to
file = open("EN2001a.txt","w")
file.writelines(insert_lines)
file.close()
print("Transcription done!")