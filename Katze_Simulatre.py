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
        "usside_paevad": 0,
        "paevad_elus": 0, #score system
        "mangimise_counter": 0, #mangimise counter, mida rohkem mangimist seda parem sest kiisjud on PIRTSAKAD ja ei taha mangida
        "kaigud_ilma_manguta": 0,
        "kriimustused": 0,
        "hammustused": 0,
        "saagid": [],
        "oues_kaimise_counter": 0,
        "rasedus": False,
        "rasedus_paevad": 0,
        "palderjanis_olek": False,
        "marg_olemine": False,
        "kylmetab": False,

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
    
    if kass["marg_olemine"]:
        print("😾 Kass on märg ja ei taha hästi mängida...")
        kass["tuju"] = max(0, kass["tuju"] - 5)


#defineeri funktsioon mis näitaks kassi seisu
def kuva_seis(kass):
    print("\n" + "=" * 100)
    print(f"🐱 {kass['nimi']} STATUS")
    print("=" * 100)

    # BASIC STATS
    print(f"|⚡ Energia : {kass['energia']}% |",f"🍖 Nälg : {kass['nalg']}% |",f"😊 Tuju : {kass['tuju']}% |",f"📅 Päevi : {kass['paevad_elus']} |",f"🚑 Haiguse päevad : {kass['usside_paevad']} |")
    # print(f"🍖 Nälg    : {kass['nalg']}%")
    # print(f"😊 Tuju    : {kass['tuju']}%")
    # print(f"📅 Päevi   : {kass['paevad_elus']}")
    # print(f"🚑 Haiguse päevad : {kass['usside_paevad']}")

    print("-" * 100)

    # COUNTERS
    print("📊 TEGEVUSED:")
    print(f"|🎮 Mängitud: {kass['mangimise_counter']} |",f"🏞️  Õues käigud: {kass['oues_kaimise_counter']} |",f"😼 Kriimustused: {kass['kriimustused']} |",f"😬 Hammustused: {kass['hammustused']} |")
    # print(f"🏞️  Õues käigud: {kass['oues_kaimise_counter']}")
    # print(f"😼 Kriimustused: {kass['kriimustused']}")
    # print(f"😬 Hammustused: {kass['hammustused']}")

    print("-" * 100)
    
    #RASEDUS
    if kass["rasedus"]:
        print(f"🤰 RASEDUS: {kass['rasedus_paevad']} päeva")
        print("-" * 100)

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

    if kass["marg_olemine"]:
        print("💧 STATUS: MÄRG")

    if kass["kylmetab"]:
        print("❄️ STATUS: KÜLMETAB")

    print("=" * 100 + "\n")

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
        kass["usside_paevad"] += 1
    else:
        kass["usside_paevad"] = 0
    
    if kass["rasedus"]:
        kass["rasedus_paevad"] += 1

    if kass["rasedus_paevad"] >= 100:
        print("🐾 Kass sünnitas kassipojad!")
        kass["rasedus"] = False
        kass["rasedus_paevad"] = 0
        kass["tuju"] = min(100, kass["tuju"] + 20)
    
    # MÄRG → KÜLMETAMINE
    if kass["marg_olemine"]:
        # iga tick teeb halvemaks
        kass["energia"] = max(0, kass["energia"] - 2)
    
        # mingi hetk hakkab külmetama
        if random.random() < 0.3:
            kass["kylmetab"] = True
    
    if kass["kylmetab"]:
        print("🥶 Kass külmetab...")
        kass["tuju"] = max(0, kass["tuju"] - 5)
        kass["energia"] = max(0, kass["energia"] - 3)
    
    # kuivamise süsteem
    if kass["marg_olemine"]:
        if random.random() < 0.3:
            kass["marg_olemine"] = False
            print("☀️ Kass kuivas ära!")

            # kui kuivas → lõpetab külmetamise
            kass["kylmetab"] = False

