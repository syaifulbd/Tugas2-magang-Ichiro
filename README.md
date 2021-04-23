# Tugas2-magang-Ichiro
Belajar OpenCV : ini untuk memenuhi tugas magang Ichiro yang kedua untuk belajar OpenCV dengan bahasa python.

## Changing Color-space
Dalam openCV terdapat banyak sekali color-space yang dapat digunakan. Perubahan color-space yang sering digunakan adalah BGR <-> HSV dan BGR <-> Gray.
Untuk merubah color-space, openCV memiliki sebuah fungsi :

     `cv.cvtColor(input_image, flag)` :
  
input_image adalah gambar yang akan dioperasikan.

flag adalah tipe konversi yang akan dilakukan. flag yang sering digunakan adalah `cv.COLOR_BGR2GRAY` dan `cv.COLOR_BGR2HSV`.

Perubahan color-space dapat digunakan untuk mendeteksi ambang warna tertentu. Tahap-tahap mendeteksi ambang warna tertentu dengan mengubah color-space adalah sebagai berikut :

1. Mengambil image's frame dari video
2. Mengubah color-space dengan memanggil fungsi `cv.cvtColor()`
3. Menentukan batas warna yang ingin dideteksi
4. Memasukkan batas warna dalam frame dengan color-space yang telah diubah
5. Melebur frame asli dengan yang telah diubah color-spacenya supaya hanya terdeteksi warna yang diinginkan

## Geometric Transformation of Images

### Scaling
Scaling adalah mengubah ukuran sebuah gambar. Mengubah ukuran gambar dapat dilakukan dengan mengganti ukurannya secara manual maupun dengan skala. 
Untuk mengubah ukuran sebuah gambar, digunakan fungsi :

    `cv.resize(input_image, ukuran, interpolation)` :
    
input_image adalah gambar yang akan diubah ukurannya

ukuran dapat diisi dengan dua cara, yaitu :
- Manual, yaitu dengan memasukkan lebar dan panjang yang diinginkan
- Skala, yaitu dengan memasukkan `fx` sebagai skala panjang dan `fy` sebagai skala lebar

interpolation adalah metode interpolasi, dimana yang umum digunakan sebagai berikut :

- `cv.INTER_LINEAR` yang dapat digunakan pada kondisi apapun, namun bagus jika digunakan untuk memperbesar
- `cv.INTER_CUBIC` yang bagus digunakan untuk memperbesar
- `cv.INTER_AREA` yang bagus digunakan untuk memperkecil

Langkah-langkah untuk mengubah ukuran gambar adalah sebagai berikut :

1. Membaca sebuah gambar yang akan diubah ukurannya
2. Mengubah ukuran gambar dengan memanggil fungsi `cv.resize()`

### Translation
