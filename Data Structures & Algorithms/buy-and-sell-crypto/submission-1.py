class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = float("inf")

        for sell in prices:
            maxP = max(maxP, sell - minBuy)   # mejor ganancia si vendo hoy
            minBuy = min(minBuy, sell)        # actualizo mejor día de compra
        return maxP
