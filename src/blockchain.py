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
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.construct_genesis()


    def construct_gensis(self):
        # Constructs the initial block
        self.construct_block(proof_no=0, prev_hash=0)


    def construct_block(self):
        # Constructs a new block and adds it to the chain
        block = Block(
            index=len(self.chain),
            proof_no=proof_no,
            prev_hash=prev_hash,
            data=self.current_data
        )
        self.current_data = []

        self.chain.append(block)
        return block


    @staticmethod
    def check_validity(block, prev_block):
        # Checks whether the blockchain is valid
        if prev_block.index + 1 != block.index:
            return False
        elif prev_block.calculate_hash != block.prev_hash:
            return False
        elif not BlockChain.verifying_proof(block.proof_no, prev_block.proof_no):
            return False
        elif block.timestamp <= prev_block.timestamp:
            return False
        
        return True


    def new_data(self, sender, recipient, quantity):
        # Adds a new transaction to the data of the transactions
        self.current_data.append({
            'sender': sender,
            'recipient': recipient,
            'quantity': quantity
        })
        return True

    
    @staticmethod
    def proof_of_work(last_proof):
        # Protects the blockchain from attack
        proof_no = 0
        while BlockChain.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1
        return proof_no

    
    @staticmethod
    def verifying_proof(last_proof, proof):
        guess  = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'


    @property
    def last_block(self):
        # Returns the last block in the chain
        return self.chain[-1]
