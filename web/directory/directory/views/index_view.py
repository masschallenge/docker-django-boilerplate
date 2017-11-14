from django.views.generic import TemplateView


class IndexView(TemplateView):
    view_name = "home_page_view"
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        return {}
