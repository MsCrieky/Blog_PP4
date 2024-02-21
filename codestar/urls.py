from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path("funfacts/", include("funfacts.urls"), name="funfacts-urls"),
    path("summernote/", include("django_summernote.urls")),
    path("", include("blog.urls"), name="blog-urls"),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
