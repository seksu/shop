# -*- coding: utf-8 -*-
########### config ############

dbAddr 	= 'localhost'
dbUser 	= 'root'
dbPass 	= ''
dbSpace = 'pos'

###############################

import os
import MySQLdb
#import PyMySQL

db = MySQLdb.connect(dbAddr,dbUser,dbPass,dbSpace)
cursor = db.cursor()

print("Welcome to Sek Su Program")
mode = '1'
total = 0;
orderList = []
engMode = False

def t2e(input):
	if(input == 'ๅ' or input == '/' or input == '-' or input == 'ภ' or input == 'ถ' or input == 'ุ' or input == 'ึ' or input == 'ค' or input == 'ต' or input == 'จ' or 
		input == 'ข' or input == 'ช' or input == 'ๆ' or input == 'ไ' or input == 'ำ' or input == 'พ' or input == 'ะ' or input == 'ั' or input == 'ี' or input == 'ร' or 
		input == 'น' or input == 'ย' or input == 'บ' or input == 'ล' or input == 'ฟ' or input == 'ห' or input == 'ก' or input == 'ด' or input == 'เ' or input == '้' or 
		input == '่' or input == 'า' or input == 'ส' or input == 'ว' or input == 'ง' or input == 'ผ' or input == 'ป' or input == 'แ' or input == 'อ' or input == 'ิ' or 
		input == 'ื' or input == 'ท' or input == 'ม' or input == 'ใ' or input == 'ฝ' or input == '+' or input == '๑' or input == '๒' or input == '๓' or input == '๔' or 
		input == 'ู' or input == '฿' or input == '๕' or input == '๖' or input == '๗' or input == '๘' or input == '๙' or input == '๐' or input == '“' or input == 'ฎ' or 
		input == 'ฑ' or input == 'ธ' or input == 'ํ' or input == '๊' or input == 'ณ' or input == 'ฯ' or input == 'ญ' or input == 'ฐ' or input == ',' or input == 'ฅ' or 
		input == 'ฤ' or input == 'ฆ' or input == 'ฏ' or input == 'โ' or input == 'ฌ' or input == '็' or input == '๋' or input == 'ษ' or input == 'ศ' or input == 'ซ' or 
		input == '.' or input == '(' or input == ')' or input == 'ฉ' or input == 'ฮ' or input == 'ฺ' or input == '์' or input == '?' or input == 'ฒ' or input == 'ฬ' or 
		input == 'ฦ' ) :
		return {
			'ๅ' : '1','/' : '2',	'-' : '3','ภ' : '4',	'ถ' : '5','ุ' : '6',	'ึ' : '7','ค' : '8',	'ต' : '9','จ' : '0',	'ข' : '-','ช' : '=',	'ๆ' : 'q','ไ' : 'w',
			'ำ' : 'e','พ' : 'r','ะ' : 't','ั' : 'y',	'ี' : 'u','ร' : 'i',	'น' : 'o','ย' : 'p',	'บ' : '[','ล' : ']',	'ฟ' : 'a','ห' : 's',	'ก' : 'd','ด' : 'f',
			'เ' : 'g','้' : 'h',	'่' : 'j','า' : 'k',	'ส' : 'l','ว' : ';',	'ง' : "'",'ผ' : 'z', 'ป' : 'x','แ' : 'c',	'อ' : 'v','ิ' : 'b',	'ื' : 'n','ท' : 'm',
			'ม' : ',','ใ' : '.', 'ฝ' : '/','+' : '!','๑' : '@','๒' : '#','๓' : '$','๔' : '%','ู' : '^','฿' : '&','๕' : '*','๖' : '(','๗' : ')','๘' : '_',
			'๙' : '+','๐' : 'Q','“' : 'W','ฎ' : 'E','ฑ' : 'R','ธ' : 'T','ํ' : 'Y','๊' : 'U','ณ' : 'I','ฯ' : 'O','ญ' : 'P','ฐ' : '{',',' : '}','ฅ' : '|',
			'ฤ' : 'A','ฆ' : 'S','ฏ' : 'D','โ' : 'F','ฌ' : 'G','็' : 'H','๋' : 'J','ษ' : 'K','ศ' : 'L','ซ' : ':','.' : '”','(' : 'Z',')' : 'X','ฉ' : 'C',
			'ฮ' : 'V','ฺ' : 'B','์' : 'N','?' : 'M','ฒ' : '<','ฬ' : '>','ฦ' : '?'
		}[input]
	else :
		return '~'+input+'`'

