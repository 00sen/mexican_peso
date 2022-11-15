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