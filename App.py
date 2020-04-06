from Repository.Repoitory import *
from Service.Service import *
from Service.Service_Taxe import *
from UI.UI import UI


repo_client = Repository_Generic('Clienti')
repo_taxe = Repository_Generic('Taxe')
serv_client = Service_Client(repo_client)
serv_taxe = Service_Taxe(repo_taxe)
console = UI(serv_client,serv_taxe)
console.console()
