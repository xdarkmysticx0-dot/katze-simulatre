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
    #see VIST restardib kaigud ilma manguta, (uuenda_seisund all lisab +1 juurde)
    kass["kaigud_ilma_manguta"] = 0
    if kass["energia"] <= 15: #saad kassi ära väsimise taset reguleerida
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
    print("\n" + "=" * 40)
    print(f"🐱 {kass['nimi']}")
    print("=" * 40)

    # BASIC
    print(f"⚡ {kass['energia']}%  🍖 KÕHUTÄIS {kass['nalg']}%  😊 {kass['tuju']}%")
    print(f"📅 Päev: {kass['paevad_elus']}  🚑 Ussid: {kass['usside_paevad']}")

    # COUNTERS
    print(f"🎮 MÄNGU {kass['mangimise_counter']} | 🏞️  ÕUE {kass['oues_kaimise_counter']} | 😼 KRIIMU {kass['kriimustused']} | 😬 AMPSTI {kass['hammustused']}")

    # STATUS LINE
    statused = []

    # need on kassi plokis = False
    if kass["ussid"]:
        statused.append("🐛 ussid")
    if kass["marg_olemine"]:
        statused.append("💧 märg")
    if kass["kylmetab"]:
        statused.append("❄️ külm")
    # need ei ole kassi plokis võrdub False
    if kass["kaigud_ilma_manguta"] >= 5:
        statused.append("😾 igav")
    elif kass["kaigud_ilma_manguta"] >= 2:
        statused.append("😿 igav")
    # kassi plokis = False
    if kass["rasedus"]:
        statused.append(f"🤰 {kass['rasedus_paevad']} päeva rase")

    # MIDA SEE TEEB ??????????????????????????????????????
    if statused:
        print("STATUS:", ", ".join(statused))

    # SAAGID ÜHEL REAL
    if kass["saagid"]:
        saagide_kogus = {}
        for s in kass["saagid"]:
            saagide_kogus[s] = saagide_kogus.get(s, 0) + 1

        saak_str = " ".join([f"{loom}-{kogus}" for loom, kogus in saagide_kogus.items()])
        print("🦴", saak_str)
    else:
        print("🦴 -")

    print("=" * 40)

def uuenda_seisund(kass):
    #nalg kasvab
    kass["nalg"] = max(0, kass["nalg"] - 5)

    #paevad loetakse
    kass["paevad_elus"] += 1

    # kui EI mänginud see käik → kasvab
    kass["kaigud_ilma_manguta"] += 1

    # iga paari käigu järel muutub hullemaks
    if kass["kaigud_ilma_manguta"] == 5:
        kass["tuju"] = max(0, kass["tuju"] - 5)
    elif kass["kaigud_ilma_manguta"] == 2:
        kass["tuju"] = max(0, kass["tuju"] - 2)

    if kass["nalg"] <= 20:
        print("😿 Kass on VÄGA näljane!")
        kass["tuju"] = max(0, kass["tuju"] - 5)
    
    elif kass["nalg"] <= 40:
        print("😾 Kass on näljane...")
        kass["tuju"] = max(0, kass["tuju"] - 2)

    if kass["ussid"]:
        kass["tuju"] = max(0, kass["tuju"] - 5)
        kass["energia"] = max(0, kass["energia"] - 3)
        kass["usside_paevad"] += 1
    else:
        kass["usside_paevad"] = 0
    
    if kass["rasedus"]:
        kass["rasedus_paevad"] += 1
    
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

def toida_kassi(kass):
    print("Annad kassile syya...")
    kass["nalg"] = min(100, kass["nalg"] + 20)

    # kui kass EI OLE näljane → tuju langeb
    if kass["nalg"] < 20:
        print("😾 Kass ei tahtnud rohkem süüa...")
        kass["tuju"] = max(0, kass["tuju"] - 5)
    else:
        print("😋 Kass sõi!")

# def oues_kaimine(kass):

#     print("Lased kassi oue...")

#     kass["energia"] = min(100, kass["energia"] + 20)
#     kass["nalg"] = min(100, kass["nalg"] + 10)
#     kass["oues_kaimise_counter"] += 1
#     # märjaks saamise chance
#     if random.random() < 0.3:
#         print("🌧️ Kass sai õues märjaks!")
#         kass["marg_olemine"] = True

#         # kuivamise chance
#         if random.random() < 0.3:
#             kass["marg_olemine"] = False
#             print("☀️ Kass kuivas ära!")

#     r = random.random() # usside saamise random

#     if not kass["ussid"] and r < 0.0000000000000015: #saad reguleerida usside saamise balance
#         print("😱 Kass tuli õuest tagasi ja sai USSID!")
#         kass["ussid"] = True
#     else:
#         print("🌿 Kass tuli tagasi õuest!")

#         # 👉 RASEDUS CHECK (SIIN!)
#         if not kass["rasedus"]:
#             r3 = random.random()
#             if r3 < 0.10:  # 10% chance
#                 kass["rasedus"] = True
#                 kass["rasedus_paevad"] = 0
#                 print("😳 Kass tuli tagasi... ja tundub, et ta on TIINE!")

