import tabulate
import uuid

class Transaction:
    def __init__(self):
        self.transaction_id = str(uuid.uuid4())
        self.items = []

    def get_transaction_id(self):
        return self.transaction_id

    def add_items(self, items):
        self.items.extend(items)

    def update_item_name(self, old_name, new_name):
        for item in self.items:
            nama_item, jumlah_item, harga_per_item = item
            if nama_item == old_name:
                item[0] = new_name
                print(f"Nama item '{old_name}' berhasil diperbarui menjadi '{new_name}'.")
                return
        print(f"Item dengan nama '{old_name}' tidak ditemukan.")

    def update_item_qty(self, item_name, new_qty):
        for item in self.items:
            nama_item, jumlah_item, harga_per_item = item
            if nama_item == item_name:
                item[1] = new_qty
                print(f"Jumlah item '{item_name}' berhasil diperbarui menjadi {new_qty}.")
                return
        print(f"Item dengan nama '{item_name}' tidak ditemukan.")

    def update_item_price(self, item_name, new_price):
        for item in self.items:
            nama_item, jumlah_item, harga_per_item = item
            if nama_item == item_name:
                item[2] = new_price
                print(f"Harga item '{item_name}' berhasil diperbarui menjadi {new_price}.")
                return
        print(f"Item dengan nama '{item_name}' tidak ditemukan.")

    def delete_item(self, item_name):
        for item in self.items:
            nama_item, _, _ = item
            if nama_item == item_name:
                self.items.remove(item)
                print(f"Item '{item_name}' berhasil dihapus dari transaksi.")
                return
        print(f"Item dengan nama '{item_name}' tidak ditemukan.")

    def reset_transaction(self):
        self.items = []
        print("Transaksi berhasil di-reset.")

    def display_items(self):
        print("Item yang dibeli:")
        for item in self.items:
            nama_item, jumlah_item, harga_per_item = item
            print(f"Nama: {nama_item}, Jumlah: {jumlah_item}, Harga per Item: {harga_per_item}")

    def total_price(self):
        total = 0
        for item in self.items:
            _, jumlah_item, harga_per_item = item
            total += jumlah_item * harga_per_item
        return total

    def check_order(self):
        is_valid = True
        total = self.total_price()

        for item in self.items:
            nama_item, jumlah_item, harga_per_item = item
            if not (nama_item and jumlah_item and harga_per_item):
                is_valid = False
                break

        if is_valid:
            print("Pesanan sudah benar")
            print("Total harga: Rp", total)

            if total > 500000:
                diskon = 0.1
            elif total > 300000:
                diskon = 0.08
            elif total > 200000:
                diskon = 0.05
            else:
                diskon = 0

            if diskon > 0:
                potongan = total * diskon
                total_setelah_diskon = total - potongan
                print("Diskon:", diskon * 100, "%")
                print("Potongan harga: Rp", potongan)
                print("Total harga setelah diskon: Rp", total_setelah_diskon)
            else:
                print("Tidak ada diskon yang diberikan.")
        else:
            print("Terjadi kesalahan input data")

        self.display_items_table(total)

    def display_items_table(self, total):
        headers = ["Nama Item", "Jumlah Item", "Harga per Item"]
        table_data = []

        for item in self.items:
            nama_item, jumlah_item, harga_per_item = item
            table_data.append([nama_item, jumlah_item, harga_per_item])

        print(tabulate.tabulate(table_data, headers=headers))
        print("Total Harga: Rp", total)


# Membuat objek Transaction
transct_123 = Transaction()

# Mendapatkan ID transaksi
transaction_id = transct_123.get_transaction_id()

# Menambahkan item yang dibeli
items = []

while True:
    nama_item = input("Masukkan nama item yang dibeli: ")
    jumlah_item = int(input("Masukkan jumlah item: "))
    harga_per_item = float(input("Masukkan harga per item: "))

    items.append([nama_item, jumlah_item, harga_per_item])

    add_more = input("Apakah ingin menambahkan item lain? (y/n): ")
    if add_more.lower() != "y":
        break

transct_123.add_items(items)

# Menampilkan item yang dibeli
transct_123.display_items()

# Memperbarui item
update_choice = input("Apakah ada item yang ingin diperbarui? (y/n): ")

if update_choice.lower() == "y":
    item_name = input("Masukkan nama item yang ingin diperbarui: ")
    update_option = input("Pilih opsi pembaruan: (a) Nama item, (b) Jumlah item, (c) Harga item: ")

    if update_option == "a":
        new_name = input("Masukkan nama item baru: ")
        transct_123.update_item_name(item_name, new_name)
    elif update_option == "b":
        new_qty = int(input("Masukkan jumlah item baru: "))
        transct_123.update_item_qty(item_name, new_qty)
    elif update_option == "c":
        new_price = float(input("Masukkan harga item baru: "))
        transct_123.update_item_price(item_name, new_price)
    else:
        print("Opsi pembaruan tidak valid.")

# Menampilkan item yang telah diperbarui
transct_123.display_items()

# Menghapus item
delete_choice = input("Apakah ada item yang ingin dihapus? (y/n): ")

if delete_choice.lower() == "y":
    item_name = input("Masukkan nama item yang ingin dihapus: ")
    transct_123.delete_item(item_name)

# Menampilkan item setelah penghapusan
transct_123.display_items()

# Reset transaksi
reset_choice = input("Apakah ingin mereset transaksi? (y/n): ")

if reset_choice.lower() == "y":
    transct_123.reset_transaction()

# Menampilkan item setelah reset
transct_123.display_items()

# Check order
transct_123.check_order()
