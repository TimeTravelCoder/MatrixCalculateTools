 **开发文档 `dev_doc.md`** 

---

### 📄 `dev_doc.md
# Matrix Calculator - 开发文档

## 🧩 项目简介

该项目是一个基于 Python 的命令行矩阵计算器，采用 SymPy 库进行符号计算，支持基础与进阶的线性代数运算，包括特征值、零空间、QR/LU/谱分解等。

---

## 📌 项目结构
matrix_calculator/
│
├── matrix_calculator.py   # 主程序，包含完整计算逻辑与交互界面
├── README.md              # 使用说明文档
└── dev_doc.md             # 当前开发文档



---

## 🛠️ 开发环境与依赖

- Python 3.7+
- SymPy >= 1.12

安装依赖：

```bash
pip install sympy
```

---

## 🚀 功能清单

| 功能项         | 描述                             |
| -------------- | -------------------------------- |
| 秩计算         | 使用 `.rank()`方法             |
| 阶梯形         | 使用 `.rref()`获取行简化阶梯形 |
| 逆矩阵         | `.inv()`，处理不可逆情况       |
| 行列式         | `.det()`                       |
| 特征多项式     | `.charpoly(x)`                 |
| 特征值         | `.eigenvals()`                 |
| 特征向量       | `.eigenvects()`                |
| 零空间         | `.nullspace()`                 |
| 谱分解         | `.diagonalize()`               |
| QR 分解        | `.QRdecomposition()`           |
| LU 分解        | `.LUdecomposition()`           |
| 秩分解（近似） | 使用列子矩阵与伪逆               |

---

## 🧩 核心逻辑说明

主循环结构如下：

```python
while True:
    -> 获取用户输入
    -> 转换为 SymPy Matrix
    -> 顺序输出各类计算结果
    -> 提示是否继续
```

### 关键函数

```python
parse_element(elem)
```

* 解析输入中的整数或分数字符串，返回 `sp.Integer` 或 `sp.Rational`

```python
mat.rref()
```

* 获取行简化阶梯形和主元列索引

```python
mat.nullspace()
```

* 求解 Ax=0 的解空间

---

## 📦 模块可扩展性建议

| 模块      | 建议扩展点                             |
| ------- | --------------------------------- |
| GUI界面   | 使用 `customtkinter`/`PyQt5`实现可视化交互 |
| 矩阵动画    | 利用 `matplotlib`对 LU / QR 分解进行动画展示 |
| 文件导出    | 增加导出计算结果为 `.txt`/`.pdf`的功能        |
| 图形化特征向量 | 可视化二维变换效果，显示零空间与特征方向              |
| 错误日志记录  | 记录用户操作和异常到日志文件中                   |

---

## ✅ 开发进度建议（可选）

* [X] 命令行输入矩阵
* [X] 基本线性代数运算
* [X] 矩阵分解功能
* [ ] 支持 LaTeX 格式输出
* [ ] 图形界面交互支持
* [ ] 支持导出计算结果文件
* [ ] 动画演示与几何可视化

---

## 🤝 贡献指南（可选）

欢迎贡献代码、提出 Issue 或 Pull Request：

* 提交前请确保代码通过测试
* 遵守项目排版规范与中文注释风格
* 建议每次更新附上变更说明（Changelog）

---

## 📬 联系方式

如需帮助或合作请联系：

📧 [example@domain.com](mailto:example@domain.com)

🔗 GitHub: [your-repo-url]

