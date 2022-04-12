self.hesapla_buton.clicked.connect(self.kama_hesapla)
self.kaydet.clicked.connect(self.dosyayaYaz)


def kama_hesapla(self):
    # verileri alıyoruz
    L = self.L_veri.text()
    b = self.b_veri.text()
    t1 = self.t1_veri.text()
    t2 = self.t2_veri.text()
    h = self.h_veri.text()
    d1 = self.mil_veri.text()
    kama_adet = self.kamaadet_veri.text()
    tork = self.tork_veri.text()
    akma = self.akma_veri.text()
    emniyet_k = self.emniyet_veri.text()

    # ondalık sayıda virgülleri değiştirme
    t1 = t1.replace(",", ".")
    t2 = t2.replace(",", ".")
    d1 = d1.replace(",", ".")
    tork = tork.replace(",", ".")

    try:

        # hesaplamalar
        milkesme_kuvveti = float(tork) / (float(d1) / 2)
        kesme_gerilmesi = int(milkesme_kuvveti) / ((int(L) * int(b)) / int(kama_adet))
        p1 = int(milkesme_kuvveti) / ((float(t2) * int(L)) / int(kama_adet))
        p2 = int(milkesme_kuvveti) / ((float(t1) * int(L)) / int(kama_adet))
        emniyet_durum = int(akma) / int(emniyet_k)

        # ekrana yazdırma
        self.kesme_sonuc_label.setText(str(kesme_gerilmesi))
        self.p1_sonuc_label.setText(str(p1))
        self.p2_sonuc_label.setText(str(p2))

        if int(emniyet_durum) > p2:
            self.durum.setText("EMNiYETLi")

        else:
            self.durum.setText("EMNiYETSiZ")

    except:
        self.durum.setText("HATALI")


def dosyayaYaz(self):
    dosya = open('Çıktı.txt', 'w')
    dosya.write(
        self.L_veri.text() + '\n' + self.h_veri.text() + '\n' + self.t2_veri.text() + '\n' + self.b_veri.text())
    dosya.close()