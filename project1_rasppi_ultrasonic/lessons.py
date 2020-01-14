import triangle.draw as draws

# variable adalah satuan unit yang dapat digunakan untuk menyimpan suatu nilai
# tipe atau jenis nilai/data yang dapat disimpan suatu variable dapat berupa apa saja
a = 'this is 1 value of variable a 0.55'
string_variable = 'string value'
integer_variable = 1
float_variable = 0.55

print("variable type: {} - value: {}".format(type(string_variable), string_variable))

# this will error
#variable_nothing # ketika mendefinisikan variable harus dibarengi dengan nilai dari var tsb
variable_nothing = None # meskipun bernilai None

# function/method pada dasarnya hanya sekumpulan baris kode, dimana bertugas melaksanakan tugas tertentu.
# function dibuat untuk menghindari banyaknya perulangan penulisan kode, dimana potongan kode tsb
#   dimaksudkan untuk melaksakan satu tugas tertentu saja.
def testing():
	#print(a)
	global string_variable
	string_variable = 'new value'
	print(string_variable)

testing()
print(string_variable)

# kita bisa mengambil nilai variable dari module lain
print("variable frow draw.py: {}".format(draws.triangle_var))
draws.triangle_var = 5
print("variable frow draw.py: {}".format(draws.triangle_var))
draws.triangleAlgorithm(5)
print("acceesing help/docstring in a function:\n{}".format(draws.triangleAlgorithm.__doc__))

class testVar(object):
	class_var = 10
	__ds = 15 # private variable
	
	# private method
	def __privateClassMethod():
		print("private class method")

tvar = testVar()
# kita juga bisa mengambil nilai variable dari sebuah class instance
print("value of tvar.class_var: {}".format(tvar.class_var))
tvar.class_var = 11 # bisa juga merubahnya
print("value of changed tvar.class_var: {}".format(tvar.class_var))
#print(tvar.__ds) # this will error

# tapi nilai variable di class tersebut sebetulnya static
print(testVar.class_var)

# tidak seperti di c++ yg bisa mendifinisikan static varibale, di python hal tsb tidak ada

# bagusnya kita tetap bisa mendifinisikan private variable dan private function/method
#   tetapi variable dan function tersebut harus berada di dalam class
print(draws.privateTriangleAlgo()) # will print None

## untuk membuat komentar(line of code yang tidak akan dieksekusi)
##   bisa dengan didahului lambang:
# Ini komentar
# atau
""" Ini juga Komentar
MultiLine
"""

# ada 2 jenis looping yang bisa digunakan yaitu:
# 1
print()
print("--"*10)
# gunakan for loop jika kita mengetahui jumlah perulangan yg diinginkan
for i in range(0,5):
	print(i)
print("--"*3)
# dan 2
# gunakan while untuk sesuatu yg belum pasti
command = None
while command!='quit':
	command = input("whats your command sir: ")
	print("your command: {}".format(command))
print("adioss..")
