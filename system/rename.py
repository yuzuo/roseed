#coding=utf8
from __future__ import division

from django.core.files.storage import FileSystemStorage
#from Clothes.system.function import make_thumb
import Image, os, time, random
from roseed import settings


class RenameStorage(FileSystemStorage):
    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        super(RenameStorage, self).__init__(location, base_url)

    #重写 _save方法        
    def _save(self, name, content):#content=request.FILES['file']
        name = name.replace('\\', '/')
        ext = os.path.splitext(name)[1].lower();
        d = os.path.dirname(name)
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_%d' % random.randint(0, 1000)
        name = os.path.join(d, fn + ext)
        name2 = super(RenameStorage, self)._save(name, content)
        return name2
