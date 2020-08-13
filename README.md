# wavetile

**wavetile** is simple sound files viwer.

## Usage
```python
from wavetile import Wavetile
with Wavetile() as wt:
    wt.add(['./sample_data/sound_0100.wav',
            './sample_data/sound_0101.wav',
            './sample_data/sound_0102.wav',
            './sample_data/sound_0103.wav',
            './sample_data/sound_0104.wav',
            './sample_data/sound_0105.wav',])
    wt.show('tile1.jpg')
```
![demo1](https://raw.githubusercontent.com/cygkichi/wavetile/master/examples/img/tile1.jpg)

```python
from wavetile import Wavetile
import glob

with Wavetile() as wt:
    file_list = glob.glob('./sample_data/*.wav')
    file_list = sorted(file_list)
    wt.add(file_list)
    wt.show('tile2.jpg')
```
![demo2](https://raw.githubusercontent.com/cygkichi/wavetile/master/examples/img/tile2.jpg)


## Installation

```bash
pip install wavetile # xxx
```


## Development Environment

```bash
# Launch a virtual environment
python3 -m venv ./venv
source ./venv/bin/activate

# Install modules
pip install --upgrade pip
pip install -r requestments.txt

# run oneshot.py
python oneshot.py ./sample_data

# test

# update
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository testpypi dist/*
```
