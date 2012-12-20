#coding=utf8
from __future__ import division

from django.core.files.storage import FileSystemStorage
#from Clothes.system.function import make_thumb
import  os, time, random
from PIL import Image,ImageEnhance
from roseed import settings


#import ImageFile
class OpacityStorage(FileSystemStorage):
    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        super(OpacityStorage, self).__init__(location, base_url)

    #重写 _save方法        
    def _save(self, name, content):#content=request.FILES['file']
        name = name.replace('\\', '/')
        ext = os.path.splitext(name)[1]
        d = os.path.dirname(name)
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_%d' % random.randint(0, 1000)
        name = os.path.join(d, fn + ext)
        name2 = super(OpacityStorage, self)._save(name, content)
        
        img_over = Image.open(self.path(name2))
        opc_over = ImageEnhance.Brightness(img_over).enhance(0.3)
        opc_over.save(self.path(d+"/" + fn+"-over" + ext))
        
        img_down=Image.open(self.path(name2))
        opc_down = ImageEnhance.Brightness(img_down).enhance(0.3)
        opc_down.save(self.path(d+"/" + fn+"-down" + ext))
        

        return name2
    
