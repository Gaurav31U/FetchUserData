from django.contrib import admin
from django.urls import path
from stock import views


urlpatterns = [
    path('', views.index_view, name="index"),
    path('ContactUs/', views.ContactUs_view, name="ContactUs"),
    path('Art/<int:Art_id>', views.Art_view, name="Art"),
    
    path('login/customer', views.login_customer_request, name="login_customer"),
    path('login/signup/customer', views.sign_up_customer_request, name="sign_up_customer"),
    path('customer/cprofile', views.createCustomer, name="cprofile"),
    path('customer/profile', views.customerProfile, name="profile"),
    path('user/update/<int:id>/',views.updateCustomer,name='cupdate'),
    path('AddtoCart/<int:Art_id>/', views.add_to_cart, name="Add_to_Cart"),
    path('MyCart', views.MyCart_view, name="Cart"),
    path('payment', views.payment_view, name="payment"),
 
    path('login/artist', views.login_artist_request, name="login_artist"),
    path('signup/artist', views.sign_up_artist_request, name="sign_up_artist"),
    path('artist/create/',views.createartist,name='acreate'),
    path('artist/update/<int:id>/',views.updateartist,name='aupdate'),
    path('profile/artist/',views.artistProfile,name='aprofile'),
    path('artist/addart', views.Add_Art_view, name="addart"),
    
    path('logout/', views.logouts, name="logouts"),
    
]