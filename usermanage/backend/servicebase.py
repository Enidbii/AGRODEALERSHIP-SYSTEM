
class ServiceInterface:
    def create_user(self, model, **k):
        try:
            return model.objects.create(**k)
        except Exception as e:
            print(e)
            return None

    def get(self, model, **k):
        try:
            return model.objects.get(**k)
        except Exception as e:
            print(e)
            return None

    def retrieve_all_records(self, model):
        try:
            return model.objects.all()
        except Exception as e:
            print(e)
            return None

    def update(self, model, instance_id, **k):
        try:
            return  model.objects.filter(pk=instance_id).update(**k)
        except Exception as e:
            print(e)
            return None

    def filter(self, model, **k):
        try:
            return model.objects.filter(**k)
        except Exception as e:
            print(e)
            return None

    def delete(self, model, user_id):
        try:
            return model.objects.delete(user_id)
        except Exception as e:
            print(e)

    def logout(self, model):
        try:
            return model.objects.none()
        except Exception as e:
            print(e)
            return None