# https://www.freecodecamp.org/news/create-cryptocurrency-using-python/
import hashlib
import time


class Block:
    def __init__(self):
        # First block class
        pass
  
  
    def calculate_hash():
        # Calculates the cryptographic hash of every block
        pass


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
