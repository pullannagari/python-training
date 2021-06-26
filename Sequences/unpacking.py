a = b = c = d = e = f = 12
print(c)

x, y = 1, 2  #unpacking a tuple
print(x)
print(y)

print("Unpacking a tuple")
data = 1, 2, 3
l, m, n = data
print(l)
print(m)
print(n)

#p, q = data  # cannot unpack, too many values to unpack
# print(p)
# print(q)

print("unpacking a list")  # we can unpack any sequence type including list
data_list = [12, 13, 14]
p, q, r = data_list
print(p)
print(q)
print(r)