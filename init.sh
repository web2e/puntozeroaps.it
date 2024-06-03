#!/bin/bash
#eseguire lo script nella root del progetto 

#imposta i permessi correttamente al file entrypoint.sh esecuito sull'avvio dei container
chmod +x entrypoint.sh

#creazione delle cartelle nella root di progetto
mkdir postgresql
mkdir backup

#creazione delle cartelle nella sottocartella etc
cd etc/
mkdir addons
mkdir filestore
mkdir sessions
