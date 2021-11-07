import time
from blocks import Block
import h5py
from db.hdf5db import *

class Blockchain:
    def __init__(self):
        self.unconfirmed_transactions = []
        #self.chain = view_db().tolist()
        self.chain = []
        self.create_genesis_block()
        self.difficulty = 2

    def create_genesis_block(self):
        genesis_block = Block(0,[],time.time(),"0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]



    def proof_of_work(self,block):

        # start with 0 nonce
        block.nonce = 0
        # compute the hash with the given nonce
        computed_hash = block.compute_hash()

        # check whether the hash has the needed number of leading 0's
        while not computed_hash.startswith('0'* self.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        # return the computed hash if it does
        return computed_hash

    def add_block(self, block, proof):
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        if proof: # if trasanction is valid
            self.chain.append(block)
            #add_block_to_db(block.transactions)

        return True

    def is_valid_proof(self,block, block_hash):
        return (block_hash.startswith("0"* self.difficulty)
                and block_hash == block.compute_hash())

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(
            index = last_block.index + 1,
            transactions = self.unconfirmed_transactions,
            timestamp = time.time(),
            previous_hash = last_block.hash
        )

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []

        return new_block.index
