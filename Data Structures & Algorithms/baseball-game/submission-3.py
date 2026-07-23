class Solution:
    def calPoints(self, operations: List[str]) -> int:
        '''
        + suma de los dos valores previos
        C se invalida el ultimo score (pop del stack)
        D se duplica el valor anterior y se agrega como score al stack
        INT se agrega como score al stack
        '''
        stack = []
        ans = 0
        for score in operations:
            '''
            Aqui no podemos hacer stack[-1] + stack[-2] nuevamente
            como lo estaba haciendo ya que seria reduplicar el valor 
            ya que el ultimo valor del stack ya tiene el resultado 
            esperado por eso solo lo consultamos, mismo caso para el caso D
            '''
            # Caso +
            if score == '+':
                stack.append(stack[-1] + stack[-2])
                ans += stack[-1]
            
            # Caso D
            elif score == "D":
                stack.append(stack[-1] * 2)
                ans += stack[-1]
                
            # Caso C
            elif score == "C":
                ans -= stack[-1]
                stack.pop()

            # Caso INT
            else:
                val = int(score)
                stack.append(val)
                ans += val

        return ans