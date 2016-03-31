import sys, math, random
import prime
def extendedEuclid(a,b):
	#print 'extendedEuclid of ',a,b
	if b==0:
		return (a,1,0)

	tuplPrime = extendedEuclid(b,a % b)
	return [tuplPrime[0], tuplPrime[2], (tuplPrime[1] - (a//b)*tuplPrime[2])]

def CRT(N,a,n):
	N = int(N)
	prod_n = reduce(lambda x,y: x*y, n)
	p = list()
	for i in xrange(0,N):
		p.append(prod_n//n[i])
	t = list()
	for i in xrange(0,N):
		t.append((extendedEuclid(p[i],n[i])[1])%n[i])
	A = 0
	for i in xrange(0,N):
		A += a[i]*t[i]*p[i]
	A = A%prod_n
	return	A


def deal(secret, n, k):
	print secret
	m = prime.get_primes(secret, 1)
	for x in prime.get_primes(m[0]*3,n):
		m.append(x)
	print 'm: ', m
	mdash = m[1:k+1]
	mi = reduce(lambda x,y: x*y, mdash)
	mdash = m[k+1:n+1]
	mk = m[0]*reduce(lambda x,y: x*y, mdash)
	print 'mi: ', mi
	print 'mk: ', mk
	if mi>mk:
		print 'mi > mk: Success'
	else:
		print 'mi < mk: Condition failed'
	M = reduce(lambda x,y: x*y, m)
	y = secret
	while(True):
		a = int(random.random()*100)
		print 'a: ',a
		y = secret + a*m[0]
		print 'y: ',y,'  mi:', mi
		if y < 0 or y > mi:
			print 'Failure. Trying again!'
		else:
			break
	Y = list()
	for x in xrange(1,n+1):
		yi = y % m[x]
		Y.append(yi)
		print 'y_'+str(x)+":", yi, 'm_'+str(x)+":", m[x]
	print 'm0:', m[0]



def reconstruct(y,m, m0):
	Ms = reduce(lambda x,y: x*y, m)
	print 'Ms: ', Ms
	yprime = CRT(len(y),y,m)
	print yprime, yprime%Ms
	d = (yprime%m0)
	print 'd: ', d, 'mod',Ms

if sys.argv[1] == 'deal':
	deal(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
elif sys.argv[1] == 'reconstruct':
	y = map(int,sys.argv[2].split(','))
	m = map(int,sys.argv[3].split(','))
	m0 = int(sys.argv[4])
	reconstruct(y,m,m0)
