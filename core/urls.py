from django.urls import path 
from .views import signup , user_activate , profile , wishlist, login_page


app_name='core'




urlpatterns = [
    path('',login_page,name='login'),
    path('signup/' , signup , name='signup'),
    path('profile/' , profile , name='profile'),
    path('profile/wishlist' , wishlist , name='wishlist'),
    path('<str:username>/activate' , user_activate , name='user_activate'),

]
