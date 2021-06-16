import os

# 讀取檔案
def read_file(filename):
	products = []#參生空清單
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products	

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		products.append([name, price])
	print(products)
	return products

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename,products):
	with open(filename,'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')


def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #相對路徑(在程式同目錄)
		print('found file')		#相對路徑(C:\Users\Desktop\coding\products)
		products = read_file(filename)
	else:
		print('file not found,will creat a new file')

	products = user_input(products)
	print_products(products)
	write_file(filename, products)

main()
