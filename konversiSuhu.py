import fungsiSuhu
from fungsiSuhu import else_stat
while True :	
	print("   Mini Calculate Temperature by Dimaz.")
	print("1. Celcius\n2. Reamur\n3. Fahrenheit\n4. Kelvin")
	suhu = input("pilih suhu yg akan dikonversikan : ")
	
	if suhu == "1" or suhu == "celcius" :
		suhu = "celcius"
		try :
			angka = float(input(f"masukan angka suhu {suhu} : "))
			konversi = input("Akan di konversikan ke suhu..  ")
			if konversi == "2" or konversi == "reamur" :
				konversi = "reamur"
				hasil = fungsiSuhu.celcius_remaur(angka)
			elif konversi == "3" or konversi == "fahrenheit" :
				konversi = "fahrenheit"
				hasil = fungsiSuhu.celcius_fahrenheit(angka)
			elif konversi == "4" or konversi == "kelvin" :
				konversi = "kelvin"
				hasil = fungsiSuhu.celcius_kelvin(angka)
			else : else_stat()
		except ValueError :
			else_stat()
		
	elif suhu == "2" or suhu == "reamur" :
		suhu = "reamur"
		try :
			angka = float(input(f"masukan angka suhu {suhu} : "))
			konversi = input("Akan dikonversikan ke suhu... ")
			if konversi == "1" or konversi == "celcius" :
				konversi = "celcius"
				hasil = fungsiSuhu.reamur_celcius(angka)
			elif konversi == "3" or konversi == "fahrenheit" :
				konversi = "fahrenheit"
				hasil = fungsiSuhu.reamur_fahrenheit(angka)
			elif konversi == "4" or konversi == "kelvin" :
				konversi = "kelvin"
				hasil = fungsiSuhu.reamur_kelvin(angka)
			else : else_stat()
		except ValueError :
			else_stat()
			
	elif suhu == "3" or suhu == "fahrenheit" :
		suhu = "fahrenheit"
		try :
			angka = float(input(f"masukan angka suhu {suhu} : "))
			konversi = input("Akan dikonversikan ke suhu... ")
			if konversi == "1" or konversi == "celcius" :
				konversi = "celcius"
				hasil = fungsiSuhu.fahrenheit_celcius(angka)
			elif konversi == "2" or konversi == "reamur" :
				konversi = "reamur"
				hasil = fungsiSuhu.fahrenheit_reamur(angka)
			elif konversi == "4" or konversi == "kelvin" :
				konversi = "kelvin"
				hasil = fungsiSuhu.fahrenheit_kelvin(angka)
			else : else_stat()
		except ValueError :
			else_stat()
	
	elif suhu == "4" or suhu == "kelvin" :
		suhu = "kelvin"
		try :
			angka = float(input(f"masukan angka suhu {suhu} : "))
			konversi = input("Akan dikonversikan ke suhu... ")
			if konversi == "1" or konversi == "celcius" :
				konversi = "celcius"
				hasil = fungsiSuhu.kelvin_celcius(angka)
			elif konversi == "2" or konversi == "reamur" :
				konversi = "reamur"
				hasil = fungsiSuhu.kelvin_reamur(angka)
			elif konversi == "3" or konversi == "fahrenheit" :
				konversi = "fahrenheit"
				hasil = fungsiSuhu.kelvin_fahrenheit(angka)
			else : else_stat()
		except ValueError :
			else_stat()
	
	else :
		angka, suhu, hasil, konversi = 0, " ", 0, " "
		else_stat()
	
	try :	
		print(f"\n	{angka}?? {suhu} = {hasil}?? {konversi}.\n")
	except NameError :
		print("Please Enter Correctly!")
	lagi = input("Try again?\nType y / yes to continue : ")
	print("\n")
	print(17*"===")
	print("\n")
	
	if lagi == "yes" or lagi == "y" :
		pass
	else :
	     break
	
print("\n	terimakasih\n			??Dims.")
