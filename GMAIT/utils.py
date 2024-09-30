import math
import random
import cmath


def minor(array, pos):
    new_arr = []
    for i in range(len(array)):
        col = []
        if i == pos[0]:
            continue

        for j in range(len(array[i])):
            if j != pos[1]:
                col.append(array[i][j])

        new_arr.append(col)

    return new_arr

def sgn(x):
    return x >= 0 if not callable(x) else x() >= 0

def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a%i == 0 and b%i == 0:
            return i
    return 1

def strpprint(pp):
    new_q = ["".join(i) for i in pp]
    return "\n".join(new_q)

def matrixpprint(pp):
    arr = [strpprint(i) for i in pp]
    return "\n\n".join(arr) 

def connect(arr1, arr2):
    arr3 = []
    for i in range(len(arr1)):
        arr3.append(arr1[i] + arr2[i])
    
    return arr3[:]


def det(array):
    if len(array) == 1:
        return array[0][0]

    else:
        a = []
        for i in range(len(array)):
            for j in range(len(array[i])):
                if isinstance(array[i][j], rational):
                    array[i][j] = float(array[i][j]) 
        for i in range(len(array)):
            a.append(array[0][i] * det(minor(array, [0, i])) * (-1)**(i))
        
        z = a[0]
        for i in range(1, len(a)):
            z+=a[i]
        return z

def numericIntegration(function, c, d, dx=0.0001):
    s = 0
    a = min(c, d)
    b = max(c, d)
    i = a
    while i <= b:
        s += (function(i) + function(i+dx))*dx/2
        i += dx
    return s * sgn(d - c)

def numericDiff(function, x, dx=0.0001):
    return (function(x+dx) - function(x-dx))/(2*dx)

class integer:
    def __init__(self, n):
        self.n = n
    
    def prime(self):
        return integer.isprime(self.n)
    
    def factorize(self):
        return integer.factorization(self.n)
    
    def __add__(self, other):
        return integer(self.n + other.n)
    
    def __mul__(self, other):
        return integer(self.n * other.n)
    
    def __div__(self, other):
        return rational([self.n, other.n])
    
    def __sub__(self, other):
        return integer(self.n - other.n)
    
    def __neg__(self):
        return integer(-self.n)
    
    def __str__(self):
        return str(self.n)
    
    def __int__(self):
        return int(self.n)
    
    def __divmod__(self, other):
        return integer(self.n % int(other))
    
    def __gt__(self, other):
        if isinstance(other, (int, float, rational)):
            return self.n > float(other)
        return self.n > other.n 
    
    def __lt__(self, other):
        if isinstance(other, (int, float, rational)):
            return self.n < float(other)
        return self.n < other.n 
    
    def __ge__(self, other):
        if isinstance(other, (int, float, rational)):
            return self.n >= float(other)
        return self.n >= other.n
    
    def __le__(self, other):
        if isinstance(other, (int, float, rational)):
            return self.n <= float(other)
        return self.n <= other.n
    
    def __eq__(self, other):
        if isinstance(other, (int, float, rational)):
            return self.n == float(other)
        return self.n == other.n
         
    @staticmethod
    def isprime(n):
        if abs(n) == 1 or n == 0:
            return False
        
        for i in range(2, int(abs(n) ** 0.5) + 1):
            if n % i == 0:
                return False
        
        return True

    @staticmethod
    def factorization(n):
        n2 = abs(n)
        if integer.isprime(n2):
            return [[n2, 1]] if n > 0 else [[-1, 1], [n2, 1]]
        if n2 == 0:
            return [[0, 1]]
        arr = []
        if n < 0:
            arr.append([-1, 1])
        for i in range(2, n2):
            k = 0
            while integer.isprime(i) and n2 % i == 0:
                if k == 0:
                    arr.append([i, 1])
                else:
                    arr[-1][-1] += 1
                n2 /= i
                k += 1
            
        return arr
    __rmul__ = __mul__
    __radd__ = __add__
    @staticmethod
    def gcd(n, m):
        for i in range(min(n, m), 0, -1):
            if n % i == 0 and m % i == 0:
                return i
    
    @staticmethod
    def lcd(n, m):
        return int(n * m / integer.gcd(n, m))
    
    @staticmethod
    def rand(nrange=[1, 10]):
        return random.randint(nrange[0], nrange[1])
        
