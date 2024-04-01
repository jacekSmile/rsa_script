import gmpy2
import libnum

def continuedFra(x, y):
    """计算连分数
    :param x: 分子
    :param y: 分母
    :return: 连分数列表
    """
    cf = []
    while y:
        cf.append(x // y)
        x, y = y, x % y
    return cf
def gradualFra(cf):
    """计算传入列表最后的渐进分数
    :param cf: 连分数列表
    :return: 该列表最后的渐近分数
    """
    numerator = 0
    denominator = 1
    for x in cf[::-1]:
        # 这里的渐进分数分子分母要分开
        numerator, denominator = denominator, x * denominator + numerator
    return numerator, denominator
def solve_pq(a, b, c):
    """使用韦达定理解出pq，x^2−(p+q)∗x+pq=0
    :param a:x^2的系数
    :param b:x的系数
    :param c:pq
    :return:p，q
    """
    par = gmpy2.isqrt(b * b - 4 * a * c)
    return (-b + par) // (2 * a), (-b - par) // (2 * a)
def getGradualFra(cf):
    """计算列表所有的渐近分数
    :param cf: 连分数列表
    :return: 该列表所有的渐近分数
    """
    gf = []
    for i in range(1, len(cf) + 1):
        gf.append(gradualFra(cf[:i]))
    return gf


def wienerAttack(e, n):
    """
    :param e:
    :param n:
    :return: 私钥d
    """
    cf = continuedFra(e, n)
    gf = getGradualFra(cf)
    for d, k in gf:
        if k == 0: continue
        if (e * d - 1) % k != 0:
            continue
        phi = (e * d - 1) // k
        p, q = solve_pq(1, n - phi + 1, n)
        if p * q == n:
            return d


n= 68781015120012754009149819243839432182753699533745468739333557116438115901358573880902197723852823949505376140916570536753019491036629572363854637530919546688901226752085109196549145599781909847664046508960094447692268230516763088293911965638780888720788954194778424857089535187609738198309161969913567107861
e= 54093680529782962282616750547542407544796590039913570980901028264103594185617926725669901283009540557359666956131385125727959502505561517117179644650419753631214251337533961664493198676862110639584202010794500844074619335752668896589407110076134931918634061631574656816488381501901503924226166074238518619869
c= 30443384983816710270001651296607959522389400057103143909277631290995899073895621701281106228069835965181342091582584186637031613250922961166298411359757600825556083868477673357860585539016515776933117915504873987178857740106223631465737111746470236003857656528610755145017342412306680097140732745012583119076

d=wienerAttack(e, n)
m=pow(c, d, n)
print(libnum.n2s(m).decode())