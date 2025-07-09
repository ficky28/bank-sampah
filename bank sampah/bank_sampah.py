# === QUERY 1 ===
# Membuat class UMKMSystem dengan atribut dasar
class UMKMSystem:
    def __init__(self, nama_umkm):
        self.nama_umkm = nama_umkm
        self.anggota = []
        self.dana_pinjaman = 50000000  # Rp50 juta

    # === QUERY 2 ===
    # Method tambah_anggota untuk menambah anggota dan pinjaman
    def tambah_anggota(self, nama, pinjaman):
        data = {"nama": nama, "pinjaman": pinjaman}
        self.anggota.append(data)

    # === QUERY 3 ===
    # Method hitung_pengembalian dengan bunga sederhana 5% per tahun
    def hitung_pengembalian(self, nama_anggota, tahun):
        for anggota in self.anggota:
            if anggota["nama"] == nama_anggota:
                pinjaman = anggota["pinjaman"]
                bunga = pinjaman * 0.05 * tahun
                total = pinjaman + bunga
                return total
        return None

# === QUERY 4 ===
# Class Koperasi yang mewarisi UMKMSystem dan memiliki atribut transaksi
class Koperasi(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm)
        self.transaksi = []

    # === QUERY 5 ===
    # Method catat_transaksi untuk menyimpan transaksi anggota
    def catat_transaksi(self, nama_anggota, jenis_transaksi, jumlah):
        data = {
            "nama": nama_anggota,
            "jenis": jenis_transaksi,
            "jumlah": jumlah
        }
        self.transaksi.append(data)

    # === QUERY 6 ===
    # Method hitung_keuntungan (jual - beli)
    def hitung_keuntungan(self):
        total_jual = 0
        total_beli = 0
        for t in self.transaksi:
            if t["jenis"] == "jual":
                total_jual += t["jumlah"]
            elif t["jenis"] == "beli":
                total_beli += t["jumlah"]
        return total_jual - total_beli

# === QUERY 7 ===
# Class BankSampah yang mewarisi UMKMSystem dengan data_sampah
class BankSampah(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm)
        self.data_sampah = {}
        self.nilai_tukar_sampah = {
            "plastik": 5000,
            "kertas": 2000,
            "kaleng": 7000,
            "botol": 4000
        }

    # === QUERY 8 ===
    # Method catat_sampah untuk mencatat sampah anggota
    def catat_sampah(self, nama_anggota, jenis_sampah, jumlah_kg):
        if nama_anggota not in self.data_sampah:
            self.data_sampah[nama_anggota] = {}
        if jenis_sampah in self.data_sampah[nama_anggota]:
            self.data_sampah[nama_anggota][jenis_sampah] += jumlah_kg
        else:
            self.data_sampah[nama_anggota][jenis_sampah] = jumlah_kg

    # === QUERY 9 ===
    # Method hitung_nilai_tukar menghitung nilai tukar total sampah anggota
    def hitung_nilai_tukar(self, nama_anggota):
        total_nilai = 0
        if nama_anggota in self.data_sampah:
            for jenis, jumlah_kg in self.data_sampah[nama_anggota].items():
                nilai_per_kg = self.nilai_tukar_sampah.get(jenis, 0)
                total_nilai += nilai_per_kg * jumlah_kg
        return total_nilai

    # === QUERY 10 ===
    # Method pesan_edukasi memberi pesan berdasar total sampah yg dikumpulkan
    def pesan_edukasi(self, nama_anggota):
        total_kg = 0
        if nama_anggota in self.data_sampah:
            total_kg = sum(self.data_sampah[nama_anggota].values())
        if total_kg == 0:
            return "Ayo mulai kumpulkan sampah untuk lingkungan lebih bersih!"
        elif total_kg < 10:
            return "Kerja bagus! Terus tingkatkan pengumpulan sampah."
        elif total_kg < 50:
            return "Hebat! Kamu sudah membantu mengurangi sampah secara signifikan."
        else:
            return "Luar biasa! Kamu adalah pahlawan lingkungan."

# === QUERY 11 ===
# Program utama untuk input dan laporan lengkap
def main():
    print("=== Sistem UMKM, Koperasi, dan Bank Sampah ===")

    nama_umkm = input("Masukkan nama UMKM: ")
    koperasi = Koperasi(nama_umkm)
    bank_sampah = BankSampah(nama_umkm)

    # Input anggota
    n = int(input("Masukkan jumlah anggota: "))
    for _ in range(n):
        nama = input("Nama anggota: ")
        pinjaman = int(input(f"Jumlah pinjaman untuk {nama} (Rp): "))
        koperasi.tambah_anggota(nama, pinjaman)
        bank_sampah.tambah_anggota(nama, pinjaman)

    # Input transaksi koperasi
    print("\n--- Input Transaksi Koperasi ---")
    m = int(input("Masukkan jumlah transaksi: "))
    for _ in range(m):
        nama = input("Nama anggota: ")
        jenis = input("Jenis transaksi (beli/jual): ").lower()
        jumlah = int(input("Jumlah transaksi (Rp): "))
        koperasi.catat_transaksi(nama, jenis, jumlah)

    # Input data sampah
    print("\n--- Input Data Sampah ---")
    k = int(input("Masukkan jumlah data sampah yang ingin dicatat: "))
    for _ in range(k):
        nama = input("Nama anggota: ")
        jenis_sampah = input("Jenis sampah (plastik/kertas/kaleng/botol): ").lower()
        jumlah_kg = float(input("Jumlah sampah (kg): "))
        bank_sampah.catat_sampah(nama, jenis_sampah, jumlah_kg)

    # Tampilkan laporan lengkap
    print("\n=== Laporan Lengkap ===")
    for anggota in koperasi.anggota:
        nama = anggota["nama"]
        pinjaman = anggota["pinjaman"]
        print(f"\nAnggota: {nama}")
        print(f"Pinjaman: Rp{pinjaman:,}")

        pengembalian = koperasi.hitung_pengembalian(nama, 1)
        if pengembalian is not None:
            print(f"Total pengembalian (1 tahun): Rp{int(pengembalian):,}")
        else:
            print("Data pengembalian tidak ditemukan.")

        keuntungan = koperasi.hitung_keuntungan()
        print(f"Keuntungan koperasi saat ini: Rp{keuntungan:,}")

        nilai_tukar = bank_sampah.hitung_nilai_tukar(nama)
        print(f"Nilai tukar sampah: Rp{int(nilai_tukar):,}")

        pesan = bank_sampah.pesan_edukasi(nama)
        print(f"Pesan edukasi: {pesan}")

if __name__ == "__main__":
    main()
