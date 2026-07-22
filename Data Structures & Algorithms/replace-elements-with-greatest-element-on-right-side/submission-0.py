class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # se usa range para poder trabajar con los indices ya que si uso arr estoy trabajando con los valores de la lista 
        for i in range(len(arr)):  
        # Se inicializa el valor en -1 dentro del loop para resetarlo siempre a -1 en caso de que sea el ultimo elemento de la lista
            h_val = -1
        # Se utiliza range(i + 1, len(arr)) en vez de arr[1:] para que no se comience siempre desde el segundo elemento de la lista, de esta forma siempre empezaremos a la derecha del valor que estamos viendo
            for j in range(i + 1, len(arr)):
        # se compara si el valor mas alto es menos que el valor del indice que estamos viendo
                if h_val < arr[j]:
        # si es mas alto actualizamos el valor mas alto
                    h_val = arr[j]
        # se actualiza el valor del indice que se esta iterando por el valor mas alto encontrado en el segundo for
            arr[i] = h_val

        return arr