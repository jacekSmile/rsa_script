import gmpy2
import libnum

def de(c, e, n):
    k = 0
    while True:
        mm = c + n*k
        result, flag = gmpy2.iroot(mm, e)
        if True == flag:
            return result
        k += 1
n= 14067473525623615859223663589118945198091192669401088734569589535726733244095067264729942915265175903139441309376381225701454902095234966599914234681888481774607095853830772571665038109641511499155604914228117882196188074964226780922239011682486198651997912713999544628177959592818928976240251790858062449396082494272361535640237914373270152455829541596341184902017633404494979208958080467979235974182507427501682492000572071306960595992848840147393057648929439822116261337091431441205378542080755128597543738922210525692259529009107645032171097155449558362749512243918901171631681472217935131865121871798425854707759
e= 3
c= 2217344750798294937344050117513831761010547351781457575945714176628679412650463329423466955026804439931765627111856888102133234836914006818023839994342283023142702993182665344445325734299047409223354338948863171846780674244925724334091153701697864918695050507247415283070309

m=de(c,e,n)
print(m)
print(libnum.n2s(int(m)).decode())