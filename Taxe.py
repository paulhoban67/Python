from Domain.Entity import *


class Taxe(Entity):

    def __init__(self, CNP, curent, gaz, internet, apa, telefon, intretinere, gunoi, chirie):
        """
        Init a taxe class
        :param CNP: str, CNP of client
        :param curent: int, one of rates of client
        :param gaz: int, one of rates of client
        :param internet: int, one of rates of client
        :param apa: int, one of rates of client
        :param telefon: int, one of rates of client
        :param intretinere: int, one of rates of client
        :param gunoi: int, one of rates of client
        :param chirie: int, one of rates of client
        """
        super().__init__(CNP)
        self.__curent = curent
        self.__gaz = gaz
        self.__internet = internet
        self.__apa = apa
        self.__telefon = telefon
        self.__intretinere = intretinere
        self.__gunoi = gunoi
        self.__chirie = chirie

    def get_curent(self):
        """
        Get one of rates of client
        :return: one of rates of client
        """
        return self.__curent

    def get_gaz(self):
        """
        Get one of rates of client
        :return: one of rates of client
        """
        return self.__gaz

    def get_internet(self):
        """
        Get one of rates of client
        :return: one of rates of client
        """
        return self.__internet

    def get_apa(self):
        """
        Get one of rates of client
        :return: one of rates of client
        """
        return self.__apa

    def get_telefon(self):
        """
        Get one of rates of client
        :return: one of rates of client
        """
        return self.__telefon

    def get_intretinere(self):
        """
        Get one of rates of client
        :return: one of rates of client
        """
        return self.__intretinere

    def get_gunoi(self):
        """
        Get one of rates of client
        :return: one of rates of client
        """
        return self.__gunoi

    def get_chirie(self):
        """
        Get one of rates of client
        :return: one of rates of client
        """
        return self.__chirie

    def set_curent(self, new_curent):
        """
        Set a new rate of client
        :param new_curent: float, new rate of client
        :return: -
        """
        self.__curent = new_curent

    def set_gaz(self, new_gaz):
        """
        Set a new rate of client
        :param new_curent: float, new rate of client
        :return: -
        """
        self.__gaz = new_gaz

    def set_internet(self, new_internet):
        """
        Set a new rate of client
        :param new_curent: float, new rate of client
        :return: -
        """
        self.__internet = new_internet

    def set_apa(self, new_apa):
        """
        Set a new rate of client
        :param new_curent: float, new rate of client
        :return: -
        """
        self.__apa = new_apa

    def set_telefon(self, new_telefon):
        """
        Set a new rate of client
        :param new_curent: float, new rate of client
        :return: -
        """
        self.__telefon = new_telefon

    def set_intretinere(self, new_intretinere):
        """
        Set a new rate of client
        :param new_curent: float, new rate of client
        :return: -
        """
        self.__intretinere = new_intretinere

    def set_gunoi(self, new_gunoi):
        """
        Set a new rate of client
        :param new_curent: float, new rate of client
        :return: -
        """
        self._gunoi = new_gunoi

    def set_chirie(self, new_chirie):
        """
        Set a new rate of client
        :param new_curent: float, new rate of client
        :return: -
        """
        self.chirie = new_chirie

    def __str__(self):
        """
        Show rates of clients
        :return:  str, rates of clients
        """
        return 'CNP-UL {}:\n                                                                      CURENT: {} LEI\n' \
               '                                                                      GAZ: {} LEI\n' \
               '                                                                      INTERNET: {} LEI\n' \
               '                                                                      APA: {} LEI\n' \
               '                                                                      TELEFON: {} LEI\n'\
               '                                                                      INTRETINERE: {} LEI\n' \
               '                                                                      GUNOI: {} LEI\n' \
               '                                                                      CHIRIE: {} LEI'\
            .format(self.get_id(),self.get_curent(), self.get_gaz(), self.get_internet(), self.get_apa(),
                    self.get_telefon(), self.get_intretinere(), self.get_gunoi(), self.get_chirie())


def test_taxe_class():
    """
    Test taxe class
    :return: -
    """
    taxe1 = Taxe(5000685957854, 55, 55, 65, 22, 111, 58, 55, 1600)
    taxe2 = Taxe(4585478569254, 55, 525, 625, 2, 12211, 528, 525, 162200)
    taxe3 = Taxe(1000256987455, 55, 5, 5, 2, 11, 8, 5, 16002)
    assert taxe1.get_id() == 5000685957854
    assert taxe2.get_id() == 4585478569254
    assert taxe3.get_id() == 1000256987455
    assert taxe1.get_curent() == taxe2.get_curent() == taxe3.get_curent() == 55

test_taxe_class()
