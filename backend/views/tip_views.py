from django.views.generic import ListView, CreateView

from backend.forms.tip_form import TipForm
from backend.models import Tip


class TipListView(ListView):

	model = Tip

	template_name = 'backend/tip/tip_index.html'

	context_object_name = 'tips_list'

	paginate_by = 10

class TipCreateView(CreateView):

	model = Tip

	form_class = TipForm

	template_name = 'backend/tip/tip_form.html'

