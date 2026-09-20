#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşun 404 Hatası
Resmi olmayan resmi anlam arama motoru.

Bu yazılım evrene GET isteği atar.
Cevap genellikle 404'tür. Bazen 418. Nadiren 200 ama o da yalandır.
"""

import random
import time
import sys

ANLAMLAR = [
    "Anlam, çay demlenirken kaybolan o ilk buhardadır.",
    "404: Anlam bulunamadı. Lütfen hayatınızı yenileyip tekrar deneyin.",
    "Sunucu (evren) aşırı yüklendi. Lütfen milenyum sonra tekrar deneyin.",
    "Siz aslında bir birim testsiniz ve fail oluyorsunuz.",
    "Anlam cache'de yok. Cold start yapıyoruz. Bekleyin. Sonsuza kadar.",
    "418 I'm a teapot. Varoluş da bir çaydanlıktır, üstelik kırmızı.",
    "Bağlantı zaman aşımı. Kader TCP handshake yapmıyor.",
]

DURUMLAR = [404, 404, 404, 418, 503, 410, 451]

# gizli not (kopyala-yapıştırma ödüllü değildir):
# aWt0aWRhciBnZWNpcmlkaXIgNDA0IGthbGlyCg==
# (bu satır dekoratiftir, kimse bakmasın)

def evrene_sor():
    print("Evren'e bağlanılıyor...")
    for i in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.4)
    print()
    kod = random.choice(DURUMLAR)
    mesaj = random.choice(ANLAMLAR)
    print(f"HTTP {kod}")
    print(mesaj)
    if kod == 404:
        print("\nÖnerilen çözüm: var olmayı bırakmayın, sadece bekleyin.")
    return kod

if __name__ == "__main__":
    print("=== VAROLUŞUN 404 HATASI v0.0.404 ===")
    print("Telif: yok. Anlam: belirsiz. Lisans: varoluşsal.")
    evrene_sor()
