"""
Anuwat Khongchuai IT431 ID:273
"""
def FindLenAndNumberElements(text):
	count_num = 0
	text_len = len(text)
	num_pattern = ['0','1','2','3','4','5','6','7','8','9']
	for i in range(0,len(text)):
		for j in range(0,len(num_pattern)):
			if text[i] == num_pattern[j]:
				count_num=count_num+1
	return text_len, count_num


text = input("Enter String : ")
text_len, count_num = FindLenAndNumberElements(text)

print("Text length is : "+str(text_len)+" || ""Found "+str(count_num)+" number elements..")