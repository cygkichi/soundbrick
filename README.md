# wavetile

**wavetile** is simple sound files viwer.

## Usage

```python
from wavetile import Wavetile
wt = Wavetile()
wt.add(['/your/sound/path/sound_001.wav',
	'/your/sound/path/sound_002.wav',
	'/your/sound/path/sound_003.wav',
	'/your/sound/path/sound_004.wav'])
wt.show('tile.jpg')
wt.close()
```

## Installation

```bash
pip install wavetiler
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
```
