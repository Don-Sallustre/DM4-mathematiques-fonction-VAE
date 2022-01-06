def limite_VAE(nombre_VAE_initial):        #limite_VAE(380)
    nombre_VAE_actuel_dispos = nombre_VAE_initial
    mois = ["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
    annee=2019
    mois_actu=0
    while nombre_VAE_actuel_dispos >0:
        nombre_VAE_actuel_dispos = nombre_VAE_actuel_dispos - (0.9*nombre_VAE_actuel_dispos+42)
        if mois_actu==11:
            mois_actu=0
            annee+=1
        mois_actu+=1
    return mois[mois_actu] , annee


