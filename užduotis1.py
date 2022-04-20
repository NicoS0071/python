def skaiciu_suma(*args):
    return sum(args)


def didziausias_skaicius(*args):
    return max(args)


def sakinys_atvirksciai(sakinys):
    sakinio_zodziai = sakinys.split()
    sarasas_atvirkciai = sakinio_zodziai[::-1]
    return " ".join(sarasas_atvirkciai)



def ar_yra(skaicius, sarasas):
    return (skaicius in sarasas)


def patikrinti_sakini(sakinys):
    zodziai = len(sakinys.split())
    skaiciai = sum(c.isdigit() for c in sakinys)
    didziosios = sum(c.isupper() for c in sakinys)
    mazosios = sum(c.islower() for c in sakinys)
    return (f"Žodžių kiekis: {zodziai}, Skaičių kiekis: {skaiciai}, Didžiųjų raidžių: {didziosios}, Mažųjų raidžių: {mazosios}")


def lyginiai_skaiciai(nuo, iki):
    '''
    Atspausdina visus paduoto rėžio (nuo… iki) lyginius skaičius
    :param nuo: Mažiausias rėžio skaičius
    :param iki: Didžiausias rėžio skaičius
    :return: Lyginių skaičių sąrašas
    '''
    sarasas = []
    for skaicius in range(nuo, iki + 1):
        if skaicius % 2 == 0:
            sarasas.append(skaicius)
    return sarasas



print(lyginiai_skaiciai(0, 51))