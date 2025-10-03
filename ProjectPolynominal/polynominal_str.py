def polynomial_str(self):
    terms = []
    for i in range(self.degree, -1, -1):
        coef_index = self.degree - i  # Индекс коэффициента в списке
        coef = self.coefficients[coef_index]
        
        # Пропускаем нулевые коэффициенты (кроме случая, когда многочлен нулевой)
        if coef == 0 and self.degree > 0:
            continue
        # Определяем знак
        if coef >= 0 and terms:  # Положительный коэффициент (не первый)
            sign = " + "
        elif coef < 0 and terms:  # Отрицательный коэффициент (не первый)
            sign = " - "
            coef = abs(coef)
        elif coef < 0:  # Отрицательный коэффициент (первый)
            sign = "-"
            coef = abs(coef)
        else:  # Положительный коэффициент (первый)
            sign = ""
        # Форматируем член многочлена
        if i == 0:  # Свободный член
            terms.append(f"{sign}{coef}")
        elif i == 1:  # x в первой степени
            if coef == 1:
                terms.append(f"{sign}x")
            else:
                terms.append(f"{sign}{coef}x")
        else:  # x в степени > 1
            if coef == 1:
                terms.append(f"{sign}x^{i}")
            else:
                terms.append(f"{sign}{coef}x^{i}")
    # Если все коэффициенты нулевые
    if not terms:
        return "0"
    return "".join(terms)