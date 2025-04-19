import sympy as sp

def parse_element(elem):
    if '/' in elem:
        num, den = elem.split('/')
        return sp.Rational(num, den)
    else:
        return sp.Integer(elem)

while True:
    print("\n" + "="*40)
    print("新的矩阵计算")
    print("="*40)
    try:
        m = int(input("\n请输入矩阵的行数m:"))
        n = int(input("请输入矩阵的列数n:"))
    except ValueError:
        print("错误:请输入有效的整数！")
        continue

    matrix = []
    for i in range(m):
        while True:
            row_str = input(f"\n请输入第{i+1}行的元素(空格分隔,支持整数和分数,例如'1 2/3 5'):\n")
            elements = row_str.split()
            if len(elements) != n:
                print(f"错误:需要输入{n}个元素,当前输入了{len(elements)}个。请重新输入。")
                continue
            try:
                row = [parse_element(elem) for elem in elements]
                matrix.append(row)
                break
            except Exception as e:
                print(f"输入无效:{e}。请重新输入。")

    mat = sp.Matrix(matrix)
    print("\n计算结果显示:")

    # 1. 秩
    print(f"\n秩:\n{mat.rank()}")

    # 2. 阶梯形
    print("\n阶梯形:")
    echelon, _ = mat.rref()
    sp.pprint(echelon)

    # 3. 逆矩阵
    if mat.shape[0] == mat.shape[1]:
        try:
            inverse = mat.inv()
            print("\n逆矩阵:")
            sp.pprint(inverse)
        except:
            print("\n逆矩阵:矩阵不可逆。")
    else:
        print("\n逆矩阵:矩阵不是方阵,无法计算。")

    # 4. 行列式
    if mat.shape[0] == mat.shape[1]:
        print(f"\n行列式:\n{mat.det()}")
    else:
        print("\n行列式:矩阵不是方阵,无法计算。")

    # 5. 特征多项式
    if mat.shape[0] == mat.shape[1]:
        x = sp.symbols('x')
        char_poly = mat.charpoly(x)
        print(f"\n特征多项式:\n{char_poly.as_expr()}")
    else:
        print("\n特征多项式:矩阵不是方阵,无法计算。")

    # 6. 特征值
    if mat.shape[0] == mat.shape[1]:
        eigenvals = mat.eigenvals()
        print("\n特征值:")
        for val, mult in eigenvals.items():
            print(f"{val}(重数:{mult})")
    else:
        print("\n特征值:矩阵不是方阵,无法计算。")

    # 7. 特征向量
    if mat.shape[0] == mat.shape[1]:
        print("\n特征向量:")
        try:
            for val, mult, vecs in mat.eigenvects():
                print(f"\n特征值: {val}(重数:{mult})")
                for vec in vecs:
                    sp.pprint(vec)
        except Exception as e:
            print(f"计算特征向量时发生错误:{e}")
    else:
        print("\n特征向量:矩阵不是方阵,无法计算。")

    # 8. 零空间
    print("\n零空间:")
    nullspace = mat.nullspace()
    if nullspace:
        for vec in nullspace:
            sp.pprint(vec)
    else:
        print("零空间仅包含零向量。")

    # 9. 矩阵分解
    print("\n矩阵分解:")

    # 谱分解
    if mat.is_diagonalizable():
        P, D = mat.diagonalize()
        print("\n谱分解:")
        print("对角矩阵 D:")
        sp.pprint(D)
        print("相似变换矩阵 P:")
        sp.pprint(P)
    else:
        print("\n谱分解:矩阵不可对角化。")

    # QR分解
    try:
        Q, R = mat.QRdecomposition()
        print("\nQR 分解:")
        print("Q =")
        sp.pprint(Q)
        print("R =")
        sp.pprint(R)
    except:
        print("\nQR 分解失败。")

    # LU分解
    try:
        L, U, _ = mat.LUdecomposition()
        print("\nLU 分解:")
        print("L =")
        sp.pprint(L)
        print("U =")
        sp.pprint(U)
    except:
        print("\nLU 分解失败。")

    # 秩分解(Rank decomposition)
    try:
        rank = mat.rank()
        B = mat[:,:rank]
        C = sp.Matrix(sp.linalg.pinv(B.tolist())) @ mat
        print("\n秩分解(近似):")
        print("B(前 r 列):")
        sp.pprint(B)
        print("C(B 的伪逆 × 原矩阵):")
        sp.pprint(C)
    except:
        print("\n秩分解失败。")

    # 是否继续
    while True:
        choice = input("\n是否继续计算另一个矩阵?(y/n): ").strip().lower()
        if choice in ('y', 'n'):
            break
        print("请输入 y 或 n。")
    
    if choice != 'y':
        print("\n感谢使用,再见！")
        break
