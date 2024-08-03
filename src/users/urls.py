from django.urls import path


from .views import LibrarianCreateView, ReaderCreateView, UserLoginView, UserLogoutView

app_name = "users"
urlpatterns = [
    path('signup/librarian', LibrarianCreateView.as_view(), name='librarian_signup'),
    path('signup/reader', ReaderCreateView.as_view(), name='reader_signup'),
    path('signin', UserLoginView.as_view(), name='signin'),
    path('logout', UserLogoutView.as_view(), name='logout')
]