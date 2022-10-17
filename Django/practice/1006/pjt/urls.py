"""pjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('movie.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 이미지 업로드는 
# 1. 저장하고 있었던 것은 텍스트/숫자, 이번에는 이미지를 저장
# 이미지 받기 위해 html form에서 설정(enctype), view(reuqest.filese), setting
# 2. 보여주기는 스태틱과 닮아있음, 셋팅에서 루트와 url설정 필요 
# 배포에서는 스태틱 모으는 작업할 것임, 이미지는 미디어 루트/url에서 설정해야함(이미지를 서버에서 보여주는 방법이기 떄문)
# 3. 서빙을 하는애를 만들고 있고, 그것이 서버임