def e2t(input):
	global engMode
	if(input == '~'):
		engMode = True
		return ""
	if(input == '`'):
		engMode = False
		return ""
	if(engMode == False):
		return {
			'1' : 'ๅ','2' : '/','3' : '-','4' : 'ภ','5' : 'ถ','6' : 'ุ','7' : 'ึ','8' : 'ค','9' : 'ต','0' : 'จ','-' : 'ข','=' : 'ช','q' : 'ๆ','w' : 'ไ',
			'e' : 'ำ','r' : 'พ','t' : 'ะ','y' : 'ั','u' : 'ี','i' : 'ร','o' : 'น','p' : 'ย','[' : 'บ',']' : 'ล','a' : 'ฟ','s' : 'ห','d' : 'ก','f' : 'ด',	
			'g' : 'เ','h' : '้','j' : '่','k' : 'า','l' : 'ส',';' : 'ว',"'" : 'ง','z' : 'ผ','x' : 'ป','c' : 'แ','v' : 'อ','b' : 'ิ','n' : 'ื','m' : 'ท',
			',' : 'ม','.' : 'ใ','/' : 'ฝ','!' : '+','@' : '๑','#' : '๒','$' : '๓','%' : '๔','^' : 'ู','&' : '฿','*' : '๕','(' : '๖',')' : '๗','_' : '๘',
			'+' : '๙','Q' : '๐','W' : '“','E' : 'ฎ','R' : 'ฑ','T' : 'ธ','Y' : 'ํ','U' : '๊','I' : 'ณ','O' : 'ฯ','P' : 'ญ','{' : 'ฐ','}' : ',','|' : 'ฅ',
			'A' : 'ฤ','S' : 'ฆ','D' : 'ฏ','F' : 'โ','G' : 'ฌ','H' : '็','J' : '๋','K' : 'ษ','L' : 'ศ',':' : 'ซ','”' : '.','Z' : '(','X' : ')','C' : 'ฉ',
			'V' : 'ฮ','B' : 'ฺ','N' : '์','M' : '?','<' : 'ฒ','>' : 'ฬ','?' : 'ฦ'
		}[input]
	if(engMode == True):
		return input

def econvert(input):
	string = ""
	for i in input:
		string += t2e(i)
	return string

def tconvert(input):
	string = ""
	for i in input:
		string += e2t(i)
	return string

def add(barcode):
	sql = "SELECT * FROM product WHERE barcode = '%s'" % (barcode)
	#try:
	cursor.execute(sql)
	results = cursor.fetchone()
	if(results):
		print(results)
		quantity = input("Quantity : ")
		sql = "UPDATE product SET quantity = quantity + '%d' WHERE barcode = '%s'" % (int(quantity),barcode)
		try:
		   cursor.execute(sql)
		   db.commit()
		except:
			print("Quantity maybe lower than zero")
			db.rollback()			
	else:
		name 	 = input("name     : ")
		price 	 = input("Price    : ")
		quantity = input("Quantity : ")
		ename = econvert(name)
		print(ename)

		sql = "INSERT INTO product(barcode,name,price,quantity) VALUES ('%s','%s','%d',%d)" %(barcode,ename,int(price),int(quantity))
		#try:
		cursor.execute(sql)
		db.commit()
		#except:
		#	db.rollback()
	print("Add Order List")
	sql = "SELECT * FROM product WHERE barcode = '%s'" % (barcode)
	cursor.execute(sql)
	results = cursor.fetchone()
	print("Current "+tconvert(str(results[1]))+" quantity : "+str(results[3]))
	print()
	#except:
	#	print("Add Error")
	#	db.rollback()

