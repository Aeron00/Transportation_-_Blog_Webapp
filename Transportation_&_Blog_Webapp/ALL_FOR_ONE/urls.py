from django.urls import path
from ALL_FOR_ONE import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="TransportApp"),
    path('Trains', views.Trains, name="Trains"),
    path('About', views.About, name="About"),
    path('blog', views.blog, name="blog"),
    path('AddBlog', views.AddBlog, name="AddBlog"),  
    path('comments', views.comments, name="comments"),
    path('Contact', views.Contactus, name="Contact"),
    path('Signup', views.Signup, name="Signup"),
    path('Login', views.Login, name="Login"),
    path('Forgotpass', views.Forgotpass, name="Forgot_Pass"),
    path('Logout', views.Logout, name="Logout"),
    path('Data', views.Data, name="Data"),
    path('User', views.User, name="User"),
    path('Edit', views.Edit, name="Edit"),
    path('payment', views.payment, name="payment"),
    path('payment_status', views.payment_status, name="payment_status"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)