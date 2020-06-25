from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('teachers/', include("teachers.urls")),
                  path("materials/", include("materialsearch.urls")),
                  path('', include('homepage.urls')),
                  path('profile/', include('profile_page.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
