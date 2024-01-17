from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from shoppingapp.models import stu,student
from shoppingapp.models import Task,Course 

# # Register your models here.
# admin.site.register(Task)
# # admin.site.register(Course)

# class courses(admin.ModelAdmin):
#     # list_display=['id','cname','cdur','ccat','cprice']
#     # list_display=('id','cname','cdur','ccat','cprice')
#     list_display=('id',)

# admin.site.register(Course,courses)

# class stus(admin.ModelAdmin):
#     list_display=['name','address','marks']


# admin.site.register(stu,stus)

# class stud(admin.ModelAdmin):
#     list_display=['names','age','address']

# admin.site.register(student,stud)
# class cour(admin.ModelAdmin):
#     list_display=['id','cname','cdur','ccat','cprice']
#     list_filter=['cprice','cdur','ccat ']


# admin.site.register(Course,cour)



# @admin.register(student)

# class courses(admin.ModelAdmin):
#     list_display=['names','age','address']


# @admin.register(stu)

# class res(admin.ModelAdmin):
#     list_display=['name','address','marks']

# @admin.register(Task)

# class tk(admin.ModelAdmin):
#     list_display=['title','datails','date','is_deleted']

#admin.site.register(Task)

# class ts(admin.ModelAdmin):
#     list_display=['title','datails','date']

# admin.site.register(Task,ts)

# class co(admin.ModelAdmin):
#     list_display=list_display=['id','cname','cdur','ccat','cprice']

# admin.site.register(Course,co)

# class st(admin.ModelAdmin):
#     list_display=['name','address','marks']

# admin.site.register(stu,st)

# class sts(admin.ModelAdmin):
#     list_display=['names','age','address']

# admin.site.register(student,sts)



@admin.register(Task)

class ts(admin.ModelAdmin):
    list_display=['title','datails','date']
    list_filter=['title']


class feesfil(admin.SimpleListFilter):
    title='fees'
    parameter_name="course Fees"
    def lookups(self,request,models_admin):
        return(('high','fees>=20000'),('low','fees<20000'))
    def queryset(self,request,queryset):
        if self.value()=='high':
            return queryset.filter(cprice__gte=20000)
        elif self.value()=='low':
            return queryset.filter(cprice__lte=20000)
        else:
            return queryset.all()
            # comment: 

@admin.register(Course)

class co(admin.ModelAdmin):
    list_display=['id','cname','cdur','ccat','cprice']
    list_filter=[feesfil]

@admin.register(stu)

class st(admin.ModelAdmin):
    list_display=['name','address','marks']
    list_filter=['marks','address','name']

@admin.register(student)

class stud(admin.ModelAdmin):
    list_display=['names','age','address']