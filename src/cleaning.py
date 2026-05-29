import pandas as pd
import numpy as np

def clean(df: pd.DataFrame) -> pd.DataFrame:
    #Ver que suciedad hay en el dataset antes de comenzar a limpiarlo
    print(f"\n Información general: {df.info()} ")
    print(f"\nTotal de valores nulos: {df.isnull().sum().sum()}")
    print(f"\nTotal de filas duplicadas: {df.duplicated().sum()}")

    #Eliminar filas duplicadas
    num_duplicados = df.duplicated().sum()
    if num_duplicados > 0:
        df = df.drop_duplicates()
        print(f"\nSe eliminaron {num_duplicados} filas duplicadas")
    else:
        print("\nNo hay duplicados")

    #Corregir tipos de datos
    #Para las columnas numéricas, convertir a tipo numérico y manejar errores
    columnas_numericas = ['age','years_experience', 'years_at_company', 'salary_usd', 'work_hours_per_week', 'meetings_per_day',
    'team_size', 'sleep_hours_per_night', 'exercise_days_per_week', 'vacation_days_taken', 'manager_support_score', 'work_life_balance_score',
    'job_satisfaction_score', 'social_support_score', 'deadline_pressure_score', 'autonomy_score', 'stress_score',
    'burnout_score', 'phq9_score', 'gad7_score']
    for columna in columnas_numericas:
        df[columna] = pd.to_numeric(df[columna], errors='coerce')
    print("\nTipos numéricos corregidos")

    #Limpiar valores númericos con valores negativos 
    for columna in columnas_numericas:
        num_negativos = (df[columna] < 0).sum()
        if num_negativos > 0:
            df.loc[df[columna] < 0, columna] = np.nan
            print(f"\nSe reemplazaron {num_negativos} valores negativos en la columna '{columna}' por NaN")
    
    #Rellenar valores nulos
    for columna in df.columns:
        if df[columna].dtype == 'object':
            valor_relleno = df[columna].mode()[0] if not df[columna].mode().empty else 'Desconocido'
            df[columna] = df[columna].fillna(valor_relleno)
            print(f"\nValores nulos en columna '{columna}' rellenados con: {valor_relleno}")
        elif df[columna].dtype in ['int64', 'float64']:
            valor_relleno = df[columna].median()
            df[columna] = df[columna].fillna(valor_relleno)
            print(f"\nValores nulos en columna '{columna}' rellenados con la mediana: {valor_relleno}")

    #Detectar y manejar outliers 
    for columna in columnas_numericas:
        Q1 = df[columna].quantile(0.25)
        Q3 = df[columna].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        num_outliers = ((df[columna] < limite_inferior) | (df[columna] > limite_superior)).sum()
        if num_outliers > 0:
            df.loc[(df[columna] < limite_inferior) | (df[columna] > limite_superior), columna] = np.nan
            print(f"\nSe reemplazaron {num_outliers} outliers en la columna '{columna}' por NaN")

    #Comprobaciones finales después de la limpieza
    print(f"\nInformación general después de la limpieza: {df.info()}")
    print(f"\nTotal de valores nulos después de la limpieza: {df.isnull().sum().sum()}")
    print(f"\nTotal de filas duplicadas después de la limpieza: {df.duplicated().sum()}")

    #Retornanos el dataframe limpio para seguir con el proceso de análisis y visualización
    return df