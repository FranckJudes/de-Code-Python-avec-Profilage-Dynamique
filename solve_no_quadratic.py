from memory_profiler import profile
import cProfile
import pstats
import numpy as np


@profile
def multiply_matrices_manual(matrix1, matrix2):
    """
    Multiplie deux matrices manuellement (sans NumPy).
    """
    size = len(matrix1)
    result = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

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

    # Multiplication des matrices
    print("Multiplication des matrices...")
    result = multiply_matrices_manual(MATRIX_1, MATRIX_2)
    print(result)
    print("Multiplication terminée.")

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
