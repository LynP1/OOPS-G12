#import class from file
from BankAccount import *

LigaBanka = []

SonsAccount = Account('Sonny','HMS7',253850)
LigaBanka.append(SonsAccount)
PagesAccount = Account('Page','Pageword',72)
LigaBanka.append(PagesAccount)
SilvasAccount = Account('TSilva','Chelsea1',0)
LigaBanka.append(SilvasAccount)

PagesAccount.transfer(LigaBanka,'TSilva',72,'Pageword')
SilvasAccount.view_balance('Chelsea1')
SonsAccount.transfer(LigaBanka,'Page',50000,'HMS7')
PagesAccount.view_balance('Pageword')