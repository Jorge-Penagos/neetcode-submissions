class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        '''
        Se usa un stack para poder visualizar el ultimo elemento del mismo, a su vez
        se usa un hash map para mapear los valores del parentesis cerrado con el parentesis abierto

        Ya que una vez que encontremos un parentesis cerrado debemos verificar que el anterior sea 
        su igual verificamos el ultimo elemento del stack haciendo match con su par, si es correcto
        se hace pop y se continua ya sea agregando abiertos o comparando cerrados
        El stack al final debe quedar vacio para regresar True
        '''
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False