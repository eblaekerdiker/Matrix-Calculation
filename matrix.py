import numpy
import numpy as np
import random
def isNumber(x):
    if type(x) == int:
         return True
    else:
         return False
rand_matrix1 = []
num = int(input("Hangi işlemi yapmak istediğinizi seçin: Toplama için 1, çıkarma için 2, çarpma için 3 e basın"))
if num==1:
    secim = int(input("Sayıları rastgele girmek istiyorsanız 1'i, elle girmek istiyorsanız 2'yi tuşlayınız"))
    if secim==1:
        RR = int(input("Random matrix 1 in satır boyutunu girin:"))
        RC = int(input("Random matrix 1 in sütun boyutunu girin:"))
        if isNumber(RR) and isNumber(RC):
            deger= print("Matrix 1 içindeki değerleri girin")
        else:
            print("Enter a valid number")
        if isNumber(deger):
            for i in range(RR):  # bu kod satır değerleri için
                a = []
                for j in range(RC):  # sütun değerleri için
                    a.append(int(input()))
                rand_matrix1.append(a)
            for i in range(RR):
                for j in range(RC):
                    print(rand_matrix1[i][j], end=" ")
                print()
        else:
            print("enter a valid number")



