# tìm các số nguyên tố từ 0 đến 100 dùng vòng lặp for
print(2)
print(3)
for i in range(5,100):
    c = int(i/2)
    for j in range(2,c):
        if i%j == 0 :
          break
    else:
            print(i)


