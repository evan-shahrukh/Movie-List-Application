from django.urls import path,include
# from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api import views
from rest_framework.routers import DefaultRouter

app_name = "watchlist"

router = DefaultRouter()
router.register('stream',views.StreamingPlatformVS,basename="streamingplatform")

urlpatterns = [
    path("",views.WatchListAV.as_view(),name="Watch-list"),
    path("<int:pk>/",views.WatchDetailAV.as_view(),name="watch-detail"),
    
    # path("platform/",views.StreamingPlatformAV.as_view(),name="streaming-platform"),
    # path("platform/<int:pk>/",views.StreamingPlatformDetailAV.as_view(),name="streamingplatform-detail"),
    
    path('',include(router.urls)),
    
    path("<int:pk>/review/",views.ReviewList.as_view(),name="review-list"),
    path("<int:pk>/review/create/",views.ReviewCreate.as_view(),name="review-create"),
    path("review/<int:pk>",views.ReviewDetail.as_view(),name="review-detail"),
    path("review/<int:pk>/update/",views.ReviewUpdate.as_view(),name="review-update"),
    path("review/<int:pk>/delete/",views.ReviewDestroy.as_view(),name="review-delete"),
]