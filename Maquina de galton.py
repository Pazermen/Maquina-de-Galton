import random
import matplotlib.pyplot as plt

def calcular_canicas(num_canicas, num_niveles):
    """
    Simula el recorrido de canicas en una máquina de Galton.

    Args:
        num_canicas (int): Número de canicas a simular.
        num_niveles (int): Número de niveles de obstáculos.

    Returns:
        list: Lista con la cantidad de canicas en cada contenedor.
    """
    # Inicializar una lista para contar las canicas en cada contenedor
    resultados = [0] * (num_niveles + 1)
    
    for _ in range(num_canicas):
        der = 0  # Contador de decisiones a la derecha
        for _ in range(num_niveles):
            if random.choice(['izquierda', 'derecha']) == 'derecha':
                der += 1
        resultados[der] += 1
    
    return resultados

def graficar_histograma(resultados):
    """
    Grafica un histograma de los resultados de la simulación.

    Args:
        resultados (list): Lista con la cantidad de canicas en cada contenedor.
    """
    niveles = list(range(len(resultados)))
    
    plt.figure(figsize=(10,6))
    plt.bar(niveles, resultados, color='skyblue', edgecolor='black')
    
    plt.title('Distribución de Canicas en la Máquina de Galton')
    plt.xlabel('Número de Decisiones a la Derecha')
    plt.ylabel('Cantidad de Canicas')
    plt.xticks(niveles)  # Asegura que cada contenedor esté etiquetado
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def main():
    num_canicas = 3000
    num_niveles = 12
    
    # Calcular los resultados de la simulación
    resultados = calcular_canicas(num_canicas, num_niveles)
    
    # Graficar el histograma de los resultados
    graficar_histograma(resultados)

if __name__ == "__main__":
    main()