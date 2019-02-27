#from probe import ffprobe_sync
from pytest import approx
import subprocess
import json
#from pathlib import Path
import main as run

def ffprobe(file):
    """ get media metadata """
    meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                	'-print_format', 'json',
                                	'-show_streams',
                                	'-show_format',
                                	str(file)], universal_newlines = True)
    return json.loads(meta)


def test_duration():

    fnin = './video000.mp4'
    fnout_480 = './video000.mp4_480p.mp4'
    fnout_720 = './video000.mp4_720p.mp4'

    orig_meta = ffprobe(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])

    meta_480 = ffprobe(fnout_480)
    meta_720 = ffprobe(fnout_720)
    duration_720 = float(meta_720['streams'][0]['duration'])
    duration_480 = float(meta_480['streams'][0]['duration'])

    assert orig_duration == approx(duration_480, rel=0.01)
    assert orig_duration == approx(duration_720, rel=0.01)


if __name__ == '__main__':
    run.video720()
    test_duration()
