# transformer_huggingface
learn more about huggingface transformer models

mv requirements.txt tmp.requirements.txt

pipreqs .

cat requirements.txt 

torch==1.5.1
transformers==3.0.2


docker build -t transformers .

docker run -it --rm --volume "$PWD":/app -m 6g transformers bash

python run.py