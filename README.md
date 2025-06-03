# Mini-projet : Classification de textes avec SVM

## 1. Présentation

Ce mini-projet a pour objectif de démontrer un pipeline complet de classification de textes en trois catégories (positif / négatif / neutre) en utilisant :

* Des techniques de prétraitement de texte (nettoyage, tokenisation, TF-IDF).
* Un algorithme de SVM linéaire implémenté « à la main ».
* Un découpage en plusieurs notebooks pour séparer la définition du modèle, le développement en cours et la phase d’entraînement / évaluation.

L’ensemble du code est écrit en Python, sans recourir à scikit-learn pour la partie SVM.

## 2. Structure du dépôt

```
.
├── README.md
├── code/
│   └── svm_model.py
├── data/
│   └── dataset.csv
└── notebooks/
    ├── encours.ipynb             # Notebook en cours de développement
    ├── text_classification.ipynb # Notebook d’entraînement et d’évaluation
    └── results.pdf               # Export PDF des résultats
```

* **`code/svm_model.py`**
  Module contenant :

  1. La fonction `tokenize(text)` pour nettoyer et découper le texte en tokens.
  2. `build_vocabulary(texts, max_features)` et `compute_tf_idf(texts, vocab)` : construction du vocabulaire et calcul TF-IDF (forme creuse sous forme de dictionnaires).
  3. La classe `LinearSVM` (implémentation Pegasos pour SVM binaire).
  4. Les fonctions `train_svm(texts, labels, max_features, C, max_iter)` et `predict_svm(models, vocab, idf, texts)` pour l’entraînement multiclasses (one-vs-rest) et la prédiction.

* **`data/dataset.csv`**
  Fichier CSV avec au minimum deux colonnes obligatoires :

  * `text` : chaîne de caractères à classifier.
  * `label` : étiquette associée (ex. `pos`, `neg`, `neutr`).

 

* **`notebooks/encours.ipynb`**
  Notebook en cours de développement, rassemblant les expérimentations initiales, les idées de prétraitement avancé et les notes sur l’implémentation du modèle. À utiliser pour prototyper de nouvelles fonctionnalités avant de les intégrer dans le notebook principal.

* **`notebooks/text_classification.ipynb`**
  Notebook principal d’expérimentation, qui :

  1. Exécute en première cellule :

     ```python
     %run ../code/svm_model.py
     ```

     pour importer toutes les définitions (`tokenize`, `train_svm`, `predict_svm`, etc.).
  2. Importe `pandas`, `random` et `Counter` pour gérer le dataset et l’évaluation.
  3. Charge `data/dataset.csv`, mélange aléatoirement et sépare en jeu d’entraînement (80 %) et jeu de test (20 %).
  4. Appelle `train_svm(texts_train, labels_train, max_features=5000, C=1.0, max_iter=5000)` pour obtenir :

     * `models` (dictionnaire de trois objets `LinearSVM`).
     * `idf` (dictionnaire indice→valeur idf).
  5. Appelle `predict_svm(models, vocab, idf, texts_test)` pour générer les prédictions.
  6. Calcule manuellement l’accuracy, la matrice de confusion et un rapport de classification (précision / rappel / F1-score / support) sans scikit-learn.
  

* **`notebooks/results.pdf`**
  Export PDF du notebook `text_classification.ipynb` montrant :

  * La répartition des labels dans le dataset.
  * Les tailles respectives des jeux train/test.
  * L’accuracy finale.
  * La matrice de confusion.
  * Le rapport de classification pour chaque classe.


## 3. Prérequis

* **Python 3.7+**
* Bibliothèques Python :

  * `pandas` (pour charger et manipuler le dataset)
  * `numpy` (optionnel, si vous souhaitez étendre ou tracer des graphes)
* Aucune dépendance à scikit-learn : tout le code SVM est implémenté “à la main” dans `svm_model.py`.

## 4. Installation et configuration

1. **Cloner le dépôt GitHub**

   ```bash
   git clone https://github.com/EL-Arby/C17596_python-calcul-scientifique2025.git
   cd C17596_python-calcul-scientifique2025
   ```

2. **Créer un environnement virtuel (fortement recommandé)**

   ```bash
   python -m venv venv
   ```

   * Sous Linux/macOS :

     ```bash
     source venv/bin/activate
     ```
   * Sous Windows (PowerShell) :

     ```powershell
     .\venv\Scripts\Activate.ps1
     ```

3. **Installer les dépendances**

   ```bash
   pip install pandas
   ```

   (Si vous souhaitez utiliser NumPy ou Matplotlib pour vos propres extensions, installez-les également.)

4. **Vérifier la structure du dépôt**

   ```
   .
   ├── README.md
   ├── code/
   │   └── svm_model.py
   ├── data/
   │   └── dataset.csv
   └── notebooks/
       ├── encours.ipynb
       ├── text_classification.ipynb
       └── results.pdf
   ```

## 5. Utilisation

### 5.1. Exécuter le notebook d’entraînement

1. **Lancer Jupyter Notebook**

   ```bash
   jupyter notebook


### 5.2. Utilisation du notebook en cours (`encours.ipynb`)

* **`notebooks/encours.ipynb`** est dédié aux expérimentations initiales et aux idées de prétraitement avancé.
* On y teste notamment :

  * Le nettoyage de tokens (stop-words, lemmatisation).
  * L’ajout d’ngrams (bi-grams/tri-grams) dans le TF-IDF.
  * Des variantes d’algorithmes (régression logistique, Naïve Bayes).
* Une fois validées, ces nouveautés pourront être intégrées dans le notebook principal (`text_classification.ipynb`).

### 5.3. Lecture du rapport PDF

* Ouvrez `notebooks/results.pdf` pour consulter les tableaux et graphiques générés lors de l’exécution du notebook `text_classification.ipynb`.

## 6. Détails techniques

### 6.1. Prétraitement de texte

* **`tokenize(text)`** :

  * Met la chaîne en minuscules.
  * Remplace tout caractère non alphanumérique par un espace.
  * Sépare sur les espaces et retourne la liste des tokens non vides.

* **`build_vocabulary(texts, max_features)`** :

  * Calcule la fréquence de document (nombre de documents contenant chaque token).
  * Construit un vocabulaire limité aux `max_features` tokens les plus fréquents (par fréquence de document).


## 7. Extensions possibles

1. **Modifier le paramètre `max_features`** dans `train_svm` pour explorer l’impact de la taille du vocabulaire.
2. **Intégrer des n-grams** (bi-grams, tri-grams) dans le calcul TF-IDF.
3. **Ajouter un module de nettoyage plus avancé** :

   * Suppression des stop-words (via liste personnalisée).
   * Lemmatisation ou stemming (spaCy, NLTK).


## 8. Auteur

**EL-Arby**
Miniproject réalisé dans le cadre du cours “Python pour le calcul scientifique” (année 2025).

---

**Licence MIT**
Ce projet est mis à disposition sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
