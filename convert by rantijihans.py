# function def kelvin to celcius
def konversi_kc(kelvin, angka):
    '''this function is used to convert from kelvin to celcius'''
    print(kelvin, 'T (Kelvin) =', kelvin-angka,'C (Celcius)')

# def parameters
kelvin = int(input ("Masukkan Suhu dalam Kelvin : \n"))
angka = 273


# call konversi kelvin to celcius
konversi_kc(kelvin, angka)  

# function def celcius to kelvin
def konversi_ck(celcius, angka):
    '''this function is used to convert from celcius to kelvin'''
    print(celcius, 'C (Celcius) =', celcius+angka,'T (Kelvin)')

#def parameters
celcius = int(input ("Masukkan Suhu dalam Celcius : \n"))

# call konversi celcius to kelvin     
konversi_ck(celcius,angka)



# function def celcius to fahrenheit
def konversi_cf(celcius):
    '''this function is used to convert from celcius to fahrenheit'''
    print(celcius, 'C (Celcius) =', (9/5)*celcius+32,'F (Fahrenheit)')

# call konversi celcius to kelvin     
konversi_cf(celcius)

# function def fahrenheit to kelvin
def konversi_fk(fahrenheit, angka):
    '''this function is used to convert from celcius to kelvin'''
    print(fahrenheit, 'F (Fahrenheit) =', (5/9)*(fahrenheit-32)+angka,'T (Kelvin)')

#def parameters
fahrenheit = int(input ("Masukkan Suhu dalam Fahrenheit : \n"))

# call konversi fahrenheit to kelvin     
konversi_fk(fahrenheit,angka)