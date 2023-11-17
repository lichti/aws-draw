# AWS Draw

Generate AWS Diagram with Python and [d2lang](https://d2lang.com)

## How to run?

```sh
git glone git@github.com:lichti/aws-draw.git && cd aws-draw
virtualenv venv
source venv/bin/activate
pip -r requirements.txt
mv credentials.ini.example credentials.ini # edit credentials.ini
mv settings.ini.example settings.ini # edit settings.ini
python run.y && d2 --scale 0.5 graph.d2
```
