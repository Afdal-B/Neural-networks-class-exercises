from numpy import array
#!/usr/bin/env python
# -*- coding: utf-8 -*-
N = 5 # nombre de lignes (et de colonnes) d'une forme

N_cell = N*N

# états des cellules du réseau (booléens)
#etats = [ False for _ in range(N_cell) ]

# seuils des cellules du réseau (réels)
seuils = [ 0.0 for _ in range(N_cell) ]

# poids des connexions du réseau (réels)
poids = [ [ 0.5 if i != j else 0.0 for j in range(N_cell)] for i in range(N_cell) ]

exemple_a_reconnaitre = [ [True,  False, True,  False, True],
                          [True,  True,  False, False, True],
                          [False, False, True,  False, True],
                          [True,  False, False, True,  True],
                          [True, False, False, False, True] ]

alphabet = \
[ [ [False, True,  True,  True,  False],  # { A }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  True],
     [True,  False, False, False, True],
     [True,  False, False, False, True] ],
   [ [True,  True,  True,  True,  False],  # { B }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False],
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False] ],
   [ [False, True,  True,  True,  True],   # { C }
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [False, True,  True,  True,  True] ],
   [ [True,  True,  True,  True,  False],  # { D }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False] ],
   [ [True,  True,  True,  True,  True],   # { E }
     [True,  False, False, False, False],
     [True,  True,  True,  False, False],
     [True,  False, False, False, False],
     [True,  True,  True,  True,  True] ],
   [ [True,  True,  True,  True,  True],   # { F }
     [True,  False, False, False, False],
     [True,  True,  True,  False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, False] ],
   [ [True,  True,  True,  True,  True],   # { G }
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, True],
     [True,  True,  True,  True,  True] ],
   [ [True,  False, False, False, True],   # { H }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  True],
     [True,  False, False, False, True],
     [True,  False, False, False, True] ],
   [ [False, False, True,  False, False],  # { I }
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False] ],
   [ [False, False, True,  True,  True],   # { J }
     [False, False, False, True,  False],
     [False, False, False, True,  False],
     [False, False, False, True,  False],
     [True,  True,  True,  True,  False] ],
   [ [True,  False, False, False, True],   # { K }
     [True,  False, False, True,  False],
     [True,  True,  True,  False, False],
     [True,  False, False, True,  False],
     [True,  False, False, False, True] ],
   [ [True,  False, False, False, False],  # { L }
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  True,  True,  True,  True] ],
   [ [True,  True,  False, True,  True],   # { N }
     [True,  False, True,  False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True] ],
   [ [True,  False, False, False, True],   # { M }
     [True,  True,  False, False, True],
     [True,  False, True,  False, True],
     [True,  False, False, True,  True],
     [True,  False, False, False, True] ],
   [ [False, True,  True,  True,  False],  # { O }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [False, True,  True,  True,  False] ],
   [ [True,  True,  True,  True,  False],  # { P }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False],
     [True,  False, False, False, False],
     [True,  False, False, False, False] ],
   [ [True,  True,  True,  True,  True],   # { Q }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, True,  True],
     [True,  True,  True,  True,  True] ],
   [ [True,  True,  True,  True,  False],  # { R }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False],
     [True,  False, False, True,  False],
     [True,  False, False, False, True] ],
   [ [False, True,  True,  True,  True],   # { S }
     [True,  False, False, False, False],
     [False, True,  True,  True,  False],
     [False, False, False, False, True],
     [True,  True,  True,  True,  False] ],
   [ [True,  True,  True,  True,  True],   # { T }
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False] ],
   [ [True,  False, False, False, True],   # { U }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [False, True,  True,  True,  False] ],
   [ [True,  False, False, False, True],   # { V }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [False, True,  False, True,  False],
     [False, False, True,  False, False] ],
   [ [True,  False, False, False, True],   # { W }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, True,  False, True],
     [False, True,  False, True,  False] ],
   [ [True,  False, False, False, True],   # { X }
     [False, True,  False, True,  False],
     [False, False, True,  False, False],
     [False, True,  False, True,  False],
     [True,  False, False, False, True] ],
   [ [True,  False, False, False, True],   # { Y }
     [False, True,  False, True,  False],
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False] ],
   [ [True,  True,  True,  True,  True],   # { Z }
     [False, False, False, True,  False],
     [False, False, True,  False, False],
     [False, True,  False, False, False],
     [True,  True,  True,  True,  True] ] ]


lettre = list(alphabet[0])


class ReseauRecurrent():
    def __init__(self,poids,seuils) -> None:
        self.poids =  poids
        self.seuils = seuils
        self.n_cell = len(self.poids)
    
    def toOneline(self,liste):
        oneLine=[]
        for i in range(len(liste)):
            oneLine+= liste[i]
        return oneLine
    
    def fit_on_one_alphabet(self,alphabet):
        #On transfome etats alphabet en une liste d'une ligne
        etats = self.toOneline(alphabet)
        error_count = 0
        for i in range (self.n_cell):
          s = 0
          for j in range(self.n_cell):
              
              s+= self.poids[j][i]*etats[j]
          s-=self.seuils[i]
          epsilon = 0.3
          if(s > 0 and etats[i]==0):
                error_count+=1
                delta = (s+epsilon)/(etats.count(True)+1)
        #On diminue de delta chaque poids ayant participé à la somme

                for j in range(self.n_cell):
                    if etats[j] == 1:
                        self.poids[j][i] -= delta
                        self.poids[i][j] -= delta 
                self.seuils[i] += delta
          elif(s<0 and etats[i]==1):
            error_count+=1
            delta = (s-epsilon)/(etats.count(True)+1)
            for j in range(self.n_cell):
                    if etats[j] == 1:
                        self.poids[j][i] -= delta
                        self.poids[i][j] -= delta 
            self.seuils[i] += delta
           
          etats[i] = True if s >= 0 else False
        
        return error_count
    
    def predict(self, alphabet):
        etats = self.toOneline(alphabet)
        predictions = []
        for i in range(self.n_cell):
            s = sum(self.poids[j] * etats[j] for j in range(self.n_cell)) - self.seuils[i]
            predictions.append(1 if s > 0 else 0)
        return predictions
        

                 


    def fit_on_all_alphabet():
        pass


res = ReseauRecurrent(poids=poids,seuils=seuils)
for _ in range(10):
    print("===============================")
    for lettre in alphabet:
        x = res.fit_on_one_alphabet(lettre)
        print(x)