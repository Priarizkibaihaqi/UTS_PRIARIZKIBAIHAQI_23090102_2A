def hitung_bmi ():
    berat_badan = int(input("masukan berat badan (kg) : "))
    tinggi_badan = float(input("masukan tinggi badan (m) : "))

    hasil_bmi = float(berat_badan / (tinggi_badan ** 2))
    print (f"berat badan : {berat_badan} kg")
    print (f"tinggi badan : {tinggi_badan} m")
    print(f"Nilai bmi anda : {hasil_bmi}")
    if hasil_bmi < 18.5 :
        print("berat badan kurang")
    elif hasil_bmi >= 18.5 and hasil_bmi < 24.9 :
        print("berat badan normal")
    elif hasil_bmi >= 25 and hasil_bmi < 29.9:
        print("Kelebihan berat badan")
    else :
        print("Obesitas")