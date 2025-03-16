class PolynomialDifferentiator:
    def __init__(self, poly_str):
        self.poly_str = poly_str
        self.terms = self.parse_polynomial()

    def parse_polynomial(self):
        """
        解析输入的多项式字符串，将其拆分为项列表
        每个项是一个包含系数和指数的元组
        """
        terms = []
        # 去除字符串中的空格
        poly_str = self.poly_str.replace(" ", "")
        # 处理正负号，将 - 替换为 +-
        poly_str = poly_str.replace("-", "+-")
        # 按 + 分割字符串
        for term_str in poly_str.split("+"):
            if term_str:
                if term_str == 'x':
                    # 处理单独的 x，系数为 1，指数为 1
                    terms.append((1, 1))
                elif term_str == '-x':
                    # 处理 -x，系数为 -1，指数为 1
                    terms.append((-1, 1))
                elif 'x' in term_str:
                    if term_str.startswith('x'):
                        # 处理 x 开头的项，系数为 1
                        coefficient = 1
                        exponent_str = term_str.split('x')[1].lstrip('^')
                    elif term_str.startswith('-x'):
                        # 处理 -x 开头的项，系数为 -1
                        coefficient = -1
                        exponent_str = term_str.split('x')[1].lstrip('^')
                    else:
                        # 处理一般项，分离系数和指数
                        coefficient_str, exponent_str = term_str.split('x')
                        coefficient = int(coefficient_str)
                        exponent_str = exponent_str.lstrip('^')
                    if exponent_str:
                        exponent = int(exponent_str)
                    else:
                        exponent = 1
                    terms.append((coefficient, exponent))
                else:
                    # 处理常数项，指数为 0
                    terms.append((int(term_str), 0))
        return terms

    def differentiate(self):
        """
        对多项式求一阶导数
        """
        derivative_terms = []
        for coefficient, exponent in self.terms:
            if exponent > 0:
                # 根据求导公式计算导数的系数和指数
                new_coefficient = coefficient * exponent
                new_exponent = exponent - 1
                derivative_terms.append((new_coefficient, new_exponent))
        return derivative_terms

    def format_derivative(self, derivative_terms):
        """
        将导数项列表格式化为字符串
        """
        formatted_terms = []
        for coefficient, exponent in derivative_terms:
            if exponent == 0:
                # 指数为 0，只输出系数
                term_str = str(coefficient)
            elif exponent == 1:
                if coefficient == 1:
                    # 系数为 1，指数为 1，只输出 x
                    term_str = 'x'
                elif coefficient == -1:
                    # 系数为 -1，指数为 1，输出 -x
                    term_str = '-x'
                else:
                    # 一般情况，输出系数和 x
                    term_str = f"{coefficient}x"
            else:
                if coefficient == 1:
                    # 系数为 1，输出 x^指数
                    term_str = f"x^{exponent}"
                elif coefficient == -1:
                    # 系数为 -1，输出 -x^指数
                    term_str = f"-x^{exponent}"
                else:
                    # 一般情况，输出系数 x^指数
                    term_str = f"{coefficient}x^{exponent}"
            formatted_terms.append(term_str)
        if not formatted_terms:
            # 若结果为空，说明导数为 0
            return '0'
        # 用 + 连接各项，去除多余的 + 号
        result = '+'.join(formatted_terms).replace('+-', '-')
        return result

    def get_derivative(self):
        """
        获取多项式的一阶导数字符串
        """
        derivative_terms = self.differentiate()
        return self.format_derivative(derivative_terms)


if __name__ == "__main__":
    poly_str = input("请输入标准的代数多项式（使用 x 作为变量）：")
    differentiator = PolynomialDifferentiator(poly_str)
    derivative = differentiator.get_derivative()
    print(f"该多项式的一阶导数是: {derivative}")

