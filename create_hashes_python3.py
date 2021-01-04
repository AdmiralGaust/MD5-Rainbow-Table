#!/usr/bin/python3

import hashlib
from sys import argv

if len(argv)<=1:
	print("[+] Usage: ./create_hashes.py [MD5| SHA1| SHA256| SHA512]")
	exit(0)

hashing_algo=argv[1]

filename="hash-{0}.txt".format(hashing_algo)


def md5_hash_generate():
	table = open(filename,'wb')
	with open('/usr/share/wordlists/rockyou.txt','rb') as f:
		words = f.readlines()
		print("Generating Hashes...")
		for i in words:
			text = i.strip()
			hash = hashlib.md5(text).hexdigest().encode() + ' : '.encode() + text + '\n'.encode()
			table.write(hash)
	table.close()

def sha1_hash_generate():
	table = open(filename,'wb')
	with open('/usr/share/wordlists/rockyou.txt','rb') as f:
		words = f.readlines()
		print("Generating Hashes...")
		for i in words:
			text = i.strip()
			hash = hashlib.sha1(text).hexdigest().encode() + ' : '.encode() + text + '\n'.encode()
			table.write(hash)
	table.close()

def sha256_hash_generate():
	table = open(filename,'wb')
	with open('/usr/share/wordlists/rockyou.txt','rb') as f:
		words = f.readlines()
		print("Generating Hashes...")
		for i in words:
			text = i.strip()
			hash = hashlib.sha256(text).hexdigest().encode() + ' : '.encode() + text + '\n'.encode()
			table.write(hash)
	table.close()

def sha512_hash_generate():
	table = open(filename,'wb')
	with open('/usr/share/wordlists/rockyou.txt','rb') as f:
		words = f.readlines()
		print("Generating Hashes...")
		for i in words:
			text = i.strip()
			hash = hashlib.sha512(text).hexdigest().encode() + ' : '.encode() + text + '\n'.encode()
			table.write(hash)
	table.close()

if __name__=="__main__":

	if hashing_algo.strip().lower()=='md5':
		md5_hash_generate()
	elif hashing_algo.strip().lower()=='sha1':
		sha1_hash_generate()
	elif hashing_algo.strip().lower()=='sha256':
		sha256_hash_generate()
	elif hashing_algo.strip().lower()=='sha512':
		sha512_hash_generate()
	else:
		print("[-] Not implemented yet...")

