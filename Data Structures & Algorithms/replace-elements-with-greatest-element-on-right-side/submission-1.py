class Solution:
    '''
    Esta solucion trata de suffix max como solucion

    Este se presenta de la siguiente forma:
    1 se empieza desde el ultimo elemento siempre y se fija una lista de apoyo con el mismo tamaño
        que la lista que recibimos pero llena de 0s
    2 se tiene que guardar siempre el ultimo valor mas alto visto y se inicializa en -1, al ser el ultimo
        elemento de la lista cumple con la condicion de dejar -1 al final siempre
    3 al tener que empezar por el ultimo elemento de la lista siempre compara el indice anterior con 
    el valor maximo visto, se coloca el numero mayor visto en la posicion actual y ademas 
    si es mayor se actualiza el ultimo valor visto con el nuevo valor para la siguiente iteracion

    [1 , 2, 3, 3, 5, 2]

    empieza por 2 y asigna -1 al valor y el max visto es 2
    pasa a ver el numero 5 asigna el numero 2 y actualiza el max visto a 5
    pasa al numero 3 y asigna el numero 5 y no actualiza ya que es menor que 5
    y esta es la iteracion que se realiza siempre, evitando escanear 2 veces el arreglo como se hizo
    en el que yo realice 
    
    '''
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        rightMax = -1
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans