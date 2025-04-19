以下是包含打包指令与依赖说明的 **README.md** 文档：

# 矩阵计算工具

## 项目简介

一个基于符号计算库 `sympy` 的矩阵计算工具，支持矩阵的秩、阶梯形、逆矩阵、行列式、特征值/向量、零空间及多种矩阵分解（谱分解、QR分解、LU分解、秩分解）等功能。用户可通过交互式界面输入矩阵元素（支持整数和分数），实时查看计算结果。

## 功能特性

1. **矩阵基本运算**：秩、阶梯形（行简化阶梯形）、逆矩阵（仅方阵）、行列式（仅方阵）
2. **特征分析**：特征多项式、特征值、特征向量（仅方阵）
3. **空间分析**：零空间（核空间）
4. **矩阵分解**：谱分解（仅可对角化方阵）、QR分解、LU分解、秩分解
5. **输入支持**：整数、分数（格式如 `2/3`），自动验证输入合法性

## 依赖环境

### 必需依赖

- **Python**：3.8+
- **sympy**：符号计算库（用于矩阵运算）

### 可选依赖（打包用）

- **pyinstaller**：用于将脚本打包为可执行文件（非必需，仅打包时需要）

## 安装指南

### 1. 克隆项目或下载文件

```bash
git clone https://your-repo-url.com/matrix-calculator.git
cd matrix-calculator
```

### 2. 安装依赖

```bash
# 通过pip安装必需依赖
pip install sympy
```

### 3. （可选）安装打包工具

```bash
pip install pyinstaller
```

## 使用方法

### 1. 直接运行脚本（推荐开发/调试）

```bash
python matrix_calculator.py
```

根据提示输入矩阵的行数、列数及元素，按步骤完成计算。

## 打包为可执行文件（跨平台）

### 1. 生成依赖清单（可选）

```bash
# 生成依赖文件 requirements.txt
pip freeze > requirements.txt
```

### 2. 打包为独立可执行程序（Windows/Linux/macOS）

```bash
# 执行打包命令（当前目录需包含 matrix_calculator.py）
pyinstaller --console --onefile --name matrix_calculator matrix_calculator.py
```

- `--console`：保留控制台窗口（用于显示输入输出）
- `--onefile`：生成单个可执行文件（体积较大，但便于分发）
- `--name`：指定输出文件名称

### 3. 运行打包后的程序

- Windows：在 `dist` 目录中找到 `matrix_calculator.exe` 并双击运行
- Linux/macOS：在 `dist` 目录中执行 `./matrix_calculator`

## 目录结构

```
matrix-calculator/
├─ matrix_calculator.py  # 主程序文件
├─ requirements.txt       # 依赖清单（通过 `pip freeze` 生成）
├─ README.md              # 项目说明文档
└─ dist/                  # 打包后生成的可执行文件目录（打包后自动创建）
```

## 贡献与反馈

1. 如需提交bug或功能建议，欢迎在仓库中创建Issue
2. 代码贡献请通过Pull Request提交，确保符合PEP8规范

## 许可证

本项目采用 **MIT License**，详见 [LICENSE](LICENSE) 文件。

## 联系作者

- 邮箱：your-email@example.com
- 项目主页：https://your-repo-url.com/matrix-calculator

### 依赖说明

- **sympy** 会自动安装其所需的子依赖（如 `mpmath`），无需手动安装其他库。
- 打包时 `pyinstaller` 会自动检测并包含 `sympy` 的依赖文件，生成的可执行文件可在未安装Python环境的设备上运行（需确保系统架构一致）。
