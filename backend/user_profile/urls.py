from django.urls import path, include
from .views import Register, ViewAllProfiles
from user_profile import views

urlpatterns = [
    path('profile_register/', views.Register.as_view()),
    path('all_profiles/', views.ViewAllProfiles.as_view()),

]