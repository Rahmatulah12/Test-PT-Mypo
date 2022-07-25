# make input telp, maximal length is 20
def input_telp():
    telp = input("Masukkan nomor telepon: ")
    if len(telp) > 20:
        print("Nomor telepon terlalu panjang")
        exit()
    new_telp = format_telp2(telp)
    print(new_telp)

def format_telp(input_telp):
    telp = input_telp.replace("-", "")
    new_telp = ""
        
    j = 0
    for string in telp :
        j += 1
        new_telp += string
        if j % 3 == 0 :
            new_telp += "-"       
    
    return new_telp.rstrip("-")

def format_telp2(input_telp) :
    digits = ""
    blk = ""
    for i in input_telp:
        if i.isnumeric():
            blk += i
        if len(blk) == 3:
            digits += blk+"-"
            blk = ""

    if len(blk) == 0:
        return digits[:-1]
    elif len(blk) == 1:
        return digits[:-2]+"-"+digits[-2]+blk
    elif len(blk) == 2:
        return digits+blk
    
if __name__ == "__main__" :
    input_telp()