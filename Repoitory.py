import pickle
from Repository.Repository_Exception import Repository_Exception


class Repository_Generic:
    def __init__(self, filename):
        """
        Init class Repository_generic
        :param filename: str, file name
        """
        self.__storage = {}
        self.__filename = filename
        self.__load_file()

    def __load_file(self):
        """
        Load objects from file
        :return: -
        """
        try:
            with open(self.__filename, 'rb') as f:
                self.__storage = pickle.load(f)
        except:
            print('Fisier invalid')

    def __write_file(self):
        """
        Write objects in file
        :return: -
        """
        try:
            with open(self.__filename, 'wb') as f:
                pickle.dump(self.__storage, f)
        except:
            print('Fisier invalid')

    def add(self, entity):
        """
        Add entity
        :param entity: class, entity
        :return:
        """
        self.__load_file()
        id = entity.get_id()
        if id in self.__storage:
            raise Repository_Exception('ID DUPLICAT')
        self.__storage[id] = entity
        self.__write_file()

    def delete(self, id):
        """
        Delete a entity by id
        :param id: int, id entity
        :return:
        """
        self.__load_file()
        if id in self.__storage:
            del (self.__storage[id])
            self.__write_file()
        else:
            raise Repository_Exception('NU EXISTA')
        self.__write_file()

    def update(self, entity):
        """
        Update a entity by entity
        :param entity: class, entity
        :return:
        """
        self.__load_file()
        id = entity.get_id()
        if id in self.__storage:
            self.__storage[id] = entity
            self.__write_file()
        else:
            raise Repository_Exception('NU EXISTA')
        self.__write_file()

    def read(self, id=None):
        """
        Read all entity or a entity by id
        :param id: int, id entity
        :return: class, entity
        """
        self.__load_file()
        if id is None:
            return self.__storage.values()
        if id in self.__storage:
            return self.__storage[id]
        else:
            raise Repository_Exception('NU EXISTA')
