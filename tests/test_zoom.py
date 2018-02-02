import os
import sys
sys.path.insert(0, os.path.abspath('.'))

import tempfile
import shutil

from PIL import Image
from Augmentor import Operations


def test_zoom():

    original_dimensions = (800, 800)

    tmpdir = tempfile.mkdtemp()
    tmp = None
    try:
        tmp = tempfile.NamedTemporaryFile(dir=tmpdir, suffix='.JPEG')
        im = Image.new('RGB', original_dimensions)
        im.save(tmp.name, 'JPEG')

        r = Operations.ZoomRandom(probability=1, min_zoom=0.5)
        im_r = r.perform_operation(im)

        assert im_r is not None
        assert im_r.size == original_dimensions

    finally:
        if tmp is not None:
            tmp.close()
        shutil.rmtree(tmpdir)

def test_zoom_min_max():

    original_dimensions = (800, 800)

    tmpdir = tempfile.mkdtemp()
    tmp = None
    try:
        tmp = tempfile.NamedTemporaryFile(dir=tmpdir, suffix='.JPEG')
        im = Image.new('RGB', original_dimensions)
        im.save(tmp.name, 'JPEG')

        r = Operations.ZoomRandom(probability=1, min_zoom=0.5, max_zoom=0.9)
        im_r = r.perform_operation(im)

        assert im_r is not None
        assert im_r.size == original_dimensions

    finally:
        if tmp is not None:
            tmp.close()
        shutil.rmtree(tmpdir)
