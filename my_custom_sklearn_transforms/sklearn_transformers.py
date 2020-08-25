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
        temp = data.drop(labels=self.columns, axis='columns')
        
        samples = temp.sample(frac =.5)
        import pandas as pd
        return pd.concat([samples, temp])
