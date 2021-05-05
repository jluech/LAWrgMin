# Backend Setup

## Python

Make sure you are using python v3.5.3 for this
- Either directly install python 3.5.3 globally on your system
- Alternatively, use pyenv
    - Install [pyenv]( https://github.com/pyenv/pyenv-installer)
    - Install pyenv python version 3.5.3 `pyenv install 3.5.3`
    - Set local python version in Targer directory to 3.5.3 `pyenv local 3.5.3`



## Backend API

### Setup API

- Install the necessary packets to run your local backend server with its flask API.
  Do so by installing the requirements listed in the `requirements.txt` file via pip:
  `pip install -r requirements.txt`
- You can start a local backend server by running the `__main__` script:
  `python __main__.py`.
  It comes with an option to remove any local files that were uploaded for tagging in previous sessions.
  To do so, run `python __main__.py --cleanup-files`.



## Corpus Processing

### Install dependencies

- Install textract v1.6.3. This will probably require manual installation.
  For more details see the [official documentation](https://textract.readthedocs.io/en/stable/installation.html).
  Verify that you install the additional packages for the parsers you need. 
- Install remaining requirements with `pip install -r corpus_processing/requirements.txt`.

### Adjust external repositories

When you run the main script for the first time it will clone the `standoff2conll` repository.
Inside that folder you can find the `standoff2conll.py` script.
Open it and search for the method `convert_files(files, options)`.
At the end of said method, replace the `stdout` log with the following piece of code:

```python
filename = str(files).replace(']', '').replace('[', '').replace('.ann', '.conll').replace('\'', '')
conll_data = conll_data.replace('\t', ' ')
if os.path.exists(filename):
    os.remove(filename)
casefile = open(filename, 'x')
casefile.write('-DOCSTART- 0\n\n')
casefile.write(conll_data)
casefile.close()
```



## Targer
_(Instance received from Florian Ruosch)_

### Setup Targer

- Get tensorflow 1.5.0 from `pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.5.0-py3-none-any.whl`
- Install remaining requirements with `pip install -r targer_instance/requirements.txt`.
  If you have any conflicts with the following dependencies, try to install them separately (only as many changes as are required!)
    - Scipy 1.3.1 seems to be tricky, try it out first `pip install scipy==1.3.1` - otherwise upgrade to `pip install scipy==1.3.2`
    - If torch v1.2.0 is not working, upgrade 1.4.0 with `pip install torch==1.4.0` (apparently that is the latest working version)
    - If torchvision v0.4.0 is not working, upgrade to 0.5.0 with `pip install torchvision==0.5.0` (apparently that is the latest working version)
    - Adjust the requirements file with all version changes you made (do **NOT** commit this ever as those are your local changes)

### Prepare Models

Models are huge and were left away for this repository.
To get them, follow the instructions in the [models](./targer_instance/models/add_models.md) folder

### Prepare Word Vectors

Execute the scripts in the [embeddings](./targer_instance/lstm/embeddings) folder to download the fasttext and glove word vectors.
