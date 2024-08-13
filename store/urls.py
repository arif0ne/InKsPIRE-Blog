
from django.urls import path
from .import views

#video number 7
from django.contrib.auth import views as auth_view   # এই মডিউলটি ক্লাস-ভিত্তিক ভিউ (ডিজাঙ্গো ১.১১ এ প্রবর্তিত) লগইন, লগআউট, পাসওয়ার্ড রিসেট এবং পাসওয়ার্ড পরিবর্তন করার মতো সাধারণ প্রামাণীকরণ টাস্কগুলি


urlpatterns = [
	path('',views.home,name='home'),
	path('about/',views.about,name='about'),
	path('blog/',views.blog,name='blog'),
	path('contact/',views.contact,name='contact'),
	path('service/',views.service,name='service'),
	path('add_post/',views.add_post,name='add_post'),
	path('category/<str:foo>/',views.category,name="category"),
	path('product/<int:pk>/', views.product,name='product'),
    

	path('post_edit/<int:pe>/', views.post_edit,name='post_edit'),
	path('post_delete/<int:pd>/', views.post_delete,name='post_delete'),
    
    
	path('search/',views.search,name='search'),
    
	path('profile/',views.profile,name='profile'),
    
    
	#for an users
	path('signup/',views.sign_up,name='sign_up'),
    
	path('signin/',auth_view.LoginView.as_view(template_name="users/signin.html"),name="sign_in"),
    
	#forget password on part 12
	path('password_reset/', auth_view.PasswordResetView.as_view(template_name="users/password_reset.html"),name="password_reset"),
	path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),name="password_reset_done"),
	path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),name="password_reset_confirm"),
	path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),name="password_reset_complete"),
    
    
	path('logout/',views.logout_user,name="logout"),
    
	path('editinfo/',views.update_info,name="editinfo"),
    
    


]