# make input telp, maximal length is 20
def input_telp():
    telp = input("Masukkan nomor telepon: ")
    if len(telp) > 20:
        print("Nomor telepon terlalu panjang")
        exit()
    new_telp = format_telp(telp)
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
    
if __name__ == "__main__" :
    input_telp()