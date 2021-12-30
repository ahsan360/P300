from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('',views.hello,name='hello' ),
    path('hello/',views.hello,name='hello' ),
    path('index/',views.index,name='index' ),
    path('signin/',views.signin,name='signin' ),
    #path('log/',views.log,name='log' ),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('posts/', views.posts,name='posts'),
    path('posts2/', views.posts2,name='posts2'),
    path('posts3/', views.posts3,name='posts3'),

    path('cpost/', views.cpost,name='cpost'),
    path('cpost2/', views.cpost2,name='cpost'),
    path('cpost3/', views.cpost3,name='cpost'),
    path('search/', views.search,name='search'),
    path('details/<int:id>', views.details,name='details'),
    path('detailss/<int:id>', views.detailss,name='detailss'),
    path('details3/<int:id>', views.details3,name='details3'),
    path('Update/<int:pk>', views.Update,name='Update'),
    path('Update2/<int:pk>', views.Update2,name='Update2'),
    path('Update3/<int:pk>', views.Update3,name='Update3'),
    path('delete/<int:pk>', views.delete,name='delete'),
    path('delete2/<int:pk>', views.delete2,name='delete2'),
    path('delete3/<int:pk>', views.delete3,name='delete3'),
    path('delete_comment/<int:pk>', views.delete_comment,name='delete_comment'),
    path('delete_comment2/<int:pk>', views.delete_comment2,name='delete_comment2'),
    path('delete_comment3/<int:pk>', views.delete_comment3,name='delete_comment3'),
    path('comment/<int:pk>', views.addcomment,name='addcomment'),
    path('comment2/<int:pk>', views.addcomment2,name='addcomment2'),
    path('comment3/<int:pk>', views.addcomment3,name='addcomment3'),
    path('log/',auth_views.LoginView.as_view(template_name='projectApp/log.html'),name='login'),
    path('logo/',auth_views.LogoutView.as_view(template_name='projectApp/home.html'),name='logout')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 