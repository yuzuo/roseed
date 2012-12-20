# -*- coding: utf-8 -*- 
from __future__ import division
import re,datetime,time
from django.core.mail import send_mail
#from django.core.cache import  cache
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage,\
    InvalidPage

#import settings
from django.template.context import RequestContext
from django.shortcuts import render_to_response, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from models import *
import simplejson
import Image
from roseed.settings import uploaddir
import random
from PIL import ImageEnhance

#from string import strip
def index(request):
    variables=RequestContext(request,{})
    if request.method=="POST":
        content=request.FILES['fileToUpload']
        img=Image.open(content)
        cw, ch = img.size
        val=220
        ext='.jpg'
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_%d' % random.randint(0, 1000)
        savePath=os.path.join(uploaddir,fn+ext).replace('\\','/')
        img.save(savePath)

        
        
        
        
        if cw >= ch or ch<=cw:
            h = thumb_img(cw, ch, 220)
            img = img.resize((220, 230), Image.ANTIALIAS)
        tsavePath=os.path.join(uploaddir,fn+"-thumb"+ext).replace('\\','/')
        img.save(tsavePath)
        
        
        pimg=ImageEnhance.Brightness(img).enhance(0.7)
        psavePath=os.path.join(uploaddir,fn+"-hover"+ext).replace('\\','/')
        pimg.save(psavePath);
        
        
        media=os.path.join('Photo',fn+ext).replace('\\','/')

        result=Photos.objects.create(photos=media)
        
        result.save()
    
    stories=Story.objects.all().order_by('-addtime')[:9]

        
    photos=Photos.objects.all().order_by('-addtime')[:9]
    
    variables=RequestContext(request,{'stories':stories,'photos':photos})
    return render_to_response('index.html',variables)

@csrf_protect
def publish(request):
    resp = None
    if request.method=="POST":
        content=request.POST.get('story',None)
        name=request.POST.get('name',None)
        if content:
            if name is None or name=="":
                name="游客"
            obj=Story.objects.create(content=content,username=name)
            obj.save()
            resp={'id':obj.id,'username':obj.username,'content':obj.content,'var_date':str(obj.addtime.strftime("%Y-%m-%d"))}
    return HttpResponse(simplejson.dumps(resp), mimetype='application/javascript')


#@csrf_protect
#def photoUpload(request):
#    variables=RequestContext(request,{})
#    if request.method=="POST":
#        content=request.FILES['fileToUpload']
#        img=Image.open(content)
#        cw, ch = img.size
#        val=220
#        
#        ext='.jpg'
#        fn = time.strftime('%Y%m%d%H%M%S')
#        fn = fn + '_%d' % random.randint(0, 1000)
#                    
#                    
#        if cw >= val:
#            h = thumb_img(cw, ch, val)
#            img = img.resize((val, h), Image.ANTIALIAS)
#            media=os.path.join('Photo',fn+ext).replace('\\','/')
#            savePath=os.path.join(uploaddir,fn+ext).replace('\\','/')
#            img.save(savePath)
#        result=Photos.objects.create(photos=media)
#        
#        result.save()
#        variables=(RequestContext,{'id':result.id,'fn':(settings.MEDIA_URL+result.photos.name).replace('\\','/')})
#    return render_to_response('index.html',variables)

def thumb_img(x, y, size):
    if x > size:
        z = int(y * size / x)
    else:
        z = y
    return z