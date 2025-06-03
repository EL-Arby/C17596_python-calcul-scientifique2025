import numpy as np

class SVM:
    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iters=1000):
        """
        SVM multi-classes (One-vs-Rest)
        
        Paramètres:
        learning_rate (float): Taux d'apprentissage
        lambda_param (float): Paramètre de régularisation
        n_iters (int): Nombre d'itérations d'entraînement
        """
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.models = []
        self.classes = []
    
    def _fit_binary(self, X, y):
        """Entraîne un classifieur binaire pour une classe spécifique"""
        n_samples, n_features = X.shape
        w = np.zeros(n_features)
        b = 0
        
        # Conversion des labels en [-1, 1]
        y_ = np.where(y == 1, 1, -1)
        
        # Descente de gradient vectorisée
        for _ in range(self.n_iters):
            linear_output = np.dot(X, w) - b
            condition = y_ * linear_output >= 1
            mask = (y_ * linear_output < 1).astype(float)
            
            # Calcul des gradients
            dw = 2 * self.lambda_param * w - np.dot(X.T, y_ * mask)
            db = np.sum(y_ * mask)
            
            # Mise à jour des paramètres
            w -= self.lr * dw
            b -= self.lr * db
        
        return w, b
    
    def fit(self, X, y):
        """Entraîne un classifieur par classe (One-vs-Rest)"""
        self.classes = np.unique(y)
        
        for cls in self.classes:
            # Créer des labels binaires pour la classe courante
            y_binary = np.where(y == cls, 1, 0)
            w, b = self._fit_binary(X, y_binary)
            self.models.append((w, b))
    
    def predict(self, X):
        """Prédit la classe pour chaque échantillon"""
        decision_scores = np.zeros((X.shape[0], len(self.classes)))
        
        # Calcul des scores de décision
        for i, (w, b) in enumerate(self.models):
            decision_scores[:, i] = np.dot(X, w) - b
        
        # Sélection de la classe avec le score le plus élevé
        return self.classes[np.argmax(decision_scores, axis=1)]
    
    def save(self, filename):
        """Sauvegarde le modèle dans un fichier .npy"""
        model_data = {
            'models': self.models,
            'classes': self.classes,
            'params': {
                'learning_rate': self.lr,
                'lambda_param': self.lambda_param,
                'n_iters': self.n_iters
            }
        }
        np.save(filename, model_data)
    
    @classmethod
    def load(cls, filename):
        """Charge un modèle depuis un fichier .npy"""
        data = np.load(filename, allow_pickle=True).item()
        svm = cls(
            learning_rate=data['params']['learning_rate'],
            lambda_param=data['params']['lambda_param'],
            n_iters=data['params']['n_iters']
        )
        svm.models = [tuple(model) for model in data['models']]
        svm.classes = data['classes']
        return svm

svm_model = SVM(learning_rate=0.001, lambda_param=0.01, n_iters=1000)
svm_model.fit(X_train, y_train)

# Sauvegarde dans le répertoire de travail
svm_model.save('/kaggle/working/svm_model.npy')
