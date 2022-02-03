# def pangkat(x, y):
#     print("X * Y", "adalah", x*y)


# angka1 = int(input("Masukan angka: "))
# angka2 = int(input("Masukan angka: "))
# pangkat(angka2, angka1)

# nilai = [10, 20, 30, 40, 50]
# list_nilai = [x for x in nilai]

# print(nilai)
# print(list_nilai)

# list_nilai2 = []
# for x in nilai:
#     list_nilai2.append(x)

# print(list_nilai2)


# nilai = [3, 5, 6, 7, 10]
# filter_list = [x for x in nilai if x % 2 == 0]
# print(filter_list)

# filter_list = [x for x in nilai if x % 2 != 0]
# print(filter_list)

# filter_list = [x + 2 for x in nilai]
# print(filter_list)

# reduce_list = [sum([nilai[0]] + [x for x in nilai])]
# print(reduce_list)

# def pangkat(x):
#     print("X * x", "adalah", x*x)

# print(pangkat(2))

# pangkat2 = lambda x: x*x
# print(pangkat(6))
# print(pangkat2(6))

# def tambah(x):
#     if x <= 10:
#         print(x)
#         x+=1
#         tambah(x)

# print(tambah(1))

# def biodata(nama, umur, pekerjaan, status):
#     print("Nama:", nama)
#     print("Umur:", umur)
#     print("Pekerjaan:", pekerjaan)
#     print("Status:", status)

# list_argument = ["Rizki", "20", "Mahasiswa", "Single"]
# biodata(*list_argument)

# biodata(umur=20,status="Single",nama="Rizki",pekerjaan="Mahasiswa")

# def biodata_optional_argument(nama = "No name", umur = 0, pekerjaan = "-", status="-"):
#     print("Nama:", nama)
#     print("Umur:", umur)
#     print("Pekerjaan:", pekerjaan)
#     print("Status:", status)

# print(biodata_optional_argument(umur=20, nama="Taufiq"))

# def pangkat(x):
#     print(x*x)
#     print('sudah hitung')

# pangkat(2)

def pangkat_return(x):
    tambah = x*x
    kurang = x-x
    kali = x*x
    bagi = x/x
    return kurang

var = pangkat_return(2)
print(var)