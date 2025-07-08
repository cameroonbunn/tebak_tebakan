username = ["andi", "budi", "cici"]
password = ["123", "456", "789"]
welcoming = "Selamat Datang di Buncem Games"

input_user = input("Masukkan username: ")
input_pass = input("Masukkan password: ")
    
if input_user in username and input_pass in password:
    index = username.index(input_user)
    if password[index] == input_pass:
        print("Login berhasil!")
        
        print("**************************************")
        print(f"****{welcoming}****")
        print("**************************************")
        print('''
        Perhatihan Pilihan di Bawah!
        1. Anjing
        2. Kucing
        3. Burung      
        ''')
        pilihan_1 = input("Manakah hewan peliharaan yang paling setia? [1/2/3] : ")
        if pilihan_1 == "1":
            print("Benar! Anjing adalah hewan peliharaan yang paling setia!")
            
            print('''
            1. Sepak Bola
            2. Basket
            3. Badminton
            ''')
            pilihan_2 = input("Taufik Hidayat adalah juara dunia di cabang olahraga? [1/2/3] : ")
            if pilihan_2 == "3":
                print("Benar! Taufik Hidayat adalah juara dunia di cabang olahraga Badminton!")
                
                print('''
                1. Jakarta
                2. Surabaya
                3. Bandung
                ''')
                pilihan_3 = input("Kota manakah yang dikenal dengan julukan Kota Kembang? [1/2/3] : ")
                if pilihan_3 == "3":
                    print("Benar! Bandung dikenal dengan julukan Kota Kembang!")
                    print("Selamat, kamu telah menyelesaikan permainan ini!")
                else:
                    print("Maaf, pilihan anda belum sesuai!")
                    exit()
            else:
                print("Maaf, pilihan anda belum sesuai!")
                exit()
        else:
            print("Maaf, pilihan anda belum sesuai!")
            exit()
    else:
        print("Password salah!")
else:
    print("Username tidak ditemukan!")