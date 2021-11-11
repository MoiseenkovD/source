from django.contrib import admin
from django.urls import path
from Sourcemodel import views
from Sourcemodel.api import source_create, source_update, source_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('source/<int:id>', views.get_by_id),
    path('source/create', views.create),
    path('source/update', views.update),
    path('source/delete', views.delete),
    path('api/source/create', source_create.SourceCreate.as_view()),
    path('api/source/update', source_update.SourceUpdate.as_view()),
    path('api/source/delete', source_delete.SourceDelete.as_view()),
]
