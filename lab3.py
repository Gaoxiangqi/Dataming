import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six import StringIO
import pydotplus


def fun_draw_tree():
    iris = load_iris()
    test_idx = [0, 50, 100]
    train_target = np.delete(iris.target, test_idx)
    train_data = np.delete(iris.data, test_idx, axis=0)

    test_target = iris.target[test_idx]
    test_data = iris.data[test_idx]

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(train_data, train_target)
    tree.export_graphviz(clf, out_file='tree.dot')
    dot_data = StringIO()
    tree.export_graphviz(clf, out_file=dot_data, feature_names=iris.feature_names, class_names=iris.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

    print(graph)
    graph.write_pdf("iris.pdf")


if __name__ == '__main__':
    # fun_make_point()
    fun_draw_tree()

