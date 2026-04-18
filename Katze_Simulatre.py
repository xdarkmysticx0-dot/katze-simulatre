#ehitame mängu 4 kihiliselt
#state, mis seisus kass on
#input, mis on inimese input
#logic, reeglid, kuidas maailm reageerib
#loop, mängu tsükkel, mäng töötab pidevalt
import random

def loo_kass():
    kass = {
        "nimi": "Skisomiisu",
        "energia": 100,
        "nalg": 50,
        "tuju": 100,
        "ussid": False,
<<<<<<< HEAD
        "usside_paevad": 0,
=======
>>>>>>> parent of 761d54b (Delete Katze_Simulatre.py)
        "paevad_elus": 0, #score system
        "mangimise_counter": 0, #mangimise counter, mida rohkem mangimist seda parem sest kiisjud on PIRTSAKAD ja ei taha mangida
        "kaigud_ilma_manguta": 0,
        "kriimustused": 0,
<<<<<<< HEAD
        "hammustused": 0,
        "saagid": [],
        "oues_kaimise_counter": 0
=======
        "hammustused": 0
>>>>>>> parent of 761d54b (Delete Katze_Simulatre.py)
    }
    return kass

def mangi_kassiga(kass):
    kass["kaigud_ilma_manguta"] = 0
    if kass["energia"] <= 15:
        print("😴 Kass on liiga väsinud mängimiseks!")
        return

    print("Mangid kassiga...")
    # energia vaheneb
    kass["energia"] = max(0, kass["energia"] - 15)
    kass["mangimise_counter"] += 1

    #50% voimalus kriimusatada
    r = random.random()
    if r < 0.5:
        print("😾 Kiisju kriimustas sind!")
        kass["tuju"] = max(0, kass["tuju"] - 20)
        kass["kriimustused"] += 1
    elif r < 0.8:
        print("😾 Kiisju hammustas sind!")
        kass["tuju"] = max(0, kass["tuju"] - 10)
        kass["hammustused"] += 1
    else:
        print("😸 Kiisju mängis ilusti!")
        kass["tuju"] = min(100, kass["tuju"] + 10)


#defineeri funktsioon mis näitaks kassi seisu
def kuva_seis(kass):
<<<<<<< HEAD
    print("\n" + "=" * 40)
    print(f"🐱 {kass['nimi']} STATUS")
    print("=" * 40)

    # BASIC STATS
    print(f"⚡ Energia : {kass['energia']}%",f"🍖 Nälg : {kass['nalg']}%")
    print(f"🍖 Nälg    : {kass['nalg']}%")
    print(f"😊 Tuju    : {kass['tuju']}%")
    print(f"📅 Päevi   : {kass['paevad_elus']}")
    print(f"🚑 Haiguse päevad: {kass['usside_paevad']}")

    print("-" * 40)

    # COUNTERS
    print("📊 TEGEVUSED:")
    print(f"🎮 Mängitud: {kass['mangimise_counter']}")
    print(f"🏞️  Õues käigud: {kass['oues_kaimise_counter']}")
    print(f"😼 Kriimustused: {kass['kriimustused']}")
    print(f"😬 Hammustused: {kass['hammustused']}")

    print("-" * 40)

    # STATUS EFFECTS
    if kass["ussid"]:
        print("🐛 STATUS: USSID!")

    if kass["kaigud_ilma_manguta"] >= 5:
        print("😾 STATUS: VÄGA IGAV!")
    elif kass["kaigud_ilma_manguta"] >= 2:
        print("😿 STATUS: igav")
    
    print("🦴 SAAGID:")
    saagide_kogus = {}

    for s in kass["saagid"]:
        if s in saagide_kogus:
            saagide_kogus[s] += 1
        else:
            saagide_kogus[s] = 1

    if saagide_kogus:
        for loom, kogus in saagide_kogus.items():
            print(f"{loom}-{kogus}")
    else:
        print(" (pole veel saaki)")

    print("=" * 40 + "\n")
