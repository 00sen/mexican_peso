import datetime as _dt
import hashlib as _hash
import json as _json

class Blockchain:
    
    def __init__(self) -> None:
        self.chain = list()
        
        genesis_block = self._create_block(data = "i am the genesis block", proof = 0, previous_hash = "0", index =0)
        
        self.chain.append(genesis_block)
        
    def mine_block(self, data: str) -> dict:
        previous_block = self.get_previous_block()
        previous_proof = previous_block["proof"]
        index = len(self.chain) + 1
        proof = self._proof_of_work(previous_proof, index, data)
        pass
    
    def _to_digest(self, new_proof: int, previous_proof: int, index: str, data: str) -> bytes:
        to_digest = str(new_proof ** 2 - previous_proof ** 2 + index ) + data
        return to_digest.encode()
        
    
    def _proof_of_work(self, previous_proof: str, index: int, data: str) -> int:
        new_proof = 1
        check_proof = False
        
        while not check_proof:
            print(new_proof)
            to_digest = self._to_digest(
                new_proof=new_proof,
                previous_proof=previous_proof, 
                index = index, 
                data = data)
            hash_value = _hash.sha256(to_digest).hexdigest()
            
            if hash_value[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1
        
        return new_proof
    
    def get_previous_block(self) -> dict:
        return self.chain[-1]
    
    def _create_block(self, data: str, proof: int, previous_hash: str, index: int
    ) -> dict:
        block = {
            "index": index,
            "timestamp" : str(_dt.datetime.now()),
            "data": data,
            "proof": proof,
            "previous_hash": previous_hash,
        }
        
        return block















"""
Genesis Block
{
    index: 0,
    timestamp: current time,
    data: "i am the genesis block"
    proof: 3,
    previous_hash: "0"
} -> hash() -> 2343aaa

{
    index: 1,
    timestamp: current time,
    data: "hello world",
    proof: 234234,
    previous_hash: 2343aaa
} -> hash() -> 98723ffe

{
    index: 2,
    timestamp: current time,
    data: "suscribe to rithmic",
    proof: 239487234,
    previous_hash: 98723ffe
}
"""