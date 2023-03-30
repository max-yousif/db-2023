## 3.1 Query 01

**Beschrijving**

Geef voor alle spelers die voor jaar "X" zijn benoemd als all-star en groter zijn dan "Y": de achternaam, voornaam en grootte. Stel dat een speler meerdere keren tot all-star is benoemd, dan verwachten we deze informatie maar 1 keer. 

Sorteer alfabetisch op achternaam, voornaam en aflopend op grootte. 

## 3.2 Query 02

**Beschrijving**

Geef voor alle spelers die in land "X" geboren zijn en die jonger dan "Y" waren toen ze stierven: de achternaam, de voornaam, de leeftijd en het land waarin ze gestorven zijn. 

Sorteer achtereenvolgens oplopend op leeftijd, alfabetisch op voornaam, alfabetisch op achternaam, alfabetisch op land. 

## 3.3 Query 03

**Beschrijving**

Maak een lijst met alle managers die tussen jaar "X" en "Y" (beiden inclusief) als "Z"<sup>e</sup> manager in het seizoen gewerkt hebben voor een team dat meer gewonnen is dan verloren, maar waar de manager in dat jaar met de ploeg meer heeft verloren dan gewonnen. 

Van deze managers willen we de achternaam, voornaam, geboortejaar, de teamnaam, het jaar waarin de manager voor het team werkte, het procentueel aantal gewonnen matchen van het team in dat jaar en het procentueel aantal verloren matchen van de manager met het team in dat jaar. 

Sorteer alfabetisch op achternaam, voornaam, aflopend op geboortejaar, alfabetisch op teamnaam en aflopend op beide procenten.


## 3.4 Query 04

**Beschrijving**

Maak een lijst met informatie over de Hall of Fame. 
We willen per jaar en per groepering (de groep die stemmen uit mocht brengen) het aantal keer dat er gestemd is geweest en het gemiddelde aantal stemmen per speler voor de jaren en groeperingen waar er minstens "X" keer gestemd is geweest. 
Voor deze lijst bekijken we echter enkel spelers die in hun carriere ook manager zijn geweest en geboren zijn na jaar "Y". 

Sorteer aflopend op jaartal, alfabetisch op groepering, aflopend op aantal keer gestemd en aflopend op gemiddelde stemmen. 


## 3.5 Query 05

**Beschrijving**

Maak een lijst van alle spelers die voldoen aan deze drie voorwaarden:

-De speler was voor jaar X al actief als pitcher,

-De speler heeft tijdens zijn matches als pitcher in totaal meer gewonnen dan verloren 

-De speler had tijdens zijn matches als pitcher meer strikeouts dan hits.

De lijst bevat de achternaam, de voornaam en het geboortejaar van deze spelers.

Sorteer achtereenvolgens alfabetisch op achternaam en voornaam, dan oplopend op geboortejaar.


## 3.6 Query 06

**Beschrijving**

Maak een lijst met informatie over spelers die

-geen fielder zijn geweest bij een team dat zijn home park in dezelfde stad had dan de geboortestad van de speler

-naar school zijn gegaan in staat "X"

Over deze spelers willen we graag weten wat hun achternaam en voornaam is en indien ze in de hall of fame hebben gestaan, in welk jaar dat was en hoeveel stemmen ze toen hebben gekregen.

Sorteer alfabetisch op achternaam en voornaam, oplopend op jaar en aflopend op aantal stemmen


## 3.7 Query 07

**Beschrijving**

We willen een lijst van alle spelers die:

-naar dezelfde school zijn gegaan als de manager die het team leidde waar de speler in het eerste jaar pitcher was, waarbij pitcher ook zijn eerste positie (stint) was. 

-"X" jaar nadat ze voor het laatst pitcher waren als batter gespeeld hebben (X kan ook negatief zijn)

-in totaal meer dan "Y" assists hebben als fielder

Van deze spelers willen we de achternaam, voornaam en het gemiddeld aantal errors per fielding game .

Sorteer aflopend op de errors, en alfabetisch op achternaam en voornaam. 


## 3.8 Query 08

**Beschrijving**

Maak een nieuwe tabel aan met de naam lahman2016."voornaam_achternaam" met daarin per speler:

-De voornaam en achternaam met kolomnamen(last_name, first_name)

-het aantal jaren waarin ze een award gewonnen hebben met kolomnaam (ycount)

We maken deze tabel enkel voor spelers die minder dan 20 jaar na het winnen van de laatste award als speler een award kregen als manager. 

Bouw daarna een tweede query die alle resultaten van deze nieuwe tabel teruggeeft gesorteerd op achternaam, voornaam en oplopende ycount.

**Belangrijk**

-Zorg ervoor dat als deze query meerdere keren gerund wordt, de tabel telkens opnieuw wordt aangemaakt (met dezelfde naam weliswaar) (CREATE OR REPLACE).  

-zorg er hier zeker voor dat lahman2016 ook de naam is van je geïmporteerde database, anders ga je de tabel niet makkelijk terugvinden. 



## 3.8 Query 09
**Beschrijving**

Verwijder nu alle rijen uit de nieuwe tabel zodat er uiteindelijk een tabel overblijft waarbij er enkel spelers zijn die hun aantal jaren waarin ze een award wonnen delen met maximum "X" andere spelers.

Bouw daarna een tweede query die alle resultaten van deze geupdate tabel teruggeeft gesorteerd op achternaam, voornaam en oplopende ycount.


# 3.9 Query 10

**Beschrijving**

Maak een tabel met per speler de achternaam en de voornaam. 
We willen dit enkel voor de spelers die bij alle teams pitcher zijn geweest die in jaar "X" meer dan "Y" wins hadden.
Sorteer alfabetisch op achternaam en voornaam.  

 
