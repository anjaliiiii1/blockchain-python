Basic Blockchain in Python
This project provides a simple implementation of a blockchain in Python. It demonstrates the core concepts behind blockchain technology including hashing, blocks, and linking blocks using previous hashes.

Features
Generates SHA-256 hashes for block data

Includes a genesis block

Dynamically adds new blocks to the blockchain

Maintains the chain using previous block hashes

File Structure
hashgenerator(data): A function to generate SHA-256 hash for a given input string.

Block class: Represents a single block in the blockchain.

Blockchain class: Manages the chain of blocks and provides methods to add new blocks.

How It Works
The Blockchain class initializes with a genesis block containing predefined data and hashes.

New blocks can be added using the add_block(data) method.

Each new block stores:

The data passed to it

Its own hash (computed using the data and previous block's hash)

The hash of the previous block
