from django.urls import path

from app1.views import Home,deleteview, updateview, SignupPage, LoginPage, LogoutPage

urlpatterns = [
    path('', Home, name = 'home'),
    path('delete/<int:id>', deleteview, name = 'delete'),
    path('<int:id>', updateview, name = 'update'),
    path('signup/', SignupPage, name = 'signup'),
    path('login/', LoginPage, name = 'login'),
    path('logout/', LogoutPage, name = 'logout')
]