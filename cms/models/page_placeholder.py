from django.core.urlresolvers import reverse
from django.db import models
from django.contrib import admin
from cms.models.placeholdermodel import Placeholder

class PagePlaceholder(models.Model):
    placeholder = models.ForeignKey(Placeholder)
    page = models.ForeignKey('Page')

    class Meta:
        permissions = ()
        app_label = 'cms'
        db_table  = 'cms_page_placeholders'

    def __unicode__(self):
        try:
            page = '%s %s' % (self.page.get_absolute_url() , self.placeholder )
        except Exception:
            page = 'PlaceHolder %s %s' % (self.page,self.placeholder)
        return page

#cms.admin.pageadmin:
#admin.site.register(PagePlaceholder)

