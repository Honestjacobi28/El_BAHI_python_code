def hotel_frais(nuits):
    return nuits * 90
def location_voiture_frais(jours):
    cout=jours*35
    if jours>=3 and jours<7:
        cout-=20
    elif jours>7:
        cout-=50
    return cout 
def vol_frais(ville):
    if ville=="Marrakech":
        return 35
    elif ville=="Paris":
        return 200
    elif ville=="Oran" :
        return 78
    elif ville=="Carthage" :
        return 182
    elif ville=="Dakar" :
        return 25
    
def voyage_frais(nuits,jours,ville,autres_frais):
    return hotel_frais(nuits)+location_voiture_frais(jours)+vol_frais(ville)+autres_frais
    
     