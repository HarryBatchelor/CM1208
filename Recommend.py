from collections import Counter

#Import the history and the queries files.
raw_history = open('history.txt','r')
raw_queries = open('queries.txt','r')

#Convert the raw data into a suitable format.
history = raw_history.read().split('\n')
queries = raw_queries.read().split('\n')

#Take out the first line of data fro the history file and get info about the data set.
infomation = history[0].split(' ')
del(history[0])

#Using the first line of history to get useful infomation
Number_of_Customers = int(infomation[0])
Number_of_items = int(infomation[1])
Number_of_Transactions = int(infomation[2])

#Debugging, this would show all the input data.
if not __debug__:
	print(infomation)
	print(history)
	print(queries)
	print('\n')

def build_customer_item_history_table():
	#Initialises the table with a row for every customer and a column for each item.
	table = []
	for i in range(Number_of_Customers):
		table.append([0]*Number_of_items)

	#This goes through each item in the history and then if the customer has bought the item it will set the coordinate to a 1
	for case in history:
		user        = int(case.split(' ')[0])-1
		item_bought = int(case.split(' ')[1])-1
		table[user][item_bought] = 1

	print("Positive entries: %s" %find_posistive_entries(table))

	#Calls a custom show tabel function to show the history table with labels for the items and users.
	if not __debug__:
		show_table(table)

def show_table(t):
	#Prints the Labels for the x axis
	print('		Item:')
	formatting = '      '
	for i in range(0,Number_of_items):
		formatting += ('  '+str(i+1))
	print(formatting)
	#Prints the lines of the table and the label for Which user the line corresponds too.
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
