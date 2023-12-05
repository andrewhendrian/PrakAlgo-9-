# -*- coding: utf-8 -*-
"""PrakAlgo[9]

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14dNkMVpo7ylWZloWl2yrHatUXZcS-Gba
"""

print('@@@@ @@   @ @@@@@  @@@@  @@@@@@ @       @')
print('@  @ @ @  @ @    @ @   @ @      @       @')
print('@@@@ @  @ @ @    @ @   @ @@@@@@ @   @   @')
print('@  @ @   @@ @    @ @@@@  @      @   @   @')
print('@  @ @    @ @@@@@  @   @ @@@@@@ @@@@@@@@@')
def banner():
    print("=====================================")
    print("ELKOM 1")
    print("=====================================")

def konversi_list_ke_tuple(input_list):
    return tuple(input_list)

# Contoh penggunaan
banner()
list_input = [1, 2, 4, 3, 1, 44]
tuple_output = konversi_list_ke_tuple(list_input)

print( list_input)
print("Hasil reverse ke tuple")
print(tuple_output)

print('@@@@ @@   @ @@@@@  @@@@  @@@@@@ @       @')
print('@  @ @ @  @ @    @ @   @ @      @       @')
print('@@@@ @  @ @ @    @ @   @ @@@@@@ @   @   @')
print('@  @ @   @@ @    @ @@@@  @      @   @   @')
print('@  @ @    @ @@@@@  @   @ @@@@@@ @@@@@@@@@')
def hitung_rata_rata(tuple_input):
    rata_rata_setiap_tuple = []

    for tup in tuple_input:
        total_nilai = 0
        jumlah_elemen = len(tup)

        for nilai in tup:
            total_nilai += nilai

        if jumlah_elemen == 0:
            rata_rata_setiap_tuple.append(0)
        else:
            rata_rata = total_nilai / jumlah_elemen
            rata_rata_setiap_tuple.append(rata_rata)

    return rata_rata_setiap_tuple


# Contoh penggunaan

tuple_input = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
rata_rata_hasil = hitung_rata_rata(tuple_input)

print( tuple_input)
print("Rata-rata tuple adalah:")
print(rata_rata_hasil)
print("=====================================")
print("    DRU       ")
print("=====================================")
print("============065002300011============")

print('@@@@ @@   @ @@@@@  @@@@  @@@@@@ @       @')
print('@  @ @ @  @ @    @ @   @ @      @       @')
print('@@@@ @  @ @ @    @ @   @ @@@@@@ @   @   @')
print('@  @ @   @@ @    @ @@@@  @      @   @   @')
print('@  @ @    @ @@@@@  @   @ @@@@@@ @@@@@@@@@')
print("=====================================")
print("    DRU      ")
print("=====================================")

def hitung_hasil_kali(input_list):
    hasil_kali = 1

    for nilai in input_list:
        hasil_kali *= nilai

    return hasil_kali

# Contoh penggunaan
list_input = [1, 1, 2, 5]
hasil_kali = hitung_hasil_kali(list_input)

print( list_input)
print( hasil_kali)

