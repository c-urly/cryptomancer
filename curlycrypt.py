#!/usr/bin/env python2.7

import random,string
from random import Random
import binascii

class Hash(object):
	"""docstring for Hash"""
	def __init__(self):
		pass
		#super(Hash, self).__init__()
		#self.arg = arg
	def base64decode(b64string):
		pass

	def base64encode(raw_data):
		raw_bytes = binascii.a2b_hex(raw_data)	


class caesar(object):
	"""docstring for caesar"""
	def __init__(self):
		pass

	def encrypt(self, text ):
		pass

	def hack(self, cipher_text):
		pass

	def decrypt(self, cipher_text):
		pass


		
class Affine(object):
	"""docstring for Affine""" 
	inverse=[]
	coeff1=[1,3,5,7,9,11,15,17,19,21,23,25]
	key = -1
	chi = 9999999999999
	freq = {'a': 0.0803, 'c': 0.0184, 'b': 0.0166, 'e': 0.1262, 'd': 0.0541, 'g': 0.0218, 'f': 0.0206, 'i': 0.0591, 'h': 0.0714, 'k': 0.0119, 'j': 0.0021, 'm': 0.0239, 'l': 0.0443, 'o': 0.0758, 'n': 0.0665, 'q': 0.0009, 'p': 0.0117, 's': 0.066, 'r': 0.0641, 'u': 0.0245, 't': 0.0836, 'w': 0.0267, 'v': 0.0075, 'y': 0.0213, 'x': 0.0005, 'z': 0.0005}
	cipher_freq={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

	
	def __init__(self, text):
		plain_text = self.text
		encrypt(plain_text)

	def __init__(self):
		self.inversemod()


	def chiSquare(self, cipher):

		for s in cipher:
			self.cipher_freq[s] = self.cipher_freq[s] + 1
		chi_stats = 0.0
		for i in range(26):
			alpha = string.lowercase[i]
			expected = self.freq[alpha]*len(cipher)
			actual = self.cipher_freq[alpha]
			chi_stats = chi_stats + ((actual-expected)*(actual-expected))/expected

	#print cipher +"........."+ str(chi_stats)
		return chi_stats


	def inversemod(self):
		for x in self.coeff1:
			self.inverse.append(self.Euclid(x))

	def Euclid(self, key):
		for x in range(26):
			if (x*key)%26 == 1:
				return x


	def encrypt(self, text):
		rand = Random()

		a = 5#rand.choice(self.coeff1)
		b = 10#rand.randint(0,25)

		cipher_text = ''
		for s in text.lower():
			x = string.lowercase.index(s)
			cipher_text = cipher_text+string.uppercase[(x*a+b)%26]

		return cipher_text

	def hack(self, cipher_text):
		
		plain_text = ''
		text = ''
		temp_chi = 999999999999
		for b in range(26):
			temp_cipher = ''
			for a in self.inverse:	
				temp_cipher = temp_cipher + string.lowercase[((-b)*a)%26]
				
				self.key = self.chiSquare(plain_text)
				
				if temp_chi > self.key:
					text = temp_cipher
					temp_chi = self.key
			
			if self.chi > temp_chi:
				plain_text = text
		return plain_text

	def decrypt(self, cipher_text, key):
		plain_text=''
		for s in cipher_text.lower():
			x = string.lowercase.index(s)
			a, b = self.Euclid(key[0]), key[1]
			plain_text  = plain_text + string.lowercase[((x-b)*a)%26]

		return plain_text 