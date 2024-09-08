class Solution:
        def numSquares(self, n: int) -> int:
            global_count = float('inf')
            def checkSquared(x : int) -> int:
                if x < 0:
                    return False
                z = int(x**0.5)
                return z * z == x
            
            def sumSquaredCheck(amount, count):
                if amount == 0:
                    return count
                
                min_count = float('inf')
                current_amount = amount
                while current_amount > 0:
                    if checkSquared(current_amount):
                        min_count = min(min_count, sumSquaredCheck(amount - current_amount, count + 1))
                    current_amount -= 1
                return min_count
            
            if n == 0:
                return 0
            
            i = n
            while i > 0:
                if checkSquared(i):
                    current_count = sumSquaredCheck(n, 0)
                    global_count = min(current_count, global_count)
                i -= 1
            return global_count

                    
