# https://www.freecodecamp.org/news/create-cryptocurrency-using-python/
import hashlib
import time


class Block:
    def __init__(self, index, proof_no, prev_hash, data, timestamp=None):
        # Constructor Method
        self.index = index
        self.proof_no = proof_no
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp or time.time()


    @property
    def calculate_hash(self):
        # Constructs the initial block
        block_of_string = f"{self.index}{self.proof_no}{self.prev_hash}{self.data}{self.timestamp}"
        return hashlib.sha256(block_of_string.encode()).hexdigest()


    def __repr__(self):
        # Constructs a new block and adds it to the chain
        return f"{self.index}-{self.proof_no}-{self.prev_hash}-{self.data}-{self.timestamp}"


class BlockChain():
    def __init__(self):
        # Constructor Method
        pass


    def construct_gensis(self):
        # Constructs the initial block
        pass


    def construct_block(self):
        # Constructs a new block and adds it to the chain
        pass


    @staticmethod
    def check_validity():
        # Checks whether the blockchain is valid
        pass


    def new_data(self, sender, recipient, quantity):
        # Adds a new transaction to the data of the transactions
        pass

    
    @staticmethod
    def contruct_proof_of_work(prev_proof):
        # Protects the blockchain from attack
        pass


    @property
    def last_block(self):
        # Returns the last block in the chain
        return self.chain[-1]
