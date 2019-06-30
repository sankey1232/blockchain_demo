# Demo of a simple blockchain
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1- Blockchain architecture
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

    def create_block(self, proof, previous_hash):
        block={'index':len(self.chain)+1,
               'timestamp':str(datetime.datetime.now()),
               'proof':proof,
               'previous_hash':previous_hash}
        self.chain.append(block)
        return block

    '''Returns the end block of the current chain which acts as
        a previous block for the block to be added'''
    def get_previous_block(self): 
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_generation = hashlib.sha256(str(new_proof**2-previous_proof**2).encode()).hexdigest()
            if hash_generation[:4]=='0000':
                check_proof = True
            else:
                new_proof+=1
        return new_proof
    
    def generate_hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        hash = hashlib.sha256(encoded_block).hexdigest()
        return hash

    def chain_validation(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.generate_hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_generation = hashlib.sha256(str(proof**2-previous_proof**2).encode()).hexdigest()
            if hash_generation[:4] != '0000':
                return False
            previous_block = block
            block_index+=1
        return True

# Part 2- Interactive web interface for blockchain
app = Flask(__name__)
bc = Blockchain()
    
# Mining a new block
@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = bc.get_previous_block()
    previous_proof = previous_block['proof']
    proof = bc.proof_of_work(previous_proof)
    previous_hash = bc.generate_hash(previous_block)
    block = bc.create_block(proof, previous_hash)
    response = {'Message': 'Congratulations, you just mined a new block!',
                'index':block['index'],
                'timestamp':block['timestamp'],
                'proof':block['proof'],
                'previous_hash':block['previous_hash']}
    return jsonify(response), 200

# Displaying the whole blockchain
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response={'chain':bc.chain, 'length':len(bc.chain)}
    return jsonify(response), 200

# Checking if the blockchain is valid
@app.route('/is_valid', methods=['GET'])
def is_valid():
    validity = bc.chain_validation(bc.chain)
    if validity:
        response = {'Message':'The blockchain is valid'}
    else:
        response = {'Message':'There are problems in the blockchain'}
    return jsonify(response), 200



    