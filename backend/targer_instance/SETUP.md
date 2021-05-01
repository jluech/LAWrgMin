# Targer
_(Instance received from Florian Ruosch)_

### Setup Python

Make sure you are using python v3.5.3 for this
- Either directly install python 3.5.3 globally on your system
- Alternatively, use pyenv
    - Install [pyenv]( https://github.com/pyenv/pyenv-installer)
    - Install pyenv python version 3.5.3 `pyenv install 3.5.3`
    - Set local python version in Targer directory to 3.5.3 `pyenv local 3.5.3`

### Setup Targer

- Get tensorflow 1.5.0 from `pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.5.0-py3-none-any.whl`
- Install remaining requirements with `pip install -r requirements.txt`.
  If you have any conflicts with the following dependencies, try to install them separately (only as many changes as are required!)
    - Scipy 1.3.1 seems to be tricky, try it out first `pip install scipy==1.3.1` - otherwise upgrade to `pip install scipy==1.3.2`
    - If torch v1.2.0 is not working, upgrade 1.4.0 with `pip install torch==1.4.0` (apparently that is the latest working version)
    - If torchvision v0.4.0 is not working, upgrade to 0.5.0 with `pip install torchvision==0.5.0` (apparently that is the latest working version)
    - Adjust the requirements file with all version changes you made (do **NOT** commit this ever as those are your local changes)

### Prepare Models

Models are huge and were left away for this repository.
To get them, follow the instructions in the [models](./models/add_models.md) folder

### Prepare Word Vectors

Execute the scripts in the [embeddings](lstm/embeddings) folder to download the fasttext and glove word vectors.
