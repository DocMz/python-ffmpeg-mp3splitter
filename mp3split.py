# Split large mp3 files in smaller parts
# First Argument is mp3 file to split, second is length in seconds the part files should have in the end
# Requires python3 and ffmpeg and ffprobe to work

import subprocess
import re
import math
import sys

INPUTFILE = sys.argv[1]
SPLITDURATION = sys.argv[2]

def getTotalDuration(inputfile):
    filelengthOutput = subprocess.run(["ffprobe", "-i", inputfile, "-show_format",
                                       "-v", "quiet"], stdout=subprocess.PIPE).stdout.decode("UTF-8")
    match = re.search("duration=([0-9]*)", filelengthOutput)
    return int(match.group(1)) + 1


splitcount = math.ceil(getTotalDuration(INPUTFILE) / SPLITDURATION)

print(splitcount)

for i in range(splitcount):
    print(i)
    subprocess.run(["ffmpeg", "-i", INPUTFILE, "-ss", str(i * SPLITDURATION),
                    "-t", str(SPLITDURATION), "part" + str(i) + ".mp3"])
