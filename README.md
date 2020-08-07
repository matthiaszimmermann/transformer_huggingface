# transformer_huggingface
learn more about huggingface transformer models

## command line snippets
mv requirements.txt tmp.requirements.txt

pipreqs .

cat requirements.txt 

torch==1.5.1
transformers==3.0.2


docker build -t transformers .

docker run -it --rm --volume "$PWD":/app -m 6g transformers bash

## examples to try inside docker container

python run.py

examples source: (paralleldots.com)[https://www.paralleldots.com/named-entity-recognition]

In a statement issued with France and UN chief António Guterres on Saturday,China committed to “update” its climate target “in a manner representing a progression beyond the current one”.  It also vowed to publish a long term decarbonisation strategy by next year.

Lionel Andrés Messi vuelve a ser el gran protagonista en las portadas de la prensa deportiva internacional al día siguiente de un partido de Champions.

Carles Alena brachte Barcelona am Dienstag nach der Pause auf die Siegerstraße, wenig später verwandelte Luis Suarez einen Handelfmeter.