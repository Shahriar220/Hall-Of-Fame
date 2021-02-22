from django.contrib import admin,auth
from django.urls import path
from halls import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('dashboard',views.dashboard,name='dashboard'),
    #auth
    path('signup',views.SignUp.as_view(),name='signup'),
    path('login',auth.views.LoginView.as_view(),name='login'),
    path('logout',auth.views.LogoutView.as_view(),name='logout'),

    #hall
    path('halloffame/create',views.CreateHall.as_view(),name='create_hall'),
    path('halloffame/<int:pk>',views.DetailHall.as_view(),name='detail_hall'),
    path('halloffame/<int:pk>/update',views.UpdateHall.as_view(),name='update_hall'),
    path('halloffame/<int:pk>/delete',views.DeleteHall.as_view(),name='delete_hall'),

    #video
    path('halloffame/<int:pk>/addvideo',views.add_video,name='add_video'),
    path('video/search',views.video_search,name='video_search'),
    path('video/<int:pk>/delete',views.DeleteVideo.as_view(),name='delete_video'),
]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
