from django.urls import path, include

from accounts.api.views import ProfileAPIView, ProfileGenericAPIView

profile_urls = [
    path('profile/', ProfileAPIView.as_view(), name='get_profile',),    
    # path('login/', ProfileGenericAPIView.as_view(), name='token_obtain_pair'),    
]