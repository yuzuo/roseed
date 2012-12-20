# -*- coding: utf-8 -*- 
from __future__ import division

from django import template
from app.models import Comment
register = template.Library()
from roseed import settings
import re,os
p=re.compile('^#(.*?)#.*')

#from app.models import *

#from views import *
#@register.inclusion_tag('find/story.html')
#def list_for_story(content_type):
    



#@register.inclusion_tag('bookurl.html')
#def books_for_author(author):
#    books = Book.objects.filter(authors__id=author.id)
#    return {'books': books}

@register.filter
def tagA(value):
    r=p.match(value)
    if r:
#        value = re.sub('<.*?>', '', value)
        value = re.sub('<script .*?>', '', value)
        value = re.sub('<script/>', '', value)
        value = re.sub('^#.*?#', '<a href="/story/?tag='+r.groups()[0]+'">#'+r.groups()[0]+'#</a>', value)
        return value
    return value

@register.filter
def mod(argstr):
    argstr_reverse=argstr[::-1]
    var=""
    for k,v in enumerate(argstr_reverse):
        if k%3==0 and k>0:
            var+=","
        var+=v
    
    return var[::-1]
#    return str(int(value) % int(arg))

@register.filter
def dodiv(value,arg):
    return value/arg

@register.filter
def domod(value,arg):
    return int(value)%int(arg)
@register.filter()
def get_photo_url(val):
    
    ext = os.path.splitext(val)[1]
    fn=os.path.splitext(val)[0]
    return os.path.join(settings.MEDIA_URL,fn+'-hover'+ext).replace('\\','/')

@register.filter
def getOrigPic(value):
    return value.replace("_.jpg",".jpg")





@register.inclusion_tag('find/Comment.html')
def content_for_comment(connentID):
    comments = Comment.objects.extra(where=['content_id=%s'],params=[connentID],order_by=['-addtime'])
    return {'comments': comments}

#import datetime
#
#class CurrentTimeNode(template.Node):
#    def __init__(self, format_string):
#        self.format_string = str(format_string)
#
#    def render(self, context):
#        now = datetime.datetime.now()
#        return now.strftime(self.format_string)
#    
#    
#    
#@register.tag
#def current_time(parser, token):
#    try:
#        tag_name, format_string = token.split_contents()
#    except ValueError:
#        msg = '%r tag requires a single argument' % token.split_contents()[0]
#        raise template.TemplateSyntaxError(msg)
#    return CurrentTimeNode(format_string[1:-1])
#
#
#
#
#
#import re
#
#class CurrentTimeNode3(template.Node):
#    def __init__(self, format_string, var_name):
#        self.format_string = str(format_string)
#        self.var_name = var_name
#
#    def render(self, context):
#        now = datetime.datetime.now()
#        context[self.var_name] = now.strftime(self.format_string)
#        return ''
#    
#@register.tag
#def do_current_time(parser, token):
#    # This version uses a regular expression to parse tag contents.
#    try:
#        # Splitting by None == splitting by spaces.
#        tag_name, arg = token.contents.split(None, 1)
#    except ValueError:
#        msg = '%r tag requires arguments' % token.contents[0]
#        raise template.TemplateSyntaxError(msg)
#
#    m = re.search(r'(.*?) as (\w+)', arg)
#    if m:
#        fmt, var_name = m.groups()
#    else:
#        msg = '%r tag had invalid arguments' % tag_name
#        raise template.TemplateSyntaxError(msg)
#
#    if not (fmt[0] == fmt[-1] and fmt[0] in ('"', "'")):
#        msg = "%r tag's argument should be in quotes" % tag_name
#        raise template.TemplateSyntaxError(msg)
#
#    return CurrentTimeNode3(fmt[1:-1], var_name)
#
#
##@register.tag(name='upper')
#def do_upper(parser, token):
#    nodelist = parser.parse(('endupper',))
#    parser.delete_first_token()
#    node=UpperNode(nodelist)
#    return node
#
#class UpperNode(template.Node):
#    def __init__(self, nodelist):
#        self.nodelist = nodelist
#
#    def render(self, context):
#        output = self.nodelist.render(context)
#        result=output.upper()
#        return result
#
#register.tag('upper', do_upper)
#
#@register.simple_tag
#def now_time(token):
#    try:
#        return datetime.datetime.now().strftime(str(token))
#    except UnicodeEncodeError:
#        return ''
    