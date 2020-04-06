class UI:
    def __init__(self, service_client, service_taxe):
        """
        Init a class UI
        :param service_client: class, service client
        :param service_taxe: class, service rates
        """
        self.__service_client = service_client
        self.__service_taxe = service_taxe

    def __menu1(self):
        """
        Menu of client
        :return:
        """
        print('                               MENIU CLIENT      ')
        print('                         ************************')
        print('                         *                      *')
        print('                         * 1. ADAUGARE CLIENT   *')
        print('                         * 2. STERGERE CLIENT   *')
        print('                         * 3. MODIFICARE CLIENT *')
        print('                         * 4. AFISARE CLIENTI   *')
        print('                         * 5. EXIT              *')
        print('                         *                      *')
        print('                         ************************')

    def __add_client(self):
        """
        Add client
        :return: str, a message
        """
        try:
            print('')
            print('                         CLIENT NOU')
            id = int(input('                         ID: '))
            nume = str(input('                         NUME: '))
            prenume = str(input('                         PRENUME: '))
            CNP = int(input('                         CNP: '))
            serie_buletin = str(input('                         SERIE: '))
            numar_buletin = int(input('                         NUMAR: '))
            taxa = 0.0
            self.__service_client.add_client(id, nume, prenume, CNP, serie_buletin, numar_buletin, taxa)
            return '                                                    ***** CLIENTUL {} A FOST ADAUGAT !!! ***** '.format(
                id)
        except ValueError as ve:
            print('')
            print('                         ERORI:')
            for error in ve.args[0]:
                print(error)
            print('')

    def __add_taxe(self):
        """
        Add init rates
        :return: -
        """
        print('')
        print('                         TAXE')
        CNP = int(input('                         CNP: '))
        self.__service_taxe.add_taxe(CNP, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    def __delete_client(self):
        """
        Delete a client
        :return: str, a message
        """
        print('')
        print('                         STERGERE CLIENT')
        id = int(input('                         ID:'))
        clienti = self.__service_client.get_all()
        taxe = self.__service_taxe.get_all()
        CNP = -1
        for client in clienti:
            if client.get_id() == id:
                CNP = client.get_CNP()
        self.__service_client.remove_client(id)
        for taxa in taxe:
            if taxa.get_id() == CNP:
                self.__service_taxe.remove_taxe(CNP)
        return '                                                    ***** CLIENTUL {} A FOST STERS !!! ***** '.format(
            id)

    def __update_client(self):
        """
        Update a client
        :return: str, a message
        """
        print('')
        print('                         MODIFICARE CLIENT')
        id = int(input('                         ID: '))
        client = self.__service_client.get_client(id)
        new_nume = str(input('                         NUME: '))
        new_prenume = str(input('                         PRENUME: '))
        '''new_CNP = int(input('      CNP:'))'''
        new_serie_buletin = str(input('                         SERIE: '))
        new_numar_buletin = int(input('                         NUMAR: '))
        self.__service_client.update_client(id, new_nume, new_prenume, client.get_CNP(), new_serie_buletin,
                                            new_numar_buletin,
                                            client.get_taxa())
        return '                                                    ***** CLIENTUL {} A FOST MODIFICAT !!! ***** '.format(
            id)

    def __show_list(self, objects):
        """
        Show all objects
        :param objects: class, objects
        :return: -
        """
        print('')
        for obiect in objects:
            print('                                                  ', obiect)

    def menu_client(self):
        """
        Menu client
        :return: -
        """
        while True:
            self.__menu1()
            print('')
            option = int(input('                         OPTION: '))
            if option == 1:
                print(self.__add_client())
                print(self.__add_taxe())
            elif option == 2:
                print(self.__delete_client())
            elif option == 3:
                print(self.__update_client())
            elif option == 4:
                self.__show_list(self.__service_client.get_all())
            elif option == 5:
                break

    def __add_taxe_curent(self):
        """
        Add one of a rate
        :return: str, a message
        """
        try:
            print('')
            print('                         TAXA')
            CNP = int(input('                         CNP: '))
            taxa = float(input('                         TAXA: '))
            taxa_class = self.__service_taxe.get_taxa(CNP)
            self.__service_taxe.update_taxe(CNP, taxa_class.get_curent() + taxa, taxa_class.get_gaz(),
                                            taxa_class.get_internet(), taxa_class.get_apa(), taxa_class.get_telefon(),
                                            taxa_class.get_intretinere(), taxa_class.get_gunoi(),
                                            taxa_class.get_chirie())
            clienti = self.__service_client.get_all()
            for client in clienti:
                if client.get_CNP() == CNP:
                    self.__service_client.update_client(client.get_id(), client.get_nume(), client.get_prenume(),
                                                        client.get_CNP(), client.get_serie_buletin(),
                                                        client.get_numar_buletin(), client.get_taxa() + taxa)

            return '                                                    ***** CURENTUL IN VLOARE DE {} LEI A FOST PLATIT !!! ***** '.format(
                taxa)
        except ValueError as ve:
            print('')
            print('                         ERORI:')
            for error in ve.args[0]:
                print(error)
            print('')

    def __add_taxe_gaz(self):
        """
        Add one of a rate
        :return: str, a message
        """
        try:
            print('')
            print('                         TAXA')
            CNP = int(input('                         CNP: '))
            taxa = float(input('                         TAXA: '))
            taxa_class = self.__service_taxe.get_taxa(CNP)
            self.__service_taxe.update_taxe(CNP, taxa_class.get_curent(), taxa_class.get_gaz() + taxa,
                                            taxa_class.get_internet(), taxa_class.get_apa(), taxa_class.get_telefon(),
                                            taxa_class.get_intretinere(), taxa_class.get_gunoi(),
                                            taxa_class.get_chirie())
            clienti = self.__service_client.get_all()
            for client in clienti:
                if client.get_CNP() == CNP:
                    self.__service_client.update_client(client.get_id(), client.get_nume(), client.get_prenume(),
                                                        client.get_CNP(), client.get_serie_buletin(),
                                                        client.get_numar_buletin(), client.get_taxa() + taxa)
            return '                                                    ***** GAZUL IN VLOARE DE {} LEI A FOST PLATIT !!! ***** '.format(
                taxa)
        except ValueError as ve:
            print('')
            print('                         ERORI:')
            for error in ve.args[0]:
                print(error)
            print('')

    def __add_taxe_internet(self):
        """
        Add one of a rate
        :return: str, a message
        """
        try:
            print('')
            print('                         TAXA')
            CNP = int(input('                         CNP: '))
            taxa = float(input('                         TAXA: '))
            taxa_class = self.__service_taxe.get_taxa(CNP)
            self.__service_taxe.update_taxe(CNP, taxa_class.get_curent(), taxa_class.get_gaz(),
                                            taxa_class.get_internet() + taxa, taxa_class.get_apa(),
                                            taxa_class.get_telefon(),
                                            taxa_class.get_intretinere(), taxa_class.get_gunoi(),
                                            taxa_class.get_chirie())
            clienti = self.__service_client.get_all()
            for client in clienti:
                if client.get_CNP() == CNP:
                    self.__service_client.update_client(client.get_id(), client.get_nume(), client.get_prenume(),
                                                        client.get_CNP(), client.get_serie_buletin(),
                                                        client.get_numar_buletin(), client.get_taxa() + taxa)
            return '                                                    ***** INTERNETUL IN VLOARE DE {} LEI A FOST PLATIT !!! ***** '.format(
                taxa)
        except ValueError as ve:
            print('')
            print('                         ERORI:')
            for error in ve.args[0]:
                print(error)
            print('')

    def __add_taxe_apa(self):
        """
        Add one of a rate
        :return: str, a message
        """
        try:
            print('')
            print('                         TAXA')
            CNP = int(input('                         CNP: '))
            taxa = float(input('                         TAXA: '))
            taxa_class = self.__service_taxe.get_taxa(CNP)
            self.__service_taxe.update_taxe(CNP, taxa_class.get_curent(), taxa_class.get_gaz(),
                                            taxa_class.get_internet(), taxa_class.get_apa() + taxa,
                                            taxa_class.get_telefon(),
                                            taxa_class.get_intretinere(), taxa_class.get_gunoi(),
                                            taxa_class.get_chirie())
            clienti = self.__service_client.get_all()
            for client in clienti:
                if client.get_CNP() == CNP:
                    self.__service_client.update_client(client.get_id(), client.get_nume(), client.get_prenume(),
                                                        client.get_CNP(), client.get_serie_buletin(),
                                                        client.get_numar_buletin(), client.get_taxa() + taxa)
            return '                                                    ***** APA IN VLOARE DE {} LEI A FOST PLATITA !!! ***** '.format(
                taxa)
        except ValueError as ve:
            print('')
            print('                         ERORI:')
            for error in ve.args[0]:
                print(error)
            print('')

    def __add_taxe_telefon(self):
        """
        Add one of a rate
        :return: str, a message
        """
        try:
            print('')
            print('                         TAXA')
            CNP = int(input('                         CNP: '))
            taxa = float(input('                         TAXA: '))
            taxa_class = self.__service_taxe.get_taxa(CNP)
            self.__service_taxe.update_taxe(CNP, taxa_class.get_curent(), taxa_class.get_gaz(),
                                            taxa_class.get_internet(), taxa_class.get_apa(),
                                            taxa_class.get_telefon() + taxa,
                                            taxa_class.get_intretinere(), taxa_class.get_gunoi(),
                                            taxa_class.get_chirie())
            clienti = self.__service_client.get_all()
            for client in clienti:
                if client.get_CNP() == CNP:
                    self.__service_client.update_client(client.get_id(), client.get_nume(), client.get_prenume(),
                                                        client.get_CNP(), client.get_serie_buletin(),
                                                        client.get_numar_buletin(), client.get_taxa() + taxa)
            return '                                                    ***** TELEFONUL IN VLOARE DE {} LEI A FOST PLATIT !!! ***** '.format(
                taxa)
        except ValueError as ve:
            print('')
            print('                         ERORI:')
            for error in ve.args[0]:
                print(error)
            print('')

    def __add_taxe_intretinere(self):
        """
        Add one of a rate
        :return: str, a message
        """
        try:
            print('')
            print('                         TAXA')
            CNP = int(input('                         CNP: '))
            taxa = float(input('                         TAXA: '))
            taxa_class = self.__service_taxe.get_taxa(CNP)
            self.__service_taxe.update_taxe(CNP, taxa_class.get_curent(), taxa_class.get_gaz(),
                                            taxa_class.get_internet(), taxa_class.get_apa(), taxa_class.get_telefon(),
                                            taxa_class.get_intretinere() + taxa, taxa_class.get_gunoi(),
                                            taxa_class.get_chirie())
            clienti = self.__service_client.get_all()
            for client in clienti:
                if client.get_CNP() == CNP:
                    self.__service_client.update_client(client.get_id(), client.get_nume(), client.get_prenume(),
                                                        client.get_CNP(), client.get_serie_buletin(),
                                                        client.get_numar_buletin(), client.get_taxa() + taxa)
            return '                                                    ***** INTRETINEREA IN VLOARE DE {} LEI A FOST PLATITA !!! ***** '.format(
                taxa)
        except ValueError as ve:
            print('')
            print('                         ERORI:')
            for error in ve.args[0]:
                print(error)
            print('')

    def __add_taxe_gunoi(self):
        """
        Add one of a rate
        :return: str, a message
        """
        try:
            print('')
            print('                         TAXA')
            CNP = int(input('                         CNP: '))
            taxa = float(input('                         TAXA: '))
            taxa_class = self.__service_taxe.get_taxa(CNP)
            self.__service_taxe.update_taxe(CNP, taxa_class.get_curent(), taxa_class.get_gaz(),
                                            taxa_class.get_internet(), taxa_class.get_apa(), taxa_class.get_telefon(),
                                            taxa_class.get_intretinere(), taxa_class.get_gunoi() + taxa,
                                            taxa_class.get_chirie())
            clienti = self.__service_client.get_all()
            for client in clienti:
                if client.get_CNP() == CNP:
                    self.__service_client.update_client(client.get_id(), client.get_nume(), client.get_prenume(),
                                                        client.get_CNP(), client.get_serie_buletin(),
                                                        client.get_numar_buletin(), client.get_taxa() + taxa)
            return '                                                    ***** GUNOIUL IN VLOARE DE {} LEI A FOST PLATIT !!! ***** '.format(
                taxa)
        except ValueError as ve:
            print('')
            print('                         ERORI:')
            for error in ve.args[0]:
                print(error)
            print('')

    def __add_taxe_chirie(self):
        """
        Add one of a rate
        :return: str, a message
        """
        try:
            print('')
            print('                         TAXA')
            CNP = int(input('                         CNP: '))
            taxa = float(input('                         TAXA: '))
            taxa_class = self.__service_taxe.get_taxa(CNP)
            self.__service_taxe.update_taxe(CNP, taxa_class.get_curent(), taxa_class.get_gaz(),
                                            taxa_class.get_internet(), taxa_class.get_apa(), taxa_class.get_telefon(),
                                            taxa_class.get_intretinere(), taxa_class.get_gunoi(),
                                            taxa_class.get_chirie() + taxa)
            clienti = self.__service_client.get_all()
            for client in clienti:
                if client.get_CNP() == CNP:
                    self.__service_client.update_client(client.get_id(), client.get_nume(), client.get_prenume(),
                                                        client.get_CNP(), client.get_serie_buletin(),
                                                        client.get_numar_buletin(), client.get_taxa() + taxa)
            return '                                                    ***** CHIRIA IN VLOARE DE {} LEI A FOST PLATIT !!! ***** '.format(
                taxa)
        except ValueError as ve:
            print('')
            print('                         ERORI:')
            for error in ve.args[0]:
                print(error)
            print('')

    def __menu2(self):
        """
        Menu rates
        :return: -
        """
        print('                                    MENIU TAXE       ')
        print('                             ************************')
        print('                             *                      *')
        print('                             * 1. CURENT            *')
        print('                             * 2. GAZ               *')
        print('                             * 3. INTERNET          *')
        print('                             * 4. APA               *')
        print('                             * 5. TELEFON           *')
        print('                             * 6. INTRETINERE       *')
        print('                             * 7. GUNOI             *')
        print('                             * 8. CHIRIE            *')
        print('                             * 9. AFISARE PLATI     *')
        print('                             * 10. EXIT             *')
        print('                             *                      *')
        print('                             ************************')

    def menu_taxe(self):
        """
        Menu rates
        :return: -
        """
        self.__menu2()
        while True:
            print('')
            option = int(input('                         OPTION: '))
            if option == 1:
                print(self.__add_taxe_curent())
            elif option == 2:
                print(self.__add_taxe_gaz())
            elif option == 3:
                print(self.__add_taxe_internet())
            elif option == 4:
                print(self.__add_taxe_apa())
            elif option == 5:
                print(self.__add_taxe_telefon())
            elif option == 6:
                print(self.__add_taxe_intretinere())
            elif option == 7:
                print(self.__add_taxe_gunoi())
            elif option == 8:
                print(self.__add_taxe_chirie())
            elif option == 9:
                self.__show_list(self.__service_taxe.get_all())
            elif option == 10:
                break

    def __menu(self):
        """
        Menu program
        :return: -
        """
        print('        MENIU       ')
        print('********************')
        print('*                  *')
        print('*  1. CLIENTI      *')
        print('*  2. PLATI TAXE   *')
        print('*  3. EXIT         *')
        print('*                  *')
        print('********************')

    def console(self):
        """
        Console
        :return: -
        """
        while True:
            self.__menu()
            print('')
            option = int(input('OPTION: '))
            if option == 1:
                self.menu_client()
            elif option == 2:
                self.menu_taxe()
            elif option == 3:
                break
