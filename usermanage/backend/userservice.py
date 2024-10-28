"""
Endpoin
"""
class ServiceInterface:
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
            return model.objects.get(pk=instance_id)
            # for key, value in k.items():
            #     setattr(instance, key, value)
            # instance.save()
        except Exception as e:
            print(e)
            return None


        # except model.DoesNotExist:
        #     print(f"{model.__name__} with id {instance_id} does not exist.")
        #     return None
        # except Exception as e:
        #     print(f"Error updating {model.__name__}: {e}")
        #     return None

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