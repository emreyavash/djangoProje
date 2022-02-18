from django.contrib import admin

from .models import Category,Teacher,Courses

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fileds=("slug",)
    list_display=("categoryName",)

class TeacherAdmin(admin.ModelAdmin):
    list_display=("teacherName",)

class CoursesAdmin(admin.ModelAdmin):
    list_display=("courseName","teacher","slug","category_course")
    readonly_fileds=("slug",)
    # def course_teacher(self, obj):
    #     html = ""

    #     for t in obj.teacher.all(): 
    #         html += t.teacherName
    #     return html
    def category_course(self,obj):
        html=""

        for c in obj.category.all():
            html += c.categoryName
        return html
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Courses,CoursesAdmin)