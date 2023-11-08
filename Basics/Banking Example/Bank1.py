#import class from file
from BankAccount import *

LigaBanka = Bank('Liga Banka',[],'538 Porpul Str, Madrid, Spain','847 324 2345')

SonsAccount = Account(LigaBanka,'Sonny','HMS7',253850)
PagesAccount = Account(LigaBanka,'Page','Pageword',72)
SilvasAccount = Account(LigaBanka,'TSilva','Chelsea1',0)

PagesAccount.transfer(LigaBanka,'TSilva',72,'Pageword')
SilvasAccount.view_balance('Chelsea1')
SonsAccount.transfer(LigaBanka,'Page',50000,'HMS7')
PagesAccount.view_balance('Pageword')

AmericaOneBank = Bank('America One Bank',[],'32 Mergle Drv, New York, USA','911 991 9898')

MessisAccount = Account(AmericaOneBank,'Mr.Ballon','LMpro',4500000000)
IsaiahsAccount = Account(AmericaOneBank,'Magical','Rakky',45000)

PagesAccount.transfer(AmericaOneBank,'Magical',25000,'Pageword')
IsaiahsAccount.view_balance('Rakky')

SonsAccount.transfer(AmericaOneBank,'Mr.Ballon',35000,'HMS7')
MessisAccount.view_balance('LMpro')