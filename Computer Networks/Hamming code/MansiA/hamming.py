#explanation here https://www.geeksforgeeks.org/hamming-code-in-computer-network/

d = input("input: ")
print ("\ngiven data is " + d) 
m = len(d)


def parity(arr, b):
    n = len(arr)
    for i in range(b): 
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)): 
                val = val ^ int(arr[-1 * j])
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:] 
    return arr 
def numR(m): 
    for i in range(m): 
        if(2**i >= m + i + 1): 
            return i 
def findRs(a, b): 
    i = 0
    j = 1
    m = len(a) 
    Rloc = '' 
    for k in range(1, m + b+1): 
        if(k == 2**i): 
            Rloc = Rloc + '0'
            i += 1
        else: 
            Rloc = Rloc + a[-1 * j] 
            j += 1
    return Rloc[::-1]  

def detErr(arr, b):
    n = len(arr) 
    re = 0
    for i in range(b): 
        x = 0
        for j in range(1, n + 1): 
            if(j & (2**i) == (2**i)): 
                x = x ^ int(arr[-1 * j])
        re = re + x*(10**i)
    return int(str(re), 2)  

r = numR(m) 
hamc = findRs(d, r) 
hamc = parity(hamc, r) 
print("data transferred is " + hamc) 

hamcErr = input("\nrecieved input: ")
print("\nreceived data is " + hamcErr) 
corr = detErr(hamcErr, r)
if(corr != 0):
    print("error is at position " + str(corr))
else:
    print("no error in received data")