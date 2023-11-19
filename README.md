# AWS Draw

Generating Diagrams for AWS Accounts with Python and [d2lang](https://d2lang.com)

I'm aiming to enhance the visibility and control of infrastructures within AWS through more precise and detailed diagrams.

The AWS Draw project originated from my personal need to create detailed diagrams illustrating accounts, resources, and their interconnections within AWS. Starting with a functional script to address a specific issue, I'm now striving to evolve it into a more comprehensive package.

There's a challenge in generating the d2lang structure, potentially requiring the creation of a class or package to address this.

I'm open to collaborations! If you have ideas for diagram types that could aid in managing and securing AWS or wish to contribute code, I'd be delighted to receive pull requests and suggestions (just open an issue on GitHub).

Together, we can expand and refine this tool for the benefit of the AWS community.

## How to run?

```sh
git clone git@github.com:lichti/aws-draw.git && cd aws-draw
virtualenv venv
source venv/bin/activate
pip -r requirements.txt
mv credentials.ini.example credentials.ini # edit credentials.ini
mv settings.ini.example settings.ini # edit settings.ini
python run.y && d2 --scale 0.5 graph.d2
```