=======
    print("--------")
    print("Nimi:", kass["nimi"])
    print(f"Energia: {kass['energia']}%")
    print(f"Nälg: {kass['nalg']}%")
    print(f"Tuju: {kass['tuju']}%")
    print("Päevi elus:", kass["paevad_elus"])
    print("Mitu korda mängitud: ", kass["mangimise_counter"])
    print("Kriimustused: ", kass["kriimustused"])
    print("Hammustused: ", kass["hammustused"])

    if kass["ussid"]:
        print("⚠️ Kassil on ussid!")
    
    # IGAVUSE STATUS (püsiv)
    if kass["kaigud_ilma_manguta"] >= 5:
        print("😾 Kass on VÄGA igavuses! (mängi temaga!)")
    elif kass["kaigud_ilma_manguta"] >= 2:
        print("😿 Kassil on igav...")
    
    #NÄLJA STAATUS
    # NÄLJA STATUS
    if kass["nalg"] >= 90:
        print("😿 Kass on VÄGA näljas!")
    elif kass["nalg"] >= 70:
        print("😾 Kass on näljane ja pahur!")
>>>>>>> parent of 761d54b (Delete Katze_Simulatre.py)

def toida_kassi(kass):
    print("Annad kassile syya...")
    kass["nalg"] = max(0, kass["nalg"] - 20)

    # kui kass EI OLE näljane → tuju langeb
    if kass["nalg"] < 20:
        print("😾 Kass ei tahtnud rohkem süüa...")
        kass["tuju"] = max(0, kass["tuju"] - 5)
    else:
        print("😋 Kass sõi!")

def uuenda_seisund(kass):
    #nalg kasvab
    kass["nalg"] = min(100, kass["nalg"] + 5)

    #paevad loetakse
    kass["paevad_elus"] += 1

    # kui EI mänginud see käik → kasvab
    kass["kaigud_ilma_manguta"] += 1

    # iga paari käigu järel muutub hullemaks
    if kass["kaigud_ilma_manguta"] == 5:
        kass["tuju"] = max(0, kass["tuju"] - 5)
    elif kass["kaigud_ilma_manguta"] == 2:
        kass["tuju"] = max(0, kass["tuju"] - 2)

    if kass["nalg"] >= 80:
        kass["tuju"] = max(0, kass["tuju"] - 3)

    if kass["ussid"]:
        kass["tuju"] = max(0, kass["tuju"] - 5)
        kass["energia"] = max(0, kass["energia"] - 3)
<<<<<<< HEAD
        kass["usside_paevad"] += 1
    else:
        kass["usside_paevad"] = 0
=======
    # #kui nalg max
    # if kass["nalg"] >= 100:
    #     print("😿 Kass on VÄGA näljas!")

    # elif kass["nalg"] >= 80:
    #     print("😾 Kass on näljane ja pahur!")
    #     kass["tuju"] = max(0, kass["tuju"] - 3)

    # # milestone eventid
    # if kass["paevad_elus"] == 5:
    #     print("🎉 Kass hakkab sinuga harjuma!")

    # if kass["paevad_elus"] == 10:
    #     print("😻 Kass usaldab sind täielikult!")
>>>>>>> parent of 761d54b (Delete Katze_Simulatre.py)

def oues_kaimine(kass):

    print("Lased kassi oue...")

    kass["energia"] = min(100, kass["energia"] + 20)
    kass["nalg"] = min(100, kass["nalg"] + 10)
<<<<<<< HEAD
    kass["oues_kaimise_counter"] += 1

    r = random.random() # usside saamise random

    if not kass["ussid"] and r < 0.15: #saad reguleerida usside saamise balance
=======

    r = random.random() # usside saamise random

    # if r < 0.15: #### SAAD REGULEERIDA USSIDE SAAMISE BALANCE
    #     print("😱 Kass tuli õuest tagasi ja sai USSID!")
    #     kass["ussid"] = True
    # else:
    #     print("🌿 Kass tuli tagasi õuest!")
    r = random.random()

    if not kass["ussid"] and r < 0.15:
>>>>>>> parent of 761d54b (Delete Katze_Simulatre.py)
        print("😱 Kass tuli õuest tagasi ja sai USSID!")
        kass["ussid"] = True
    else:
        print("🌿 Kass tuli tagasi õuest!")

        r2 = random.random() # looma pyydmise random

        if r2 < 0.3:
            print("🐭 Kass püüdis hiire kinni!")
            kass["tuju"] = min(100, kass["tuju"] + 10)
<<<<<<< HEAD
            kass["saagid"].append("🐭 hiir")
=======
>>>>>>> parent of 761d54b (Delete Katze_Simulatre.py)

        elif r2 < 0.4:
            print("🦔 Kass püüdis siili kinni!")
            kass["tuju"] = min(100, kass["tuju"] + 30)
