

# Support Vector Machine - 决策向量机是一种常见的监督学习算法，
# 主要用于分类和回归问题。
# SVM 的基本思想是找到一个能够将不同类别的样本分开的最优超平面，
# 使得离超平面最近的样本点（称为支持向量）到超平面的距离最大化，
# 从而实现分类或回归任务。

# 导入必要的库
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# 加载数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 构建 SVM 模型
svm_model = LinearSVC()

# 训练模型
svm_model.fit(X_train, y_train)

# 预测测试集
y_pred = svm_model.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print("准确率: {:.2f}%".format(accuracy * 100))
