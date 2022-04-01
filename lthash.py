from Crypto.Hash import SHAKE128
import math

class LtHash:
	def __init__(self, n=1024, d=16):
		self.n = n
		self.d = d
		self.digest = [None]*self.n

	def eval(self, x: set[str]) -> None:
		q = pow(2,self.d)
		h_sum = [0]*self.n
		for xi in x:
			assert isinstance(xi, str), "Database has to consist of strings"
			h_new = self.__h(bytes( xi  , 'utf-8'))
			h_sum = [sum(x)%q for x in zip(h_sum, h_new)]
			self.digest = h_sum

	def add(self,lthash) -> None:
		assert lthash.n == self.n, "number of elements n has to be the same"
		assert lthash.d == self.d, "modulus q=2^d has to be the same"
		assert lthash.digest != [None]*lthash.n, "The added hash has not been evaluated"
		if self.digest == [None]*self.n:
			self.digest = [0]*self.n
		q = pow(2,self.d)
		self.digest = [sum(x)%q for x in zip(self.digest, lthash.digest)]

	def add_data(self,m) -> None:
		if self.digest == [None]*self.n:
			self.digest = [0]*self.n
		q = pow(2,self.d)
		lthash = LtHash(self.n,self.d)
		lthash.eval(m)
		self.digest = [sum(x)%q for x in zip(self.digest, lthash.digest)]

	def rem(self,lthash) -> None:
		assert lthash.n == self.n, "number of elements n has to be the same"
		assert lthash.d == self.d, "modulus q=2^d has to be the same"
		assert lthash.digest != [None]*lthash.n, "The subtracted hash has not been evaluated"
		assert self.digest != [None]*self.n, "The hash has not been evaluated"
		q = pow(2,self.d)
		digest_temp = [-x for x in lthash.digest]
		self.digest = [sum(x)%q for x in zip(self.digest, digest_temp)]

	def __h(self,xi) -> list[int]:
		#input: byte string
		#assert xi is a byte string

		lout = self.n * self.d
		lout_hash = math.ceil(lout/8)

		# Evaluating the XOF
		shake = SHAKE128.new(xi)

		# Format to a bitstring
		digest_hex = shake.read(lout_hash).hex()
		digest_bin = "{0:b}".format(int(digest_hex,16)).zfill(lout_hash*8)

		# Truncate
		digest_bin = digest_bin[:lout]

		# Format to a vector of n elements y \in Z_q
		h_out = [None]*self.n
		for i in range(self.n):
			h_out[i] = int(digest_bin[i*self.d:(i+1)*self.d],2)

		return h_out







