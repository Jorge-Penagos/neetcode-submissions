class Solution:
    def encode(self, strs: List[str]) -> str:
        res = b""
        for s in strs:
            data = s.encode("utf-8")
            res += len(data).to_bytes(4, "big") + data
        return res.decode("latin1")  # guardar como string

    def decode(self, s: str) -> List[str]:
        res, bts = [], s.encode("latin1")
        i = 0
        while i < len(bts):
            length = int.from_bytes(bts[i:i+4], "big")
            i += 4
            res.append(bts[i:i+length].decode("utf-8"))
            i += length
        return res
