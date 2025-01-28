from matplotlib import pyplot as plt

def num2words(num):
	under_20 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
	tens = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
	above_100 = {100: 'Hundred',1000:'Thousand', 1000000:'Million', 1000000000:'Billion'}
 
	if num < 20:
		 return under_20[num]
	
	if num < 100:
		return tens[(int)(num/10)-2] + ('' if num%10==0 else ' ' + under_20[num%10])
 
	# find the appropriate pivot - 'Million' in 3,603,550, or 'Thousand' in 603,550
	pivot = max([key for key in above_100.keys() if key <= num])
 
	return num2words((int)(num/pivot)) + ' ' + above_100[pivot] + ('' if num%pivot==0 else ' ' + num2words(num%pivot))

def word_score(num):
    word_str = num2words(num).lower()
    total = 0
    for c in word_str:
        if c == ' ':
            continue
        else:
            total += ord(c)-96
    return total
    
nums = range(400)
scores = []
max_val = 0
for i in nums:
    s = word_score(i)
    scores.append(s)
    if s >= i:
        max_val = i

print(i)
plt.plot(nums, nums)
plt.plot(nums, scores)
plt.show()