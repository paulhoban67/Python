from Domain.Entity import *


class Client(Entity):

    def __init__(self, id, nume, prenume, CNP, serie_buletin, numar_buletin, taxa):
        """
        Init a Client class
        :param id: int, id
        :param nume: str, name of client
        :param prenume: str, first name of client
        :param CNP: str, CNP of client
        :param serie_buletin: str, series of identity document
        :param numar_buletin: str, number of identity document
        :param taxa: float, rate of client
        """
        super().__init__(id)
        self.__nume = nume
        self.__prenume = prenume
        self.__CNP = CNP
        self.__serie_buletin = serie_buletin
        self.__numar_buletin = numar_buletin
        self.__taxa = taxa

    def get_nume(self):
        """
        Get name of client
        :return: str, name of client
        """
        return self.__nume

    def get_prenume(self):
        """
        Get name of client
        :return: str, first name of client
        """
        return self.__prenume

    def get_CNP(self):
        """
        Get CNP of client
        :return: str, first name of client
        """
        return self.__CNP

    def get_serie_buletin(self):
        """
        Get series of client
        :return: str, series of client
        """
        return self.__serie_buletin

    def get_numar_buletin(self):
        """
        Get number of client
        :return: str, number of client
        """
        return self.__numar_buletin

    def get_taxa(self):
        """
        Get rate of client
        :return: float, rate of client
        """
        return self.__taxa

    def set_nume(self, new_nume):
        """
        Set a new name of client
        :param new_name: str, new name of client
        :return: -
        """
        self.__nume = new_nume

    def set_prenume(self, new_prenume):
        """
        Set a new first name of client
        :param new_name: str, new first name of client
        :return: -
        """
        self.__prenume = new_prenume

    def set_CNP(self, new_CNP):
        """
        Set a CNP of client
        :param new_name: str, CNP of client
        :return: -
        """
        self.__CNP = new_CNP

    def set_serie_buletin(self, new_serie_buletin):
        """
        Set a series of client
        :param new_name: str, series of client
        :return: -
        """
        self.__serie_buletin = new_serie_buletin

    def set_numar_buletin(self, new_numar_buletin):
        """
        Set a number of client
        :param new_name: str, number of client
        :return: -
        """
        self.__numar_buletin = new_numar_buletin

    def set_taxa(self, new_taxa):
        """
        Set a new rate of client
        :param new_name: str, new rate of client
        :return: -
        """
        self.__taxa = new_taxa

    def __str__(self):
        """
        Show a clients
        :return: str, clients
        """
        return '( {} )    {} {} - CNP: {} , SERIA: {} , NUMAR: {} -------TOTAL: {} LEI'.format(self.get_id(),
                                                                                           self.__nume,
                                                                                           self.__prenume,
                                                                                           self.__CNP,
                                                                                           self.__serie_buletin,
                                                                                           self.__numar_buletin,
                                                                                           self.__taxa)


def test_client_class():
    """
    Test client class
    :return: -
    """
    client1 = Client(1, 'Hoban', 'Paul-Adelin', 5000928245045, 'MM', 985745, 25)
    client2 = Client(2, 'Hoban', 'Adriana-Cecilia', 9760302789458, 'MM', 456732, 88)
    client3 = Client(3, 'Hoban', 'Pavel', 7700525895483, 'MM', 421658, 585)
    assert client1.get_id() == 1
    assert client2.get_id() == 2
    assert client3.get_id() == 3
    assert client1.get_nume() == client2.get_nume() == client3.get_nume() == 'Hoban'
    assert client1.get_CNP() == 5000928245045
    assert client2.get_CNP() == 9760302789458
    assert client3.get_CNP() == 7700525895483


test_client_class()
