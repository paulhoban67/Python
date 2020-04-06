from Domain.Client import Client


class Service_Client:

    def __init__(self, repository):
        """
        Init a class Service client
        :param repository: class, repository
        """
        self.__repository = repository
        self.__undo_operations = []
        self.__redo_operations = []
        self.__redo_count = 0
        self.__reserve_action = []

    def add_client(self, id, nume, prenume, CNP, serie_buletin, numar_buletin, taxa):
        """
        Add a client
        :param id: int id of client
        :param nume: str, name of client
        :param prenume: str, fist name of client
        :param CNP: str, CNP of client
        :param serie_buletin: str, series of client
        :param numar_buletin: str, number of client
        :param taxa: float, rates of client
        :return: -
        """
        client = Client(id, nume, prenume, CNP, serie_buletin, numar_buletin, taxa)
        self.__repository.add(client)
        self.__undo_operations.append(lambda: self.__repository.delete(id))
        self.__redo_operations.append(lambda: self.__repository.add(client))

    def update_client(self, id, nume, prenume, CNP, serie_buletin, numar_buletin, taxa):
        """
        Update a client
        :param id: int id of client
        :param nume: str, name of client
        :param prenume: str, fist name of client
        :param CNP: str, CNP of client
        :param serie_buletin: str, series of client
        :param numar_buletin: str, number of client
        :param taxa: float, rates of client
        :return: -
        """
        for client in self.get_all():
            if id == client.get_id():
                client_undo = Client(client.get_id(), client.get_nume(), client.get_prenume(), client.get_CNP(),
                                 client.get_serie_buletin(), client.get_numar_buletin(), client.get_taxa())
                break
        client = Client(id, nume, prenume, CNP, serie_buletin, numar_buletin, taxa)
        self.__repository.update(client)
        self.__undo_operations.append(lambda: self.__repository.update(client_undo))
        self.__redo_operations.append(lambda: self.__repository.update(client))

    def remove_client(self, id):
        """
        Remove a client by id
        :param id: int, id of client to remove
        :return: -
        """
        lista = self.__repository.read()
        for client in lista:
            if client.get_id() == id:
                self.__repository.delete(id)
                self.__undo_operations.append(lambda: self.__repository.add(client))
                self.__redo_operations.append(lambda: self.__repository.delete(id))
                return
        self.__repository.delete(id)

    def get_all(self):
        """
        Get all clients
        :return: class, all clients
        """
        return self.__repository.read()

    def get_client(self, id):
        """
        Get a client by id
        :param id: int, id of client
        :return: class, client with the id = id
        """
        return self.__repository.read(id)

