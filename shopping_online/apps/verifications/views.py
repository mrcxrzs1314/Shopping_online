from django.views import View
from utils.json_fun import to_json_data
from users.models import Users


class CheckUsernameView(View):
    """
    Check whether the user exists
    GET username/(?P<username>\w{5,20})/
    """
    def get(self, request, username):

        data = {
            'username': username,
            'count': Users.objects.filter(username=username).count()
        }
        return to_json_data(data=data)






