"""Trendyol Kargo Fiyatları
        0.00 - 19.99 = 2.99TL
        20.00 - 29.99 = 4.48TL
        30.00 - 49.99 = 8.26TL
        50.00TL ve üstü = 11.00TL"""
"""Formül:
        Ürün Fiyatı + Kargo Bedeli+ Komisyon Bedeli"""
"""Komisyon Bedelleri:
        Tuhafiye=%16
        Sanatsal=%14"""
platform=int(input("1)Trendyol\t2)Hepsiburada :\t"))
if platform==1:
    while True:
        kategori=int(input("\n\t1)%14\t2)%15\t3)%16 :\t\t"))

        if kategori==1:
            while True:
                hamfiyat=float(input("\nEklemek istediğiniz ürün  Fiyatı:\t"))
                if (hamfiyat>0.00 and hamfiyat<=19.99):
                     maaliyetlisatis =(hamfiyat + 3.00) * 1.16 #maaliyetli bedelimiz
                     print("######\t",maaliyetlisatis, "TL" "\t######" )
                     cikis = input("\nÇıkmak için 'q'ya bas:\t")
                     if cikis == "q":
                         break
                elif (hamfiyat>=20.00 and hamfiyat<=29.99):
                    maaliyetsatis=(hamfiyat+4.50) * 1.16
                    print("######\t",maaliyetsatis, "TL" "\t######")
                    cikis = input("\nÇıkmak için 'q'ya bas:\t")
                    if cikis == "q":
                        break
                elif (hamfiyat>=30.00 and hamfiyat<=49.99):
                    maaliyetsatis = (hamfiyat + 8.30) * 1.16
                    print("######\t",maaliyetsatis, "TL" "\t######")
                    cikis = input("\nÇıkmak için 'q'ya bas:\t")
                    if cikis == "q":
                        break
                elif (hamfiyat>=50.00):
                    maaliyetsatis = (hamfiyat + 11.00) * 1.16
                    print("######\t",maaliyetsatis, "TL" "\t######")
                    cikis = input("\nÇıkmak için 'q'ya bas:\t")
                    if cikis == "q":
                        break
                else:
                    print("Fiyat negatif olamaz")
                    break

        elif kategori==2:
            while True:
                hamfiyat=float(input("\nEklemek istediğiniz ürünün fiyatı:\t"))
                if (hamfiyat>0.00 and hamfiyat<=19.99):
                     maaliyetlisatis =(hamfiyat + 3.00) * 1.175 #maaliyetli bedelimiz
                     print("######\t",maaliyetlisatis, "TL" "\t######" )
                     cikis = input("\nÇıkmak için 'q'ya bas:\t")
                     if cikis == "q":
                         break
                elif (hamfiyat>=20.00 and hamfiyat<=29.99):
                    maaliyetsatis=(hamfiyat+4.50) * 1.175
                    print("######\t",maaliyetsatis, "TL" "\t######")
                    cikis = input("\nÇıkmak için 'q'ya bas:\t")
                    if cikis == "q":
                        break
                elif (hamfiyat>=30.00 and hamfiyat<=49.99):
                    maaliyetsatis = (hamfiyat + 8.30) * 1.175
                    print("######\t",maaliyetsatis, "TL" "\t######")
                    cikis = input("\nÇıkmak için 'q'ya bas:\t")
                    if cikis == "q":
                        break
                elif (hamfiyat>=50.00):
                    maaliyetsatis = (hamfiyat + 11.00) * 1.175
                    print("######\t",maaliyetsatis, "TL" "\t######")
                    cikis = input("\nÇıkmak için 'q'ya bas:\t")
                    if cikis == "q":
                        break
                else:
                    print("Fiyat negatif olamaz")
                    break

        elif kategori==3:
            while True:
                hamfiyat = float(input("\nEklemek istediğiniz ürünün fiyatı:\t"))
                if (hamfiyat>0.00 and hamfiyat<=19.99):
                     maaliyetlisatis =(hamfiyat + 3.00) * 1.19 #maaliyetli bedelimiz
                     print("######\t",maaliyetlisatis, "TL" "\t######" )
                     cikis = input("\nÇıkmak için 'q'ya bas:\t")
                     if cikis == "q":
                         break
                elif (hamfiyat>=20.00 and hamfiyat<=29.99):
                    maaliyetsatis=(hamfiyat+4.50) * 1.19
                    print("######\t",maaliyetsatis, "TL" "\t######")
                    cikis = input("\nÇıkmak için 'q'ya bas:\t")
                    if cikis == "q":
                        break
                elif (hamfiyat>=30.00 and hamfiyat<=49.99):
                    maaliyetsatis = (hamfiyat + 8.30) * 1.19
                    print("######\t",maaliyetsatis, "TL" "\t######")
                    cikis = input("\nÇıkmak için 'q'ya bas:\t")
                    if cikis == "q":
                        break
                elif (hamfiyat>=50.00):
                    maaliyetsatis = (hamfiyat + 11.00) * 1.19
                    print("######\t",maaliyetsatis, "TL" "\t######")
                    cikis = input("\nÇıkmak için 'q'ya bas:\t")
                    if cikis == "q":
                        break
                else:
                    print("Fiyat negatif olamaz")
                    break
        else:
            print("Böyle bir kategori bulunmamakta")
elif platform==2:
    """KARGO FİYATLARI:
            29.99TL üstü 11.50TL
            29.99 altı 5.90TL"""
    while True:
        kategori=int(input("1)%14\t2)%16 : \t"))
        if kategori==1:
            hamfiyat = float(input("Eklemek istediğiniz ürünün fiyatı:\t"))
            if (hamfiyat<=29.99):
                maaliyetlisatis = (hamfiyat + 6.00) * 1.215 # maaliyetli bedelimiz
                print("######\t",maaliyetlisatis, "TL" "\t######")
                cikis = input("\nÇıkmak için 'q'ya bas:\t")
                if cikis == "q":
                    break
            elif (hamfiyat>=30.00):
                maaliyetsatis = (hamfiyat + 11.50) * 1.215
                print("######\t",maaliyetsatis, "TL" "\t######")
                cikis = input("\nÇıkmak için 'q'ya bas:\t")
                if cikis == "q":
                    break
            else:
                print("Fiyat negatif olamaz")
                break
        elif kategori==2:
            hamfiyat = float(input("Eklemek istediğiniz ürünün fiyatı:\t"))
            if (hamfiyat <= 29.99):
                maaliyetlisatis = (hamfiyat + 6.00) * 1.23  # maaliyetli bedelimiz
                print("######\t", maaliyetlisatis, "TL" "\t######")
                cikis = input("\nÇıkmak için 'q'ya bas:\t")
                if cikis == "q":
                    break
            elif (hamfiyat >= 30.00):
                maaliyetsatis = (hamfiyat + 11.50) * 1.23
                print("######\t", maaliyetsatis, "TL" "\t######")
                cikis = input("\nÇıkmak için 'q'ya bas:\t")
                if cikis == "q":
                    break
            else:
                print("Fiyat negatif olamaz")
                break









