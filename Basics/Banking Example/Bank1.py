#import class from file
from BankAccount import *

LigaBanka = []

SonsAccount = Account(LigaBanka,'Sonny','HMS7',253850)
PagesAccount = Account(LigaBanka,'Page','Pageword',72)
SilvasAccount = Account(LigaBanka,'TSilva','Chelsea1',0)

PagesAccount.transfer(LigaBanka,'TSilva',72,'Pageword')
SilvasAccount.view_balance('Chelsea1')
SonsAccount.transfer(LigaBanka,'Page',50000,'HMS7')
PagesAccount.view_balance('Pageword')
