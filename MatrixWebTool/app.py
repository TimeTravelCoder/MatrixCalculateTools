from flask import Flask, request, render_template
from sympy import Matrix, Rational, latex, symbols

app = Flask(__name__)

def parse_element(elem):
    if '/' in elem:
        num, den = elem.split('/')
        return Rational(num, den)
    else:
        return int(elem)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
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
            results = {}

            # 1. 秩
            results['rank'] = mat.rank()

            # 2. 阶梯形
            echelon, _ = mat.rref()
            results['rref'] = latex(echelon)

            # 3. 逆矩阵
            if mat.shape[0] == mat.shape[1]:
                try:
                    inverse = mat.inv()
                    results['inv'] = latex(inverse)
                except:
                    results['inv_error'] = "矩阵不可逆。"
            else:
                results['inv_error'] = "矩阵不是方阵,无法计算。"

            # 4. 行列式
            if mat.shape[0] == mat.shape[1]:
                results['det'] = latex(mat.det())
            else:
                results['det_error'] = "矩阵不是方阵,无法计算。"

            # 5. 特征多项式
            if mat.shape[0] == mat.shape[1]:
                x = symbols('x')
                char_poly = mat.charpoly(x)
                results['charpoly'] = latex(char_poly.as_expr())
            else:
                results['charpoly_error'] = "矩阵不是方阵,无法计算。"

            # 6. 特征值
            if mat.shape[0] == mat.shape[1]:
                eigenvals = mat.eigenvals()
                eigenval_list = []
                for val, mult in eigenvals.items():
                    eigenval_list.append(f"{latex(val)}(重数:{mult})")
                results['eigenvals'] = eigenval_list
            else:
                results['eigenvals_error'] = "矩阵不是方阵,无法计算。"

            # 7. 特征向量
            if mat.shape[0] == mat.shape[1]:
                eigenvecs = []
                try:
                    for val, mult, vecs in mat.eigenvects():
                        eigenvec_group = {
                            'value': latex(val),
                            'multiplicity': mult,
                            'vectors': [latex(vec) for vec in vecs]
                        }
                        eigenvecs.append(eigenvec_group)
                    results['eigenvecs'] = eigenvecs
                except Exception as e:
                    results['eigenvecs_error'] = f"计算特征向量时发生错误:{str(e)}"
            else:
                results['eigenvecs_error'] = "矩阵不是方阵,无法计算。"

            # 8. 零空间
            nullspace = mat.nullspace()
            if nullspace:
                results['nullspace'] = [latex(vec) for vec in nullspace]
            else:
                results['nullspace'] = "零空间仅包含零向量。"

            # 9. 矩阵分解
            # 谱分解
            if mat.is_diagonalizable():
                P, D = mat.diagonalize()
                results['spectral_P'] = latex(P)
                results['spectral_D'] = latex(D)
            else:
                results['spectral_error'] = "矩阵不可对角化。"

            # QR分解
            try:
                Q, R = mat.QRdecomposition()
                results['QR_Q'] = latex(Q)
                results['QR_R'] = latex(R)
            except:
                results['QR_error'] = "QR 分解失败。"

            # LU分解
            try:
                L, U, _ = mat.LUdecomposition()
                results['LU_L'] = latex(L)
                results['LU_U'] = latex(U)
            except:
                results['LU_error'] = "LU 分解失败。"

            # 秩分解(Rank decomposition)
            try:
                rank = mat.rank()
                B = mat[:, :rank]
                C = Matrix(Matrix(B.tolist()).pinv()) @ mat
                results['rank_B'] = latex(B)
                results['rank_C'] = latex(C)
            except:
                results['rank_error'] = "秩分解失败。"

            results['original'] = latex(mat)

            return render_template('index.html', results=results)

        except Exception as e:
            return render_template('index.html', error=f"系统错误: {str(e)}")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port=15000)# 启动应用程序，设置调试模式为True，以便在开发过程中进行调试。