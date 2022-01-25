# Threading en Tkinter

Om in het project TKinter en TI netjes met elkaar te laten samenwerken kan het handig zijn om zogeheten 'Threads' te
gebruiken.

Dat zijn truukjes (zoals de `tkinter.after` functie) die kunnen doen alsof je computer meerdere dingen tegelijk kan
doen.

Er zijn drie filetjes:

1. `withafter.py` Hier zie je wat het probleem is. Als je in een after-call 'dure dingen' doet, dan 'hangt' de
   user-interface. Voelt niet prettig in het gebruik. In dit geval is het 'dure ding' een `time.sleep`, maar in je
   TI-code is dit waarschijnlijk een while-loop)
2. Dit is de variant met 'Threads'. Je ziet dat ze heel erg lijken op een after-call. In beide gevallen geef je
   het 'werk' dat gedaan moet worden aan een of ander stuk code dat je zelf niet hebt geschreven.

   Ik gok dat je deze versie gewoon kan gebruiken, maar het is bekend dat in deze aanpak een paar bugs zitten als 
   je programma groter wordt en het Tkinter wat langer gaat kosten om bijv. z'n layout te berekenen.
3. Hier zie je een combinatie van beide aanpakken: 
   * after wordt gebruikt om netjes de tekst te laten zien
   * threads worden gebruikt om het werk te doen
   Dit is een stukje ingewikkelder, maar dit laat zien hoe je evt. problemen bij #2 zou kunnen omzeilen

Succes!