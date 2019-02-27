from probe import ffprobe_sync
from pytest import approx
#import subprocess


def test_duration480():

    fnin = './video000.mp4'
    fnout_480 = './video000.mp4_480p.mp4'


    orig_meta = ffprobe_sync(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])

    meta_480 = ffprobe_sync(fnout_480)
    duration_480 = float(meta_480['streams'][0]['duration'])

    assert orig_duration == approx(duration_480)

def test_duration720():

    fnin = './video000.mp4'
    fnout_720 = './video000.mp4_720p.mp4'

    orig_meta = ffprobe_sync(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])

    meta_720 = ffprobe_sync(fnout_720)
    duration_720 = float(meta_720['streams'][0]['duration'])

    assert orig_duration == approx(duration_720)

if __name__ == '__main__':
    test_duration480()
    test_duration720()

