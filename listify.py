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
    def __init__(self, n=5):
        self.kapasitas = n
        self.id_depan = None
        self.id_belakang = None
        self.isi_saat_ini = 0 
        self.data = [None] * n

    def enqueue(self, nama, kategori, harga):
        item = Item(nama, kategori, harga)
        if self.isi_saat_ini < self.kapasitas:
            if self.isi_saat_ini == 0:
                self.id_depan = self.id_belakang = 0
            else:
                self.id_belakang = self.id_belakang + 1
                if self.id_belakang == self.kapasitas:
                    self.id_belakang = 0
            self.data[self.id_belakang] = item
            self.isi_saat_ini = self.isi_saat_ini + 1
            print("\nItem Berhasil Ditambahkan Ke Listify!")
        else:  
            print("\nListify sudah penuh. Item tidak dapat ditambahkan.")

    def dequeue(self):
        if self.isi_saat_ini > 0: 
            item = self.data[self.id_depan]
            self.data[self.id_depan] = None  
            self.id_depan = self.id_depan + 1
            if self.id_depan == self.kapasitas:
                self.id_depan = 0
            self.isi_saat_ini = self.isi_saat_ini - 1
            print("\nMenghapus Item:", item.nama)
            return item
        else: 
            print("\nListify kosong. Tidak ada item yang dapat dihapus.")
            return None
    
    def change_capacity(self, new_capacity):
       if new_capacity <= 0:
           print("\nKapasitas harus merupakan bilangan bulat positif.")
       elif new_capacity < self.isi_saat_ini:
           print("\nKapasitas baru tidak dapat lebih kecil dari jumlah item yang ada.")
       else:
           new_data = [None] * new_capacity
           current_index = self.id_depan
           for i in range(self.isi_saat_ini):
               new_data[i] = self.data[current_index]
               current_index = (current_index + 1) % self.kapasitas
           self.data = new_data
           self.kapasitas = new_capacity
           print("\nKapasitas Listify berhasil diubah menjadi", new_capacity)

    def is_empty(self):
        return self.isi_saat_ini == 0

    def get_items_by_kategori(self, kategori):
        items = [item for item in self.data if item is not None and item.kategori == kategori]
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
            for i, item in enumerate(self.data, start=1):
                if item is not None:
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
    print("\nKapasitas Listify Saat Ini:", listify_list.kapasitas)
    print("============ Menu ============")
    print("1. Tambah Item")
    print("2. Hapus Item Pertama")
    print("3. Tampilkan Item Per Kategori")
    print("4. Tampilkan Semua Item")
    print("5. Ubah Kapasitas Listify")
    print("6. Keluar")
    print("==============================")
    
    choice = input("Masukkan Pilihan (1-6): ")

    if choice == '1':
        nama = input("Masukkan Nama Item: ")
        kategori = input("Masukkan Kategori Item: ")
        harga = float(input("Masukkan Harga Item: "))
        listify_list.enqueue(nama, kategori, harga)

    elif choice == '2':
        listify_list.dequeue()

    elif choice == '3':
        kategori = input("Masukkan Kategori: ")
        listify_list.get_items_by_kategori(kategori)

    elif choice == '4':
        listify_list.display_all_items()

    elif choice == '5':
        new_capacity = int(input("Masukkan kapasitas baru: "))
        listify_list.change_capacity(new_capacity)
        
    elif choice == '6':
        print("Keluar Program...")
        break
    else:
        print("Pilihan Tidak Ada! Coba Lagi.")