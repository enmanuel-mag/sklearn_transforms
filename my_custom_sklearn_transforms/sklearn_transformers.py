from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        # Devolvemos un nuevo dataframe de datos sin las columnas no deseadas
        data['DIV_PC'] = data['TOTAL_VENTAS'] - data['TOTAL_COMPRAS']
        return data

class AddExamples(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        import pandas as pd
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = pd.DataFrame(X, index=range(X.shape[0]),
                          columns=range(X.shape[1]))
        data = X.copy()
        # Devolvemos un nuevo dataframe de datos sin las columnas no deseadas
        
        samples = data.sample(frac =.5)
        return pd.concat([samples, data])
