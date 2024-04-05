import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder

#verilen datamız
data = {
    'year': [2018, 2015, 2020, 2012],
    'km': [50000, 80000, 20000, 120000],
    'engine_size': [1.6, 2.0, 1.8, 1.4],
    'brand': ['Toyota', 'Honda', 'Volkswagen', 'Ford'],
    'price': [120000, 90000, 150000, 60000]
}

#datayı numpy arraye dönüştürüyoruz
X_numerical = np.array([data['year'], data['km'], data['engine_size']]).T
X_categorical = np.array(data['brand']).reshape(-1, 1)
y = np.array(data['price']).reshape(-1, 1)

#nümerik özellikler için scaling
X_numerical = (X_numerical - X_numerical.mean(axis=0)) / X_numerical.std(axis=0)

#markalara one hot encoding kullanarak stringden nümerik arraye dönüştürüyoruz
encoder = OneHotEncoder(sparse=False)
X_categorical_encoded = encoder.fit_transform(X_categorical)

#kontrol amaçlı bastırıyorum arraye dönüşmüş stringleri
print("One-hot encoded categorical data:")
for brand, encoded in zip(data['brand'], X_categorical_encoded):
    print(f"{brand}: {encoded}")

#önceki nümerik verilerle one hot encodingle elde ettiklerimi birleştiriyorum
X = np.concatenate((X_numerical, X_categorical_encoded), axis=1)

#bias ekliyoruz
X = np.c_[np.ones(X.shape[0]), X]

#parametreleri initialize ediyoruz
theta = np.zeros((X.shape[1], 1))

#hipotez fonksiyonu
def hypothesis(X, theta):
    return np.dot(X, theta)

#cost fonksiyonu
def cost_function(X, y, theta):
    m = len(y)
    return (1 / (2 * m)) * np.sum((hypothesis(X, theta) - y) ** 2)

#gradient descent fonksiyonu
def gradient_descent(X, y, theta, alpha, iterations):
    m = len(y)
    costs = []
    for _ in range(iterations):
        gradient = (1 / m) * np.dot(X.T, (hypothesis(X, theta) - y))
        theta -= alpha * gradient
        cost = cost_function(X, y, theta)
        costs.append(cost)
    return theta, costs

#hiperparametreleri seçiyoruz
alphas = [0.01, 0.02, 0.04, 0.08, 0.2]
iterations = 100

#her alpha(learning rate) değeri için başlatıyoruz
final_thetas = []
for alpha in alphas:
    theta = np.zeros((X.shape[1], 1))
    theta, costs = gradient_descent(X, y, theta, alpha, iterations)
    final_thetas.append(theta)
    plt.plot(range(iterations), costs, label=f'Alpha = {alpha}')

plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.title('Cost Function vs. Iterations for Different Alpha Values')
plt.legend()
plt.show()

#her alpha değeri için fiyatı tahmin edip %lik tutarlılığa bakıyoruz
for alpha, theta in zip(alphas, final_thetas):
    predicted_prices = hypothesis(X, theta)
    accuracy = np.mean(np.abs(predicted_prices - y) / y) * 100
    print(f"\nAlpha: {alpha}")
    print("Predicted Prices:")
    print(predicted_prices)
    print("Actual Prices:")
    print(y)
    print(f"Accuracy: {100 - accuracy}%")
