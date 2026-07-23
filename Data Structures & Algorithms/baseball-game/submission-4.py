class Solution:
    def calPoints(self, operations: List[str]) -> int:
        '''
        De esta forma evitamos tener que hacer operaciones adicionales en cada if que encontremos
        Ya que el sum(stack) se encargara de la suma del resultado al final
        Ambas formas son correctas en las soluciones del problema 
        '''
        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)