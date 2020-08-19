import os
import attr
import typing
import shutil

from soundbrick.utils import make_unit_image, marge_images

@attr.s(kw_only=True)
class Soundbrick(object):
    is_showlabel: bool       = attr.ib(default=True)
    label_size: float        = attr.ib(default=15.0)
    label_color: str         = attr.ib(default="#000000")
    label_alpha: float       = attr.ib(default=1.0)
    helical_edge_color: str  = attr.ib(default="#000000")
    vartical_edge_color: str = attr.ib(default="#55ff55")
    background_color: str    = attr.ib(default="#ffffff")
    line_color: str          = attr.ib(default="#0000ff")
    dpi: int                 = attr.ib(default=100)
    yrange: typing.List[float] = attr.ib(default=[-1, 1])
    xsize_per_second:float     = attr.ib(default=3.0)
    ysize: float               = attr.ib(default=1.0)
    aspect: float              = attr.ib(default=0.5)

    wavelist       = attr.ib(init=False, default=[])
    unitimagelist   = attr.ib(init=False, default=[])
    tmpdir          = attr.ib(init=False, default='./tmp')

'''
    def __init__(self):
        self.wavelist = []
        self.unitimagelist = []
        self.tmpdir = os.path.abspath('./tmp')
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
'''
