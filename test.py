a = 2
print(a)

# %%проверить число на одинаковые цифры
value = '1111'
len(value) == value.count(value[0])

# %%проверить число на одинаковые цифры
value = '1111'
print(len(value) == value.count(value[0]))

# %%test
n = 0
d = set()
st = 0
s = 'МОЛОКО'
for a in s:
    for b in s:
        for c in s:
            for k in s:
                for e in s:
                    for f in s:
                        st = a + b + c + k + e + f
                        if st.count('М') == s.count('М') and st.count('О') == s.count('О') and st.count('Л') == s.count('Л') and st.count('К') == s.count('К'):
                            d.add(st)
print(d)
print(len(d))


# %% определите максимально возможное количество цифр 3 которое может получиться в результате применения представленного ниже алгоритма в строке состояющей из 30 цифр, 30 цифр 4 и 30 цифр 5, идущих в произвольномм порядке
s = '4' * 30 + '5' * 30 + '3' * 30
while ('43' in s) or ('53' in s):
  if '43' in s:
    s = s.replace('43', '33', 1)
  else:
    s = s.replace('53', '433', 1)
print(s.count('3'))

# %% какая строка получится в результате применения приведённой ниже программы к строке, состояющей из 128 идущих подряд "4" и следом идущих подряд 67 "7". В ответ запишите полученную строку
s = '4' * 128 + '7' * 67
while ('444' in s) or ('7777' in s):
  if '444' in s:
    s = s.replace('444', '7', 1)
  else:
    s = s.replace('7777', '44', 1)
print(s)

# %% Узнать длину самого длинного числа из строчки
def fun(x):
    a = 0
    while x > 0:
        a += 1 
        x //= 10
    return a
    
max_value = 0
value1 = '123 123456'
value1 = value1.split()
for i in value1:
    if fun(int(i)) > max_value:
        max_value = fun(int(i))
print(max_value)

# %% делители
def f2(n):
  k = 1
  d = 2
  n = 0
  while n > d * d:
    if n % d == 0:
      k = k + 2
      d = d + 1
      if k > 2:
          break
  if n == d * d:
    k = k + 1
  if k == 2:
    return 1
  else:
    return 0

for x in range (20):
    print(f2(x))

for i in range(191600, 192020 + 1):
    if f2(i) == 1:
        d = 2
        while i > d * d:
            if i % d == 0:
                print(i, i // d)
            d = d + 1
