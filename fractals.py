import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')

#warna yang dipilih, ditulis dalam kurung siku dengan nilai R, G, B
WARNA = np.array([[0/255, 153/255, 255/255], [255/255, 153/255, 0],
                  [51/255, 255/255, 0/255], [0, 250/255, 138/255],[0.0, 38/255, 252/255],
                  [76/255., 250/255., 0.0], [0.0, 250/255., 23/255], [0.0, 250/255., 158/250]])

#polinomial yang dicari, ditulis dalam kurung siku dengan nilai-nilai koefisiennya
polinomial = np.poly1d([0,1,0,-2,0,-1])
turunan_polinomial = polinomial.deriv()
akar_polinomial = np.roots(polinomial)

#pembentukan bidang kompleks
resolusi_titik = 1600
x = np.linspace(-2, 2, resolusi_titik)
y = np.linspace(-2, 2, resolusi_titik)
X, Y = np.meshgrid(x,y)
img = plt.scatter(X,Y)
z = X + Y*1j

#iterasi-iterasi di bidang kompleks, dan ngewarnainnya
for i in range(50):
    z = z - polinomial(z)/turunan_polinomial(z)
kedekatan = 0.001
Z_T = []
for r in polinomial.roots:
    Z_T.append(abs(z-r) < kedekatan)

colored_arr = np.zeros(shape=(resolusi_titik, resolusi_titik, 3))

for i in range(resolusi_titik):
    for j in range(resolusi_titik):
        for k, z_t in enumerate(Z_T):
            if z_t[i][j]:
                colored_arr[i][j] = WARNA[k]

#output gambarnya
plt.figure(figsize=(15,15))
plt.imshow(colored_arr)
plt.savefig('filename1-4', dpi=300)