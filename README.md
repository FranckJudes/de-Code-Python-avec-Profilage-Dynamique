# README : Code Python  Pylint avec Profilage Dynamique

Ce document explique comment analyser, corriger et rendre un code Python propre et conforme aux bonnes pratiques avec **Pylint**, ainsi que l’ajout du **profilage dynamique** pour mesurer les performances (temps d'exécution et consommation mémoire). Nous utiliserons les fichiers suivants :
1. `solve_quadratic.py` (Pylint)
2. `matrix_multiplication.py` (Profilage dynamique)

---

## **Prérequis**

1. **Python installé** : Assurez-vous que Python est installé sur votre système.
2. **Installation de Pylint** :
   ```bash
   pip install pylint
   ```
3. **Installation des outils de profilage** :
   - `memory_profiler` :
     ```bash
     pip install memory-profiler
     ```
   - `cProfile` : Inclus nativement avec Python.

---

## **Partie 1 : Correction avec Pylint**

### **Analyse initiale avec Pylint**

Lancez l'analyse Pylint sur le fichier cible. Par exemple :
```bash
pylint solve_quadratic.py
```
Pylint génère un rapport indiquant les erreurs de style, problèmes de conception, etc. 

Exemple :
```text
************* Module solve_quadratic
solve_quadratic.py:1:0: C0114: Missing module docstring (missing-module-docstring)
solve_quadratic.py:13:0: C0103: Variable name "coeff_a" doesn't conform to snake_case naming style (invalid-name)
...
```

### **Correction du Code**

1. **Ajout de docstrings**
   - Fournissez une documentation claire pour chaque module, fonction et classe.
2. **Renommage des variables**
   - Utilisez `snake_case` pour les noms de variables et de fonctions.
3. **Respect des lignes courtes**
   - Limitez les lignes à 80 caractères maximum.
4. **Suppression des redondances**
   - Combinez les fonctions similaires pour réduire la duplication.

### **Validation avec Pylint**

Exécutez à nouveau Pylint après les corrections :
```bash
pylint solve_quadratic.py
```

Une note proche de 10/10 confirme que le code est conforme.

---

## **Partie 2 : Profilage Dynamique**

Le profilage dynamique mesure les performances du code, comme le temps d'exécution et l'utilisation de la mémoire. Nous utilisons ici deux outils :
- `cProfile` pour profiler le temps d'exécution.
- `memory_profiler` pour analyser la consommation mémoire.

### **Configuration du Profilage**

1. **Ajout du profilage mémoire**
   - Utilisez le décorateur `@profile` pour les fonctions que vous souhaitez analyser.
   - Exemple :
     ```python
     from memory_profiler import profile

     @profile
     def multiply_matrices(matrix1, matrix2):
         return np.dot(matrix1, matrix2)
     ```

2. **Ajout du profilage du temps d'exécution**
   - Intégrez `cProfile` dans le fichier principal pour mesurer les performances :
     ```python
     import cProfile
     import pstats

     profiler = cProfile.Profile()
     profiler.enable()
     main()
     profiler.disable()

     stats = pstats.Stats(profiler)
     stats.strip_dirs()
     stats.sort_stats("time")
     stats.print_stats(10)
     ```

### **Exécution du Profilage**

1. **Profilage de la mémoire**
   - Exécutez le script avec `memory_profiler` :
     ```bash
     python -m memory_profiler matrix_multiplication.py
     ```

2. **Profilage du temps d'exécution**
   - Lancez simplement le script contenant `cProfile` :
     ```bash
     python matrix_multiplication.py
     ```

### **Exemple de Sorties**

1. **Sortie de `memory_profiler`** :
   ```text
   Line #    Mem usage    Increment  Occurrences   Line Contents
   -------------------------------------------------------------
       8     18.5 MiB     0.0 MiB           1   @profile
       9     18.6 MiB     0.1 MiB           1   def multiply_matrices(matrix1, matrix2):
      10     18.6 MiB     0.0 MiB           1       return np.dot(matrix1, matrix2)
   ```

2. **Sortie de `cProfile`** :
   ```text
         120 function calls in 0.005 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.004    0.004    0.005    0.005 matrix_multiplication.py:9(multiply_matrices)
   ```

---

## **Conclusion**

En combinant l'analyse statique avec Pylint et le profilage dynamique, vous pouvez :
- Améliorer la qualité du code.
- Identifier et corriger les problèmes de performance.
- Garantir un code propre, maintenable et performant.

N’oubliez pas d’intégrer ces outils dans vos processus de développement pour des résultats optimaux.

