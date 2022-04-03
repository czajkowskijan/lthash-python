from lthash import LtHash

def test_rem(n,d,m1, m1rem) -> bool:
	# All data inputs have to be sets

	# Hash of the data
	lthash1 = LtHash(n,d)
	lthash1.eval(m1)

	# Hash of the data to be removed
	lthash2 = LtHash(n,d)
	lthash2.eval(m1rem)

	# Hash of the rest of the data
	lthash3 = LtHash(n,d)
	lthash3.eval(m1-m1rem)

	# Is the hash of m1rest different from Hash(m1)-Hash(m1rem)?
	lthash1.rem(lthash2)
	return lthash3.digest != lthash1.digest
	 

def test_add(n,d,m1, m1add) -> bool:
	# All data inputs have to be sets

	# Hash of the data
	lthash1 = LtHash(n,d)
	lthash1.eval(m1)

	# Hash of the data to be added
	lthash2 = LtHash(n,d)
	lthash2.eval(m1add)

	# Hash of the union of the data
	lthash3 = LtHash(n,d)
	lthash3.eval(m1.union(m1add))

	# Is the hash of m1+m1add different from Hash(m1)+Hash(m1add)?
	lthash1.add(lthash2)
	return lthash3.digest != lthash1.digest

def test_rem_data(n,d,m1, m1rem) -> bool:
	# All data inputs have to be sets

	# Hash of the data
	lthash1 = LtHash(n,d)
	lthash1.eval(m1)

	# Hash of the rest of the data
	lthash3 = LtHash(n,d)
	lthash3.eval(m1-m1rem)

	# Is rem_data faulty?
	lthash1.rem_data(m1rem)
	return lthash1.digest != lthash3.digest

def test_add_data(n,d,m1, m1add) -> bool:
	# All data inputs have to be sets

	# Hash of the data
	lthash1 = LtHash(n,d)
	lthash1.eval(m1)

	# Hash of the union of the data
	lthash3 = LtHash(n,d)
	lthash3.eval(m1.union(m1add))

	# Is add_data faulty?
	lthash1.add_data(m1add)
	return lthash1.digest != lthash3.digest

def test_hom(n,d,m1,m1add,m1rem) -> None:
	if test_rem(n,d,m1, m1rem):
		print('Method rem is not working!')
	elif test_rem_data(n,d,m1, m1rem):
		print('Method rem_data is not working!')
	elif test_add(n,d,m1, m1add):
		print('Method add is not working!')
	elif test_add_data(n,d,m1, m1add):
		print('Method add_data is not working!')
	else:
		print('Set homomorphism works!')
