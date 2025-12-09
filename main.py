# 1 - misol
kvadrat = tuple(n**2 for n in range(1, 21) if n % 2 == 0)
print(kvadrat)

# 2 - misol
_3ga_karrali_sonlar = tuple(n for n in range(1, 51) if n % 3 == 0)
print(_3ga_karrali_sonlar)

# 3 - misol
uzunlik = tuple(len(w) for w in ["python", "tuple", "set", "loop"])
print(uzunlik)

# 4 - misol
juftlar_yigindisi = tuple(n for n in range(1, 101) if sum(int(d) for d in str(n))%2==0)
print(juftlar_yigindisi)

# 5 - misol
first_letters = tuple(w[0] for w in ["python", "tuple", "set", "loop"])
print(first_letters)
