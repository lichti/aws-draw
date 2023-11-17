# AWS Draw

## Generate AWS Diagram with Python and d2lang

## How to run?

- git glone git@github.com:lichti/aws-draw.git
- cd aws-draw
- virtualenv venv
- source venv/bin/activate
- pip install boto3 py-d2
- mv credentials.ini.example credentials.ini
- mv settings.ini.example settings.ini
- edit credentials.ini and settings.ini
- python run.y && d2 --scale 0.5 graph.d2