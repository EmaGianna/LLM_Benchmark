#lista a diccionario
def list_to_dict(in_list):
    """
    The function `list_to_dict` converts a list into a dictionary where the index of each element in the
    list becomes the key in the dictionary.
    
    :param in_list: Thank you for providing the code snippet. Could you please provide an example of the
    `in_list` that you would like to convert to a dictionary using the `list_to_dict` function?
    :return: The function `list_to_dict` is returning a dictionary where the keys are the indices of the
    elements in the input list `in_list`, and the values are the elements themselves.
    """
    dict_ = {}
    for i, valor in enumerate(in_list):
        dict_[i] = valor

    return dict_


def  return_numeric_df(df):
    """
    The function `return_numeric_df` selects numeric columns from a DataFrame and renames the columns
    with specific names.
    
    :param df: It looks like the function `return_numeric_df` takes a DataFrame as input and returns a
    new DataFrame containing only the columns with numeric data types. Additionally, it renames the
    columns of the new DataFrame with specific names
    :return: A DataFrame containing only the columns with numeric data types, with renamed columns.
    """
    df = df.select_dtypes(include=['number'])
    df.columns = ['id_promtp','tiempo de lectura','cantidad de oraciones','cantidad de caracteres','cantidad de letras'
                ,'cantidad de silabas','largo promedio de oraciones','promedio de letras por palabra','cantidad de stopwords'
                ,'cantidad de palabras','densidad lexica','riqueza lexica']
    return df

def create_scatter_graph(df_llama, df_gemma, column, path_save_html):
    """
    The function `create_scatter_graph` generates a scatter graph comparing data from two DataFrames and
    saves it as an HTML file.
    
    :param df_llama: The `df_llama` parameter is a DataFrame containing data related to the Llama model.
    It is used to plot a scatter graph comparing a specific column between the Llama and Gemma models
    :param df_gemma: The `df_gemma` parameter is a DataFrame containing data related to the model Gemma.
    It is used in the function `create_scatter_graph` to plot a scatter graph comparing a specific
    column between two models, Llama and Gemma
    :param column: The `column` parameter in the `create_scatter_graph` function is used to specify
    which column from the dataframes `df_llama` and `df_gemma` you want to compare in the scatter graph.
    It represents the specific column data that you want to visualize in the graph
    :param path_save_html: The `path_save_html` parameter in the `create_scatter_graph` function is the
    file path where you want to save the HTML file of the scatter graph that will be generated. You can
    specify the directory where you want to save the HTML file along with the desired filename. For
    example, you
    """

    import plotly.graph_objects as go
    # Crear la figura
    fig = go.Figure()

    # Añadir la primera gráfica de líneas (Llama)
    fig.add_trace(go.Scatter(x=df_llama['id_promtp'], y=df_llama[column],
                             mode='lines+markers', name='Llama'))
    ## Añadir la segunda gráfica de líneas (Gemma)
    fig.add_trace(go.Scatter(x=df_gemma['id_promtp'], y=df_gemma[column],
                             mode='lines+markers', name='Gemma'))

    # Configurar el título y los ejes
    fig.update_layout(
        title=f'Comparación de {column}',
        xaxis_title='ID Prompt',
        yaxis_title=column,
        legend_title='Modelo LLM',
        xaxis=dict(
            tickmode='linear',  # Usar modo de ticks lineal
            tick0=1,            # Primer tick en el valor 1
            dtick=1             # Distancia entre ticks igual a 1
        )
    )

    # Mostrar el gráfico
    fig.show()
    # Guardar grafico en html
    fig.write_html(f"{path_save_html}{column.replace(' ','_')}.html")