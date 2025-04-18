# MinBZK GitHub Pages

Deze repository bevat de GitHub Pages site voor de MinBZK organisatie, met als primaire doel het afhandelen van redirects voor hoofdlettergevoelige URL's.

## Functionaliteit

Deze site zorgt voor de volgende redirects:

1. De homepage (`minbzk.github.io`) verwijst door naar `https://github.com/minbzk/`
2. Bij een 404 melding op `/algoritmekader/...` wordt er automatisch een redirect uitgevoerd naar `/Algoritmekader/...`

## Toekomstige wijzigingen

In de toekomst staat een hernoeming van de repository gepland, waarbij `Algoritmekader` wordt hernoemd naar `algoritmekader`. 
De redirect code in `404.html` bevat commentaar over hoe de redirect aangepast moet worden wanneer deze wijziging plaatsvindt.

## Configuratie

- De `index.html` regelt de redirect van de homepage
- De `404.html` bevat JavaScript dat de redirects afhandelt voor de hoofdlettergevoelige URL's

## Onderhoud

Als de hoofdlettergevoeligheid van repositories verandert, kan de redirect logica in `404.html` worden aangepast.
