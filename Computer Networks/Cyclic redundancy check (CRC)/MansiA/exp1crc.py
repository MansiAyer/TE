g = "1011"
n = 3
print("g is " + g)
d = input("input: \n")
print ("given data is " + d) 

def xor(x, y): 
    xorred = [] 
    for i in range(1, len(y)): 
        if x[i] == y[i]: 
            xorred.append('0') 
        else: 
            xorred.append('1') 
    return ''.join(xorred) 
   
def mod2div(divn, divs): #divide data by generator to get remainder, if remainder is zero then data is valid else invalid
    z = len(divs) 
    t_q = divn[0 : z] #to ensure data and gen are of same length in each cycle of division
    while z < len(divn): 
        if t_q[0] == '1': 
             t_q = xor(divs, t_q) + divn[z] 
        else:  
            t_q = xor('0'*z, t_q) + divn[z] #storing remainder from each digit in temp output
   
        z += 1
    if t_q[0] == '1': 
        t_q = xor(divs, t_q) 
    else: 
        t_q = xor('0'*z, t_q) 
    outp = t_q #final remainder after all cycles of dividing data
    return outp 
   
def encode(a, b): 
    big = a + '000' 
    crc = mod2div(big, b) 
    en = a + crc 
    return en       

def decode(a, b): 
    big = a + '000' 
    rem = mod2div(big, b) 
    return rem 

#encoding  
Enc = encode(d,g) 
print("\n" + Enc + " is encoded data") 
  
#decoding  
f_rem = decode( Enc, g)  
print("\n" + f_rem + " is remainder after decoding data")

#checking output remainder after decoding encoded data
if f_rem == '000': 
    print("\n" + "data received without error") 
else: 
    print("\n" + "Error during data transmission") 