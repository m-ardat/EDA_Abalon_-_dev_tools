import pandas as pd
from explainerdashboard import RegressionExplainer, ExplainerDashboard
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsRegressor

if __name__ == '__main__':

    df = pd.read_csv('processed_abalon.csv')
    df.drop(columns='Unnamed: 0', axis=1, inplace=True)

    X_full = df.drop('Rings', axis=1)
    y = df['Rings']
    X_train_full, X_test_full, y_train_full, y_test_full = train_test_split(X_full,
                                                                            y,
                                                                            test_size=0.2,
                                                                            random_state=10
                                                                            )

    categorical = list(X_full.select_dtypes('object').columns)
    numeric_features = list(X_full.select_dtypes('number').columns)

    ct = ColumnTransformer([
        ('ohe', OneHotEncoder(handle_unknown="ignore"), categorical),
        ('scaling', MinMaxScaler(), numeric_features)
    ])

    X_train_transformed = ct.fit_transform(X_train_full)
    X_test_transformed = ct.transform(X_test_full)
    new_features = list(ct.named_transformers_['ohe'].get_feature_names_out())
    new_features.extend(numeric_features)
    X_train_transformed = pd.DataFrame(X_train_transformed, columns=new_features)
    X_test_transformed = pd.DataFrame(X_test_transformed, columns=new_features)

    model = KNeighborsRegressor()
    params_model = {'n_neighbors': range(1, 30),
                    'weights': ['uniform', 'distance'],
                    'metric': ['minkowski', 'euclidean', 'manhattan'],
                    'p': [1, 2]
                    }
    scoring = ['neg_mean_absolute_error', 'r2']
    gs = GridSearchCV(model,
                      params_model,
                      scoring=scoring,
                      refit='neg_mean_absolute_error',
                      cv=5,
                      n_jobs=-1,
                      verbose=2
                      )

    gs.fit(X_train_transformed, y_train_full)
    best_model = gs.best_estimator_

    explainer = RegressionExplainer(best_model,
                                    X_test_transformed.iloc[:10],
                                    y_test_full.iloc[:10]
                                    )
    db = ExplainerDashboard(explainer)
    db.to_yaml("dashboard.yaml", explainerfile="explainer.dill", dump_explainer=True)

    print('Dashboard is saved')
