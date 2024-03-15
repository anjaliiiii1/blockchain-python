import hashlib

# Function to generate a SHA-256 hash for given data
def hashgenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

# Block class to represent individual blocks in the blockchain
class Block:
    def __init__(self, data, block_hash, prev_hash):

        self.data = data          # Data stored in the block

        self.block_hash = block_hash  # Hash of this block

        self.prev_hash = prev_hash    # Hash of the previous block

# Blockchain class to manage the chain of blocks
class Blockchain:

    def __init__(self):

        # Generate hashes for the start and last blocks
        hashlast = hashgenerator('gen_last')
        hashstart = hashgenerator('gen_hash')

        # Create the genesis block
        genesis = Block('gen_data_Anjali', hashstart, hashlast)
        self.chain = [genesis]  # Initialize the blockchain with the genesis block

    # Method to add a new block to the blockchain
    def add_block(self, data):

        prev_hash = self.chain[-1].block_hash  # Get the hash of the last block

        # Generate hash for the new block by combining data and previous hash
        block_hash = hashgenerator(data + ":" + prev_hash)

        # Create the new block
        block = Block(data, block_hash, prev_hash)

        # Append the new block to the chain
        self.chain.append(block)

# Create an instance of the Blockchain
bc = Blockchain()

# Add some blocks to the blockchain
bc.add_block('1')
bc.add_block('2')
bc.add_block('3')

# Print out the details of each block in the blockchain
for block in bc.chain:

    print(block.__dict__)  # Print the attributes of each block
