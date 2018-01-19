#!/usr/bin/env python2.7

import string,PyPDF2
freq={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}


def calc_freq(text):
	for s in text.lower():
		if s>='a' and s<='z':
			freq[s] = freq[s] + 1;
			#print s
def main():

	# with open('test','rb') as f:
	# 	text = f.read()
	# total = 0
#creating a pdf file object
	pdfFileObj = open('file', 'rb') #file: any big pdf
 
# creating a pdf reader object
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# printing number of pages in pdf file
	num_of_pages = pdfReader.numPages
 
	
 	total = 0
# extracting text 
	for i in range(num_of_pages):
		pageObj = pdfReader.getPage(i)
		calc_freq(pageObj.extractText())

	#calc_freq(text)
		
	for s in freq.keys():
		total = total + freq[s]

	for s in freq.keys():
		freq[s] = round(float(freq[s])/total,4)
	
	print freq
# closing the pdf file object
	#pdfFileObj.close()

if __name__ == '__main__':
	main()