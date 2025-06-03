# README.ipynb - Documentation du projet

"""
# 🧠 Mini-Projet : Classification de texte 

Ce notebook contient la documentation du projet de classification de texte en 3 catégories (pos, neg, neutr) en utilisant un modèle SVM codé manuellement (sans scikit-learn). et

* Des techniques de prétraitement de texte (nettoyage, tokenisation, TF-IDF).

L’ensemble du code est écrit en Python, sans recourir à scikit-learn pour la partie SVM.

## 📁 Structure du Dépôt

```
.
├── code/                          # Contient le code source Python
│   └── svm_model.py              # Implémentation manuelle d'un SVM
│
├── notebooks/                    # Contient les notebooks Jupyter
│   └── text_classification.ipynb # Notebook de classification utilisant svm_model.py
│
├── FD_2025/                      # Ressources pédagogiques (PDF)
│   ├── Chap 2 ACP.pdf
│   ├── FD_PCS_2025.pdf
│   ├── TD 2 ACP.pdf
│   └── TD_TP¨_FD_2025.pdf
│
├── README.ipynb                  # Ce notebook de documentation
```

## 🚀 Utilisation

1. S'assurer que Python est installé avec `numpy` et `pandas` :
```bash
pip install numpy pandas
```

2. Exécuter le notebook `notebooks/text_classification.ipynb`.

3. Le notebook :
   - Charge les données texte à classer
   - Effectue le prétraitement
   - Importe le modèle `svm_model.py` depuis `code/`
   - Entraîne et évalue la classification pour 3 catégories : **pos**, **neg**, **neutr**





* **`data/dataset.csv`**
  Fichier CSV avec au minimum deux colonnes obligatoires :

  * `text` : chaîne de caractères à classifier.
  * `label` : étiquette associée (ex. `pos`, `neg`, `neutr`).



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


## 5. Utilisation

### 5.1. Exécuter le notebook d’entraînement

1. **Lancer Jupyter Notebook**

   ```bash
   jupyter notebook

## 6. Détails techniques

### 6.1. Prétraitement de texte

* **`tokenize(text)`** :

  * Remplace tout caractère non alphanumérique par un espace.
  * Sépare sur les espaces et retourne la liste des tokens non vides.
* **`Stemming(text)`** :
* * **`Stopwords(text)`** :

---

**Licence MIT**
Ce projet est mis à disposition sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
