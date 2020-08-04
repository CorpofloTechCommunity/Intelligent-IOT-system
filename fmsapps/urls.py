from django.urls import include, path

app_name = 'fms'

urlpatterns = [
    path('graphql/', include('fmsapps.graphql.urls', namespace='graphql')),
]