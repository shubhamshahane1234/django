from django.contrib import admin
from django.urls import path,include
from django.urls.conf import include
from home import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name="index")
]
