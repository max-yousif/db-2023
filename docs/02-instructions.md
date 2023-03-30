# 2. Instructies bij gebruik van de notebook

Hieronder volgen onvolledige functies (e.g., `query_42(connection, col_names, super_voorbeeldparam = ['joske', 'jef'])`). Aan jullie om ze aan te vullen zodat de functie:  

1. Een correcte query opstelt
2. De query uitvoert op de database
3. Het resultaat teruggeeft in een DataFrame.

Voor stap  3 is de nodige functie al voorhanden, i.e.: `res_to_df(res, column_names)`.
Voor stap 2 zal je nog 2 functies moeten implementeren (instructies volgen in het volgende deel). Gelukkig zal dit niet veel tijd vragen, jullie werk zal dus vooral bestaan uit stap 1, queries opstellen. Elke functie heeft minstens 2 inputargumenten:

1. `connection`:   Een connection object 
2. `column_names`: De kolomnamen van het "DataFrame" (i.e. de tabel met de resultaten van je query)
    
Gevolgd door eventuele extra argumenten (e.g., `super_voorbeeldparam = ['joske','jef']`) die dienen om parameters in de query te injecteren. 

**Nogmaals: verander niets aan de namen van de functies, namen van de functie-parameters en de kolomnamen van de resulterende DataFrames. Wijzigingen hieraan leiden onvermijdelijk tot een score van 0 op die query.**

In deze notebook kan je naar believen extra cellen toevoegen om je queries te testen, resultaten te inspecteren etc. Daar _dient_ deze notebook immers voor: deze notebook wordt **niet ingediend** als oplossing.

We vragen jullie om de finale, ingevulde functies te kopiëren naar een extern python script dat _enkel en alleen_ deze ingevulde functies bevat. Cf. de laatste sectie van deze notebook voor instructies omtrent hoe in te dienen.

## 2.1 Voorbeeld-query opstellen

Om jullie al wat op weg te zetten volgt hier een voorbeeldje over hoe je te werk kan gaan.

**Beschrijving**

Het resultaat van deze functie is een DataFrame met teamnaam, jaar en aantal homeruns van teams die meer dan een gegeven aantal `homeruns` hadden in dat jaar.

Sorteer aflopend op aantal homeruns.

**Oplossing**

## 2.2 Voorbeeld-query runnen

Om een query te runnen moeten we verbinding maken met de gegevensbank.
Implementeer hiervoor 2 functies: verbind_met_gb() en run_query(). De lege functies staan hieronder. 
De implementatie van deze functies wordt niet nagekeken en telt niet mee voor het resultaat. Het is echter wel belangrijk dat ze werken, aangezien onze implementaties van de functies opgeroepen worden tijdens de evaluatie en het dus belangrijk is dat je je oplossingen in de notebook kunt testen (ipv in de phpmyadmin console zelf). 

1. Eerst maken we een verbindingsobject met de databank
2. Vervolgens runnen we onze query, en inspecteren we het resultaat.


TIP: mysql.connector is zeker de moeite waard om eens te bekijken.