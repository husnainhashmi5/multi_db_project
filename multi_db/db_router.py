class MyDatabaseRouter:
    """
    A database router to store LahoreHotel in 'default' and IslamabadHotel in 'secondary'.
    """

    def db_for_read(self, model, **hints):
        """Direct read operations to the correct database."""
        if model.__name__ == 'IslamabadHotel':  # IslamabadHotel → secondary DB
            return 'secondary'
        return 'default'  # LahoreHotel → default DB

    def db_for_write(self, model, **hints):
        """Direct write operations to the correct database."""
        if model.__name__ == 'IslamabadHotel':  # IslamabadHotel → secondary DB
            return 'secondary'
        return 'default'  # LahoreHotel → default DB

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations only within the same database."""
        if obj1._state.db == obj2._state.db:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure models are migrated to the correct database."""
        if model_name == 'islamabadhotel':  # IslamabadHotel → secondary DB
            return db == 'secondary'
        return db == 'default'  # LahoreHotel → default DB
