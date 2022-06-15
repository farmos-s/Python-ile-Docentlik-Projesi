import time
import colorama
import pyautogui

from colorama import Fore, Back, Style
import os
import keyboard

colorama.init(autoreset=True)
from texttable import Texttable


class EğitimOgretimFaaliyetleri():
    def __init__(self,
                 # ---------------------------------- uluslararası
                 uluslararsıa=20, uluslararsıb=15,
                 uluslararsıc=5, uluslararası_liste_T_F=[],

                 # -------------------------------------------- ulusal
                 ulusala=8, ulusalb=4,
                 ulusal_makale_sayısı=[], ulusal_liste_T_F=[],
                 toplam_makale=0, ulusal_makale_1_1=0,

                 # -------------------------------------- lisasüstü
                 makale_list=[],
                 lisans_liste_T_F=[],
                 lisans_doc_sonrası=[],
                 lisans_doc_oncesi=[],

                 # --------------------------------------- kitap

                 kitap_liste_T_F=[],

                 #-----------------------------------------Atıflar
                 atıflar_doc_sonrası =[],
                 atıflar_doc_oncesi=[],

                 #-------------------------------------
                 lisansüstü_Tez_tp_puan= [],
                 lisansüstü_Tez_T_F=[],
                 lisansüstü_Tez_doc_oncesi=[],

                 # -------------------------------------- global
                 makale_sayısı=0, basvuran_kısı=0,
                 doktora_sonrası=[], doktora_oncesi=[]

                 ):

        # 1_uluslararası bolum
        self.uluslararsıa = uluslararsıa
        self.uluslararsıb = uluslararsıb
        self.uluslararsıc = uluslararsıc
        self.uluslararası_liste_T_F = uluslararası_liste_T_F

        # 2_ulusal bolum
        self.ulusala = ulusala
        self.ulusalb = ulusalb
        self.ulusal_makale_sayısı = ulusal_makale_sayısı
        self.toplam_makale = toplam_makale
        self.ulusal_liste_T_F = ulusal_liste_T_F
        self.ulusal_makale_1_1 = ulusal_makale_1_1

        # 3_lisasüstü
        self.makale_list = makale_list
        self.lisans_liste_T_F = lisans_liste_T_F
        self.lisans_doc_sonrası = lisans_doc_sonrası
        self.lisans_doc_oncesi = lisans_doc_oncesi

        # 4_kitap
        self.kitap_liste_T_F = kitap_liste_T_F

        # 5_Atıflar
        self.atıflar_doc_sonrası = atıflar_doc_sonrası
        self.atıflar_doc_oncesi = atıflar_doc_oncesi


        # 6_Doktora tez danışmanlığı

        self.lisansüstü_Tez_tp_puan = lisansüstü_Tez_tp_puan
        self.lisansüstü_Tez_T_F = lisansüstü_Tez_T_F






        # global
        self.makale_sayısı = makale_sayısı
        self.basvuran_kısı = basvuran_kısı
        self.doktora_sonrası = doktora_sonrası
        self.doktora_oncesi = doktora_oncesi

    def clear(self):
        """
            Bu fonksiyon terminal penceresini ilk haline getirir.
        """
        # İşletim Sistemi Windows ise
        if os.name == 'nt':
            _ = os.system('cls')
        # İşletim Sistemi MacOS ise
        elif os.name == 'mac':
            _ = os.system('clear')
        # İşletim Sistemi Linux ise
        elif os.name == 'posix':
            _ = os.system('clear')
        # Yabancı bir işletim sistemi ise
        else:
            _ = os.system('clear')
  
    def Lısansustu_Tez_Danışmanlığı  (self):

        time.sleep(1)
        print("""
╒══════════════════════════════════════════════════════════════════════════════╕
│                      6. Lisansüstü Tez Danışmanlığı                          │
╞══════════════════════════════════════════════════════════════════════════════╡
│ Adayın danışmanlığını yürüttüğü tamamlanan lisansüstü tezlerden              │ 
├──────────────────────────────────────────────────────────────────────────────┤
│ a) Doktora tez danışmanlığı                                                  │
├──────────────────────────────────────────────────────────────────────────────┤
│ b) Yüksek lisans tez danışmanlığı                                            │
├──────────────────────────────────────────────────────────────────────────────┤
│ c) Doktora (eş danışmanlık)                                                  │
├──────────────────────────────────────────────────────────────────────────────┤
│ d) Yüksek Lisans (eş danışmanlık)                                            │
├──────────────────────────────────────────────────────────────────────────────┤
│ p) Puan Hesapla                                                              │
├──────────────────────────────────────────────────────────────────────────────┤
│ q) Çıkış Yap                                                                 │
├──────────────────────────────────────────────────────────────────────────────┤
│ * Bu madde kapsamında en fazla 10 puan alınabilir. İkinci/eş danışman olması │
│ durumunda asıl danışman a ve b bentleri için öngörülen puanların tamamını,   │
│ ikinci danışman ise yarısını alır                                            │
╘══════════════════════════════════════════════════════════════════════════════╛
        """)

        while True:


            Lisansüstü_Tez  = input("Lisansüstü Tez Danışmanlığı Hesapla :")
            # -------------------------------------------------------------------------A SECENEGİ

            if Lisansüstü_Tez == "a" or Lisansüstü_Tez == "A":
                print("""--> Doktora tez danışmanlığı :
                                        1.Kaç tane
                                        2.Çıkmak İçin
                        """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------Kaç tane
                    if secenek == "1":

                        Lisansüstü_Tez_sayısı_1 = input("Toplam kaç tane :")
                        try:
                            Lisansüstü_Tez_sayısı_1_1 = int(Lisansüstü_Tez_sayısı_1)
                            self.Lisansüstü_Tez_puan_1= Lisansüstü_Tez_sayısı_1_1 * 4

                            self.lisansüstü_Tez_tp_puan.append(self.Lisansüstü_Tez_puan_1)
                            break
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")


                    elif secenek == "2":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")




            #  --------------------------------------------------------------------------------B SECENEGİ
            elif Lisansüstü_Tez == "b" or Lisansüstü_Tez == "B":
                print("İşleminiz Sorgunalnıyor")
                time.sleep(1)
                print("""--> Yüksek lisans tez danışmanlığı:                                
                                       1.Kaç tane
                                       2.Çıkmak İçin
                               """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------kişi sayısı
                    if secenek == "1":
                        Lisansüstü_Tez_sayısı_2 = input("Toplam kaç tane:")
                        try:
                            self.Lisansüstü_Tez_sayısı_2_1 = int(Lisansüstü_Tez_sayısı_2)
                            self.Lisansüstü_Tez_puan_2 = self.Lisansüstü_Tez_sayısı_2_1 * 2

                            self.lisansüstü_Tez_tp_puan.append(self.Lisansüstü_Tez_sayısı_2)

                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------ makale sayısı

                    elif secenek == "2":
                        break
                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")

            #  ------------------------------------------------------------------C SECENEGİ

            elif Lisansüstü_Tez == "c" or Lisansüstü_Tez == "C":
                print("İşleminiz Sorgunalnıyor")
                time.sleep(1)
                print("""--> Doktora (eş danışmanlık) :
                                                                          
                                        1.Kaç tane
                                        2.Çıkmak İçin
        
                                               """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ---------------------------------------------------------------------------------------------- (kişi sayısı)
                    if secenek == "1":
                        Lisansüstü_Tez_sayısı_3= input("Toplam kaç tane:")
                        try:
                            Lisansüstü_Tez_sayısı_3_1 = int(Lisansüstü_Tez_sayısı_3)
                            self.lisansüstü_Tez_puan = Lisansüstü_Tez_sayısı_3_1 * 2

                            self.lisansüstü_Tez_tp_puan.append(self.Lisansüstü_Tez_puan_3)

                            continue
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")


                    elif secenek == "2":
                        break
                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")

            elif Lisansüstü_Tez == "d" or Lisansüstü_Tez == "D":
                print("İşleminiz Sorgunalnıyor")
                time.sleep(1)
                print("""--> Yüksek Lisans (eş danışmanlık) :
        
                                        1.Kaç tane
                                        2.Çıkmak İçin
        
                                               """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ---------------------------------------------------------------------------------------------- (kişi sayısı)
                    if secenek == "1":
                        Lisansüstü_Tez_sayısı_4 = input("Toplam kaç tane:")
                        try:
                            self.Lisansüstü_Tez_sayısı_4_1 = int(Lisansüstü_Tez_sayısı_4)
                            self.Lisansüstü_Tez_puan_4 = self.Lisansüstü_Tez_sayısı_4_1 * 1

                            self.lisansüstü_Tez_tp_puan.append(self.Lisansüstü_Tez_puan_4)

                            continue
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")


                    elif secenek == "2":
                        break
                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")


            # ------------------------------------------------------------------ toplama işlemi
            elif Lisansüstü_Tez == "p" or Lisansüstü_Tez == "P":

                lisansüstü_Tez_puanı = self.lisansüstü_Tez_tp_puan
                lisansüstü_Tez_toplam_puan= sum(lisansüstü_Tez_puanı)

                if  lisansüstü_Tez_toplam_puan>0:
                    try:
                        if lisansüstü_Tez_toplam_puan > 10:
                            print("Bu maddeden en fazla 10 puan alınabilir ")
                            self.doktora_sonrası.append(10)
                        elif lisansüstü_Tez_toplam_puan < 10:
                            self.doktora_sonrası.append(lisansüstü_Tez_toplam_puan)
                        self.doktora_sonrası_puan()
                        self.doktora_oncesi_puan()



                        soru = input("sistem yenılensın mı (E,H): ")
                        if soru == "e" or soru == "E":
                            self.lisansüstü_Tez_T_F.clear()
                            lisansüstü_Tez_puanı.clear()
                            self.lisansüstü_Tez_T_F.append(True)
                            self.clear()
                        else:
                            self.lisansüstü_Tez_T_F.clear()
                            lisansüstü_Tez_puanı.clear()
                            self.lisansüstü_Tez_T_F.append(True)
                            break


                    except:
                        time.sleep(1)

                elif lisansüstü_Tez_toplam_puan == 0:
                    try:
                        soru_2 = input("Bu tuşa veri girmeden mi bastınız (Evet ise 'E',Hayır ise 'H' tuşuna basınız):")
                        if soru_2 == "e" or soru_2 == "E":
                            self.uluslararası_liste_T_F.clear()
                            print("Lütfen veri giriniz...")
                            break
                        else:
                            if self.uluslararası_liste_T_F == [True]:
                                self.doktora_sonrası_puan()
                                self.doktora_oncesi_puan()
                                break

                    except:
                        print("hata")
                        break

            elif Lisansüstü_Tez =="q" or Lisansüstü_Tez =="Q" :
                break
            else:
                print("İşleminiz Gerçekleşiyor")
                time.sleep(1)
                print("Geçersiz İşlem......")

    def doktora_sonrası_puan(self):

        sayilar = self.doktora_sonrası
        toplam = sum(sayilar)
        print("Doktora sonrası aldığınız puan :", toplam)


    def doktora_oncesi_puan(self):

        sayilar = self.doktora_oncesi
        toplam = sum(sayilar)
        print("Doktora öncesi aldığınız puan :", toplam)


    print(f"""{Fore.LIGHTWHITE_EX} 
         ------------------------------------------
        |                                          |
        |                                          |
        | işlemler;                                |
        |                                          |
        | 1.Eğitim Bilimleri Temel Puan Hesapla    |
        | 2.Aşamaların Son Hali                    |
        | 10.Kontrol Aşaması                       |  
        | Programdan çıkmak için 'q' ya basın      |
        |                                          |
         ------------------------------------------""")

egitim = EğitimOgretimFaaliyetleri()

while True:
    işlem = input("İşlem Secin:")
    print("İşleminiz Sorgunalnıyor")
    time.sleep(1)
    if işlem == "q":
        break
    elif işlem == "1":
        egitim.Lısansustu_Tez_Danışmanlığı()

    elif işlem == "2":
        egitim.uluslararası_Makale()
    elif işlem == "10":
        egitim.kontrol_ıslemi()

    else:
        print("İşleminiz Gerçekleşiyor")
        time.sleep(1)
        print("Geçersiz İşlem......")
