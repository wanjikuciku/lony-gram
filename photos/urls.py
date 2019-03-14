from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r"^$", views.index, name = 'index'),
    url(r"^ajax/like/$",views.like, name = 'like'),
    url(r"^ajax/comment/$",views.comment, name = "comment"),
    url(r"^add/image$", views.add_image, name = "add_image"),
    url(r"^profile/(\d+)/$", views.profile, name = "profile" ),
    url(r"^profile/update/$", views.update_profile, name = "update_profile"),
    url(r"search/$", views.search_user, name = "search"),
    url(r"^accounts/profile/$", views.my_profile, name = "my_profile")

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)