#         r2 = random.random() # looma pyydmise random

#         if r2 < 0.3:
#             print("🐭 Kass püüdis hiire kinni!")
#             kass["tuju"] = min(100, kass["tuju"] + 10)
#             kass["saagid"].append("🐭 hiir")

#         elif r2 < 0.4:
#             print("🦔 Kass püüdis siili kinni!")
#             kass["tuju"] = min(100, kass["tuju"] + 30)
#             kass["saagid"].append("🦔 siil")

#         elif r2 < 0.6:
#             print("🐦 Kass püüdis linnu kinni!")
#             kass["tuju"] = min(100, kass["tuju"] + 20)
#             kass["saagid"].append("🐦 lind")

#         elif r2 < 0.8:
#             print("🐸 Kass püüdis konna kinni!")
#             kass["tuju"] = min(100, kass["tuju"] + 10)
#             kass["saagid"].append("🐸 konn")

#         elif r2 < 0.9:
#             print("🕷️ Kass püüdis ämbliku kinni!")
#             kass["tuju"] = min(100, kass["tuju"] + 5)
#             kass["saagid"].append("🕷️ ämblik")

#         elif r2 < 0.95:
#             print("🦎 Kass püüdis sisaliku kinni!")
#             kass["tuju"] = min(100, kass["tuju"] + 5)
#             kass["saagid"].append("🦎 sisalik")

#         elif r2 < 0.99:
#             print("🦂 Kass püüdis skorpioni kinni!")
#             kass["tuju"] = min(100, kass["tuju"] + 5)
#             kass["saagid"].append("🦂 skorpion")

#         else:
#             print("🦄 Haruldane elukas! Kiisju leidis ükssarviku!")
#             kass["tuju"] = min(100, kass["tuju"] + 100)
#             kass["saagid"].append("🦄 ükssarvik")

########################## OUES KAIMINE SIMPLIFIED ###########################################

def oues_kaimine(kass):
    print("Lased kassi õue...")

    kass["energia"] = min(100, kass["energia"] + 20)
    kass["nalg"] = min(100, kass["nalg"] + 10)
    kass["oues_kaimise_counter"] += 1

    print("🌿 Kass tuli tagasi õuest!")

    # 👉 NEW: instead of all random logic
    run_events(kass)

########################## OUES KAIMINE SIMPLIFIED ###########################################

########################## EVENTS ###########################################

def event_vihm(kass):
    if random.random() < 0.3:
        print("🌧️ Kass sai õues märjaks!")
        kass["marg_olemine"] = True

        if random.random() < 0.3:
            kass["marg_olemine"] = False
            print("☀️ Kass kuivas ära!")

def event_ussid(kass):
    if not kass["ussid"] and random.random() < 0.01:
        print("😱 Kass sai ussid!")
        kass["ussid"] = True

def event_rasedus(kass):
    if not kass["rasedus"] and random.random() < 0.10:
        kass["rasedus"] = True
        kass["rasedus_paevad"] = 0
        print("😳 Kass tuli tagasi... ja tundub, et ta on TIINE!")

# def event_saak(kass):
#     r = random.random()

#     if r < 0.3:
#         print("🐭 Kass püüdis hiire!")
#         kass["tuju"] = min(100, kass["tuju"] + 10)
#         kass["saagid"].append("🐭 hiir")

#     elif r < 0.4:
#         print("🦔 Kass püüdis siili!")
#         kass["tuju"] = min(100, kass["tuju"] + 30)
#         kass["saagid"].append("🦔 siil")

#     elif r < 0.6:
#         print("🐦 Kass püüdis linnu!")
#         kass["tuju"] = min(100, kass["tuju"] + 20)
#         kass["saagid"].append("🐦 lind")

#     elif r < 0.8:
#         print("🐸 Kass püüdis konna!")
#         kass["tuju"] = min(100, kass["tuju"] + 10)
#         kass["saagid"].append("🐸 konn")

#     elif r < 0.9:
#         print("🕷️ Kass püüdis ämbliku!")
#         kass["tuju"] = min(100, kass["tuju"] + 5)
#         kass["saagid"].append("🕷️ ämblik")

#     elif r < 0.95:
#         print("🦎 Kass püüdis sisaliku!")
#         kass["tuju"] = min(100, kass["tuju"] + 5)
#         kass["saagid"].append("🦎 sisalik")

#     elif r < 0.99:
#         print("🦂 Kass püüdis skorpioni!")
#         kass["tuju"] = min(100, kass["tuju"] + 5)
#         kass["saagid"].append("🦂 skorpion")

#     else:
#         print("🦄 HARULDANE ELUKAS! Kiisju leidis ükssarviku!")
#         kass["tuju"] = min(100, kass["tuju"] + 100)
#         kass["saagid"].append("🦄 ükssarvik")

########################## EVENTS ###########################################

