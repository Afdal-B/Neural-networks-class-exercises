
from numpy import array, dot, random
import matplotlib.pyplot as plt

################################### La classe perceptron ####################################### 

# La fonction d'activation 
f_activation = lambda x: 0 if x < 0 else 1

class Perceptron:
    def __init__(self) -> None:
        self.w = random.rand(3)
        self.eta = 0.2
        self.fig, self.ax = plt.subplots()
        self.data = None
    
    # Une methode pour entrainer notre perceptron 
    def fit(self, exemples):
        self.data = exemples
        i = 0
        # Les erreurs d'une époque 
        epochs_erreur = []
        epochs_count = 0
        while True:
            x, d = exemples[i % 4]
            # Calculons S
            s = f_activation(dot(x, self.w))
            erreur = d - s
            epochs_erreur.append(erreur)
            # On sauvegarde le vecteur poids avant de le modifier
            self.w_prec = self.w
            self.w = self.w + self.eta * erreur * x
            i += 1           
            # Tracer les points
            for x, d in exemples:
                if d == 0:
                    self.ax.plot(x[0], x[1], 'ro')  # points rouges pour la classe 0
                else:
                    self.ax.plot(x[0], x[1], 'bo')  # points bleus pour la classe 1
            
            
            self.showhyperplan()
             # Si nous sommes à la fin d'une époque
            if (i % 4 == 0):
                epochs_count += 1
                
                print(f"époque numéro {epochs_count} \t nombre d'erreurs {4 - epochs_erreur.count(0)}")
                # Si il n'y a aucune erreur, on arrête 
                if((array(epochs_erreur) == array([0,0,0,0])).all()):
                    break
                else:
                    epochs_erreur = []
        plt.show()

    def predict(self, x1, x2):
        inputs = array([x1, x2, 1]) 
        prediction = f_activation(dot(inputs, self.w))
        return prediction

    def showEquation(self):
        #w1x1 + w2x2 + w3 = 0 
        return f"L'équation de la droite est ({self.w[0]}X1 + {self.w[1]}X2 + {self.w[2]} = 0)"
    
    def showhyperplan(self,trainning = True):
        x = [-1, 2]
        y = [(-self.w[2] / self.w[1]) - ((self.w[0] / self.w[1]) * i) for i in x]
        self.ax.set_xlim(-0.25, 1.25)
        self.ax.set_ylim(-0.25, 1.25)
        self.ax.set_title("Tracé successif des hyperplans séparateurs")
        self.ax.plot(x, y)

        if(not trainning):
            plt.show()
    
    def showHyperplanSeparateur(self):
        x = [-1,2]
        y = [(-self.w[2] / self.w[1]) - ((self.w[0] / self.w[1]) * i) for i in x]
        _, ax = plt.subplots()
        for z, d in self.data:
            if d == 0:
                ax.plot(z[0], z[1], 'ro')  # points rouges pour la classe 0
            else:
                ax.plot(z[0], z[1], 'bo')  # points bleus pour la classe 1
        ax.set_xlim(-0.25, 1.25)
        ax.set_ylim(-0.25, 1.25)
        ax.plot(x, y)
        ax.set_title("Tracé de l'hyperplan séparateur")
        plt.show()