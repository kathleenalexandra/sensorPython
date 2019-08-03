

def HextoDec (string):
    ret = 0
    for i,d in enumerate(string) : 
        hex = "0123456789ABCDEF"
        value= hex.index(d) # 0 to 15
        #index = string.index(i)
        power = (len(string) -(i+1)) #power of 16
        ret += (value*16**power)
    return ret 

print(HextoDec("10DE2F8F01001901"))  

