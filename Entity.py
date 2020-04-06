class Entity():
    def __init__(self, id):
        """
        Init a entity
        :param id: int, id of entity
        """
        self.__id = id

    def get_id(self):
        """
        Get id of entity
        :return: int, id of entity
        """
        return self.__id
