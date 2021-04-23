# Tugas2-magang-Ichiro
Belajar OpenCV : ini untuk memenuhi tugas magang Ichiro yang kedua untuk belajar OpenCV dengan bahasa python.

## Changing Color-space
Dalam openCV terdapat banyak sekali color-space yang dapat digunakan. Perubahan color-space yang sering digunakan adalah BGR <-> HSV dan BGR <-> Gray.
Untuk merubah color-space, openCV memiliki sebuah fungsi :

`cv.cvtColor(src, flag)` :
  
src adalah gambar yang akan dioperasikan.

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

`cv.resize(src, size, interpolation)` :
    
src adalah gambar yang akan diubah ukurannya

size dapat diisi dengan dua cara, yaitu :
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
Untuk menggeser sebuah gambar, openCV memiliki fungsi :

`cv.wrapAffine(src, Matrix, size)` :

src adalah gambar yang akan digeser

Matrix adalah matriks perpindahan yang diinginkan. Biasanya digunakan [1,0,tx],[0,1,ty] dengan tx perpindahan horizontal dan ty perpindahan vertikal.

size adalah ukuran gambar

Langkah-langkah untuk menggeser sebuah gambar adalah sebagai berikut :

1. Membaca sebuah gambar yang akan digeser
2. Mendapatkan ukuran gambar
3. Membuat matriks pergeseran yang akan dilakukan
4. Menggeser gambar dengan memanggil fungsi `cv.wrapAffine()`

### Rotation
Untuk memutar sebuah gambar, dapat digunakan fungsi :

- `cv.getRotationMatrix2D(center, angle, scale)` :

center adalah koordinat poros perputaran yang akan dilakukan

angle adalah besar sudut perputaran

scale adalah skala gambar setelah diputar

- `cv.wrapAffine(src, Matrix, size)` :

src adalah gambar yang akan diputar

Matrix adalah matriks perputaran yang didapat dengan memanggil fungsi `cv.getRotationMatrix2D()`

size adalah ukuran gambar

Langkah-langkah untuk memutar gambar adalah sebagai berikut :

1. Membaca gambar yang akan diputar
2. Mendapatkan matriks perputaran dengan memanggil fungsi `cv.getRotationMatrix2D()`
3. Memutar gambar dengan memanggil fungsi `cv.wrapAffine()`

### Affine Transformation
Affine Transformation adalah memindahkan sebuah gambar berdasarkan tiga koordinat yang diberikan. Untuk melakukan affine transformation, digunakan fungsi :

- `cv.getAffineTransform(src, dst)` :

src adalah titik asal sebelum transformasi

dst adalah titik tujuan transformasi

- `cv.wrapAffine(src, Matrix, size)` :

src adalah gambar yang akan mengalami transformasi

Matrix adalah matriks transformasi yang didapat dengan memanggil fungsi `cv.getAffineTransform()`

size adalah ukuran gambar

Langkah-langkah untuk melakukan Affine Transformation adalah sebagai berikut :

1. Membaca gambar yang akan ditranformasi
2. Menentukan tiga titik asal dan titik tujuan transformasi
3. Membuat matriks tranformasi dengan memanggil fungsi `cv.getAffineTransform()`
4. Melakukan Affine Transformation dengan memanggil fungsi `cv.wrapAffine()`

### Perspective Transformation
Perspective Transformation adalah memindahkan sebuah gambar berdasarkan empat koordinat yang diberikan, namun dalam transformasi ini sumbu-x dan sumbu-y tetap pada tempatnya. Untuk melakukan Perspective Transformation digunakan fungsi :

- `cv.getPerspectiveTransform(src, dst)` :

src adalah titik asal sebelum transformasi

dst adalah titik tujuan transformasi

- `cv.wrapAffine(src, Matrix, size)` :

src adalah gambar yang akan mengalami transformasi

Matrix adalah matriks transformasi yang didapat dengan memanggil fungsi `cv.getAffineTransform()`

size adalah ukuran gambar

Langkah-langkah untuk melakukan Affine Transformation adalah sebagai berikut :

