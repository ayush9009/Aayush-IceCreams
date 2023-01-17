"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Aayush Ice Cream Admin"
admin.site.site_title = "Aayush Ice Cream Admin Portal"
admin.site.index_title = "Welcome to Aayush Ice Creams"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    # ye simply kahra agr ye path math hora to home.urls pai bej do ise
]


# to hua kyajab apna 10.8000 aise link khola to ye hello devta kai paas gya,hello hai project aur isme urls.py hai jisme sare 
# urls mention hai jo ki batata hai ki kaha beja jaye,jaise yaha agr blank path hai to humne home.urls pai chla ja jise humne 
# include kar raka,jo ki home kai urls.py  mai hai 
