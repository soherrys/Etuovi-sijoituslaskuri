def laske_kannattavuus(kohde):
    vuokra = 500
    vastike = 150
    laina = 300
    hinta = kohde['hinta']
    vuokratuotto = round((vuokra * 12) / hinta * 100, 2)
    kassavirta = vuokra - vastike - laina
    roi = round((kassavirta * 12) / (hinta * 0.3) * 100, 2)
    return {
        'nimi': kohde['nimi'],
        'hinta': hinta,
        'vuokratuotto': vuokratuotto,
        'kassavirta': kassavirta,
        'roi': roi
    }
