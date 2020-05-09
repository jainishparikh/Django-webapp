from django.contrib.auth.models import User


class UpdatedBackend(object):
    def authenticate(self, request, username=None, password=None):
        try:
            print("in updated backend", username, request)
            user = User.objects.get(email=username)
            if user.check_password(password):
                # if password == user.password:
                return user
        except:
            print("No user found")
            return None

    def get_user(self, user_id):
        try:
            print("in updated backend")
            return User.objects.get(pk=user_id)
        except:
            return None
