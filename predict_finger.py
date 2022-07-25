def input_n() :
    n = input("Masukkan Jumlah N: ")
    
    # check if n is not number
    if not n.isdigit() :
        print("N harus berupa angka")
        exit()
    
    n = int(n)
    if n > 100 :
        print("N tidak boleh lebih dari 100")
        exit()
    fingers = [
        'kelingking tangan kiri', 
        'jari manis tangan kiri',
        'jari tengah tangan kiri',
        'jari telunjuk tangan kiri', 
        'ibu jari tangan kiri',
        'kelingking tangan kanan', 
        'jari manis tangan kanan',
        'jari tengah tangan kanan',
        'jari telunjuk tangan kanan', 
        'ibu jari tangan kanan'
    ]
    finger = ''
    index_finger = 0
    i = 1
    while i <= n :
        finger = fingers[index_finger]
        index_finger += 1
        if i % 10 == 0 :
            index_finger = 0
        i += 1
    print(f"Jumlah {n} adalah {finger}")
    


if __name__ == "__main__" :
    input_n()