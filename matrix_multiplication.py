"""
Module pour résoudre une équation du second degré de la forme ax² + bx + c = 0,
avec profilage de mémoire et de temps d'exécution.
"""
from memory_profiler import profile
import cProfile
import pstats
import numpy as np



@profile
def multiply_matrices(matrix1, matrix2):
    """
    Multiplie deux matrices.
    """
    return np.dot(matrix1, matrix2)

def main():
   
    MATRIX_1 = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    MATRIX_2 = np.array([
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ])
    print("Multiplication des matrices...")
    result = multiply_matrices(MATRIX_1, MATRIX_2)
    print(result)

if __name__ == "__main__":
    # Utilisation de cProfile pour profiler la fonction main
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()

    # Génération des statistiques de profilage
    stats = pstats.Stats(profiler)
    stats.strip_dirs()  # Nettoie les chemins des fichiers dans le rapport
    stats.sort_stats("time")  # Trie par temps d'exécution
    stats.print_stats(10)  # Affiche les 10 premières entrées
