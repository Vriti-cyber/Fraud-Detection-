import hashlib  
import json   
import time   

class Block:
    """
    A Block is like one page in a diary. Each page contains:
    - Page number (index)
    - When it was written (timestamp)
    - What happened (data - like "Client 1 updated the model")
    - A fingerprint of the previous page (previous_hash)
    - Its own unique fingerprint (hash)
    """
    
    def __init__(self, index, data, previous_hash):
     
        self.index = index                  
        self.timestamp = time.time()         
        self.data = data                      
        self.previous_hash = previous_hash    
        self.hash = self.calculate_hash()    
        
        print(f"Created Block {index}: '{data}'")
    
    def calculate_hash(self):
        """
        This creates a unique fingerprint for this block.
        Think of it like a snowflake - no two are exactly the same!
        Even changing ONE letter in the data would create a completely different fingerprint.
        """

        block_contents = json.dumps(self.__dict__, sort_keys=True).encode()
        
  
        fingerprint = hashlib.sha256(block_contents).hexdigest()
        
        return fingerprint


class Blockchain:
    """
    A Blockchain is like a special diary where:
    - Each page is connected to the one before it
    - If someone tries to change an old page, all the fingerprints would break
    - Everyone can see the diary, but nobody can secretly change it
    """
    
    def __init__(self):
        print("\nCreating a new blockchain diary...")
        
       
        self.chain = [self.create_genesis_block()]
        
        print("Blockchain diary is ready!")
    
    def create_genesis_block(self):
        """
        The Genesis Block is the very first block in the chain.
        It's special because it has no previous block to point to.
        Like the first page of a diary - nothing came before it!
        """
        print("   Creating Genesis Block (the first page)...")
        return Block(0, "Genesis Block - The Beginning", "0") 
    
    def add_block(self, data):
        """
        Adding a new block is like writing a new page in your diary:
        1. Look at the last page you wrote
        2. Create a new page with today's date and what happened
        3. Include the fingerprint of the previous page
        4. Add it to the diary
        """
        print(f"\nAdding new entry to the blockchain...")
        
       
        previous_block = self.chain[-1]
        
        
        new_block = Block(len(self.chain), data, previous_block.hash)
        
     
        self.chain.append(new_block)
        
        print(f"Successfully added Block {new_block.index}")
    
    def display_chain(self):
        """
        This shows everything in our blockchain diary.
        It's like opening the diary and reading all the pages in order.
        """
        print("\n" + "="*50)
        print("THE COMPLETE BLOCKCHAIN DIARY")
        print("="*50)
        
        for block in self.chain:
            print("\n" + "-"*40)
            print(f"BLOCK #{block.index}")
            print("-"*40)
            print(f"   When:     {time.ctime(block.timestamp)}")
            print(f"   What:     {block.data}")
            print(f"   Previous: {block.previous_hash[:15]}... (shortened)")
            print(f"   This Hash: {block.hash[:15]}... (shortened)")
        
        print("\n" + "="*50)
        print("Notice how each block contains the previous block's fingerprint?")
        print("That's what makes it a CHAIN!")
        print("="*50)


if __name__ == "__main__":
    
    print("\n" + "*"*50)
    print("DEMONSTRATING OUR BLOCKCHAIN")
    print("*"*50)
    

    print("\nSTEP 1: Creating a new blockchain...")
    my_diary = Blockchain()
    

    print("\nSTEP 2: Adding some entries...")
    my_diary.add_block("Client 1: Updated AI model with new data")
    my_diary.add_block("Client 2: Added security patch for fraud detection")
    my_diary.add_block("Client 3: Improved accuracy by 2.5%")
    

    print("\nSTEP 3: Let's look at our complete blockchain diary:")
    my_diary.display_chain()
    
  
    print("\n" + "="*50)
    print("WHY THIS IS SECURE (The Magic Part!)")
    print("="*50)
    print("""
    Imagine someone tries to cheat by changing Block #1's data.
    
    Here's what happens:
    1. Changing the data changes Block #1's fingerprint (hash)
    2. But Block #2 STILL has the OLD fingerprint stored!
    3. Now Block #1 and Block #2 don't match anymore
    4. Everyone would know something was tampered with!
    
    To hide the change, they'd have to recalculate ALL fingerprints
    for every single block after it. That's impossible to do secretly!
    
    This is why blockchain is called "immutable" - once something is
    recorded, it can never be changed without everyone noticing!
    """)
    
    print("\nAnd that's how a blockchain works! Simple, right?")