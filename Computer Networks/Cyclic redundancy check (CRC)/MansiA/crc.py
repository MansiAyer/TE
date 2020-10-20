d = int(input("data in binary: "))
g = int(input("generator in binary: "))
#accept polyn idk what polynomial is but
# explanation of crc https://ecomputernotes.com/computernetworkingnotes/communication-networks/cyclic-redundancy-check
# 
print ('Hello World')
print (d)
print (g)

#code from this site https://www.geeksforgeeks.org/cyclic-redundancy-check-python/
#bit edited, works, but idk if it's right
def xor(a, b): 
   
    # initialize result 
    result = [] 
   
    # Traverse all bits, if bits are 
    # same, then XOR is 0, else 1 
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
   
    return ''.join(result) 
   
   
def mod2div(divident, divisor): 
   
    # Number of bits to be XORed at a time. 
    pick = len(divisor) 
   
    # Slicing the divident to appropriate 
    # length for particular step 
    tmp = divident[0 : pick] 
   
    while pick < len(divident): 
   
        if tmp[0] == '1': 
   
            # replace the divident by the result 
            # of XOR and pull 1 bit down 
            tmp = xor(divisor, tmp) + divident[pick] 
   
        else:   # If leftmost bit is '0' 
  
            # If the leftmost bit of the dividend (or the 
            # part used in each step) is 0, the step cannot 
            # use the regular divisor; we need to use an 
            # all-0s divisor. 
            tmp = xor('0'*pick, tmp) + divident[pick] 
   
        # increment pick to move further 
        pick += 1
   
    # For the last n bits, we have to carry it out 
    # normally as increased value of pick will cause 
    # Index Out of Bounds. 
    if tmp[0] == '1': 
        tmp = xor(divisor, tmp) 
    else: 
        tmp = xor('0'*pick, tmp) 
   
    checkword = tmp 
    return checkword 
   
def encodeData(data, key): 
   
    l_key = len(key) 
   
    # Appends n-1 zeroes at end of data 
    appended_data = data + '0'*(l_key-1) 
    remainder = mod2div(appended_data, key) 
   
    # Append remainder in the original data 
    codeword = data + remainder 
    return codeword     
    

def decodeData(data, key): 
   
    l_key = len(key) 
   
    # Appends n-1 zeroes at end of data 
    appended_data = data + '0'*(l_key-1) 
    remainder = mod2div(appended_data, key) 
   
    return remainder 


d = list(input("Enter data you want to send->")) 
#s.sendall(input_string) 
data =(''.join(format(ord(x), 'b') for x in d)) 
print (data) 
g = "101"
  
ansEn = encodeData(data,g) 
print(ansEn) 
  
  
ansDe = decodeData(data, g) 
print("Remainder after decoding is->"+ansDe) 
  
# If remainder is all zeros then no error occured 
temp = "0" * (len(g) - 1) 
if ansDe == temp: 
    print("THANK you Data ->"+data + " Received No error FOUND") 
else: 
    print("Error in data") 

#
#end of first code
#


#code from this site https://www.tutorialspoint.com/python-program-to-cyclic-redundancy-check
#unedited, untested, idk what's going on here but look python has a predefined crc library?? USE
frompycrc.crclib import *
def main():
#-----------------------------------------------------------------------------
#Sender Side
div = str(input("Input divisor in binary type: "))
#user_dataword = str(raw_input("Input dataword in binary type: "))
userdataword = '1001'
print ("\nSender:")
sen = Sender(bin2dec(userdataword), div)
sen.send()
print ("arg_dataword:", sen.arg_dataword2)
print ("remainder:", sen.remainder2)
print ("codeword:", sen.codeword2)
#-----------------------------------------------------------------------------
#Channel
print ("\nChannel:")
ch = Channel(sen.codeword)
print ("Through to the channel get channel codeword:", dec2bin(ch.ch_codeword))
#-----------------------------------------------------------------------------
#Receiver Side
print ("\nReceiver:")
rcv = Receiver(ch.ch_codeword, div)
rcv.receive()
print ("syndrome:", rcv.syndrome2)
print ("Discard or not?", rcv.discard)
print ("rx_dataword:", rcv.rx_dataword2)
if __name__ == '__main__':
   main()


#
#end of second code 
#

#modified working code

g = "1011"
n = 3
print("g is " + g)
d = input("input: \n")
print (d + " is data") 


def xor(a, b): 
   # initialize result 
    result = [] 
   
    # Traverse all bits, if bits are 
    # same, then XOR is 0, else 1 
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
   
    return ''.join(result) 
   
   
def mod2div(divident, divisor): 
   
    # Number of bits to be XORed at a time. 
    pick = len(divisor) 
   
    # Slicing the divident to appropriate 
    # length for particular step 
    tmp = divident[0 : pick] 
   
    while pick < len(divident): 
   
        if tmp[0] == '1': 
   
            # replace the divident by the result 
            # of XOR and pull 1 bit down 
            tmp = xor(divisor, tmp) + divident[pick] 
   
        else:   # If leftmost bit is '0' 
  
            # If the leftmost bit of the dividend (or the 
            # part used in each step) is 0, the step cannot 
            # use the regular divisor; we need to use an 
            # all-0s divisor. 
            tmp = xor('0'*pick, tmp) + divident[pick] 
   
        # increment pick to move further 
        pick += 1
   
    # For the last n bits, we have to carry it out 
    # normally as increased value of pick will cause 
    # Index Out of Bounds. 
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
print("\n" + ansEn + " is encoded") 
  
#decoding  
ansDe = decode( ansEn, g) 
print("\n" + "Remainder after decoding is "+ansDe) 
  
#checking 
if ansDe == '000': 
    print("\n" + "no error") 
else: 
    print("\n" + "Error") 