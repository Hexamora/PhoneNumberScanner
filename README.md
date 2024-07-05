# PhoneNumberScanner

Script **"Phonenumberscanner"** yang telah disediakan memiliki beberapa kegunaan utama:

**Validasi dan Parsing Nomor Telepon:** Script ini menggunakan library phonenumbers untuk memvalidasi dan mem-parse nomor telepon yang dimasukkan pengguna. Hal ini memastikan bahwa nomor telepon yang diinput sesuai dengan format yang diharapkan.

**Informasi Terkait Nomor Telepon:** Script ini dapat memberikan informasi terkait nomor telepon seperti negara, wilayah, operator telepon, format internasional dan nasional, serta zona waktu yang terkait dengan nomor telepon tersebut.

**Geolokasi:** Script ini menggunakan library geopy dan layanan geolocation dari Nominatim untuk menentukan lokasi geografis yang lebih spesifik terkait dengan nomor telepon. Informasi seperti koordinat latitude, longitude, dan kota dapat diperoleh jika informasi tersebut tersedia dari layanan geolocation.

**Iteratif dan Interaktif:** Script ini dirancang untuk berjalan secara iteratif dan interaktif. Pengguna diminta untuk memasukkan nomor telepon yang ingin di-scan, dan setelah informasi diperoleh, pengguna memiliki opsi untuk mengulang proses atau keluar dari program.

**Penggunaan dalam Forensik atau Investigasi:** Script semacam ini dapat digunakan dalam konteks forensik digital atau investigasi untuk memeriksa validitas nomor telepon yang diberikan, mengidentifikasi lokasi geografis terkait, dan melacak informasi terkait penyedia layanan telekomunikasi.

Dengan demikian, **"Phonenumberscanner"** dapat menjadi alat yang berguna untuk memeriksa dan mendapatkan informasi dasar terkait nomor telepon, serta menambahkan lapisan geolokasi untuk informasi yang lebih detail terkait lokasi geografis nomor telepon tersebut.

## Installation

Dibawah ini adalah urutan dalam menginstall Script di Linux.

```bash
$ pip install phonenumbers geopy requests
$ git clone https://github.com/Hexamora/PhoneNumberScanner.git
$ cd PhoneNumberScanner
$ python PhoneNumberScanner.py
```
