#coding=utf8
from __future__ import division

from django.core.files.storage import FileSystemStorage
#from Clothes.system.function import make_thumb
import Image, os, time, random
from PIL import Image
from roseed import settings


#import ImageFile
class ImageStorage(FileSystemStorage):
    def __init__(self, location=settings.MEDIA_ROOT,size=160, base_url=settings.MEDIA_URL):
        super(ImageStorage, self).__init__(location, base_url)

    #重写 _save方法        
    def _save(self, name, content):#content=request.FILES['file']
        name = name.replace('\\', '/')
        ext = os.path.splitext(name)[1]
        d = os.path.dirname(name)
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_%d' % random.randint(0, 1000)
        name = os.path.join(d, fn + ext)
        name2 = super(ImageStorage, self)._save(name, content)
        img = Image.open(self.path(name2))
        cw, ch = img.size
        if cw >= ch:
            h = thumb_img(cw, ch, self.size)
            img = img.resize((self.size, h), Image.ANTIALIAS)
        else:
            w = thumb_img(ch, cw, self.size)
            img = img.resize((w, self.size), Image.ANTIALIAS)
        img.save(self.path(d + '/thumb_' + fn + ext))
        return name2

def thumb_img(x, y, size):
    if x > size:
        z = int(y * size / x)
    else:
        z = y
    return z
