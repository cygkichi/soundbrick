# wavetile

**wavetile** is simple sound files viwer.

## Usage
### Example.1
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
### Example.2
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


## Args

```python
Wavetile(
    is_showlabel = True,     #
    label_size = 15,         #
    label_color = "#ff5470", #
    label_alpha = 1.0,       #
    helical_edge_color = "#232323",  #
    vartical_edge_color = "#ff5470", #
    background_color = "#f5f5dc",    #
    line_color = "#078080",          #
    yrange = [-1,1]                  #
)

Wavetile().add(
    file_list # list of input-sound-filepath
    )

Wavetile().show(
    file # output-image-filepath
)

```

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
