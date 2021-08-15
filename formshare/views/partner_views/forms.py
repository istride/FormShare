from formshare.views.classes import PartnerView
from formshare.processes.db import get_project_details


class PartnerForms(PartnerView):
    def process_view(self):
        return {
            "projectDetails": get_project_details(self.request, self.projectID),
        }
