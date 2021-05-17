a = 2
print(a)

# проверить число на одинаковые цифры
value = '1111'
print(len(value) == value.count(value[0]))


n = 0
d = set()
st = 0
print(d)
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