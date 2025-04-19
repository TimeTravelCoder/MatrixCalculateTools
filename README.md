以下是整合了命令行工具和 Web 工具信息的 `README.md` 文档：

# 矩阵计算工具项目

本项目包含一个命令行矩阵计算器和一个基于 Flask 的在线矩阵计算器，均采用 SymPy 库进行符号计算，支持基础与进阶的线性代数运算，包括特征值、零空间、QR/LU/谱分解等。

## 项目结构
### 命令行工具（MatrixCLITool）
- `MatrixCLITool.py`：主程序，包含完整计算逻辑与交互界面
- `README.md`：使用说明文档
- `dev_doc.md`：当前开发文档

### 在线矩阵计算器（MatrixWebTool）
- `app.py`：Flask 应用的主文件，处理用户输入和矩阵计算
- `templates/index.html`：HTML 模板文件，用于显示用户界面和计算结果
- `static/style.css`：CSS 样式文件，用于美化界面
- `requirements.txt`：项目依赖文件

## 依赖环境
### 命令行工具
- **必需依赖**
  - **Python**：3.8+
  - **sympy**：符号计算库（用于矩阵运算）
- **可选依赖（打包用）**
  - **pyinstaller**：用于将脚本打包为可执行文件（非必需，仅打包时需要）

### 在线矩阵计算器
- **Python 3.x**
- **Flask 2.3.2**
- **SymPy 1.12**

## 安装指南

### 命令行工具
1. **克隆项目或下载文件**
```bash
git clone https://github.com/TimeTravelCoder/MatrixCalculateTools.git
cd matrix-calculator
```
2. **安装依赖**
```bash
# 通过pip安装必需依赖
pip install sympy
```
3. **（可选）安装打包工具**
```bash
pip install pyinstaller
```

### 在线矩阵计算器
#### 本地运行
1. **生成依赖文件**
在项目根目录下执行以下命令：
```bash
pip freeze > requirements.txt
```
2. **安装依赖**
```bash
pip install -r requirements.txt
```
3. **运行应用**
```bash
python app.py
```
应用启动后，在浏览器中访问 `http://127.0.0.1:15000` 即可使用。

#### 部署在远程 CentOS 服务器（root 用户）
1. **安装必要的系统依赖**
```bash
yum update -y
yum install -y python3 python3-pip python3-devel
```
2. **克隆项目**
```bash
git clone https://your-repo-url.com/matrix-calculator.git
cd matrix-calculator/MatrixWebTool
```
3. **创建虚拟环境（可选但推荐）**
```bash
cd /root/matrix_calculator
python3 -m venv venv
source venv/bin/activate
```
4. **安装项目依赖**
```bash
pip install -r requirements.txt
```
5. **防火墙配置**
```bash
firewall-cmd --permanent --add-service=http
firewall-cmd --reload
```
6. **启动并设置开机自启**
```bash
systemctl daemon-reload
systemctl start matrix_calculator
systemctl enable matrix_calculator
```

现在，你可以通过服务器的 IP 地址或域名访问矩阵计算器应用。

## 使用方法

### 命令行工具
直接运行脚本（推荐开发/调试）
```bash
python MatrixCLITool.py
```
根据提示输入矩阵的行数、列数及元素，按步骤完成计算。

### 在线矩阵计算器
1. 输入矩阵的行数和列数。
2. 点击“生成矩阵输入”按钮，生成矩阵输入框。
3. 在输入框中输入矩阵元素。
4. 点击“计算”按钮，查看计算结果。

## 功能特性

### 命令行工具
1. **矩阵基本运算**：秩、阶梯形（行简化阶梯形）、逆矩阵（仅方阵）、行列式（仅方阵）
2. **特征分析**：特征多项式、特征值、特征向量（仅方阵）
3. **空间分析**：零空间（核空间）
4. **矩阵分解**：谱分解（仅可对角化方阵）、QR 分解、LU 分解、秩分解
5. **输入支持**：整数、分数（格式如 `2/3`），自动验证输入合法性

### 在线矩阵计算器
- **基本矩阵操作**：计算矩阵的秩、行简化阶梯形（RREF）、逆矩阵、行列式。
- **特征值和特征向量**：计算矩阵的特征多项式、特征值和特征向量。
- **零空间计算**：计算矩阵的零空间。
- **矩阵分解**：支持谱分解、QR 分解、LU 分解和秩分解。

## 打包为可执行文件（命令行工具）
### 1. 生成依赖清单（可选）
```bash
# 生成依赖文件 requirements.txt
pip freeze > requirements.txt
```
### 2. 打包为独立可执行程序（Windows/Linux/macOS）
```bash
# 执行打包命令（当前目录需包含 MatrixCLITool.py）
pyinstaller --console --onefile --name matrix_calculator MatrixCLITool.py
```
- `--console`：保留控制台窗口（用于显示输入输出）
- `--onefile`：生成单个可执行文件（体积较大，但便于分发）
- `--name`：指定输出文件名称

### 3. 运行打包后的程序
- Windows：在 `dist` 目录中找到 `matrix_calculator.exe` 并双击运行
- Linux/macOS：在 `dist` 目录中执行 `./matrix_calculator`

## 注意事项
- 输入的矩阵元素可以是整数或分数（如 `1/2`）。
- 部分计算（如逆矩阵、行列式、特征多项式等）仅对方阵有效。
- 如果计算失败，命令行工具会输出相应错误信息，在线计算器页面将显示相应的错误信息。

## 贡献与反馈
### 命令行工具
1. 如需提交 bug 或功能建议，欢迎在仓库中创建 Issue
2. 代码贡献请通过 Pull Request 提交，确保符合 PEP8 规范

### 在线矩阵计算器
如果你发现任何问题或有改进建议，请随时提交 Issue 或 Pull Request。

## 联系作者
- **命令行工具**
  
  - 项目主页：[https://github.com/TimeTravelCoder/MatrixCalculateTools.git](https://github.com/TimeTravelCoder/MatrixCalculateTools)
- **在线矩阵计算器**
  - 如需帮助或合作请联系：
    - 📧 [example@domain.com](mailto:example@domain.com)
    - 🔗 GitHub: https://github.com/TimeTravelCoder/MatrixCalculateTools

## 许可证
本项目采用 **MIT License**，详见 [LICENSE](LICENSE) 文件。
