# transformer huggingface 1st experiment
learn more about huggingface transformer models

## command line snippets
mv requirements.txt tmp.requirements.txt

pipreqs .

cat requirements.txt 

torch==1.5.1
transformers==3.0.2


docker build -t transformers .

docker run -it --rm --volume "$PWD":/app -m 6g transformers bash

## examples to try (inside docker container)

python run.py (this will download and install the model inside of the container)

examples source: [paralleldots.com](https://www.paralleldots.com/named-entity-recognition)

In a statement issued with France and UN chief António Guterres on Saturday,China committed to “update” its climate target “in a manner representing a progression beyond the current one”.  It also vowed to publish a long term decarbonisation strategy by next year.

Lionel Andrés Messi vuelve a ser el gran protagonista en las portadas de la prensa deportiva internacional al día siguiente de un partido de Champions.

Carles Alena brachte Barcelona am Dienstag nach der Pause auf die Siegerstraße, wenig später verwandelte Luis Suarez einen Handelfmeter.

## reading material

* [huggingface intro](https://huggingface.co/transformers/quicktour.html)
* [model summary](https://huggingface.co/transformers/model_summary.html)
* [transformer intro](http://nlp.seas.harvard.edu/2018/04/03/attention.html)
* [supported tasks with examples](https://huggingface.co/transformers/task_summary.html)
* [train spanish ner transformer](https://chriskhanhtran.github.io/posts/named-entity-recognition-with-transformers/)
