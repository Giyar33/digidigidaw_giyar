#membuat garis
def garis ():
    print ("----------------------------------------------")

#fungsi buble ascending ( dari kecil ke besar )
def sort_asc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangfan pertama
    for i in range(n):
        #perulangan kedua
        for j in range (n-i-1):
            #membandingkan masing" elemen ke kanan
            if array[j] > array[j+1]:
                #jika lebih besar, tukar ke kiri
                array[j], array[j+1] = array[j+1], array[j]
    return array

#fungsi buble descending ( dari besar ke kecil )
def sort_desc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangfan pertama
    for i in range(n):
        #perulangan kedua
        for j in range (n-i-1):
            #membandingkan masing" elemen ke kanan
            if array[j] < array[j+1]:
                #jika lebih besar, tukar ke kiri
                array[j], array[j+1] = array[j+1], array[j]
    return array

#fungsi rata-rata
def rata_rata(angka):
    return sum(angka)/len(angka)

#input nilai
garis()
print("Masukan tiga buah nilai")
nama = input("Masukan nama anda : ")
nilai_a = int(input("Nilai 1 : "))
nilai_b = int(input("Nilai 2 : "))
nilai_c = int(input("Nilai 3 : "))
nilai_d = int(input("Nilai 4 : "))
nilai_e = int(input("Nilai 5 : "))
nilai_f = int(input("Nilai 6 : "))
nilai_g = int(input("Nilai 7 : "))
nilai_h = int(input("Nilai 8 : "))
nilai_i = int(input("Nilai 9 : "))
nilai_j = int(input("Nilai 10 : "))
angka = [nilai_a, nilai_b, nilai_c, nilai_d, nilai_e, nilai_f, nilai_g, nilai_h, nilai_i, nilai_j]
garis()
print()

#nilai akhir
print("Hasil Akhir------")
print("Nama anda : ",(nama))
print("Urutan Angka ascending : ",(sort_asc(angka)))
print("Urutan Angka descending : ",(sort_desc(angka)))
garis()
print()

#cari nilai terbesar (max)
print ("Angka Terbesar : ",max(angka))
garis()
print()

#cari nilai terkecil (min)
print ("Angka Terkecil : ",min(angka))
garis()
print()

#cari nilai rata-rata
print ("Rata-ratanya : ",round(rata_rata(angka),2))
garis()
print()

#jumlah angka
print ("Jumlahya : ",sum(angka))
