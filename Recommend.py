import numpy as np
from collections import Counter
import matplotlib

raw_history = open('history.txt','r')
raw_queries = open('queries.txt','r')

history = raw_history.read().split('\n')
queries = raw_queries.read().split('\n')

infomation = history[0].split(' ')
del(history[0])

Customers = int(infomation[0])
items = int(infomation[1])
Transactions = int(infomation[2])

if not __debug__:
	print(infomation)
	print(history)
	print(queries)
	print('\n')

def build_customer_item_history_table():
	table = []
	for i in range(Customers):
		table.append([0]*items)
	for case in history:
		user        = int(case.split(' ')[0])-1
		item_bought = int(case.split(' ')[1])-1
		table[user][item_bought] = 1
	print("Positive entries: %s" %find_posistive_entries(table))
	show_table(table)

def show_table(t):
	print('		Item:')
	formatting = '      '
	for i in range(0,items):
		formatting += ('  '+str(i+1))
	print(formatting)
	for i in range(len(t)):
		print('User %s %s' %(i+1,t[i]))
	print()

def find_posistive_entries(t):
	return (Counter(str(t))['1'])

def main():
	build_customer_item_history_table()
	print('Average angle:  ')
	for cart in queries:
		print("Shopping Cart: %s" %cart)
		items_in_cart = cart.split(' ')
		for item in items_in_cart:
			print('Item: %s match: 0 angle: 0'%item)
		print()
main()
