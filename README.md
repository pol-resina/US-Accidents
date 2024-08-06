# US-Accidents 23

En aquest README explicarem com executar el codi per otenir els mateixos resultats que hem obtingut nosaltres. En primer lloc, cal destacar que trobem el report i l'apendix del report i que el codi esta en angles ja que tenim pensat pujar el projecte a github. En segon lloc, l'estructura de carpetes del projecte és la següent:

* **data**: Carpeta on es troben els fitxers csv amb les dades. Trobem les dades originals tretres de kaggle i les dades ja netejades. De la mateixa manera, trobem els fitxers amb les dades per a la predicció de l'autor, que s'explica en el report. 

* **notebooks**: Carpeta on es troben els notebooks amb el codi. Els codis funcionen i no donen cap error i es pot veure la sortida ja que els hem executat abans. No obstant aixo, si es volen executar, cal tenir en compte l'ordre d'execució.

En primer lloc, hem fet un notebook per a visualitzar les dades i fer un anàlisi exploratori. Aquest notebook es troba a la carpeta **notebooks** i es diu **data_exploration.ipynb**. 

En segon lloc, s'ha de tenir en compte el notebook **preprocessing.ipynb**. En aquest notebook es netegen les dades i es preparen per a la predicció i es guarden 4 csv amb les dades netejades (X_train, y_train, X_test, y_test).

En tercer lloc, s'ha de tenir en compte el notebook **predict_author.ipynb**. En aquest notebook es preparen i es guarden les dades per la predicció d'un cas que hem plantejat nosaltres.

Per últim, s'ha de tenir en compte el notebook **model.ipynb**. En aquest notebook s'entrenen tots els models i es fa la comparació entre ells. Finalment, es treuen mètriques per a veure quin model es millor que s'expliquen en el report. De fet, tot el que esta en el report es troba en aquests notebooks. No es recomana executar el notebook **model.ipynb** ja que tarda molt en executar-se (1 hora més o menys).


