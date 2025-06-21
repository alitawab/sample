"""mixin file """
class SerializerMixin:
    """class for mixin"""
    def to_dict(self):
        """function for to_dict"""
        return{
            column.name: getattr(self, column.name)
            for column in self.__table__.column
        }
