from typing import Iterable
import math


class RegressaoLinearSimples:
    formula_ = None
    formula_str = None

    cov_ = None

    def prever(self, x):
        if self.formula is None:
            raise Exception('Formula Vazia, dê um "fit" primeiro.')
        return self.formula(x)

    def fit(self, x: Iterable[int], y: Iterable[int]):
        # Y = A - b*X
        if len(x) != len(y):
            raise Exception('Must Be the same Len')
        E_X, E_Y, E_X_Y = self.get_mean(x, y)
        B = self.cov(x, y) / self.dp(x)**2
        A = E_Y - B * E_X

        def prever(x):
            Ya = A + B * x
            return Ya

        self.formula = prever
        self.formula_str = f'Y = {A} + {B} * X'

    def cov(self, x: Iterable, y: Iterable):
        E_X, E_Y, E_X_Y = self.get_mean(x, y)
        cov =  E_X_Y - (E_X * E_Y)
        self.cov_ = cov
        return cov

    def dp(self, x: Iterable):
        var = self.var(x)
        return math.sqrt(var)

    def var(self, x: Iterable):
        E_X = self.get_mean(x)
        X_2 = x**2
        E_X_2 = self.get_mean(X_2)

        var = E_X_2 - E_X**2
        return var

    def get_mean(self, x: Iterable, y: Iterable = None):
        E_X = sum(x) / len(x)

        if (y is None):
            return E_X

        E_Y = sum(y) / len(y)
        x_y = x * y
        E_X_Y = sum(x_y) / len(x_y)

        return E_X, E_Y, E_X_Y
