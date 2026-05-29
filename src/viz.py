import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.config import OUT_PATH_GRAPH



def plot_graph(df: pd.DataFrame):
   #Paises con más burnout
    burnout_pais_puesto = (
    df.groupby(['country','burnout_level'])
    .size() 
    .reset_index(name='count')
    .sort_values(by='count', ascending=False)
    )
    plt.figure(figsize=(18, 8))
    sns.barplot(
        data=burnout_pais_puesto,
        x='country',
        y='count'   
    )
    plt.title('Burnout medio por país')
    plt.xlabel('País')
    plt.ylabel('Burnout')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUT_PATH_GRAPH / "burnout_pais.png")
    plt.show()

    #Mayor burnout por edad
    burnout_edad_puesto = (
    df.groupby(['grupo_edad', 'burnout_level'])
    .size()
    .reset_index(name= 'count')
    .sort_values(by='count', ascending=False)
    )
    plt.figure(figsize=(16, 8))
    sns.barplot(
        data=burnout_edad_puesto,
        x='grupo_edad',
        y='count'
    )
    plt.title('Burnout medio por grupo de edad')
    plt.xlabel('Grupo de Edad')
    plt.ylabel('Burnout')
    plt.tight_layout()
    plt.savefig(OUT_PATH_GRAPH / "burnout_edad.png")
    plt.show()

    #Tipos de empresa con más burnout
    burnout_empresa = (
        df.groupby(['company_size', 'burnout_level'])
        .size()
        .reset_index(name='count')
        .sort_values(by='count', ascending=False)
    )
    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=burnout_empresa,
        x='company_size',
        y='count'
    )
    plt.title('Burnout medio según tamaño de empresa')
    plt.xlabel('Tamaño de Empresa')
    plt.ylabel('Burnout')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(OUT_PATH_GRAPH / "burnout_empresa.png")
    plt.show()

    #Burnout por Genero
    burnout_genero = (
        df.groupby(['gender', 'burnout_level'])
        .size()
        .reset_index(name='count')
        .sort_values(by='count', ascending=False)
    )
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=burnout_genero,
        x='gender',
        y='count'
    )
    plt.title('Burnout medio por género')
    plt.xlabel('Género')
    plt.ylabel('Burnout')
    plt.tight_layout()
    plt.savefig(OUT_PATH_GRAPH / "burnout_genero.png")
    plt.show()

    #heatmap por país y puesto de trabajo del burnout
    heatmap_data = (
        df.groupby(['country', 'job_role'])['burnout_score']
        .mean()
        .reset_index()
    )
    heatmap_pivot = heatmap_data.pivot(
        index='job_role',
        columns='country',
        values='burnout_score'
    )
    plt.figure(figsize=(18, 10))
    sns.heatmap(
        heatmap_pivot,
        annot=True,
        fmt='.1f',
        cmap='coolwarm'
    )
    plt.title('Mapa de calor de burnout por país y puesto')
    plt.xlabel('País')
    plt.ylabel('Puesto')
    plt.tight_layout()
    plt.savefig(OUT_PATH_GRAPH / "heatmap_burnout.png")
    plt.show()