########################## DATA DRIVEN LOOTS ###########################################

LOOT_TABLE = [
    # CHANCE / NAME / TUJU PUNKTID
    (0.3, "🐭 hiir", 10),
    (0.1, "🦔 siil", 30),
    (0.2, "🐦 lind", 20),
    (0.2, "🐸 konn", 10),
    (0.1, "🕷️ ämblik", 5),
    (0.09, "🦎 sisalik", 5),
    (0.009, "🦂 skorpion", 5),
    (0.001, "🦄 ükssarvik", 100),
]

def roll_loot(kass):
    r = random.random() # vahemik 0 - 1, random.random() tagastab ujukomaarvu (float) vahemikus 0.0 ≤ x < 1.0
    kasvav_piirvaartus = 0 # see on vahemiku aluseks, et for cycle saaks vorrelda genereeritud ujukomaarvu loomade chance arvuga

    for chance, name, tuju in LOOT_TABLE:
        kasvav_piirvaartus += chance # random gen on ntx 0.5, chance lisab koigepealt 0.3 kasvavasse piirvaartusesse, 
        # IF kontrollib kas 0.5 < 0.3, saab vastuseks false, rinse n repeat, 0.3+0.1 ka false, rinse n repeat, 0.6 on juba lind
        if r < kasvav_piirvaartus:
            print(f"Kiisju püüdis {name}!")
            kass["saagid"].append(name)
            kass["tuju"] = min(100, kass["tuju"] + tuju)
            return

def event_loot(kass):
    roll_loot(kass)

########################## DATA DRIVEN LOOTS ###########################################

########################## DATA DRIVEN EVENTS ###########################################

EVENTS = [
    {
        "name": "vihm",
        "chance": 0.3,
        "message": "🌧️ Kass sai märjaks!",
        #condition missing
        "effects": [
            ("marg_olemine", True)
        ]
    },
    {
        "name": "kylm",
        "chance": 0.3,
        "condition": lambda k: k["marg_olemine"],
        "message": "🥶 Kass hakkas külmetama!",
        "effects": [("kylmetab", True)]
    },
    {
        "name": "kuivamine",
        "chance": 0.3,
        "condition": lambda k: k["marg_olemine"],
        "message": "☀️ Kass kuivas ära!",
        "effects": [
            ("marg_olemine", False),
            ("kylmetab", False)
        ]
    },
    {
        "name": "ussid",
        "chance": 0.0,# NERF USSID IF 0.0
        "condition": lambda k: not k["ussid"],
        "message": "😱 Kass sai ussid!",
        "effects": [
            ("ussid", True)
        ]
    },
    {
        "name": "rasedus",
        "chance": 0.10,
        "condition": lambda k: not k["rasedus"],
        "message": "😳 Kass on nüüd TIINE!",
        "effects": [
            ("rasedus", True),
            ("rasedus_paevad", 0)
        ]
    },
]

EVENTS.append({
    "name": "loot",
    "chance": 0.8, ### Lihtsama kontrollimise jaoks loot chance 1 ja saad loot_table loomade loot chancesid eraldi reguleerida
    "action": event_loot
})

########################## DATA DRIVEN EVENTS ###########################################

########################## GENERIC EVENT RUNNER ###########################################

def run_events(kass):
    for event in EVENTS:
        
        # chance check
        if random.random() >= event["chance"]:
            continue
        
        # optional condition # naiteks checkib kas kass on juba rase, et skippida event
        #
        # Check optional event condition (e.g. only runs if cat is pregnant / wet / etc.)
        if "condition" in event and not event["condition"](kass):
            continue
        
        # message
        if "message" in event:
            print(event["message"])

        # apply effects
        if "effects" in event:
            for stat, value in event["effects"]:
                if isinstance(value, bool):
                    kass[stat] = value
                else:
                    kass[stat] += value
        
        # after effects
        if "action" in event:
            event["action"](kass)

########################## GENERIC EVENT RUNNER ###########################################


########################## EVENTS RUNNER ###########################################

# def random_event(kass):
#     events = [
#         event_vihm,
#         event_ussid,
#         event_rasedus,
#         event_saak
#     ]

#     event = random.choice(events)
#     event(kass)

########################## EVENTS RUNNER ###########################################


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
        return "kurbus"

    if kass["usside_paevad"] >= 5:
        return "ussid"

    if kass["rasedus"] and kass["rasedus_paevad"] >= 100:
        return "pere"

    return None

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
        pohjus = kas_mang_labi(kass)

        if pohjus:
            if pohjus == "kurbus":
                print("💔 Kass on nii õnnetu, et lahkub sinu juurest...")

            elif pohjus == "ussid":
                print("☠️ Ussid võtsid kassi üle...")

            elif pohjus == "pere":
                print("🐾 Kass sünnitas kassipojad!")
                print("🏡 Ta lahkub koos oma perega...")

            print(f"Sa hoolitsesid tema eest {kass['paevad_elus']} päeva.")
            print("GAME OVER")
            break

mang()