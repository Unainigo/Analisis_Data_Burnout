import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:

    #Limpiar espacios en strings
    columnas_texto = df.select_dtypes(include='object').columns
    for columna in columnas_texto:
        df[columna] = df[columna].str.strip()
    print("\nEspacios eliminados en columnas de texto")

    #Normalizar texto en columnas de tipo string a minúsculas
    for columna in columnas_texto:
        df[columna] = df[columna].str.lower()
    print("\nTexto normalizado a minúsculas en columnas de texto")

    #Para las columnas de tipo fecha, convertir a datetime y al formato español
    columnas_fecha = ['date', 'created_at', 'updated_at', 'survey_date', 'registration_date']
    for columna in columnas_fecha:
        if columna in df.columns:
            # Convertir a tipo fecha
            df[columna] = pd.to_datetime(df[columna], errors='coerce')
            # Formato español -> dd/mm/yyyy
            df[columna] = df[columna].dt.strftime('%d/%m/%Y')
        print(f"Columna {columna} convertida a formato español")
    
    #Crear caracteristica de grupo de edad a partir de la columna de edad
    bins = [18, 25, 35, 45, 55, 65]
    labels = [
        '18-25',
        '26-35',
        '36-45',
        '46-55',
        '56-65'
    ]
    df['grupo_edad'] = pd.cut(
        df['age'],
        bins=bins,
        labels=labels
    )


    return df