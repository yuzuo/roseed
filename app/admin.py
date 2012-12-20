# -*- coding: utf-8 -*- 
from django.contrib import admin
from app.models import  *

#from django.db.models.fields.files import FieldFile
import os


def delete_file(filename):
    path, name = os.path.split(filename)
    media_root = settings.MEDIA_ROOT
    main_path = os.path.join(media_root, path, name).replace('\\','/')
    if os.path.isfile(main_path):
        os.remove(main_path)

def delete_thumb_file(filename):
    path,name=os.path.split(filename)
    media_root=settings.MEDIA_ROOT
    thumb_path=os.path.join(media_root,path,'thumb_'+name).replace('\\','/')
    if os.path.isfile(thumb_path):
        os.remove(thumb_path)
        


"""
介绍管理
"""
class IntroAdmin(admin.ModelAdmin):
    list_display = ('id','title','get_avatar','addtime')
    list_display_links=('title',)    
    list_filter = ('title',)
    actions = ('delete_selected',)
    list_per_page = 10
    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        if change==True and form.changed_data:
            intro=Intro.objects.extra(where=['id=%s'],params=[obj.id])[0]
            if 'avatar' in form.changed_data:
                delete_file(intro.avatar.name)
        obj.save()
        
    def delete_model(self, request, obj):
        """
        Given a model instance delete it from the database.
        """
        intro=Intro.objects.extra(where=['id=%s'],params=[obj.id])[0]
        delete_file(intro.avatar.name)
        obj.delete()
        
    def delete_selected(self, request, queryset):
        for obj in queryset:
            self.delete_model(request, obj)
    delete_selected.short_description = u'删除选中项' 

admin.site.register(Intro, IntroAdmin)




"""
课件栏目管理
"""
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','parent')    
    search_fields = ('title',)
    list_display_links = ('title',)
    list_filter = ('addtime',)
    list_per_page = 10

    actions = ('delete_selected',)
    def queryset(self, request):
        qs = super(CategoryAdmin, self).queryset(request)
        return qs.filter(pk__gt=1)
    
    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """

        obj.save()    
    def delete_model(self, request, obj):
        """
        Given a model instance delete it from the database.
        """
        category = Category.objects.extra(where=['id=%s'], params=[obj.id])[0]
        subcagegories=Category.objects.raw("select *from app_category where parent_id = %s",[category.id])
        if subcagegories:
            for sub in subcagegories:
                delete_file(sub.image.name)
        delete_file(category.image.name)
        obj.delete()
        
    def delete_selected(self, request, queryset):
        for obj in queryset:
            self.delete_model(request, obj)
    delete_selected.short_description = u'删除选中项'  
admin.site.register(Category, CategoryAdmin)



"""
栏目内容管理
"""
class ProductsAdmin(admin.ModelAdmin):
    list_display=('id','title','title','get_work','category')
    list_display_links=("title",)
    list_filter = ('category','addtime')
    actions = ('delete_selected',)
    list_per_page = 10
        
    def delete_selected(self, request, queryset):
        for obj in queryset:
            self.delete_model(request, obj)
    delete_selected.short_description = u'删除选中项' 

admin.site.register(Products, ProductsAdmin)




"""
标记管理
"""
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_display_links=('name',)    
    list_filter = ('addtime',)
    actions = ('delete_selected',)
    list_per_page = 10
    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
       
        obj.save()
    def delete_model(self, request, obj):
        """
        Given a model instance delete it from the database.
        """
        obj.delete()
        
    def delete_selected(self, request, queryset):
        for obj in queryset:
            self.delete_model(request, obj)
    delete_selected.short_description = u'删除选中项' 

admin.site.register(Comment,CommentAdmin)




"""
栏目内容管理
"""
class StoryAdmin(admin.ModelAdmin):
    list_display=('id','content','username')
    list_display_links=("content",)
    list_filter = ('content','addtime')
    actions = ('delete_selected',)
    list_per_page = 10
        
    def delete_selected(self, request, queryset):
        for obj in queryset:
            self.delete_model(request, obj)
    delete_selected.short_description = u'删除选中项' 

admin.site.register(Story, StoryAdmin)


class PhotosAdmin(admin.ModelAdmin):
    list_display=('id','get_photo','photos','addtime')
    list_display_links=("get_photo",)
    list_filter = ('addtime',)
    actions = ('delete_selected',)
    list_per_page = 10
    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        if change==True and form.changed_data:
            intro=Photos.objects.extra(where=['id=%s'],params=[obj.id])[0]
            if 'photos' in form.changed_data:
                delete_file(intro.photos.name)
                delete_file(intro.photos.name.replace('.jpg','-hover.jpg'))
                delete_file(intro.photos.name.replace('.jpg','-thumb.jpg'))
        obj.save()
        
    def delete_model(self, request, obj):
        """
        Given a model instance delete it from the database.
        """
        intro=Photos.objects.extra(where=['id=%s'],params=[obj.id])[0]
        delete_file(intro.photos.name)
        delete_file(intro.photos.name.replace('.jpg','-hover.jpg'))
        delete_file(intro.photos.name.replace('.jpg','-thumb.jpg'))

        obj.delete()
        
    
    
    
    def delete_selected(self, request, queryset):
        for obj in queryset:
            self.delete_model(request, obj)
    delete_selected.short_description = u'删除选中项' 

admin.site.register(Photos, PhotosAdmin)