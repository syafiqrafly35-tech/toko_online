from flask import Flask

app = Flask(__name__)

# Data Produk & Jasa Aluminium Bending / Kusen
PRODUCTS = [
    {
        "id": 1,
        "nama": "Kusen Aluminium 3 Inch",
        "kategori": "Kusen",
        "harga_dasar": 95000,
        "satuan": "meter lari",
        "badge": "Terlaris",
        "gambar": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80",
        "deskripsi": "Kusen aluminium profil 3 inch cocok untuk pintu & jendela rumah tinggal. Tahan rayap, presisi, dan tahan cuaca.",
        "pilihan_warna": ["Silver", "Cokelat", "Hitam", "Putih"],
    },
    {
        "id": 2,
        "nama": "Jasa Bending Aluminium Lengkung",
        "kategori": "Bending Custom",
        "harga_dasar": 150000,
        "satuan": "titik / meter",
        "badge": "Layanan Utama",
        "gambar": "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=800&q=80",
        "deskripsi": "Pengerjaan bending/pembengkokan profil aluminium presisi tinggi untuk bentuk arch, setengah lingkaran, atau sudut custom.",
        "pilihan_warna": ["Semua Merk Profil"],
    },
    {
        "id": 3,
        "nama": "Pintu Frame Aluminium Glass",
        "kategori": "Pintu & Jendela",
        "harga_dasar": 1850000,
        "satuan": "unit lengkap",
        "badge": "Premium",
        "gambar": "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=800&q=80",
        "deskripsi": "Pintu kaca rangka aluminium tebal lengkap dengan engsel, kunci tanam, dan aksesoris. Cocok untuk toko atau kantor.",
        "pilihan_warna": ["Black Matte", "Anodized Silver"],
    },
    {
        "id": 4,
        "nama": "Jendela Casement / Swing",
        "kategori": "Pintu & Jendela",
        "harga_dasar": 750000,
        "satuan": "unit",
        "badge": "Populer",
        "gambar": "https://images.unsplash.com/photo-1503708998063-fb28b70427ed?auto=format&fit=crop&w=800&q=80",
        "deskripsi": "Jendela jungkit/swing aluminium kedap suara dan kedap air hujan. Dilengkapi rambuncis kuncian kokoh.",
        "pilihan_warna": ["Putih", "Hitam", "Urat Kayu"],
    },
]


