# Tugas2-magang-Ichiro
Belajar OpenCV

## Optional Project
Mendeteksi warna merah di dalam warna biru.

### Import
Menggunakan cv2 sebagai cv dan numpy sebagai np.

```
import numpy as np
import cv2 as cv
```

### Mengambil video
Membuka camera dan mengambil video dari webcam.

```
vid=cv.VideoCapture(0)
```

### Mengambil gambar
Melakukan perulangan untuk setiap gambar dalam video dan memuat gambar tersebut. Kemudian merubah color-space nya dari BGR ke HSV. 

```
_, im = vid.read()
imhsv = cv.cvtColor(im, cv.COLOR_BGR2HSV)
```

### Mendeteksi warna biru
Langkah-langkah mendeteksi benda berwarna biru :

1. Menentukan batas atas dan batas bawah warna biru
2. Membatasi gambar dengan warna biru
3. Melakukan median blur
4. Melakukan thresholding
5. Mencari contours dan menyimpannya

```
upper_blue=np.array([120,255,255])
lower_blue=np.array([90,50,50])

mask1=cv.inRange(imhsv, lower_blue, upper_blue)
mask1=cv.medianBlur(mask1, 11)
ret,thresh1 = cv.threshold(mask1,127,255,cv.THRESH_BINARY)
contours1, hierarchy = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
```

### Mendeteksi warna merah
Langkah-langkah mendeteksi benda berwarna merah :

1. Menentukan batas atas dan batas bawah warna merah
2. Membatasi gambar dengan warna merah
3. Melakukan thresholding
4. Mencari contours dan menyimpannya

```
upper_red=np.array([180, 255, 255])
lower_red=np.array([170,100,50])

mask2=cv.inRange(imhsv, lower_red, upper_red)
ret,thresh2 = cv.threshold(mask2,127,255,cv.THRESH_BINARY)
contours2, hierarchy = cv.findContours(thresh2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
```

### Memberi kotak pada benda biru
Langkah-langkah memberi kotak pada benda terdeteksi berwarna biru :

1. Mendapatkan area setiap kontur-kontur dan membatasinya
2. Mencari kotak pada kontur dengan pendekatan boundingRect
3. Membuat kotak sesuai hasil pendekatan
4. Memberi nama pada kotak

```
for contour1 in contours1 :
  cnt1=contour1
  area=cv.contourArea(cnt1)
  if(area>200) :
    x1,y1,w1,h1 = cv.boundingRect(cnt1)
    cv.rectangle(im,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
    cv.putText(im, "Blue Color", (x1, y1), cv.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0))
```

### Memberi kotak pada benda merah dalam background biru
Langkah-langkah memberi kotak pada benda terdeteksi berwarna merah :

1. Mendapatkan area setiap kontur-kontur dan membatasinya
2. Mencari kotak pada kontur dengan pendekatan boundingRect
3. Membandingkan hasil pendekatan pada kontur merah dan biru
4. Apabila kontur merah ada di dalam kontur biru maka buat kotak kontur merah
5. Memberi nama kotak kontur merah

```
for contour2 in contours2 :
        cnt2=contour2
        x2,y2,w2,h2 = cv.boundingRect(cnt2)
        for contour1 in contours1 :
            cnt1=contour1
            area=cv.contourArea(cnt2)
            if(area>200) :
                x1,y1,w1,h1 = cv.boundingRect(cnt1)

                if (x2>x1 and x2<(x1+w1)) and (y2>y1 and y2<(y1+h1)):
                    cv.rectangle(im,(x2,y2),(x2+w2,y2+h2),(0,0,255),2)
                    cv.putText(im, "Red Color", (x2, y2), cv.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255))
```

### Menampilkan gambar

```
    cv.imshow('res', im)
    cv.imshow('mask1', thresh1)
    cv.imshow('mask2', thresh2)
```
