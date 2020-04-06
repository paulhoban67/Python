from Domain.Taxe import Taxe


class Service_Taxe:

    def __init__(self, repository):
        """
        Init class Service taxe
        :param repository: class, repository
        """
        self.__repository = repository
        self.__undo_operations = []
        self.__redo_operations = []
        self.__redo_count = 0
        self.__reserve_action = []

    def add_taxe(self, CNP, curent, gaz, internet, apa, telefon, intretinere, gunoi, chirie):
        """
        Add rates
        :param CNP: str, CNP of client
        :param curent: float, one of rates of client
        :param gaz: float, one of rates of client
        :param internet: float, one of rates of client
        :param apa: float, one of rates of client
        :param telefon: float, one of rates of client
        :param intretinere: float, one of rates of client
        :param gunoi: float, one of rates of client
        :param chirie: float, one of rates of client
        :return:
        """
        taxe = Taxe(CNP, curent, gaz, internet, apa, telefon, intretinere, gunoi, chirie)
        self.__repository.add(taxe)
        self.__undo_operations.append(lambda: self.__repository.delete(CNP))
        self.__redo_operations.append(lambda: self.__repository.add(taxe))

    def update_taxe(self, CNP, curent, gaz, internet, apa, telefon, intretinere, gunoi, chirie):
        """
          Update rates
          :param CNP: str, CNP of client
          :param curent: float, one of rates of client
          :param gaz: float, one of rates of client
          :param internet: float, one of rates of client
          :param apa: float, one of rates of client
          :param telefon: float, one of rates of client
          :param intretinere: float, one of rates of client
          :param gunoi: float, one of rates of client
          :param chirie: float, one of rates of client
          :return: -
          """
        taxe = Taxe(CNP, curent, gaz, internet, apa, telefon, intretinere, gunoi, chirie)
        self.__repository.update(taxe)

    def remove_taxe(self, CNP):
        """
        Remove a rate by CNP
        :param CNP: str, CNP of client
        :return: -
        """
        lista = self.__repository.read()
        for taxa in lista:
            if taxa.get_id() == CNP:
                self.__repository.delete(CNP)
                return
        self.__repository.delete(CNP)

    def get_all(self):
        """
        Get all rates
        :return: class, all rates
        """
        return self.__repository.read()

    def get_taxa(self, CNP):
        """
        Get one rate by CNP
        :param CNP: str, CNP of client
        :return: class, a rate of CNP
        """
        return self.__repository.read(CNP)

