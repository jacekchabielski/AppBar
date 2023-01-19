from django.urls import path, include
from .views import Register, ViewAllProfiles, ChangeAvatar, ViewSingleProfile
from user_profile import views

urlpatterns = [
    path('profile_register/', views.Register.as_view()),
    path('all_profiles/', views.ViewAllProfiles.as_view()),
    path('change_avatar/', views.ChangeAvatar.as_view()),
    path('single_profile/<int:id>/', views.ViewSingleProfile.as_view()),

]