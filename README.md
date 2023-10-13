# plant_disease_classification

### End-to-End implementation of a Plant Disease Classification model using CNN

# Plant-Disease-Classification--Project

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

# How to run?

### STEPS:

Clone the repository

```bash
https://github.com/nirmitktripathii/plant_disease_classification
```

### STEP 01- Create a conda environment after opening the repository

```terminal
python venv create plant_disease python=3.9.5 -y
```

```terminal
cd ./plant_diseae/Script/activate cnncls
```

### STEP 02- install the requirements

```terminal
pip install -r requirements.txt
```

```terminal
# Finally run the following command
python app.py
```

Now,

```terminal
open up you local host and port
```

### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag
