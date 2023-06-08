# Kelompok 6
# Algoritma dan Struktur Data
# TPLB2'59 - Semester 2
# Listify | Simplify Your Item List.

class Item:
    def __init__(self, nama, kategori, harga):
        self.nama = nama
        self.kategori = kategori
        self.harga = harga

class Listify:
    def __init__(self):
        self.queue = []

    def add_item(self, nama, kategori, harga):
        item = Item(nama, kategori, harga)
        self.queue.append(item)
        print("\nItem Berhasil Ditambahkan Ke Listify!")

    def remove_item(self):
        if self.is_empty():
            print("List di Listify Kosong.")
        else:
            item = self.queue.pop(0)
            print("Menghapus Item:", item.nama)

    def is_empty(self):
        return len(self.queue) == 0

    def get_items_by_kategori(self, kategori):
        items = [item for item in self.queue if item.kategori == kategori]
        if len(items) == 0:
            print("\nItem Dengan Kategori:", kategori)
            print("----------------------------------------------------------------------------")
            print("| {:<5s} | {:<20s} | {:<20s} | {:<18s} | ".format("No", "Nama", "Kategori", "Harga"))
            print("----------------------------------------------------------------------------")
            print("| {:<72s} |  ".format("Kategori Tidak Ditemukan."))
            print("----------------------------------------------------------------------------")
        else:
            print("\nItem Dengan Kategori:", kategori)
            print("----------------------------------------------------------------------------")
            print("| {:<5s} | {:<20s} | {:<20s} | {:<18s} | ".format("No", "Nama", "Kategori", "Harga"))
            print("----------------------------------------------------------------------------")
            for i, item in enumerate(items, start=1):
                print("| {:<5d} | {:<20s} | {:<20s} | {:<18.0f} | ".format(i, item.nama, item.kategori, item.harga))
            print("----------------------------------------------------------------------------")

    def display_all_items(self):
        if self.is_empty():
            print("\n")
            print("----------------------------------------------------------------------------")
            print("| {:<5s} | {:<20s} | {:<20s} | {:<18s} | ".format("No", "Nama", "Kategori", "Harga"))
            print("----------------------------------------------------------------------------")
            print("| {:<72s} |  ".format("Item Di Listify Kosong."))
            print("----------------------------------------------------------------------------")
        else:
            print("\nSemua Item di Listify:")
            print("----------------------------------------------------------------------------")
            print("| {:<5s} | {:<20s} | {:<20s} | {:<18s} | ".format("No", "Nama", "Kategori", "Harga"))
            print("----------------------------------------------------------------------------")
            for i, item in enumerate(self.queue, start=1):
                print("| {:<5d} | {:<20s} | {:<20s} | {:<18.0f} | ".format(i, item.nama, item.kategori, item.harga))
            print("----------------------------------------------------------------------------")


logo = """
██╗     ██╗███████╗████████╗██╗███████╗██╗   ██╗
██║     ██║██╔════╝╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
██║     ██║███████╗   ██║   ██║█████╗   ╚████╔╝ 
██║     ██║╚════██║   ██║   ██║██╔══╝    ╚██╔╝  
███████╗██║███████║   ██║   ██║██║        ██║   
╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝╚═╝        ╚═╝   
                                                 
Welcome to Listify! | Simplify Your Item List.
"""

# Main Program
listify_list = Listify()

print(logo)

while True:
    print("\n============ Menu ============")
    print("1. Tambah Item")
    print("2. Hapus Item Pertama")
    print("3. Tampilkan Item Per Kategori")
    print("4. Tampilkan Semua Item")
    print("5. Keluar")
    print("==============================")
    
    choice = input("Masukkan Pilihan (1-5): ")

    if choice == '1':
        nama = input("Masukkan Nama Item: ")
        kategori = input("Masukkan Kategori Item: ")
        harga = float(input("Masukkan Harga Item: "))
        listify_list.add_item(nama, kategori, harga)

    elif choice == '2':
        listify_list.remove_item()

    elif choice == '3':
        kategori = input("Masukkan Kategori: ")
        listify_list.get_items_by_kategori(kategori)

    elif choice == '4':
        listify_list.display_all_items()

    elif choice == '5':
        print("Keluar Program...")
        break

    else:
        print("Pilihan Tidak Ada! Coba Lagi.")