@app.route("/")
def home():
  html_content = f"""
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Katalog & Kalkulator Kusen Aluminium Bending</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script>
            // Fungsi Kalkulator Estimasi Otomatis
            function hitungHarga(id, hargaDasar) {{
                let inputVolume = document.getElementById('volume-' + id).value;
                let hasilSpan = document.getElementById('total-' + id);
                let btnWa = document.getElementById('btn-wa-' + id);
                
                let volume = parseFloat(inputVolume) || 0;
                let total = volume * hargaDasar;
                
                // Format ke Rupiah
                let formatRupiah = new Intl.NumberFormat('id-ID', {{ style: 'currency', currency: 'IDR', maximumFractionDigits: 0}}).format(total);
                hasilSpan.innerText = formatRupiah;
                
                // Update link WhatsApp otomatis dengan data hitungan
                let namaProduk = document.getElementById('nama-produk-' + id).innerText;
                let pesan = `Halo, saya mau pesan ${namaProduk} dengan volume ${volume} (${id === 2 ? 'titik/meter' : 'meter/unit'}). Total estimasi Rp ${total.toLocaleString('id-ID')}. Mohon info lanjut.`;
                btnWa.href = "https://wa.me/6281234567890?text=" + encodeURIComponent(pesan);
            }}
        </script>
    </head>
    <body class="bg-slate-900 text-slate-100 min-h-screen font-sans antialiased">

        <!-- Header -->
        <header class="bg-slate-800 border-b border-slate-700 py-10 px-4 sm:px-6 shadow-md">
            <div class="max-w-6xl mx-auto text-center">
                <span class="bg-amber-500/10 text-amber-400 text-xs font-semibold px-3 py-1 rounded-full border border-amber-500/20 uppercase tracking-wider">
                    Workshop & Bending Aluminium Profesional
                </span>
                <h1 class="text-3xl sm:text-5xl font-extrabold text-white mt-4 mb-3 tracking-tight">
                    Katalog & Kalkulator Estimasi Kusen
                </h1>
                <p class="text-slate-400 max-w-2xl mx-auto text-base sm:text-lg">
                    Pilih jenis produk, masukkan ukuran atau volume kebutuhan bangunan Anda, dan hitung estimasi biayanya secara instan!
                </p>
            </div>
        </header>

        <!-- Product Grid & Calculator -->
        <main class="max-w-6xl mx-auto py-12 px-4 sm:px-6">
            <div class="flex items-center justify-between mb-8">
                <h2 class="text-2xl font-bold text-white tracking-wide">Pilihan Produk & Layanan</h2>
                <span class="text-sm text-slate-400">{len(PRODUCTS)} Layanan Tersedia</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
    """

  for p in PRODUCTS:
    harga_formatted = f"Rp {p['harga_dasar']:,}".replace(",", ".")
    warna_tags = "".join([
        f'<span class="bg-slate-700 text-slate-300 text-xs px-2.5 py-1 rounded-md">{w}</span>'
        for w in p["pilihan_warna"]
    ])

    html_content += f"""
                <div class="bg-slate-800 rounded-2xl border border-slate-700 overflow-hidden shadow-xl hover:border-amber-500/50 transition-all duration-300 flex flex-col justify-between">
                    <div>
                        <div class="relative h-60 overflow-hidden bg-slate-950">
                            <img src="{p['gambar']}" alt="{p['nama']}" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
                            <span class="absolute top-4 left-4 bg-amber-500 text-slate-950 font-bold text-xs px-3 py-1 rounded-full uppercase tracking-wider shadow">
                                {p['badge']}
                            </span>
                        </div>
                        <div class="p-6">
                            <div class="text-xs text-amber-400 font-semibold uppercase tracking-wider mb-1">{p['kategori']}</div>
                            <h3 id="nama-produk-{p['id']}" class="text-xl font-bold text-white mb-2">{p['nama']}</h3>
                            <p class="text-slate-400 text-sm leading-relaxed mb-4">{p['deskripsi']}</p>
                            
                            <div class="mb-4">
                                <span class="text-xs text-slate-400 block mb-1">Spesifikasi / Warna Tersedia:</span>
                                <div class="flex flex-wrap gap-2">
                                    {warna_tags}
                                </div>
                            </div>

                            <!-- Kalkulator Mini per Produk -->
                            <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-700/60 mb-4">
                                <label class="block text-xs text-amber-400 font-semibold mb-1 uppercase tracking-wider">
                                    Simulasi Hitung Estimasi ({p['satuan']}):
                                </label>
                                <div class="flex items-center gap-3">
                                    <input type="number" id="volume-{p['id']}" placeholder="Masukkan jumlah/panjang" min="1" value="1" 
                                           oninput="hitungHarga({p['id']}, {p['harga_dasar']})"
                                           class="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-white text-sm focus:outline-none focus:border-amber-500">
                                    <span class="text-xs text-slate-400 whitespace-nowrap">{p['satuan']}</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Footer Kartu & Tombol Order WA -->
                    <div class="p-6 pt-0 border-t border-slate-700/50 mt-2 flex items-center justify-between gap-4">
                        <div>
                            <span class="text-xs text-slate-400 block">Total Estimasi:</span>
                            <span id="total-{p['id']}" class="text-xl font-extrabold text-amber-400">{harga_formatted}</span>
                        </div>
                        <a id="btn-wa-{p['id']}" 
                           href="https://wa.me/6281234567890?text=Halo,%20saya%20mau%20pesan%20{p['nama']}%20dengan%20volume%201%20{p['satuan']}" 
                           target="_blank" 
                           class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-5 rounded-xl text-sm transition-all duration-200 shadow-md flex items-center gap-2">
                            Pesan via WA
                        </a>
                    </div>
                </div>
    """

  html_content += """
            </div>
        </main>

        <!-- Footer -->
        <footer class="bg-slate-950 border-t border-slate-800 py-8 text-center text-slate-500 text-sm">
            <p>&copy; 2026 Bengkel Bending & Kusen Aluminium. All Rights Reserved.</p>
        </footer>

    </body>
    </html>
    """
  return html_content


if __name__ == "__main__":
  app.run(debug=True)