def oues_kaimine(kass):

    print("Lased kassi oue...")

    kass["energia"] = min(100, kass["energia"] + 20)
    kass["nalg"] = min(100, kass["nalg"] + 10)
    kass["oues_kaimise_counter"] += 1
    # märjaks saamise chance
    if random.random() < 0.3:
        print("🌧️ Kass sai õues märjaks!")
        kass["marg_olemine"] = True

        # kuivamise chance
        if random.random() < 0.3:
            kass["marg_olemine"] = False
            print("☀️ Kass kuivas ära!")

    r = random.random() # usside saamise random

    if not kass["ussid"] and r < 0.15: #saad reguleerida usside saamise balance
        print("😱 Kass tuli õuest tagasi ja sai USSID!")
        kass["ussid"] = True
    else:
        print("🌿 Kass tuli tagasi õuest!")

        # 👉 RASEDUS CHECK (SIIN!)
        if not kass["rasedus"]:
            r3 = random.random()
            if r3 < 0.10:  # 10% chance
                kass["rasedus"] = True
                kass["rasedus_paevad"] = 0
                print("😳 Kass tuli tagasi... ja tundub, et ta on TIINE!")

        r2 = random.random() # looma pyydmise random

        if r2 < 0.3:
            print("🐭 Kass püüdis hiire kinni!")
            kass["tuju"] = min(100, kass["tuju"] + 10)
            kass["saagid"].append("🐭 hiir")

        elif r2 < 0.4:
            print("🦔 Kass püüdis siili kinni!")
            kass["tuju"] = min(100, kass["tuju"] + 30)
            kass["saagid"].append("🦔 siil")

        elif r2 < 0.6:
            print("🐦 Kass püüdis linnu kinni!")
            kass["tuju"] = min(100, kass["tuju"] + 20)
            kass["saagid"].append("🐦 lind")

        elif r2 < 0.8:
            print("🐸 Kass püüdis konna kinni!")
            kass["tuju"] = min(100, kass["tuju"] + 10)
            kass["saagid"].append("🐸 konn")

        elif r2 < 0.9:
            print("🕷️ Kass püüdis ämbliku kinni!")
            kass["tuju"] = min(100, kass["tuju"] + 5)
            kass["saagid"].append("🕷️ ämblik")

        elif r2 < 0.95:
            print("🦎 Kass püüdis sisaliku kinni!")
            kass["tuju"] = min(100, kass["tuju"] + 5)
            kass["saagid"].append("🦎 sisalik")

        elif r2 < 0.99:
            print("🦂 Kass püüdis skorpioni kinni!")
            kass["tuju"] = min(100, kass["tuju"] + 5)
            kass["saagid"].append("🦂 skorpion")

        else:
            print("🦄 Haruldane elukas! Kiisju leidis ükssarviku!")
            kass["tuju"] = min(100, kass["tuju"] + 100)
            kass["saagid"].append("🦄 ükssarvik")
                         
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

def palderjan(kass):
    kass["palderjanis_olek"] = True
    kass["tuju"] = min(100, kass["tuju"] + 75)
    print("💉 Kiisju on aines")

def kuivata_kass(kass):
    if not kass["marg_olemine"]:
        print("😐 Kass ei ole märg.")
        return

    print("🧻 Kuivatad kassi...")
    kass["marg_olemine"] = False
    kass["kylmetab"] = False
    kass["tuju"] = min(100, kass["tuju"] + 5)

def kas_mang_labi(kass):
    if kass["tuju"] <= 0:
        return True

    if kass["usside_paevad"] >= 5:
        print("☠️ Ussid võtsid kassi üle...")
        return True

    return False

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
        print("5 - anna kiisjule palderjani")
        print("6 - kuivata kiisjut")
        print("7 - valju mangust")

        valik = input("vali: ")

        if valik in ["1", "2", "3", "4", "5", "6", "7"]:
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
        #catnip
        elif valik == "5":
            palderjan(kass)
        #kuivatamine
        elif valik == "6":
            kuivata_kass(kass)

        elif valik == "7":
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