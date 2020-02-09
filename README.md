# python-ffmpeg-mp3splitter

pythonscript for splitting large mp3 files into smaller ones.

Split large mp3 files in smaller parts

## Usage

Requires python3 and ffmpeg and ffprobe to work

First Argument is mp3 file to split, second is length in seconds the part files should have in the end

## Example

Spilts my.mp3 into parts with a 1800 second duration (30mins).

```
python mp3split.py ./my.mp3 1800
```
