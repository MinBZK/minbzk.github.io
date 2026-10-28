# MinBZK GitHub Pages

Deze repository bevat de GitHub Pages site voor de MinBZK organisatie, met als primaire doel het doorsturen van sites die naar een ander adres zijn verhuisd.

## Functionaliteit

Deze site zorgt voor de volgende redirects:

1. De homepage (`minbzk.github.io`) verwijst door naar `https://github.com/minbzk/`
2. Bij een 404 melding op `/Algoritmekader/...` (ook met een kleine letter) wordt er doorgestuurd naar dezelfde pagina op `https://algoritmes.overheid.nl/nl/algoritmekader/...`. Het Algoritmekader staat nu op de site van het Algoritmeregister; de paden van de pagina's zijn gelijk gebleven.
3. Bij een 404 melding op `/NeRDS/...` wordt er doorgestuurd naar dezelfde pagina op `https://nerds.digitaledienst.overheid.nl/...`. De NeRDS is verhuisd naar de Nederlandse Digitale Dienst en heeft daar een eigen domein; GitHub stuurt een Pages-adres na een verhuizing niet zelf door.

4. Bij een 404 melding op `/storybook/...` wordt er doorgestuurd naar dezelfde pagina op `https://nederlandsedigitaledienst.github.io/design-system/...`. De Storybook is verhuisd en heet daar het NLDD Designsysteem.

5. Bij een 404 melding op `/regelrecht/...` wordt er doorgestuurd naar dezelfde pagina op `https://regelrecht.rijks.app/...`. De landingspagina van RegelRecht stond eerst op dit adres en heeft nu een eigen domein. Gedrukte publicaties verwijzen nog naar het oude adres.

Voor de verhuisde sites staat er daarnaast per oude pagina een echte doorstuurpagina in de mappen `NeRDS/`, `storybook/`, `regelrecht/` en `Algoritmekader/`. Een zoekmachine ziet op de 404-pagina alleen een 404; een bestaande pagina met een directe `meta refresh` leest Google als een permanente redirect. Die pagina's maak je opnieuw met `python generate_redirects.py`, dat de lijst uit de sitemap van de nieuwe site haalt. De regel in `404.html` vangt de adressen op waar geen pagina voor is.

`Algoritmekader/html/beslishulp.html` staat niet in de sitemap en is met de hand gemaakt. Het is de losse pagina van de beslishulp AI-verordening die het oude Algoritmekader in een iframe toonde; hij stuurt door naar `https://algoritmes.rijksapp.nl/beslishulp-ai-verordening`. Het script laat dit bestand staan.

Een verhuisde site voeg je toe aan de lijst `moved` in `404.html`. De redirect werkt pas als de oude repository in deze organisatie geen eigen Pages-site meer heeft, want die gaat voor.

## Configuratie

- De `index.html` regelt de redirect van de homepage
- De `404.html` bevat JavaScript dat de redirects afhandelt voor de verhuisde sites

## Onderhoud

Krijgt een verhuisde site nieuwe pagina's, draai dan `python generate_redirects.py` opnieuw.

## Licentie
Dit project is gelicentieerd onder de [European Union Public License v1.2](./LICENSE).

