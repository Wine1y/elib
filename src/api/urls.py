from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


app_name = "api"
urlpatterns = [
    path('auth/', include("api.api_urls.auth"), name="auth"),
    path('books/', include("api.api_urls.books"), name="books_api"),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path('schema/swagger-ui', SpectacularSwaggerView.as_view(url_name="api:schema"), name="schema_swagger")
]