def preSell(barcode):
	global total
	global orderList
	cursor = db.cursor()
	sqlSell = "SELECT * FROM product WHERE barcode = '%s'" % (barcode)
	try:
		cursor.execute(sqlSell)
		results = cursor.fetchone()
		print("Name : "+tconvert(str(results[1]))+"\tPrice : "+str(results[2])+"\tQuantity : "+str(results[3]))
		total = total + results[2]
		print("Total price : "+str(total))
		print()
	except:
		print("Error: unable to fecth data")

def sell(barcode):
	sql = "UPDATE product SET quantity = quantity - 1 WHERE barcode = '%s'" % (barcode)
	try:
	   cursor.execute(sql)
	   db.commit()
	except:
		print("Quantity maybe lower than zero")
		db.rollback()

def check(barcode):
	global total
	cursor = db.cursor()
	sqlSell = "SELECT * FROM product WHERE barcode = '%s'" % (barcode)
	try:
		cursor.execute(sqlSell)
		results = cursor.fetchone()
		print("Name : "+tconvert(str(results[1]))+"\tPrice : "+str(results[2])+"\tQuantity : "+str(results[3]))
		total = total + results[2]
		print("Total price : "+str(total))
		print()
	except:
		print("Error: unable to fecth data")

def sellReturn(Barcode):
	global total
	cursor = db.cursor()
	sqlSell = "SELECT * FROM product WHERE barcode = '%s'" % (barcode)
	try:
		cursor.execute(sqlSell)
		results = cursor.fetchone()
		if(total - results[2] >= 0):
			print("Name : "+tconvert(str(results[1]))+"\tPrice : "+str(results[2])+"\tQuantity : "+str(results[3]))
			total = total - results[2]
			print("Return complete")
			print("Total price : "+str(total))
			sql = "UPDATE product SET quantity = quantity + 1 WHERE barcode = '%s'" % (barcode)
			try:
			   cursor.execute(sql)
			   db.commit()
			except:
				print("ERR : ")
				db.rollback()
			print()
		else:
			print("Can't return")
			print()
	except:
		print("Error: unable to fecth data")		
	
def printMode():
	print("1 : Sell")
	print("2 : Add")
	print("3 : Check")
	print("4 : Delete")

def selectMode():
	while 1:
		global mode
		global value
		printMode()
		value = input("Select mode : ")
		if value == '1' or value == '2' or value == '3' or value == '4':
			mode = value
			break
		else :
			print("Wrong input try again!")

selectMode()

while True : 
	if(mode == '1'):
		os.system('cls')
		total = 0
		print("******  Sell MODE  ******")
		while 1:
			barcode = input("Barcode : ")
			if(barcode == "cm"):
				confirm = input("Total price will clear to zero y/n : ")
				if(confirm == 'y'):
					total = 0
					selectMode()
					break
				print()
			if(barcode == "r"):
				print()
				print("******  Return MODE  ******")
				barcode = input("Barcode : ")
				sellReturn(barcode)
				print("******  Sell MODE  ******")
			else:
				sell(barcode)

	if(mode == '2'):
		os.system('cls')
		total = 0
		print("******  ADD MODE  ******")
		while 1:
			barcode = input("Barcode : ")
			if barcode == "cm":
				selectMode()
				break
			add(barcode)

	if(mode == '3'):
		os.system('cls')
		print("******  CHECK MODE  ******")
		total = 0
		while 1:
			barcode = input("Barcode : ")
			if barcode == "cm":
				selectMode()
				break
			check(barcode)	

	if(mode == '4'):
		os.system('cls')
		print("******  DELETE MODE  ******")
		while 1:
			barcode = input("Barcode : ")
			if barcode == "cm":
				selectMode()
				break
			confirm = input("Barcode : ")
			if confirm == 'yes':
				print("Deleted!")

db.close()
