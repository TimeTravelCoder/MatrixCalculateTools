# 在线矩阵计算器

这是一个基于 Flask 和 SymPy 构建的在线矩阵计算器，可用于计算矩阵的各种属性和进行矩阵分解。

## 功能特性

- **基本矩阵操作**：计算矩阵的秩、行简化阶梯形（RREF）、逆矩阵、行列式。
- **特征值和特征向量**：计算矩阵的特征多项式、特征值和特征向量。
- **零空间计算**：计算矩阵的零空间。
- **矩阵分解**：支持谱分解、QR 分解、LU 分解和秩分解。

## 安装与运行

### 环境要求

- Python 3.x
- Flask 2.3.2
- SymPy 1.12

### 生成依赖文件

你可以使用 `pip freeze` 命令来生成项目的依赖文件，该文件会记录当前 Python 环境中安装的所有包及其版本信息。在项目根目录下执行以下命令：

```bash
pip freeze > requirements.txt
```

这会将依赖信息保存到 `requirements.txt` 文件中。

### 安装依赖

生成依赖文件后，可使用以下命令安装项目所需的依赖：

```bash
pip install -r requirements.txt
```

### 运行应用

```bash
python app.py
```

应用启动后，在浏览器中访问 `http://127.0.0.1:5000` 即可使用。

## 部署在远程 CentOS 服务器（root 用户）

### 1. 安装必要的系统依赖

首先，确保服务器上安装了 Python 3 和相关开发工具：

```bash
yum update -y
yum install -y python3 python3-pip python3-devel
```

### 2. 上传项目文件

你可以使用 `scp` 命令将项目文件从本地机器上传到远程服务器，假设项目文件夹名为 `matrix_calculator`：

```bash
scp -r /path/to/local/matrix_calculator root@your_server_ip:/root/
```

### 3. 创建虚拟环境（可选但推荐）

为项目创建一个独立的 Python 虚拟环境，避免不同项目间的依赖冲突：

```bash
cd /root/matrix_calculator
python3 -m venv venv
source venv/bin/activate
```

### 4. 安装项目依赖

在虚拟环境中安装项目所需的 Python 包：

```bash
pip install -r requirements.txt
```

### 5. 配置 Gunicorn

Gunicorn 是一个 Python WSGI HTTP 服务器，用于在生产环境中运行 Flask 应用。安装 Gunicorn：

```bash
pip install gunicorn
```

创建一个服务文件 `/etc/systemd/system/matrix_calculator.service`，内容如下：

```ini
[Unit]
Description=Matrix Calculator Flask Application
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/root/matrix_calculator
Environment="PATH=/root/matrix_calculator/venv/bin"
ExecStart=/root/matrix_calculator/venv/bin/gunicorn -w 4 -b 0.0.0.0:8000 app:app

[Install]
WantedBy=multi-user.target
```

### 6. 启动并设置开机自启

```bash
systemctl daemon-reload
systemctl start matrix_calculator
systemctl enable matrix_calculator
```

### 7. 配置 Nginx 作为反向代理（可选但推荐）

Nginx 可以处理静态文件、负载均衡和 SSL 加密等。安装 Nginx：

```bash
yum install -y nginx
```

创建一个 Nginx 配置文件 `/etc/nginx/conf.d/matrix_calculator.conf`，内容如下：

```nginx
server {
    listen 80;
    server_name your_domain_or_ip;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

启动 Nginx 并设置开机自启：

```bash
systemctl start nginx
systemctl enable nginx
```

### 8. 防火墙配置

如果服务器启用了防火墙，需要开放相应的端口：

```bash
firewall-cmd --permanent --add-service=http
firewall-cmd --reload
```

现在，你可以通过服务器的 IP 地址或域名访问矩阵计算器应用。

## 使用方法

1. 输入矩阵的行数和列数。
2. 点击“生成矩阵输入”按钮，生成矩阵输入框。
3. 在输入框中输入矩阵元素。
4. 点击“计算”按钮，查看计算结果。

## 代码结构

- `app.py`：Flask 应用的主文件，处理用户输入和矩阵计算。
- `templates/index.html`：HTML 模板文件，用于显示用户界面和计算结果。
- `static/style.css`：CSS 样式文件，用于美化界面。
- `requirements.txt`：项目依赖文件。

## 示例代码

### 矩阵输入处理

```python
def parse_element(elem):
    if '/' in elem:
        num, den = elem.split('/')
        return Rational(num, den)
    else:
        return int(elem)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        m = int(request.form['rows'])
        n = int(request.form['cols'])
        matrix = []
        errors = []

        # 验证行数和列数是否为正整数
        if m <= 0 or n <= 0:
            return render_template('index.html', error="行数和列数必须为正整数！")

        for i in range(m):
            row = []
            for j in range(n):
                elem = request.form.get(f'matrix[{i}][{j}]', '0').strip()
                try:
                    row.append(parse_element(elem))
                except Exception as e:
                    errors.append(f"行{i + 1}列{j + 1}: 无效输入 '{elem}'")
            matrix.append(row)

        if errors:
            return render_template('index.html', error="<br>".join(errors))

        mat = Matrix(matrix)
        # 进行矩阵计算
        ...
```

### 矩阵计算示例

```python
# 计算矩阵的秩
results['rank'] = mat.rank()

# 计算行简化阶梯形（RREF）
echelon, _ = mat.rref()
results['rref'] = latex(echelon)

# 计算逆矩阵
if mat.shape[0] == mat.shape[1]:
    try:
        inverse = mat.inv()
        results['inv'] = latex(inverse)
    except:
        results['inv_error'] = "矩阵不可逆。"
else:
    results['inv_error'] = "矩阵不是方阵,无法计算。"

# 计算行列式
if mat.shape[0] == mat.shape[1]:
    results['det'] = latex(mat.det())
else:
    results['det_error'] = "矩阵不是方阵,无法计算。"

# 计算特征多项式
if mat.shape[0] == mat.shape[1]:
    x = symbols('x')
    char_poly = mat.charpoly(x)
    results['charpoly'] = latex(char_poly.as_expr())
else:
    results['charpoly_error'] = "矩阵不是方阵,无法计算。"
```

## 注意事项

- 输入的矩阵元素可以是整数或分数（如 `1/2`）。
- 部分计算（如逆矩阵、行列式、特征多项式等）仅对方阵有效。
- 如果计算失败，页面将显示相应的错误信息。

## 贡献

如果你发现任何问题或有改进建议，请随时提交 Issue 或 Pull Request。

## 许可证

本项目采用 [MIT 许可证](LICENSE)。
