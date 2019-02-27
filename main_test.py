#from probe import ffprobe_sync
from pytest import approx
import subprocess
import json
from pathlib import Path


def ffprobe_sync(filein: Path) -> dict:
    """ get media metadata """
    meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                	'-print_format', 'json',
                                	'-show_streams',
                                	'-show_format',
                                	str(filein)], universal_newlines = True)
    return json.loads(meta)

def test_duration():

    fnin = './video000.mp4'
    fnout_480 = './video000.mp4_480p.mp4'
    #fnout_720 = './video000.mp4_720p.mp4'

    #orig_meta = ffprobe_sync(fnin)
    orig_duration = subprocess.call(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1',fnin])

    #meta_480 = ffprobe_sync(fnout_480)
   # meta_720 = ffprobe_sync(fnout_720)
    #duration_720 = float(meta_720['streams'][0]['duration'])
    duration_480 = subprocess.call(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1',fnout_480])

    assert orig_duration == approx(duration_480)
    #assert orig_duration == approx(duration_720)


if __name__ == '__main__':
    test_duration()
