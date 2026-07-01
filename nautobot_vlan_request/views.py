from nautobot.apps.views import ObjectListView, ObjectEditView
from .models import VLANRequest
from .tables import VLANRequestTable
from .forms import VLANRequestForm
from .filters import VLANRequestFilterSet


class VLANRequestListView(ObjectListView):
    queryset = VLANRequest.objects.all()
    table = VLANRequestTable
    filterset = VLANRequestFilterSet


class VLANRequestEditView(ObjectEditView):
    queryset = VLANRequest.objects.all()
    model_form = VLANRequestForm