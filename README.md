
Documentation and tutorials for the Girls of Steel (FRC 3504) data science team.

Rendered docs are available at 


## Building docs locally

### One time setup
Create a virtual environment and install required software

```
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt 
```


### Actually building
```
sphinx-build -M html source build
```