Zubat_pokemon = [2, 4, 5]
Arktos_pokemon = [4, 5]
def pokebattle(pokemon):
    if sum(pokemon) > 10:
        print("opponent sent Knackrack lv.99")
    else:
        print("opponent sent Taubsi lv.8")
def hauptstory():
    pokebattle(Zubat_pokemon)
    pokebattle(Arktos_pokemon)
hauptstory()