import os
import shutil

from soundbrick.utils import make_unit_image, marge_images

DEFAULT_CONFIG = {
    "is_showlabel"        : True,
    "label_size"          : 15,
    "label_color"         : "#000000",
    "label_alpha"         : 1,
    "helical_edge_color"  : "#000000",
    "vartical_edge_color" : "#55ff55",
    "background_color"    : "#ffffff",
    "line_color"          : "#0000ff",
    "dpi"                 : 100,
    "yrange"              : [-1, 1],
    "xsize_per_second"    : 3.0,
    "ysize"               : 1.0,
    "aspect"              : 0.5,
}


class Soundbrick:
    def __init__(self, **kwargs):
        self.config = DEFAULT_CONFIG
        self.config.update(kwargs)
        print(self.config)
        # print('init')
        self.wavelist = []
        self.unitimagelist = []
        self.tmpdir = os.path.abspath('./tmp')
        # print('enter mkdir '+self.tmpdir)
        if os.path.exists(self.tmpdir):
            shutil.rmtree(self.tmpdir)
        os.mkdir(self.tmpdir)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # print('exit rmtree '+self.tmpdir)
        shutil.rmtree(self.tmpdir)

    def close(self):
        shutil.rmtree(self.tmpdir)

    def add(self, file_list):
        for w in file_list:
            path = os.path.abspath(w)
            print('add ' + path)
            outfile = self.tmpdir + '/' + \
                path.split('/')[-1].replace('.wav', '.jpg')
            self.unitimagelist.append(outfile)
            make_unit_image(path, outfile, self.config)
            self.wavelist.append(path)

    def show(self, file):
        """
        file : output image file
        """
        # print('makefig')
        # print(self.wavelist)
        marge_images(self.unitimagelist, file, self.config)
