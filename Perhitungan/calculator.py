def calculator():
    print("\n\t===========================================")
    print("\tProgram Kalkulator Sederhana")
    print("\t============================================")
    print("\t1. Penjumlahan")
    print("\t2. Pengurangan")
    print("\t3. Pembagian")
    print("\t4. Perkalian")
    print("\t===========================================")
    print("\tSilahkan pilih 1-4")
    print("  ")
    pil = input("\tMasukan pilihan :")
    if pil == "1":
        tambah()
    elif pil == "2":
        kurang()
    elif pil == "3":
        bagi()
    elif pil == "4":
        kali()
    else:
        print ("\tMaaf, input yangAnda masukkan salah")
        print ("\tCoba ulangi kembali")
        tanya ()


def tambah ():
    print("\t1. penjumlahan")
    a = int(input("\tMasukan nilai x= "))
    b = int(input("\tMasukan nilai y= "))
    c = a+b
    print ("\tx+y=",c)
    tanya ()
def kurang ():
    print("\t2. Penguranagn")
    a = int(input("\tMasukan nilai x= "))
    b = int(input("\tMasukan nilai y= "))
    c = a-b
    print ("\tx-y=",c)
    tanya ()
def bagi ():
    print("\t3. Pembagian")
    a = int(input("\tMasukan nilai x= "))
    b = int(input("\tMasukan nilai y= "))
    c = a/b
    print ("\tx/y=",c)
    tanya ()
def kali():
    print("\t4. Perkalian")
    a = int(input("\tmasukan nilai x= "))
    b = int(input("\tMasukan nilai y= "))
    c = a*b
    print ("\tx*y=",c)
    tanya()


def menu():
    print("\n\t===========================================")
    print("\tProgram Kalkulator Sederhana")
    print("\t============================================")
    print("\t1. Penjumlahan")
    print("\t2. Pengurangan")
    print("\t3. Pembagian")
    print("\t4. Perkalian")
    print("\t===========================================")
    print("\tSilahkan pilih 1-4")
    print("  ")
    pil = input("\tMasukan pilihan :")
    if pil == "1":
        tambah()
    elif pil == "2":
        kurang()
    elif pil == "3":
        bagi()
    elif pil == "4":
        kali()
    else:
        print ("\tMaaf, input yangAnda masukkan salah")
        print ("\tCoba ulangi kembali")
        tanya ()
def tanya():
    tanya = input("\n\tKembali ke menu calculator (y/n)? ")
    if tanya == "y" :
        menu()
    elif tanya == "n":
        exit
    else:
        print ("\n\tSalah input..........!!!")

calculator()
    
            