class rational:
    def __init__(self, num):
        #num = [p, q] -> number = p / q
        self.num = num[:]
    
    def __str__(self):
        return "%s / %s" % (str(self.num[0]), str(self.num[1]))
    
    def __call__(self):
        return self.num[0] / self.num[1]
    
    def pprint(self):
        str1 = str(self.num[0])
        str2 = str(self.num[1])
        mlen = max(len(str1), len(str2))
        if str2 != "1":
            a = "".join([" "for i in range((mlen - len(str1))//2)])
            b = a+"".join([" " for i in range((mlen - len(str1))%2)])
            str12 = a + str1 + b
            c = "".join([" "for i in range((mlen - len(str2))//2)])
            d = a+"".join([" " for i in range((mlen - len(str2))%2)])
            str22 = c + str2 + d
            lines = [[str12], ["".join(["-" for i in range(mlen)])], [str22]]
        else:
            lines = [[" " for i in range(len(str1))], [str1], [" " for i in range(len(str1))]]
        
        return lines
        
    
    def simplify(self):
        '''
        p = integer(self.num[0]) if isinstance(self.num[0], int) else self.num[0]
        q = integer(self.num[1]) if isinstance(self.num[1], int) else self.num[1]
        p_fac = dict(p.factorize())
        q_fac = dict(q.factorize())
        
        nfrac = [[i, j - q_fac[i] if i in q_fac.keys() else j] for i, j in p_fac.items()]
        n2frac = []
        for i, j in q_fac.items():
            if i not in p_fac.keys():
                n2frac.append([i, -j])
        
        nfrac += n2frac[:]
        np = 1
        nq = 1
        for i, j in nfrac:
            if j >= 0 :
                np *= i ** j
            
            else:
                nq *= i ** (-j)
        '''
        x = math.gcd(self.num[0], self.num[1])
        return rational([int(self.num[0] / x), int(self.num[1] / x)])
    
    def inv(self):
        return rational([self.num[1], self.num[0]])
    
    def __add__(self, other):
        if isinstance(other, float):
            return self * rational.convRat(other, 2)
        if isinstance(other, (int, integer)):
            n2 = rational([int(other), 1])
        else:
            n2 = other
        
        return rational([self.num[0] * n2.num[1] + n2.num[0] * self.num[1], self.num[1] * n2.num[1]])
    
    def __neg__(self):
        return rational([-self.num[0], self.num[1]])
    
    def __sub__(self, other):
        return self + (-other)
    
    def __mul__(self, other):
        if isinstance(other, (int, integer, float)):
            if isinstance(other, float):
                return self * rational.convRat(other, 2)
            if self.num[0] * int(other) % self.num[1] == 0:
                return self.num[0] * int(other) / self.num[1]
            return rational([self.num[0] * int(other), self.num[1]])
        return rational([self.num[0] * other.num[0], self.num[1] * other.num[1]])
    
    def __truediv__(self, other):
        if isinstance(other, (int, integer)):
            return rational([self.num[0], self.num[1] * int(other)])
        
        elif isinstance(other, rational):
            return self * other.inv()
        
    def __abs__(self):
        return self if self() >= 0 else -self
    
    def __float__(self):
        return self.num[0] / self.num[1]
    
    def __eq__(self, other):
        return float(self) == float(other)
    __rmul__ = __mul__
    __radd__ = __add__
    @staticmethod
    def rand(nrange=[1000, 10000]):
        return rational([random.randint(nrange[0], nrange[1]), random.randint(nrange[0], nrange[1])])
    @staticmethod
    def convRat(num, digits_after):
        n = digits_after
        b = int(num * 10 ** (n))
        c = 10 ** (n)
        return rational([b, c])
    

        
            
    
class AlgebraicReal:
    def __init__(self, num):
        # num = [rational_part(a) : rational, [coeff(b) : int, nth_root of (x:rational), n:int>0], [coeff(b2),n2th_root of (x2), n2], ...] -> num = a + b(x)^(1/n) + b2(x2)^(1/n2)+...
        self.num = num[:]
    def __call__(self):
        s = self.num[0]() if hasattr(self.num[0], '__call__') else self.num[0]
        for r, x, n in self.num[1:]:
            z = (r() if hasattr(r, '__call__') else r) * (x() if hasattr(x, '__call__') else x) ** (1 / n)
            s += z
            
        return s
            
    def __str__(self):
        '''
        array = []
        #[str(self.num[0])] + ["%s * (%s)^(1 / %d)"%(str(c), str(x), n) for c, x, n in self.num[1:]])
        if self.num[0] != 0:
            array.append(str(self.num[0]))
        
        for c, x, n in self.num[1:]:
            if c != 0:
                if c == 1:
                    array.append("(%s)^(1/%d)"%(str(x), n))
                else:
                    array.append("%s * (%s)^(1 / %d)"%(str(c), str(x), n))
        
        return " + ".join(array)
        '''
        return strpprint(self.pprint())
    def pprint(self):
        if self.num[0] != 0:
            lines = self.num[0].pprint() if hasattr(self.num[0], 'pprint') else [[" "], [str(self.num[0])], [" "]]
        elif hasattr(self.num[0], 'pprint'):
            if self.num[0]() != 0:
                lines = self.num[0].pprint() if hasattr(self.num[0], 'pprint') else [[" "], [str(self.num[0])], [" "]]
            else:
                lines = [[], [], []]
        else:
            lines = [[], [], []]
            
        for r, x, n in self.num[1:]:
            if r == 0:
                continue
            temp_lines = [["  "], [" +"], ["  "]]
            #temp_lines += r.pprint() if hasattr(r, 'pprint') else [[" " for i in range(len(str(r)) + 2)], [" " + str(r) + " "], [" " for i in range(len(str(r)) + 2)]]
            if hasattr(r, 'pprint'):
                z = r.pprint()
                q = connect(connect([[" "], [" "], [" "]], z), [[" "], [" "], [" "]])[:]
                temp_lines1 = connect(temp_lines, q)[:]
            else:
                if r != 1:
                    temp_lines1 = connect(temp_lines, [[" " for i in range(len(str(r)) + 2)], [" " + str(r) + " "], [" " for i in range(len(str(r)) + 2)]])[:]
                else:
                    temp_lines1 = temp_lines[:]
                
            temp_lines2 = connect(temp_lines1, [[str(n) + " "], ["".join([" " for i in range(len(str(n)) - 1)]) + "\\/"], [" " for i in range(len(str(n)) + 1)]])[:]
            temp_lines3 = connect(temp_lines2, [["_" for i in range(len(str(x)))], [str(x)], [" " for i in range(len(str(x)))]])[:]
            #print(temp_lines3)
            lines = connect(lines, temp_lines3[:])[:]
        return lines
    def simplify(self):
        rat_part = [self.num[0].simplify() if hasattr(self.num[0], 'simplify') else self.num[0]]
        arr = []
        for coeff, x, n in self.num[1:]:
            xfact = integer.factorization(x)
            ncoeff = coeff
            nxfact = xfact[:]
            for i in range(len(nxfact)):
                if nxfact[i][1] >= n:
                    ncoeff *= nxfact[i][0] ** (int(nxfact[i][1] / n))
                    nxfact[i][1] -= int(nxfact[i][1] / n) * n
            z = 1
            for i, j in nxfact:
                z *= i ** j
            
            if z == 1:
                rat_part[0] += ncoeff
                continue
            arr.append([ncoeff, z, n])
        
        new_arr = []
        for coeff, x, n in arr:
            t = 0
            for i in range(len(new_arr)):
                if x == new_arr[i][1] and n == new_arr[i][2]:
                    new_arr[i][0] += coeff
                    t = 1
            if t == 0:
                new_arr.append([coeff, x, n])
                    
                
        return AlgebraicReal(rat_part + new_arr)   
    
    def __add__(self, other):
        if isinstance(other, (int, integer, rational)):
            new_arr = self.num[:]
            new_arr[0] += other
            return AlgebraicReal(new_arr[:]).simplify()
        else:
            rat_part = [self.num[0] + other.num[0]]      
            irr_part = self.num[1:] + other.num[1:]
            return AlgebraicReal(rat_part + irr_part).simplify()
    
    def __neg__(self):
        narr = [-i for i in self.num]
        return AlgebraicReal(narr)
    
    def __sub__(self, other):
        return self + (-other)
    
    def __mul__(self, other):
        if isinstance(other, (int, integer, rational)):
            new_arr = self.num[:]
            new_arr[0] = other * new_arr[0]
            for i in range(1, len(new_arr)):
                new_arr[i][0] = other * new_arr[i][0]
            
            return AlgebraicReal(new_arr[:])
        
        rat_part = [self.num[0] * other.num[0]]
        irr_part = []
        for i in range(len(self.num)):
            for j in range(1, len(other.num)):
                if i == 0:
                    irr_part.append([self.num[0] * other.num[j][0], other.num[j][1], other.num[j][2]])
                
                else:
                    n = self.num[i][2]
                    m = other.num[j][2]
                    l = integer.lcd(n, m)
                    irr_part.append([self.num[i][0] * other.num[j][0], (self.num[i][1] ** int(l / n)) * (other.num[j][1] ** int(l / m)), l])
        for i in range(1, len(self.num)):
            irr_part.append([other.num[0] * self.num[i][0], self.num[i][1], self.num[i][2]])
        return AlgebraicReal(rat_part + irr_part).simplify()
    __rmul__ = __mul__
    __radd__ = __add__
    def __pow__(self, other):
        s = AlgebraicReal([1, [0, 1, 1]])
        for i in range(other):
            s *= self
        
        return s.simplify()

    @staticmethod
    def rand(num=1, nrange_coeff=[1, 100], nrange_surd=[100, 1000], nrange_root=[1, 5]):
        arr = [rational.rand(nrange=nrange_coeff[:])]
        for i in range(num):
            arr.append([random.randint(nrange_coeff[0], nrange_coeff[1]), random.randint(nrange_surd[0], nrange_surd[1]), random.randint(nrange_root[0], nrange_root[1])])
        
        return AlgebraicReal(arr[:]).simplify()
    
    @staticmethod
    def randpure(num=1, nrange_coeff=[1, 100], nrange_surd=[100, 1000], nrange_root=[2, 5]):
        arr = [0]
        for i in range(num):
            arr.append([random.randint(nrange_coeff[0], nrange_coeff[1]), random.randint(nrange_surd[0], nrange_surd[1]), random.randint(nrange_root[0], nrange_root[1])])
        
        return AlgebraicReal(arr[:]).simplify()
    
    @staticmethod
    def randpurer(num=1, nrange_surd=[100, 1000], nrange_root=[2, 5]):
        arr = [0]
        for i in range(num):
            arr.append([1, random.randint(nrange_surd[0], nrange_surd[1]), random.randint(nrange_root[0], nrange_root[1])])
        
        return AlgebraicReal(arr[:]).simplify()
    
        
class poly:
    def __init__(self, coeffs):
        self.coeffs = coeffs[:]
        for i in range(len(self.coeffs)):
            if isinstance(self.coeffs[i], float):
                if int(self.coeffs[i]) == self.coeffs[i]:
                    self.coeffs[i] = int(self.coeffs[i])
        self.deg = len(coeffs) - 1
    
    def __call__(self, x):
        s = 0
        for i in range(self.deg + 1):
            s += self.coeffs[i] * x ** i
        
        return s
    
    def __str__(self):
        '''
        string = []
        for i in range(self.deg + 1):
            if i < self.deg:
                if i > 1:
                    if self.coeffs[i] == 0:
                        continue;
                    elif self.coeffs[i] == 1 or self.coeffs[i] == -1:
                        string += ["%s%s^%d"%("+" if self.coeffs[i] == 1 else "-", "x", i)]
                    else:
                        string += ["%s%s%s^%d"%("+" if math.copysign(1, self.coeffs[i])==1 else "" , str(self.coeffs[i]), "x", i)]
                elif i == 1:
                    if self.coeffs[i] == 0:
                        continue;
                    elif self.coeffs[i] in [1, -1]:
                        string += ["%s%s"%("+" if math.copysign(1, self.coeffs[i])==1 else "-" , "x")]
                    else:
                        string += ["%s%s%s"%("+" if math.copysign(1, self.coeffs[i])==1 else "" ,str(self.coeffs[i]), "x")]
                elif i == 0:
                    if self.coeffs[i] == 0:
                        continue;
                    string += ["%s%s"%("+" if math.copysign(1, self.coeffs[i])==1 else "" , str(self.coeffs[i]))]
            
            else:
                if i > 1:
                    if self.coeffs[i] == 0:
                        continue;
                    elif self.coeffs[i] in [1, -1]:
                        string += ["%s%s^%d"%("+" if math.copysign(1, self.coeffs[i])==1 else "-" , "x", i)]
                    else:
                        string += ["%s%s%s^%d"%("+" if math.copysign(1, self.coeffs[i])==1 else "", str(self.coeffs[i]), "x", i)]
                elif i == 1:
                    if self.coeffs[i] == 0:
                        continue;
                    elif self.coeffs[i] in [1, -1]:
                        string += ["%s%s"%("+" if math.copysign(1, self.coeffs[i])==1 else "-" , "x")]
                    else:
                        string += ["%s%s%s"%("+" if math.copysign(1, self.coeffs[i])==1 else "" ,str(self.coeffs[i]), "x")]
                elif i == 0:
                    if self.coeffs[i] == 0:
                        continue;
                    string += ["%s"%(str(self.coeffs[i]))]

        string.reverse()
        return "".join(string)
        '''
        return strpprint(self.pprint())
    
    def pprint(self):
        new_array = self.coeffs[:]
        new_array.reverse()
        lines = [[], [], []]
        for i in range(len(new_array)):
            temp_lines1 = [[" "], ["+" if sgn(new_array[i]) else "-"], [" "]]
            if not isinstance(new_array[i], rational):
                if i == self.deg:
                    temp_lines2 = connect(temp_lines1, [[" " for i in range(len(str(new_array[i])))], [str(abs(new_array[i]))], [" " for i in range(len(str(new_array[i])))]])
                elif i == self.deg - 1:
                    temp_lines2 = connect(temp_lines1, [[" " for i in range(len(str(new_array[i])) + 1)], [str(abs(new_array[i])) + "x"], [" " for i in range(len(str(new_array[i])) + 1)]])
                    
                else:
                    if abs(new_array[i]) != 1:
                        temp_lines2 = connect(temp_lines1, [["".join([" " for i in range(len(str(abs(new_array[i]))) + 1)]) + str(self.deg - i)], [str(abs(new_array[i])) + "x" + "".join([" " for i in range(len(str(self.deg - i)))])], [" " for i in range(len(str(abs(new_array[i]))) + len(str(self.deg - i)))]])
                    else:
                        temp_lines2 = connect(temp_lines1, [["".join([" "]) + str(self.deg - i)], ["x" + "".join([" " for i in range(len(str(self.deg - i)))])], [" " for i in range(1 + len(str(self.deg - i)))]])
                lines = connect(lines, temp_lines2)
            else:
                if i == self.deg:
                    temp_lines2 = connect(temp_lines1, abs(new_array[i]).pprint())
                elif i == self.deg - 1:
                    temp_lines2 = connect(temp_lines1, connect(abs(new_array[i]).pprint(), [[" "], ["x"], [" "]]))
                else:
                    if abs(new_array[i]) != 1:
                        temp_lines2 = connect(temp_lines1, connect(abs(new_array[i]).pprint(), [[" " + str(self.deg - i)], ["x"+ "".join([" " for i in range(len(str(self.deg - i)))])], [" "+"".join([" " for i in range(len(str(self.deg - i)))])]]))
                    else:
                        temp_lines2 = connect(temp_lines1, [[" " + str(self.deg - i)], ["x"+ "".join([" " for i in range(len(str(self.deg - i)))])], [" "+"".join([" " for i in range(len(str(self.deg - i)))])]])
                lines = connect(lines, temp_lines2)
        
        return lines[:]
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            x = self.coeffs[:]
            x[0] += other
            return poly(x[:])
        
        elif isinstance(other, poly):
            large_poly = self if self.deg >= other.deg else other
            small_poly = self if self.deg < other.deg else other
            
            res_arr = small_poly.coeffs[:] + [0 for i in range(large_poly.deg - small_poly.deg)]
            for i in range(len(large_poly.coeffs)):
                res_arr[i] += large_poly.coeffs[i]
            
            return poly(res_arr[:])
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x = [other * i for i in self.coeffs[:]]
            return poly(x)
        
        elif isinstance(other, poly):
            arr = [0 for i in range(self.deg + other.deg + 1)]
            for i in range(len(self.coeffs)):
                for j in range(len(other.coeffs)):
                    arr[i + j] += self.coeffs[i] * other.coeffs[j]
            
            return poly(arr[:])
    
    def __pow__(self, other):
        if isinstance(other, int):
            p = poly([1])
            for i in range(other):
                p *= self
            return p
    def __eq__(self, other):
        return self.coeffs[:] == other.coeffs[:]
    
    def __truediv__(self, other):
        
        def normalize(poly):
            while poly and poly[-1] == 0:
                poly.pop()
            if poly == []:
                poly.append(0)


        def poly_divmod(num, den):
            #Create normalized copies of the args
            num = num[:]
            normalize(num)
            den = den[:]
            normalize(den)

            if len(num) >= len(den):
                #Shift den towards right so it's the same degree as num
                shiftlen = len(num) - len(den)
                den = [0] * shiftlen + den
            else:
                return [0], num

            quot = []
            divisor = float(den[-1])
            for i in range(shiftlen + 1):
                #Get the next coefficient of the quotient.
                mult = num[-1] / divisor
                quot = [mult] + quot

                #Subtract mult * den from num, but don't bother if mult == 0
                #Note that when i==0, mult!=0; so quot is automatically normalized.
                if mult != 0:
                    d = [mult * u for u in den]
                    num = [u - v for u, v in zip(num, d)]

                num.pop()
                den.pop(0)

            normalize(num)
            return quot, num
        return poly(poly_divmod(self.coeffs[:], other.coeffs)[0])
    
    def __mod__(self, other):
        def normalize(poly):
            while poly and poly[-1] == 0:
                poly.pop()
            if poly == []:
                poly.append(0)


        def poly_divmod(num, den):
            #Create normalized copies of the args
            num = num[:]
            normalize(num)
            den = den[:]
            normalize(den)

            if len(num) >= len(den):
                #Shift den towards right so it's the same degree as num
                shiftlen = len(num) - len(den)
                den = [0] * shiftlen + den
            else:
                return [0], num

            quot = []
            divisor = float(den[-1])
            for i in range(shiftlen + 1):
                #Get the next coefficient of the quotient.
                mult = num[-1] / divisor
                quot = [mult] + quot

                #Subtract mult * den from num, but don't bother if mult == 0
                #Note that when i==0, mult!=0; so quot is automatically normalized.
                if mult != 0:
                    d = [mult * u for u in den]
                    num = [u - v for u, v in zip(num, d)]

                num.pop()
                den.pop(0)

            normalize(num)
            return quot, num
        return poly(poly_divmod(self.coeffs[:], other.coeffs)[1])

    def __round__(self, ndigits = 3):
        return poly([round(i, ndigits=ndigits) for i in self.coeffs])


        
    
    def diff(self):
        array = []
        for i in range(1, len(self.coeffs)):
            array.append(i * self.coeffs[i])
        
        return poly(array)
    
    def resultant(self, other):
        array = []
        for i in range(self.deg + other.deg):
            l = []
            for j in range(self.deg + other.deg):
                l.append(0)
            array.append(l)
        for i in range(other.deg):
            for j in range(self.deg + 1):
                array[j + i][i] = self.coeffs[j]
        
        for i in range(self.deg):
            for j in range(other.deg + 1):
                array[j + i][i + other.deg] = other.coeffs[j]

        return det(array)
    
    def disc(self):
        n = self.deg
        return (1/self.coeffs[-1])*((-1)**(n*(n-1)/2)) * self.resultant(self.diff())
    
    def roots(self):
        if self.deg == 1:
            return rational([-self.coeffs[0], self.coeffs[1]]).simplify()
        
        if self.deg == 2:
            a = self.coeffs[2]
            b = self.coeffs[1]
            c = self.coeffs[0]
            d = b**2 - 4*a*c
            return [(-b + cmath.sqrt(d))/(2*a), (-b - cmath.sqrt(d))/(2*a)]
        
        if self.deg == 3:
            a = self.coeffs[3]
            b = self.coeffs[2]
            c = self.coeffs[1]
            d = self.coeffs[0]
            
            d0 = b**2 - 3*a*c
            d1 = 2*b**3-9*a*b*c+27*d*a**2
            C = ((d1 + cmath.sqrt(d1**2-4*d0**3)) / 2)**(1/3)
            r1 = (-1/(3*a)) * (b + C + d0/C)
            r2, r3 = (self / poly([-r1, 1])).roots()
            
            return [r1, r2, r3]
            
    
    __rmul__ = __mul__
    __radd__ = __add__
    @staticmethod
    def rand(deg, coeff_range = [0, 10]):
        coeffs = [(-1)**random.randint(1, 10) * random.randint(coeff_range[0], coeff_range[1]) for i in range(deg + 1)]
        return poly(coeffs)
    
    @staticmethod
    def randrat(deg, coeff_range = [0, 10]):
        coeffs = [(-1)**random.randint(1, 10) * rational.rand(nrange=coeff_range[:]).simplify() for i in range(deg + 1)]
        return poly(coeffs)
    
    @staticmethod
    def newtonsmethod(pl, start, max_iter):
        x_i = start
        x_ig = start
        for i in range(max_iter):
            x_ig = x_i
            x_i -= pl(x_i) / pl.diff()(x_i)
            x_i = round(x_i, ndigits=10)
            if x_i == x_ig:
                break
        
        return x_i

class matrix:
    def __init__(self, array):
        self.array = array[:]
    def __str__(self):
        '''
        new_arr = []
        longest_length = 0
        for i in self.array:
            z = []
            for j in i:
                s = str(j)
                if len(s) > longest_length:
                    longest_length = len(s)
                z.append(s)

            new_arr.append(z)
            
        fstring = []
        for i in new_arr:
            for j in range(len(i)):
                x = ""
                for k in range(int((longest_length - len(i[j]))/2)):
                    x += " "
                z = "".join([x, i[j], x, " " if longest_length - len(i[j]) % 2 == 1 else "",  ", " if j != len(i) - 1 else ""])
                fstring.append(z)
            fstring.append("\n")
            
        return "".join(fstring)
        '''
        return matrixpprint(self.pprint())
    def pprint(self):
        tot_cells = []
        for i in self.array:
            cells = []
            for j in i:
                lines = [[], [], []]
                if hasattr(j, 'pprint'):
                    lines = connect(lines, j.pprint())
                else:
                    lines = connect(lines, [[" " for i in range(len(str(j)))], [k for k in str(j)], [" " for i in range(len(str(j)))]])
                    
                cells.append(lines)
            
            tot_cells.append(cells)
        
        longest_length = 0
        for i in tot_cells:
            for j in i:
                if max([len(k) for k in j]) > longest_length:
                    longest_length = max([len(k) for k in j])
        tot_lines = []
        for i in range(len(tot_cells)):
            lines = [[], [], []]
            for j in range(len(tot_cells[i])):
               mlen = max([len(k) for k in tot_cells[i][j]])
               new_cell = connect(tot_cells[i][j], [[" " for k in range((longest_length - mlen)//2)]for h in range(3)])
               new_cell2 = connect([[" " for k in range((longest_length - mlen)//2 + (longest_length - mlen) % 2)]for h in range(3)], new_cell)
               lines = connect(lines, new_cell2)
               lines = connect(lines, [["   "], [" , "], ["   "]])
            tot_lines.append(lines)
        
        return tot_lines[:]
            
    def __call__(self, x):
        new_arr = []
        for i in range(len(self.array)):
            sub = []
            for j in range(len(self.array[0])):
                sub.append(self.array[i][j](x) if isinstance(self.array[i][j], poly) else self.array[i][j])
            new_arr.append(sub)
        return matrix(new_arr[:])
        
    
    def __add__(self, other):
        self_copy = self.array[:]
        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                self_copy[i][j] += other.array[i][j]

        return matrix(self_copy)
    
    def __mul__(self, other):
        if isinstance(other, (int, float, poly)):
            x = self.array[:]
            for i in range(len(x)):
                for j in range(x[i]):
                    x[i][j] = other * x[i][j]

            return matrix(x)
        
        elif isinstance(other, matrix):
            if len(self.array[0]) != len(other.array):
                raise Exception("Dimensions not compatible.")
            
            else:
                arr = []
                for i in range(len(self.array)):
                    sub_arr = []
                    for j in range(len(other.array[0])):
                        sub_arr.append(sum([self.array[i][k] * other.array[k][j] for k in range(len(self.array[i]))]))
                    arr.append(sub_arr[:])
                
                return matrix(arr)
    
    def det(self):
        return det(self.array[:])
    
    def __eq__(self, other):
        return self.array[:] == other.array[:]
    
    def charpoly(self):
        new_arr = [[j for j in i] for i in self.array[:]]
        for i in range(len(self.array)):
            new_arr[i][i] = poly([float(new_arr[i][i]), -1])
        
        return matrix(new_arr[:]).det()
    
    def eigenvalue(self):
        return [i.real for i in self.charpoly().roots()[:]]
    
    __rmul__ = __mul__
    __radd__ = __add__
    @staticmethod
    def rand(dims=[3, 3], nrange=[1, 10]):
        arr = []
        for i in range(dims[0]):
            sub = []
            for j in range(dims[1]):
                sub.append(random.randint(nrange[0], nrange[1]))

            arr.append(sub)
        
        return matrix(arr)
    
    @staticmethod
    def randpoly(dims = [3, 3], max_deg = 1, coeff_range = [1, 10]):
        arr = []
        for i in range(dims[0]):
            sub = []
            for j in range(dims[1]):
                sub.append(poly.rand(random.randint(0, max_deg), coeff_range=coeff_range[:]))

            arr.append(sub)
        
        return matrix(arr)
    @staticmethod
    def randrat(dims=[3, 3], nrange=[1, 10]):
        arr = []
        for i in range(dims[0]):
            sub = []
            for j in range(dims[1]):
                sub.append(rational.rand(nrange[:]).simplify())

            arr.append(sub)
        
        return matrix(arr)

def generate_integrable_ratExpr(deg=3, nranges = [1, 10]):
    p = poly([1])
    p_deg = random.randint(0, deg)
    q = poly([1])
    q_deg = random.randint(0, deg)
    for i in range(p_deg // 2):
        s1 = random.randint(1, 2) % 2
        p *= s1 * poly.rand(2, coeff_range=nranges[:]) + (1-s1)*poly.rand(1, coeff_range=nranges[:])*poly.rand(1, coeff_range=nranges[:])
    for i in range(q_deg // 2):
        s2 = random.randint(1, 2) % 2
        q *= s2 * poly.rand(2, coeff_range=nranges[:]) + (1-s2)*poly.rand(1, coeff_range=nranges[:])*poly.rand(1, coeff_range=nranges[:])
    for i in range(p_deg % 2):
        p *= poly.rand(1, coeff_range=nranges[:])
    for i in range(q_deg % 2):
        q *= poly.rand(1, coeff_range=nranges[:])
    
    str1 = str(p)
    str2 = str(q)
    str1cpy = str1[:]
    str2cpy = str2[:]
    len_measure1 = len(str1cpy.split("\n")[0])
    len_measure2 = len(str2cpy.split("\n")[0])
    str3 = "".join(["-" for j in range(max(len_measure1, len_measure2))])
    z = str1 + "\n" + str3 + "\n" + str2 + "\n"
    return [p, q, z]

def generate_eulersub(deg=2, nranges=[1, 10]):
    rat1 = generate_integrable_ratExpr(deg=deg, nranges=nranges[:])
    sq_term = poly.rand(2, coeff_range=nranges[:])
    for i in range(len(sq_term.coeffs[:])):
        sq_term.coeffs[i] = abs(sq_term.coeffs[i])
    sqf = lambda x : math.sqrt(sq_term(x)) if sq_term(x) > 0 else 1
    rat2seed = random.randint(1, 2)%2
    rat2 = (lambda x : sqf(x)) if rat2seed else (lambda x : 1/sqf(x))
    tot_func = lambda x : (rat1[0](x) / rat1[1](x)) * rat2(x)
    p1, q1, z1 = rat1[:]
    z3 = sq_term.pprint()[:]
    z3_cp2 = ["\\", "/"] + z3[1]
    z3_cp1 = ["  ", "/"] + z3[0]
    v = [" " for i in range(len(z3_cp1))]
    z3_cpy = [
                [" ", " "] + ["-" for i in range(len(z3[2]) - 2)], 
                z3_cp1[:],
                z3_cp2[:],
                v
            ]
    z1, z2 = p1.pprint(), q1.pprint()
    l1 = max([len("".join(i)) for i in z1])
    l2 = max([len("".join(i)) for i in z2])
    l3 = max(l1, l2)
    p1pprintmod = p1.pprint()[:-1]
    q1pprintmod = q1.pprint()[:-1]
    for i in range(len(p1pprintmod)):
        string = p1pprintmod[i] + [" " for i in range(l3-len("".join(p1pprintmod[i])))]
        p1pprintmod[i] = string
        
    for i in range(len(q1pprintmod)):
        string = q1pprintmod[i] + [" " for i in range(l3-len("".join(q1pprintmod[i])))]
        q1pprintmod[i] = string
    
    p1pprint = [[" " for i in range(l3)]] + [[" " for i in range(l3)]] + p1pprintmod[:]
    q1pprint = q1pprintmod[:]+[[" " for i in range(l3)]]
    ratstr1 = p1pprint + [["-"for i in range(l3)]] + q1pprint
    ratstr1 = connect([["/"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["\\"]], ratstr1)
    ratstr1 = connect(ratstr1, [["\\"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["/"]])
    
    
    if rat2seed:
            z3_cpy2 = [
                v,
                v,
                [" ", "  "] + ["-" for i in range(len(z3[2]) - 2)],
                z3_cp1[:],
                z3_cp2[:],
                v,
                v,
                v    
            ]
            
            finstr = connect(ratstr1, z3_cpy2)
            return [tot_func, strpprint(finstr)]
    
    else:
        z3_cpy2 = [
                v,
                v,
                v,
                [" " for i in range((len(v)-1) // 2)] + ["1"] + [" " for i in range((len(v)-1) // 2 + (len(v)-1) % 2)],
                ["-" for i in range(len(v))],
                [" ", "  "] + ["-" for i in range(len(z3[2]) - 2)], 
                z3_cp1[:],
                z3_cp2[:],
            ]
        finstr = connect(ratstr1, z3_cpy2)
        return [tot_func, strpprint(finstr)]

def generate_trig(nranges=[1, 10]):
    a, s, c = random.randint(nranges[0], nranges[1]), random.randint(nranges[0], nranges[1]), random.randint(nranges[0], nranges[1])
    a2, s2, c2 = random.randint(nranges[0], nranges[1]), random.randint(nranges[0], nranges[1]), random.randint(nranges[0], nranges[1])
    a3, t = random.randint(nranges[0], nranges[1]), random.randint(nranges[0], nranges[1])
    modeseed = random.randint(1, 3) 
    if modeseed == 1:
        p = lambda x : a + s * math.sin(x) + c * math.cos(x)
        q = lambda x : a2 + s2 * math.sin(x) + c2 * math.cos(x)
        p_str = "%d + %dsin(x) + %dcos(x)" % (a, s, c)
        q_str = "%d + %dsin(x) + %dcos(x)" % (a2, s2, c2)
        return [lambda x : p(x) / q(x), p_str + "\n" + "".join(["-" for i in range(max(len(p_str), len(q_str)))]) + "\n" + q_str]
    
    elif modeseed == 2:
        l = random.randint(nranges[0], nranges[1])
        s = random.randint(1, 2) % 2
        p = lambda x : l / (a3 + t * ((-1)**s) * math.tan(x))
        q_str = "%d + %dtan(x)"%(a3, t * ((-1)**s)) if not s else "%d - %dtan(x)"%(a3, t)
        t_str = str(l) + "\n" + "".join(["-" for i in range(max(len(str(l)), len(q_str)))]) + "\n" + q_str
        return [p, t_str]
    
    elif modeseed == 3:
        return generate_trig_prod(nranges=nranges[:])

def generate_trig_prod(nranges=[1, 10]):
    a, b = random.randint(nranges[0], nranges[1]), random.randint(nranges[0], nranges[1])
    function = lambda x : (math.sin(x)**a)*(math.cos(x))**b
    x = [i for i in str(a)] if a != 1 else [" "]
    y = [i for i in str(b)] if a != 1 else [" "]
    string_array = [[" ", " ", " "] + x + [" ", " ", " ", " ", " "] + y + [" "],
                    ["s", "i", "n"] + [" " for i in range(len(str(a)))] + ["x", " "] + ["c", "o", "s"] + [" " for i in range(len(str(b)))] + ["x"]]
    string = "\n".join(["".join(i) for i in string_array])
    return [function, string]

def generate_fourier_s(nranges=[1, 10], deg=2, p_range=[1, 5], exp_cond=False):
    p1 = poly.rand(deg, coeff_range=nranges[:])
    c1 = random.randint(nranges[0], nranges[1])
    period = 2*random.randint(p_range[0], p_range[1])
    rand_exp = lambda x : math.exp(c1 * x)
    f = (lambda x : p1(x) * rand_exp(x))
    if not exp_cond:
        f = lambda x : p1(x)
    a_n_d = lambda n : (lambda x : f(x) * math.cos(2 * n * math.pi * x / period))
    b_n_d = lambda n : (lambda x : f(x) * math.sin(2 * n * math.pi * x / period)) 
    a_n = lambda n : numericIntegration(a_n_d(n), -period/2, period/2) / (period/2)
    b_n = lambda n : numericIntegration(b_n_d(n), -period/2, period/2) / (period/2)
    a_0 = numericIntegration(f, -period/2, period/2) / period
    if not exp_cond:
        return [f, period, a_n, b_n, a_0, strpprint(p1.pprint()), p1, c1]
    poly_pprint = connect(connect([["/"], ["|"], ["\\"]], p1.pprint()), [["\\"], ["|"], ["/"]])
    array = [[" "], ["e"], [" "]]
    for i in str(c1):
        array[0].append(i)
    array[0].append("x")
    for i in range(len(str(c1)) + 1):
        array[1].append(" ")
        array[2].append(" ")
    
    full_pprint = connect(array, poly_pprint)
    return [f, period, a_n, b_n, a_0, strpprint(full_pprint), p1, c1]

def fourier_s_poly(p1, p_range=[1, 5]):
    period = 2*random.randint(p_range[0], p_range[1])
    f = lambda x : p1(x)
    a_n_d = lambda n : (lambda x : f(x) * math.cos(2 * n * math.pi * x / period))
    b_n_d = lambda n : (lambda x : f(x) * math.sin(2 * n * math.pi * x / period)) 
    a_n = lambda n : numericIntegration(a_n_d(n), -period/2, period/2) / (period/2)
    b_n = lambda n : numericIntegration(b_n_d(n), -period/2, period/2) / (period/2)
    a_0 = numericIntegration(f, -period/2, period/2) / period
    return [period, a_n, b_n, a_0]

def randFunction(nranges=[1, 10], n=2, max_deg=2):
    functions = [(math.sin, [[" ", " ", " ", " ", " ", " "], ["s", "i", "n", "(", "x", ")"], [" ", " ", " ", " ", " ", " "]]), 
                 (math.cos, [[" ", " ", " ", " ", " ", " "], ["c", "o", "s", "(", "x", ")"], [" ", " ", " ", " ", " ", " "]]), 
                 (math.exp, [[" ", "x"], ["e"," "], [" ", " "]])]
    return functions[random.randint(0, len(functions) - 1)]


def runge_kutta_2nd(coeffs, function, start, step, init_vals):
    '''
    init_vals = [y(x0), y'(x0)]
    '''
    def f(x):
        z_i = init_vals[-1]
        y_i = init_vals[0]
        x_i = start
        while x_i < x:
            k1 = step * z_i
            L1 = step * (1/coeffs[-1]) * (function(x_i) - coeffs[0] - coeffs[1]*y_i)
            
            k2 = step * (z_i+L1/2)
            L2 = step * (1/coeffs[-1]) * (function(x_i+step/2) - coeffs[0] - coeffs[1]*(y_i + k1/2))
            
            k3 = step * (z_i + L2/2)
            L3 = step * (1/coeffs[-1]) * (function(x_i+step/2) - coeffs[0] - coeffs[1]*(y_i + k2/2))
            
            k4 = step * (z_i + L3)
            L4 = step * (1/coeffs[-1]) * (function(x_i+step) - coeffs[0] - coeffs[1]*(y_i + k3))
            
            y_i += (1/6)*(L1+2*L2+2*L3+L4)
            z_i += (1/6)*(k1+2*k2+2*k3+k4)
            x_i += step
        return y_i
    
    return f
def random_diff_eq_2(nranges=[1, 10], n=2, max_deg=2):
    coeffs = [random.randint(nranges[0], nranges[1]) * (-1)**random.randint(0, 1) for i in range(3)]
    ppr = [[], [], []]
    for i in range(len(coeffs) - 1, -1, -1):
        if coeffs[i] != 0:
            if abs(coeffs[i]) != 1:
                ppr = connect(ppr[:], [[" " for j in range(len(str(abs(coeffs[i]))) + 2)]+["'" for j in range(i)],["+" if coeffs[i] > 0 else "-"]+[j for j in str(abs(coeffs[i]))] + ["y"] + [" " for j in range(i)], [" " for j in range(len(str(abs(coeffs[i]))) + i + 2)]])[:]
            else:
                ppr = connect(ppr[:], [[" " for j in range(1+ 2)]+["'" for j in range(i)],["+" if coeffs[i] > 0 else "-"]+ ["y"] + [" " for j in range(i)], [" " for j in range(i + 3)]])[:]  
    ppr = connect(ppr[:], [["   "], [" = "], ["   "]])
    f, pprint_s = randFunction(nranges=nranges[:], n=n, max_deg=max_deg) if random.randint(0, 1) else ((lambda x : 1), [[], [], []])
    h = poly.rand(random.randint(0, max_deg), coeff_range=nranges[:])
    s = h.pprint()
    fin_ppr = connect(ppr[:], connect(pprint_s[:], connect([[" "], ["("], [" "]], connect(s, [[" "], [")"], [" "]]))))
    init_vals = [random.randint(nranges[0], nranges[1]), random.randint(nranges[0], nranges[1])]
    fin_func = runge_kutta_2nd(coeffs, lambda x : h(x) * f(x), 0, 0.000001, init_vals[:])
    return fin_func, strpprint(fin_ppr), init_vals

