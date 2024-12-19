import random
opcije_kompa1=["blok","puni"]
opcije_kompa2=["napad","blok","puni"]
opcije_igraca1=["blok","puni"]
opcije_igraca2=["napad","blok","puni"]
while True:
    igrac=input("izaberite jednu od akcija")
    komp=random.choice(opcije_kompa1)
    print(komp)
