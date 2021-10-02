import uvicorn
from fastapi import FastAPI
from update import post
app = FastAPI()


@app.get("/")
async def root():
    return {"message": f'''KOMPAS.com - Pebalap Ducati, Francesco Bagnaia, berhasil menyabet pole position untuk balapan MotoGP Amerika 2021. Kepastian itu diraih Francesco Bagnaia setelah menjadi yang tercepat pada sesi kualifikasi 2 (Q2) MotoGP Amerika 2021, Minggu (3/10/2021) dini hari WIB. Berlangsung di Circuit of the Americas (COTA), Francesco Bagnaia menjadi yang tercepat dengan catatan waktu 2 menit 2,781 detik. Francesco Bagnaia dibayangi oleh Fabio Quartararo (Monster Energy Yamaha) dan sang raja COTA Marc Marquez (Repsol Honda) yang secara berurutan mengisi posisi kedua dan ketiga.

Artikel ini telah tayang di Kompas.com dengan judul "Hasil Kualifikasi MotoGP Amerika - Bagnaia Hattrick Pole Position, Marquez Ketiga, Rossi Crash!", Klik untuk baca: https://www.kompas.com/motogp/read/2021/10/03/04230118/hasil-kualifikasi-motogp-amerika-bagnaia-hattrick-pole-position-marquez.
Penulis : Celvin Moniaga Sipahutar
Editor : Firzie A. Idris

Download aplikasi Kompas.com untuk akses berita lebih mudah dan cepat:
Android: https://bit.ly/3g85pkA
iOS: https://apple.co/3hXWJ0L'''}


@app.post("/update")
async def update():
    pid = post()
    return "Hello World!" + pid


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
