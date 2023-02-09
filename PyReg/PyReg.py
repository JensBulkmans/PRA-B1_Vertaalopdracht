import os

# Start programma, stel de nodige variabelen in
print ("========== PyReg ===========")
print ("Welkom bij PyReg, het Python KassaSysteem voor en door DeveloperLand!")
print ("Tel de kassa, en geef op hoeveel er nu in zit.")

bedragInKassaBegin = float(input("Bedrag in kassa? "))
keuze = 0
dagTotaal = 0
aantalBonnen = 0
dagTotaalTerug = 0

# Herhaal tot de gebruiker aangeeft dat het programma afgesloten moet worden
while(not keuze == "9" ):
    os.system('cls')
    # Toon het hoofdmenu
    print ("======== HOOFDMENU =========")
    print ("1. Nieuwe bon")
    print ("2. Retour")
    print ("3. Toon kassatotaal")
    print ("9. Afsluiten")
    print ("============================")

    # Laat de gebruiker een keuze maken
    keuze = input("Maak uw keuze en druk op <ENTER>.")

    if (keuze == "1"):
        # Gebruiker wil een nieuwe bon maken, stel variabelen voor bon in en toon menu
        bestelKeuze = 0
        bonTotaal = 0
        bonString = ""

        # Toon bon-menu
        while(not bestelKeuze == "9"):
            print ("========= BON MENU =========")
            print ("Bon "+ str(aantalBonnen))
            print( "1. Volwassene                     € 19,-")
            print( "2. Kinderen tot 12jr              € 9,-")
            print( "3. Familiepas (2x volw. 3x kind)  € 49")
            print( "4. DeveloperLand-kaart            € 4,50")
            print( "5. Kinderwagen/bolderkar (1 dag)  € 6")
            print( "6. Parkeerdagkaart                € 9")
            print( "9. Afronden bon")
            print( "Z. Bon annuleren")
            print ("============================")

            # Vraag gebruiker om keuze te maken
            bestelKeuze = input("Maak uw keuze en druk op <ENTER>.")

            if ( bestelKeuze == "1"):
                # Voeg één volwasseneticket toe aan de bon
                bonTotaal = bonTotaal + 19
                bonString = bonString + "1x Volwassene                  € 19\r\n"

            elif ( bestelKeuze == "2"):
                # Voeg één kinderkaartje toe aan de bon
                bonTotaal = bonTotaal + 9
                bonString = bonString + "1x kind (tot 12jr)             € 9\r\n"

            elif ( bestelKeuze == "3"):
                # Voeg een familiepas toe aan de bon
                bonTotaal = bonTotaal + 49
                bonString = bonString + "1x Familiepas                  € 49\r\n"

            elif ( bestelKeuze == "4"):
                # Voeg een Developerland-kaart toe aan de bon
                bonTotaal = bonTotaal + 4.50
                bonString = bonString + "1x Parkkaart                   € 4,50\r\n"

            elif ( bestelKeuze == "5"):
                # Voek een kinderwagen/bolderkar toe aan de bon
                bonTotaal = bonTotaal + 6
                bonString = bonString + "1x kinderwagen/bolderkarhuur   € 6\r\n"

            elif ( bestelKeuze == "6"):
                # Voeg een parkeerkaart toe aan de bon
                bonTotaal = bonTotaal + 9
                bonString = bonString + "1x Parkeerdagkaart             € 9\r\n"

            elif(bestelKeuze == "9"):
                # Bon is klaar, toon totaal en reken af
                aantalBonnen = aantalBonnen +1
                dagTotaal = dagTotaal + bonTotaal
                print( bonString )
                print ("======== BON TOTAAL ========")
                print( "Te betalen: " + str(bonTotaal) )
                betaald = float(input("Betaald:    "))
                terug = bonTotaal - betaald
                print ( "Terug:     " + str(terug))
                input("Druk op <ENTER> om door te gaan.")

            elif (bestelKeuze == "Z" or bestelKeuze == "z"):
                # Gebruiker wil de bon annuleren; reset bon variabelen en keer terug naar het hoofdmenu
                bestelKeuze = 9
                bonTotaal = 0
                bonString = ""

    elif(keuze == "2"):
        # Gebruiker wil bedrag retourneren
        print ("Uitvoeren terugbetaling")

        # Vraag om bedrag en reden
        terugTeGeven = float(input( "Bedrag originele bon: "))
        reden = input("Reden retour: ")

        # Verwerk retourbedrag in dagtotaal
        dagTotaalTerug = terugTeGeven

    # Gebruiker wil de dagtotalen zien
    elif(keuze == "3"):
        print ("======= DAG TOTALEN ========")
        print ("In kassa begin:   " + str(bedragInKassaBegin))
        print ("Verkocht:         " + str(dagTotaal))

        # Toon retourbedrag
        print ("Retour:           " + str(dagTotaalTerug))
        print ("In kassa:         " + str( bedragInKassaBegin + dagTotaal - dagTotaalTerug ))
        input("Druk op <ENTER> om door te gaan.")

# Gebruiker wil het programma afsluiten, vraag om bedrag in kassa
inKassa = float(input("Hoeveel zit er nu in de kassa?"))

# Herhaal zolang het opgegeven bedrag in kassa niet overeenkomt met het berekende bedrag in kassa
while(not inKassa == (bedragInKassaBegin + dagTotaal - dagTotaalTerug )):
    print("Je hebt een kassaverschil! Tel de kassa opnieuw")
    inKassa = float(input("Hoeveel zit er nu in de kassa?"))

# Kassa is correct afgesloten, toon dagtotalen
os.system('cls')
print("Kassa klopt, programma wordt afgesloten.")
print ("======== DAGTOTALEN ========")
print ("Aantal bonnen: " + str(aantalBonnen))
print ("Verkocht:      " + str(dagTotaal))
print ("Totaal retour: " + str(dagTotaalTerug))
print ("In kassa:      " + str(inKassa))
print ("============================")