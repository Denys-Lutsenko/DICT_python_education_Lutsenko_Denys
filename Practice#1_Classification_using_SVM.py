import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn import svm
from sklearn.inspection import DecisionBoundaryDisplay

# Показати отриману отриману скатерограму
def visualize_classification_result(model, X, y, title=None):
    plt.figure(figsize=(8,6))
    plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
    ax = plt.gca()
    DecisionBoundaryDisplay.from_estimator(model, X,
                                          plot_method="contour",
                                          colors="k",
                                          levels=[-1, 0, 1],
                                          alpha=0.5,
                                          linestyles=['--', '-'],
                                          ax=ax)
    ax.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=100, linewidths=1, facecolors='none', edgecolors='k')
    if title:
        plt.title(title)

    plt.show()


# Згенерувати датасет
X, y = make_moons(n_samples=100, noise=0.2, random_state=100)
# Використати лінійне ядро для SVM:
linear_model = svm.SVC(kernel="linear", C=1000)
linear_model.fit(X, y)
visualize_classification_result(linear_model, X, y, "Линейная SVM с C=1000")
# Використати поліноміальне ядро для SVM
poly_model = svm.SVC(kernel="poly", degree=3, gamma="auto", C=1)
poly_model.fit(X, y)
visualize_classification_result(poly_model, X, y, "Поліноміальний SVM зі ступенем=3 і C=1")
# Використати ядро RBF для SVM
rbf_model = svm.SVC(kernel="rbf", gamma=0.1, C=1)
rbf_model.fit(X, y)
visualize_classification_result(rbf_model, X, y, "RBF SVM з гамма=0.1 та C=1")
