#file khusus function

def celcius_remaur(angka):  #Celcius =>
	hasil = (4 / 5) * angka
	return hasil
def celcius_fahrenheit(angka):
	hasil = (9 / 5) * (angka + 32)
	return hasil
def celcius_kelvin(angka):
	hasil = angka + 273
	return hasil
			
def reamur_celcius(angka):  #Reamur =>
	hasil = 5/4 * angka
	return hasil
def reamur_fahrenheit(angka):
	hasil = (9/4) * (angka + 32)
	return hasil
def reamur_kelvin(angka):
	hasil = (5/4) * (angka + 273)
	return hasil
			
def fahrenheit_celcius(angka):  #Fahrenheit =>
	hasil = (5/9) * (angka - 32)
	return hasil
def fahrenheit_reamur(angka):
	hasil = (4/9) * (angka - 32)
	return hasil
def fahrenheit_kelvin(angka):
	hasil = 5/9 * (angka - 32) + 273
	return hasil
	
def kelvin_celcius(angka):  #Kelvin =>
	hasil = angka - 273
	return hasil
def kelvin_reamur(angka):
	hasil = 4/5 * (angka - 273)
	return hasil
def kelvin_fahrenheit(angka):
	hasil = 9/5 * (angka - 273) + 32
	return hasil 