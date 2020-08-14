from django.urls import include, path

app_name = 'iiots'

urlpatterns = [
    path('graphql/', include('iiotsapps.graphql.urls', namespace='graphql')),
]