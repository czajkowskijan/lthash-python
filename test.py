from lthash import LtHash

def test_hom(n,d,m1, m1rem):

	# Hash of the data
	lthash1 = LtHash(n,d)
	lthash1.eval(m1)

	# Hash of the data to be removed
	lthash2 = LtHash(n,d)
	lthash2.eval(m1rem)

	# Hash of the rest of the data
	lthash3 = LtHash(n,d)
	lthash3.eval(m1-m1rem)

	# Is the hash of m1rest the same as Hash(m1)-Hash(m1rem)?
	lthash1.rem(lthash2)
	if lthash3.digest == lthash1.digest:
		print('Homomorphism test passed')

def test_col(n,d,m1):
	# Hash of the data
	lthash1 = LtHash(n,d)
	lthash1.eval(m1)

	# Hash of the data to collide
	lthash2 = LtHash(n,d)
	lthash2.eval(m1)
	m_temp = {'Hello'}
	for i in range(pow(2,d)):
		lthash2.add_data(m_temp)

	if lthash1.digest == lthash2.digest:
		print('Trivial collision found')