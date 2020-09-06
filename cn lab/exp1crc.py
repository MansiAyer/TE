
g = "1011"
n = 3
print("g is " + g)
d = input("input: \n")
print (d + " is data") 


def xor(a, b): 
    result = [] 
   
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
   
    return ''.join(result) 
   
   
def mod2div(divident, divisor): 
   
    pick = len(divisor) 
   
    tmp = divident[0 : pick] 
   
    while pick < len(divident): 
   
        if tmp[0] == '1': 
             tmp = xor(divisor, tmp) + divident[pick] 
   
        else:  
            tmp = xor('0'*pick, tmp) + divident[pick] 
   
        pick += 1
   
    if tmp[0] == '1': 
        tmp = xor(divisor, tmp) 
    else: 
        tmp = xor('0'*pick, tmp) 
   
    checkword = tmp 
    return checkword 
   
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
ansEn = encode(d,g) 
print("\n" + ansEn + " encoded") 
  
#decoding  
ansDe = decode( ansEn, g) 
print("\n" +ansDe) 
  
#checking 
if ansDe == '000': 
    print("\n" + "no error") 
else: 
    print("\n" + "Error") 