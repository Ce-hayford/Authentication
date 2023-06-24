from django.urls import path
from . import views

urlpatterns = [
    
    path('login/', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('passwordChange/', views.passwordChange, name='password_change'),
    path('passwordChange/done/', views.passwordChangeDone, name='password_change_done'),
    path('resetPage/<uidb64>/<token>/', views.resetPage, name='reset_page'),
    path('resetPage/done/', views.resetPageDone, name='reset_page_done'),
]
