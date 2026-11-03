from django.contrib import admin
from django.urls import path

admin.site.site_header = "Управление магазином"
admin.site.site_title = 'Админ панель'
admin.site.index_title = 'Админка'

urlpatterns = [
    path('admin/', admin.site.urls),
]
