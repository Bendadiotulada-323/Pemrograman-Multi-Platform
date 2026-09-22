a = int(input("Masukkan angka pertamamu bung: "))
b = int(input("Masukkan angka keduamu bung: "))
c = int(input("Masukkan angka ketigamu bung: "))

if a >= b and a >= c:
    largest = a
    print("Angka Terbesar adalah:", largest)
elif b >= a and b >= c:
    largest = b
    print("Angka Terbesar adalah:", largest)
elif c >= b and c >= b:
    largest = c
    print("Angka Terbesar adalah:", largest)
else:
    print("Tidak Ada Angka Terbesar")

