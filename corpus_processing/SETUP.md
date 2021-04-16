# Corpus Processing

### Setup Python

Make sure you are using python v3.6.13 for this
- Either directly install python 3.6.13 globally on your system
- Alternatively, use pyenv
    - Install [pyenv]( https://github.com/pyenv/pyenv-installer)
    - Install pyenv python version 3.6.13 `pyenv install 3.6.13`
    - Set local python version to 3.6.13 `pyenv local 3.6.13`

### Install dependencies
- Install textract v1.6.3. This will probably require manual installation.
  For more details see the [official documentation](https://textract.readthedocs.io/en/stable/installation.html).
  Verify that you install the additional packages for the parsers you need. 
- Install remaining requirements with `pip install -r requirements.txt`.
