from . import views
from django.urls import path

urlpatterns = [
    path('',views.codelabs,name="codelabs"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login_view,name="login"),
    path('home/',views.home,name="home"),
    path('logout/',views.logout_view,name="logout"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('courses/',views.courses,name="courses"),
    path('contactus/',views.contactus,name="contactus"),
    
]