<<<<<<< HEAD
            kass["saagid"].append("🦔 siil")
=======
>>>>>>> parent of 761d54b (Delete Katze_Simulatre.py)

        elif r2 < 0.6:
            print("🐦 Kass püüdis linnu kinni!")
            kass["tuju"] = min(100, kass["tuju"] + 20)
<<<<<<< HEAD
            kass["saagid"].append("🐦 lind")
=======
>>>>>>> parent of 761d54b (Delete Katze_Simulatre.py)

        elif r2 < 0.8:
            print("🐸 Kass püüdis konna kinni!")
            kass["tuju"] = min(100, kass["tuju"] + 10)
<<<<<<< HEAD
            kass["saagid"].append("🐸 konn")
=======
>>>>>>> parent of 761d54b (Delete Katze_Simulatre.py)

        elif r2 < 0.9:
            print("🕷️ Kass püüdis ämbliku kinni!")
            kass["tuju"] = min(100, kass["tuju"] + 5)
<<<<<<< HEAD
            kass["saagid"].append("🕷️ ämblik")
=======
>>>>>>> parent of 761d54b (Delete Katze_Simulatre.py)

        elif r2 < 0.95:
            print("🦎 Kass püüdis sisaliku kinni!")
            kass["tuju"] = min(100, kass["tuju"] + 5)
<<<<<<< HEAD
            kass["saagid"].append("🦎 sisalik")
=======
>>>>>>> parent of 761d54b (Delete Katze_Simulatre.py)

        elif r2 < 0.99:
            print("🦂 Kass püüdis skorpioni kinni!")
            kass["tuju"] = min(100, kass["tuju"] + 5)
<<<<<<< HEAD
            kass["saagid"].append("🦂 skorpion")
=======
>>>>>>> parent of 761d54b (Delete Katze_Simulatre.py)

        else:
            print("🦄 Haruldane elukas! Kiisju leidis ükssarviku!")
            kass["tuju"] = min(100, kass["tuju"] + 100)
<<<<<<< HEAD
            kass["saagid"].append("🦄 ükssarvik")
=======
>>>>>>> parent of 761d54b (Delete Katze_Simulatre.py)
            
def ravi_ussid(kass):
    if not kass["ussid"]:
        print("🤔 Kassil pole usse.")
        return

    print("💊 Annad kassile ussirohtu...")
    kass["ussid"] = False

    # väike reward, et mängija tunneks kasu
    kass["tuju"] = min(100, kass["tuju"] + 10)
    kass["energia"] = min(100, kass["energia"] + 5)

    print("😺 Kass tunneb end palju paremini!")

def kas_mang_labi(kass):
<<<<<<< HEAD
    if kass["tuju"] <= 0:
        return True

    if kass["usside_paevad"] >= 5:
        print("☠️ Ussid võtsid kassi üle...")
        return True

    return False
=======
    return kass["tuju"] <= 0
>>>>>>> parent of 761d54b (Delete Katze_Simulatre.py)

####################################
####################################
####################################
#siin on vaja mangija inputi defineerida
def kysi_tegevus():
    while True:
        print()
        print("1 - toida kiisjut toiduga")
        print("2 - mangi kiisjuga")
        print("3 - mine oue")
        print("4 - anna ussirohtu")
        print("5 - valju mangust")

        valik = input("vali: ")

        if valik in ["1", "2", "3", "4", "5"]:
            return valik
        else:
            print("❌ Vali olemasolev number!")

#mangu loop
def mang():
    kass = loo_kass()

    while True:
        kuva_seis(kass)
        valik = kysi_tegevus()

        if valik == "1":
            toida_kassi(kass)
        
        elif valik == "2":
            mangi_kassiga(kass)

        elif valik == "3":
            oues_kaimine(kass)

        elif valik == "4":
            ravi_ussid(kass)

        elif valik == "5":
            print("Aitah mangimast")
            print(f"Sa hoolitsesid kassi eest {kass['paevad_elus']} päeva.")
            break

        #aeg liigub siin
        uuenda_seisund(kass)

        #game over check
        if kas_mang_labi(kass):
            print("💔 Kass on nii õnnetu, et lahkub sinu juurest...")
            print(f"Sa hoolitsesid tema eest {kass['paevad_elus']} päeva.")
            print("GAME OVER")
            break

mang()