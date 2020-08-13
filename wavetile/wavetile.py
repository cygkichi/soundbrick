import os
import shutil

from wavetile.utils import make_unit_image, marge_images

class Wavetile:
    def __init__(self):
        print('init')
        self.tmpdir = os.path.abspath('./tmp')
        self.wavelist = []
        self.unitimagelist =[]

    def __enter__(self):
        print('enter mkdir '+self.tmpdir)
        if os.path.exists(self.tmpdir):
            shutil.rmtree(self.tmpdir)
        os.mkdir(self.tmpdir)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('exit rmtree '+self.tmpdir)
        shutil.rmtree(self.tmpdir)

    def add(self, file_list):
        for w in file_list:
            path = os.path.abspath(w)
            print('add '+path)
            outfile = self.tmpdir + '/' + path.split('/')[-1].replace('.wav','.jpg')
            self.unitimagelist.append(outfile)
            make_unit_image(path, outfile)
            self.wavelist.append(path)

    def show(self, file):
        """
        file : output image file
        """
        print('makefig')
        print(self.wavelist)
        marge_images(self.unitimagelist, file)


