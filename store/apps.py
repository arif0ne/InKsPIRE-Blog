from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'
    verbose_name = "All Dynamic Assets"
    

    #day 8 | for Profile
    def ready(self):
        import store.signals
