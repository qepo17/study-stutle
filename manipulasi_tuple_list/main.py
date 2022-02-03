# my_list = [1, 2, 3, 4, 5]
# print(my_list[1])  # 2

# print(my_list[1:3])  # [2, 3]

# print(my_list[0:3:2])  # [1, 3]

# print(my_list[::-3])  # [5, 2]

# mentees = {"alfian", "yusuf", "velicia"}

# mentee = "taufiq"

# if mentee in mentees:
#     print("ada")
# else:
#     print("tidak ada")

# mentees_backend = {"budi", "bambang"}
# mentees_semua = mentees.union(mentees_backend)
# print(mentees_semua)

# nilai = {80, 90, 10}
# nilai_backend = {90, 100, 80}

# print(nilai.union(nilai_backend))
# print(nilai.intersection(nilai_backend))
# print(nilai.difference(nilai_backend))

# my_list = [3, 2, 1, 5, 4]
# my_list.sort()
# print(my_list)

# mentees = {"yusuf", "alfian", "velicia"}
# nilai = {80, 90, 10}

# sorted_mentees = sorted(mentees, reverse=True)
# print(sorted_mentees)

# nilai = sorted(nilai)
# print(nilai)

from operator import itemgetter


dict = [
    (20, 30, 90),
    (10, 20, 30),
    (40, 50, 60),
]

# 30
# 90
# 60

siswa_urut = sorted(dict, key=lambda x: x[2])
print(siswa_urut)

siswa_urut = sorted(dict, key=itemgetter(2))
print(siswa_urut)
