from Crypto.Util.number import *
import gmpy2
from flag import flag
assert flag[:5]==b'flag{'

m = bytes_to_long(flag)
p = getPrime(1024)
q = getPrime(1024)
n = p * q
print('n =',n)
e = 0x10001
M = 2021 * m * 1001 * p
c = pow(M,e,n)
print('c =',c)

#n = 17365231154926348364478276872558492775911760603002394353723603461898405740234715001820111548600914907617003806652492391686710256274156677887101997175692277729648456087534987616743724646598234466094779540729413583826355145277980479040157075453694250572316638348121571218759769533738721506811175866990851972838466307594226293836934116659685215775643285465895317755892754473332034234495795936183610569571016400535362762699517686781602302045048532131426035260878979892169441059467623523060569285570577199236309888155833013721997933960457784653262076135561769838704166810384309655788983073376941843467117256002645962737847
#c = 6944967108815437735428941286784119403138319713455732155925055928646536962597672941805831312130689338014913452081296400272862710447207265099750401657828165836013122848656839100854719965188680097375491193249127725599660383746827031803066026497989298856420216250206035068180963797454792151191071433645946245914916732637007117085199442894495667455544517483404006536607121480678688000420422281380539368519807162175099763891988648117937777951069899975260190018995834904541447562718307433906592021226666885638877020304005614450763081337082838608414756162253825697420493509914578546951634127502393647068722995363753321912676