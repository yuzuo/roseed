#-*-coding:utf-8-*-
from django.db import models
import os
from roseed import settings 
# Create your models here.
from system.rename import RenameStorage
from django.core.exceptions import ValidationError

def validate_image_extension(obj):
    ext=os.path.splitext(obj.name)[1].lower()
    if ext not in (u'.png',u'.jpeg',u'.jpg',u'.bmp',u'gif'):
        raise ValidationError(u'Only png,jpeg,jpg,bmp,gif type allowed here')



class Intro(models.Model):
    title=models.CharField(max_length='100',verbose_name="标题")
    desc=models.TextField(verbose_name="介绍",blank=True,null=True)
    avatar=models.ImageField(upload_to="Avatar",verbose_name="头像",storage=RenameStorage(),validators=[validate_image_extension])
    addtime=models.DateTimeField(auto_now_add=True,editable=False,verbose_name=u'添加时间')
    updatetime=models.DateTimeField(auto_now=True,editable=False,verbose_name=u'编辑时间')
    def __unicode__(self):
        return u'%s' %(self.title)
    def __str__(self):
        return '%s' %self.title
    class Meta:
        verbose_name_plural=u'个人信息'
        verbose_name=u'个人信息'
        ordering=['-addtime']
    def get_avatar(self):
        if self.avatar is not None and self.avatar.name is not '':
            return u"<img src=%s width=50 />" %(settings.MEDIA_URL+self.avatar.name)
        else:
            return u'No image here'       
    get_avatar.short_description = '头像'
    get_avatar.allow_tags = True
    
class Category(models.Model):
    title=models.CharField(max_length=100,verbose_name='名称')
    parent=models.ForeignKey("self",verbose_name='父级')
    orderNum=models.IntegerField(default=1,verbose_name="排序")
    addtime = models.DateTimeField(auto_now_add=True, editable=False,verbose_name="添加时间")
    updatetime = models.DateTimeField(auto_now=True, editable=False,verbose_name="编辑时间")
    def __unicode__(self):
        return u'%s' %(self.title)
    class Meta:
        verbose_name_plural="分类"
        verbose_name="分类"
        ordering = ['-addtime']
        
class Products(models.Model):
    category=models.ForeignKey(Category,verbose_name=u"类别")
    title=models.CharField(max_length=100,verbose_name=u'标题')
    desc=models.TextField(verbose_name="描述",blank=True,null=True)
    work=models.ImageField(upload_to="Work",verbose_name="展示",storage=RenameStorage(),validators=[validate_image_extension])
    orderNum=models.IntegerField(default=1,verbose_name=u'排序')
    addtime=models.DateTimeField(auto_now_add=True,editable=False,verbose_name=u'添加时间')
    updatetime=models.DateTimeField(auto_now=True,editable=False,verbose_name=u'编辑时间')
    def __unicode__(self):
        return u'%s' %(self.title)
    def __str__(self):
        return '%s' %self.title
    def get_work(self):
        if self.avatar is not None and self.work.name is not '':
            return u"<img src=%s width=50 />" %(settings.MEDIA_URL+self.work.name)
        else:
            return u'No image here'       
    get_work.short_description = '展示'
    get_work.allow_tags = True
    
    class Meta:
        verbose_name_plural=u'产品'
        verbose_name=u'产品'
        ordering=['-addtime']
        
        
class Comment(models.Model):
    name=models.CharField(max_length=100,verbose_name=u'用户名')
    desc=models.TextField(verbose_name="留言内容")
    addtime=models.DateTimeField(auto_now_add=True,editable=False,verbose_name=u'添加时间')
    updatetime=models.DateTimeField(auto_now=True,editable=False,verbose_name=u'编辑时间')
    def __unicode__(self):
        return u'%s' %(self.name)
    def __str__(self):
        return '%s' %self.name
    class Meta:
        verbose_name_plural=u'评论'
        verbose_name=u'评论'
        ordering=['-addtime']
        
class Story(models.Model):
    username=models.TextField(verbose_name="用户名",default='匿名',max_length=100)
    content=models.TextField(verbose_name="内容")
    addtime=models.DateTimeField(auto_now_add=True,editable=False,verbose_name=u'添加时间')
    updatetime=models.DateTimeField(auto_now=True,editable=False,verbose_name=u'编辑时间')    
    def __unicode__(self):
        return u'%s' %(self.content[:10])
    def __str__(self):
        return '%s' %self.content[:10]
    class Meta:
        verbose_name_plural=u'留言墙'
        verbose_name=u'留言墙'
        ordering=['-addtime']    



class Photos(models.Model):
    photos=models.ImageField(upload_to="Photo",verbose_name="贴画",storage=RenameStorage(),validators=[validate_image_extension])
    addtime=models.DateTimeField(auto_now_add=True,editable=False,verbose_name=u'添加时间')
    updatetime=models.DateTimeField(auto_now=True,editable=False,verbose_name=u'编辑时间')    
    
    def get_photo(self):
        if self.photos is not None and self.photos.name is not '':
            return u"<img src=%s width=50 />" %(settings.MEDIA_URL+self.photos.name)
        else:
            return u'No image here'       
    get_photo.short_description = '贴画'
    get_photo.allow_tags = True
    
    class Meta:
        verbose_name_plural=u'图片墙'
        verbose_name=u'图片墙'
        ordering=['-addtime']   