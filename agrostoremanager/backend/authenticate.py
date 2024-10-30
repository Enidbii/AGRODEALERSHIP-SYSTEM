from usermanage.backend.authentication import AuthenticateUser

class AgroStore(object):
    def register(self,request):
        return AuthenticateUser().register(request)

    def login(self, request):
        return AuthenticateUser().login(request)

    def update(self, request):
        return AuthenticateUser().update(request)

    def create_agrostore(self, request):
        return AuthenticateUser().create_corporate(request)

    def update_agrostore(self, request):
        return AuthenticateUser().update_corporate(request)
