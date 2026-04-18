#defineeri oma andmestruktuur, motle labi mis olekud kassil on

# tuju (õuest olemine mõjutab tuju)
# nälg (õues olemine mõjutab nälga)
# energia (õues olemine, mängimine)
# tervis (piirdume ainult ussidega), kas usse on (õuest tulles), 

#terminali mäng töötab tavaliselt mingis lõpmatus tsyklis
# kuvada olek -> kysida mida teha -> teha see -> uuesti (olekud muutuvad)
import random
suvaline_nr = random.randint(0, 100)
print(suvaline_nr)

kassi_tuju = 100 #hea tuju on 100, halb tuju on 0
#30% toenaosusega kassi tuju kukub 100 pealt 50 peale?
kassi_isu = 100
kassi_energiatase = 100
kassi_tervis = False #ussid = true?

if suvaline_nr < 30:
    kassi_tuju = 50
    print("Nyyd on kiisul halb tuju ja ta kyynistab sind vagivaldselt")
else:
    print("Kiisu nurrub roomsalt")

# m2ng peaks olema selline et kui inimene AKA mangija vastab yhele inputile, muutuvad
# koik stats mingil maaral, tuju voiks langeda siis kui mangimist ei ole
# energiatase voiks langeda siis kui kiisu oues kaia ei saa
# 

valik = input("Vali mangukaik:\n" \
"1. Anna kiisjule syya\n" \
"2. Lase kiisju oue\n" \
"3. Mangi kiisjuga\n" \
"4. Anna kiisjule ussirohtu\n" \
"5.  ")



# def kassi_tuju():
#     if 