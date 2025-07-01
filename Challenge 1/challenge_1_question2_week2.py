import codecs
x="43104f0c32077b0230455f346e5e77285868722d345a643b6256350636027d77"
e=''
for i in range(0,len(x),4) :
    a=x[i:i+2]
    b=x[i+2:i+4]
    c=int(a,16)^int(b,16)
    e +=format(int(a,16), '02x')+format(c, '02x')
print((codecs.decode(e,"hex")))
