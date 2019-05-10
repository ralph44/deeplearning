import matplotlib.pyplot as plt
import numpy as np

#Punkte im Koordinatensystem
X = [0.00, 0.22, 0.24, 0.33, 0.37, 0.44, 0.44, 0.57, 0.93, 1.00]
Y = [0.00, 0.22, 0.58, 0.20, 0.55, 0.39, 0.54, 0.53, 1.00, 0.61]

#hypothese
weight = 0.75
bias = 0.45
x1 = np.linspace(0.0, 1.0, num=2.0)
funktion = weight*x1+bias

#Plotten der aktuellen Line und den dazugehoerigen Punkten
plt.plot(X, Y, 'o')
plt.plot(funktion)
plt.show()

predict = []
errors = []
ableitung_nach_weight = []
ableitung_nach_bias = []

#Random groesse des Fehlers, der die Whileschleife true macht
summeError = 10

##Neue Matrizen fur die neue Runde
while summeError>=0.13:
    predict = []
    errors = []

    #Berechnen der einzelnen Errorwerte und die Prediction
    for i in range(len(X)):
        p = weight * X[i] + bias
        e = 0.5 * (Y[i] - p) ** 2
        predict.append(p)
        errors.append(e)

    ##Neue Matrizen fur die neue Runde
    summeError = 0

    #Berechnen der Summe von dem Error
    for i in range(len(predict)):
        summeError = summeError + errors[i]

    ##Neue Matrizen fur die neue Runde
    ableitung_weight = 0
    ableitung_bias = 0
    ableitung_nach_weight = []
    ableitung_nach_bias = []

    #Schleife mit der Ableitung der SummErrorFunktion nach Bias und Weight
    for i in range(len(X)):
        ableitung_weight = X[i] * (weight * X[i] + bias - Y[i])
        ableitung_bias = bias + weight * X[i] - Y[i]

        ableitung_nach_weight.append(ableitung_weight)
        ableitung_nach_bias.append(ableitung_bias)

    ##Neue Matrizen fur die neue Runde
    summeAbleitungNachWeight = 0
    summeAbleitungNachBias = 0

    #Berechnen der Summe der Ableitungsfunktionen von Weight und Bias
    for i in range(len(predict)):
        summeAbleitungNachWeight = summeAbleitungNachWeight + ableitung_nach_weight[i]
        summeAbleitungNachBias = summeAbleitungNachBias + ableitung_nach_bias[i]

    #Weight und Bias werden mit der Learningrate in kleineren Schritten in die richtige Richtung gehen
    weight = weight - 0.01 * summeAbleitungNachWeight
    bias = bias - 0.01 * summeAbleitungNachBias
    print("Der Error ist kleiner geworden", summeError)

#Ausgabe des Weight und Bias Wertes und des Errors
print("das hier'ist die ableitung weight Matrix", summeAbleitungNachWeight)
print("das hier'ist die ableitung bias Matrix", summeAbleitungNachBias)
print("Der Error ist kleiner geworden", summeError)

#Zeigen des finalen Ergebnis
plt.plot(X, Y, 'o')
x1 = np.linspace(0.0, 1.0, num=2)
funktion = weight * x1 + bias
plt.plot(funktion)
plt.show()
