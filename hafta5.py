import random
import calendar

def tarih_olustur(baslangic, bitis):
    tarih_listesi = []

    gun1, ay1, yil1 = map(int, baslangic.split('-'))
    gun2, ay2, yil2 = map(int, bitis.split('-'))

    for yil in range(yil1, yil2 + 1):
        for ay in range(1, 13):
            max_gun = calendar.monthrange(yil, ay)[1]

            for gun in range(1, max_gun + 1):
                tarih = "{:02d}-{:02d}-{}".format(gun, ay, yil)
                tarih_listesi.append(tarih)

                if (gun, ay, yil) == (gun2, ay2, yil2):
                    return tarih_listesi

    return tarih_listesi

def url_olustur(gazete, kategori, tarih):
    gun = int(tarih.split('-')[-3])  # Gün
    ay = int(tarih.split('-')[-2])  # Ay
    yil = int(tarih.split('-')[-1])  # Yıl
    return "www.{}.com.tr/{}/{}/{}-{}-{}".format(gazete, kategori, yil, yil, ay, gun)

gazeteler = ["sabah", "hürriyet", "milliyet", "newyorktimes", "cumhuriyet"]

kategoriler = ["spor", "ekonomi", "magazin", "siyaset", "teknoloji"]

baslangic_tarihi = "01-01-2010"
bitis_tarihi = "10-02-2015"
tarih_listesi = tarih_olustur(baslangic_tarihi, bitis_tarihi)

veri_seti = []
for tarih in tarih_listesi:
    gazete = random.choice(gazeteler)
    kategori = random.choice(kategoriler)
    url = url_olustur(gazete, kategori, tarih)
    veri_seti.append(url)

with open("h5url.txt", "a") as f:
    for url in veri_seti:
        f.write(url + "\n")

for url in veri_seti[:3]:
    print(url)
# hafta5