1. Membaca gambar yang akan ditranformasi
2. Menentukan tiga titik asal dan titik tujuan transformasi
3. Membuat matriks tranformasi dengan memanggil fungsi `cv.getAffineTransform()`
4. Melakukan Affine Transformation dengan memanggil fungsi `cv.wrapAffine()`

## Image Thresholding

### Simple Thresholding
Membuat nilai pada semua pixel dalam sebuah gambar hanya pada ambang tertentu. Threshold hanya digunakan untuk gambar Gray-scale. Untuk simple thresholding, openCV memiliki fungsi :

`cv.thershold(src, thresh, maxval, type)` :

src adalah gambar input

thresh adalah ambang yang dibuat

maxval adalah nilai pixel terbesar

type adalah tipe thresholding. Tipe ini dibagi menjadi :

- cv.THRESH_BINARY
- cv.THRESH_BINARY_INV
- cv.THRESH_TRUNC
- cv.THRESH_TOZERO
- cv.THRESH_TOZERO_INV

### Adaptive Thresholding
Thresholding namun dengan ambang yang lebih sesuai yang didapat dari mengidentifikasi di sekitar pixel tersebut. Untuk Adaptive Threshold digunakan fungsi :

`cv.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)`

src adalah gambar input

maxvalue adalah nilai pixel terbesar

adaptiveMethod adalah metode adaptasi untuk thresholding. Terdapat 2 metode yaitu :
- cv.ADAPTIVE_THRESH_MEAN_C: nilai ambangnya adalah rata-rata pixel sekitar dikurangi C
- cv.ADAPTIVE_THRESH_GAUSSIAN_C: nilai ambangnya adalah penjumlahan Gauss pixel sekitar dikurangi C.

thresholdType adalah tipe thresholding yang digunakan

blockSize adalah rentang sekitar

C adalah konstanta untuk menentukan ambang

### Otsu's Binaryzation
Mencari nilai thresh yang optimal secara otomatis. Dilakukan dengan cara menambahkan tipe tambahan pada threshold yang bernama `cv.THRESH_OTSU`. Hasil dari Otsu's binaryzation akan lebih maksimal apabila sebelumnya gambar difilter terlebih dahulu dengan memanggil fungsi `cv.GaussianBlur(src, ksize, sigmaX)`.

Langkah-langkah mengimplementasikan Otsu's Binaryzation :

1. Membaca gambar input
2. Memfilter gambar dengan memanggil fungsi `cv.GaussianBlur()`
3. Melakukan thresholding dengan tipe tambahan `cv.THRESH_OTSU`

## Smoothing Image

### Image Filtering
Gambar juga dapat difilter. Memfilter gambar bertujuan untuk menghilangkan noise, membuat gambar blur, dan lain sebagainya. Untuk memfilter sebuah gambar diperlukan fungsi `cv.filter2D(src, depth, kernel)`.

### Image Bluring/Image Smoothing

#### Averaging
Menggabungkan box filter yang umum dengan gambar. Sistemnya adalah mengambil pixel yang berada di bawah kernel dan menggantikannya dengan pixel tengah. Smoothing averaging dilakukan dengan memanggil fungsi `cv.blur(src, size)` atau `cv.boxFilter()`.

#### Gaussian Bluring
Memfilter gambar menggunakan box filter yang didalamnya terdapat Gaussian kernel. Untuk melakukan Gaussian Bluring dapat memanggil fungsi `cv.GaussianBlur(src, ksize, sigmaX)`. Jika ingin membuat Gauss kernel sendiri bisa memanggil fungsi `cv.getGaussianKernel()`.

#### Median Bluring
Mengambil pixel yang berada di bawah kernel dan diganti dengan niai median. Untuk melakukan median-bluring diperlukan memanggil fungsi `cv.medianBlur(src, size)`

#### Bilateral Filtering
Hampir sama seperti Gaussian bluring, hanya saja jika Gaussian bluring memperhatikan pixel terdekat, jika bilateral filtering memeperhatikan berdasarkan intensitas yang sama. Bilateral filtering dianggap lebih optimal. Untuk melakukannya dapat memanggil fungsi `cv.bilateralFilter()`

