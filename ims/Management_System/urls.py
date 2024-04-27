
from django.urls import path
from.views import*
urlpatterns = [
    path('resource_type/',ResourceTypeView.as_view({'get':'list','post':'create'})),
    path('resource_type/<int:pk>/',ResourceTypeView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

    path('resources/',ResourcesView.as_views()),
    path('department/',DepartmentView.as_views()),
    path('vendor/',VendorView.as_views()),
    path('purchase/',PurchaseView.as_views()),


]

