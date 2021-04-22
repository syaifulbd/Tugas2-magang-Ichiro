# Tugas2-magang-Ichiro
Belajar OpenCV : ini untuk memenuhi tugas magang Ichiro yang kedua untuk belajar OpenCV dengan bahasa python.

## Changing Color-space
Dalam openCV terdapat banyak sekali bentangan warna yang dapat digunakan. Perubahan bentangan warna yang sering digunakan adalah BGR <-> HSV dan BGR <-> Gray.
Untuk merubah bentangan warna, openCV memiliki sebuah fungsi :
  `cv.cvtColor(input_image, flag)` :
  
`input_image` adalah gambar yang akan dioperasikan.

`flag` adalah tipe konversi yang akan dilakukan.

`flag` yang sering digunakan adalah `cv.COLOR_BGR2GRAY` dan `cv.COLOR_BGR2HSV`.

