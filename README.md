# MinBZK GitHub Pages

Deze repository bevat de GitHub Pages site voor de MinBZK organisatie, met als primaire doel het afhandelen van redirects voor hoofdlettergevoelige URL's.

## Functionaliteit

Deze site zorgt voor de volgende redirects:

1. De homepage (`minbzk.github.io`) verwijst door naar `https://github.com/minbzk/`
2. Bij een 404 melding op `/algoritmekader/...` wordt er automatisch een redirect uitgevoerd naar `/Algoritmekader/...`
3. Bij een 404 melding op `/NeRDS/...` wordt er doorgestuurd naar dezelfde pagina op `https://nederlandsedigitaledienst.github.io/NeRDS/...`. De NeRDS is verhuisd naar de organisatie NederlandseDigitaleDienst, en GitHub stuurt een Pages-adres na een verhuizing niet zelf door.

4. Bij een 404 melding op `/storybook/...` wordt er doorgestuurd naar dezelfde pagina op `https://nederlandsedigitaledienst.github.io/design-system/...`. De Storybook is verhuisd en heet daar het NLDD Designsysteem.

Een verhuisde site voeg je toe aan de lijst `moved` in `404.html`. De redirect werkt pas als de oude repository in deze organisatie geen eigen Pages-site meer heeft, want die gaat voor.

## Toekomstige wijzigingen

In de toekomst staat een hernoeming van de repository gepland, waarbij `Algoritmekader` wordt hernoemd naar `algoritmekader`. 
De redirect code in `404.html` bevat commentaar over hoe de redirect aangepast moet worden wanneer deze wijziging plaatsvindt.

## Configuratie

- De `index.html` regelt de redirect van de homepage
- De `404.html` bevat JavaScript dat de redirects afhandelt voor de hoofdlettergevoelige URL's

## Onderhoud

Als de hoofdlettergevoeligheid van repositories verandert, kan de redirect logica in `404.html` worden aangepast.

## Licentie
Dit project is gelicentieerd onder de [European Union Public License v1.2](./LICENSE).

