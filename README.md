
**Trabajo ﬁn de Ciclo Complementario**

**Licenciatura en Ciencia de Datos**

**Benchmark de LLMs desde la perspectiva de indicadores lingüísticos aplicados a las respuestas**

**Director de la Carrera:** German Giro

**Profesor:** Alejandro Hernández

**Alumno:** Norberto Emanuel Vicente Giannattasio

[Introducción 2](#_heading=h.gjdgxs)

[Que es un Modelo de Lenguaje Grande ( Large Language Model) 2](#_heading=h.30j0zll)

[Brevísima historia de los LLM 4](#_heading=h.1fob9te)

[Consideraciones Iniciales 5](#_heading=h.3znysh7)

[Objetivo 5](#_heading=h.2et92p0)

[Consideraciones acerca de Frameworks de pruebas actuales. 5](#_heading=h.tyjcwt)

[Selección de LLMs 6](#_heading=h.3dy6vkm)

[Herramientas Utilizadas 6](#_heading=h.1t3h5sf)

[Propuesta de Framework de Benchmark para LLMs 8](#_heading=h.hzjcld6bt1oz)

[Descripción del experimento 8](#_heading=h.sa5kokof1719)

[Prompts de experimentación 8](#_heading=h.elewjo9c9pgr)

[Respuestas a los Prompts de experimentación por parte de los LLM 8](#_heading=h.i4bhb5ekbm8v)

[Indicadores seleccionados 8](#_heading=h.y03eydxiib3e)

[Comparaciones de indicadores aplicados 8](#_heading=h.g9k2e42oxuaz)

[Conclusiones 8](#_heading=h.nipqvjiiv9jo)

[Apéndice A: Detalles Técnicos del Entorno de Experimentación 8](#_heading=h.fgwbd292mzop)

[Referencias 9](#_heading=h.2s8eyo1)

# Introducción

No nos sumergimos mucho en los basamentos teórico técnicos de los Modelos de Lenguaje Grande (LLM), ya que no es el objetivo de este trabajo, pero haremos una breve introducción describiendo qué son los LLM y una breve historia acerca de los mismos.

## Que es un Modelo de Lenguaje Grande ( Large Language Model)

Los LLMs o Modelos de Lenguaje Grande (LLM desde este momento por sus siglas en inglés) son algoritmos avanzados de aprendizaje profundo capaces de realizar una amplia gama de tareas relacionadas con el procesamiento del lenguaje natural (NLP).

La diferencia que todos hemos notado desde finales de 2022 o principios de 2023 estriba en el tamaño y cantidad de datos de entrenamiento. Los nuevos modelos, cimentados en la arquitectura Transformers —actualmente la más popular—, se entrenan con vastos conjuntos de datos, lo que les confiere una impresionante habilidad para reconocer, resumir, traducir, predecir y generar texto. Si además añadimos una funcionalidad de chatbot para interactuar, como lo hizo OpenAI con ChatGPT, Meta con Llama2 o Google con Gemini, entonces tenemos una experiencia nueva, una experiencia cognitiva que los humanos no habíamos tenido con ninguna máquina. Esa es la razón por la que nos divertimos y “enganchamos” tanto a los modelos como ChatGPT: para nuestro cerebro, estamos teniendo **una experiencia cognitiva**, una conversación, como la podríamos tener con un bibliotecario de amplísimos conocimientos o cualquier otra persona.

Es fundamental distinguir entre los LLMs y la AI generativa. Mientras que los LLMs se centran en el texto, la AI generativa abarca un espectro más amplio, multimodal, incluyendo la creación de imágenes, música y más. Todos los LLMs pueden considerarse parte de la AI generativa, pero no toda AI generativa es un LLM.

A modo de ejemplo, [Claude2](https://www.anthropic.com/index/claude-2) de Anthropic, Gemini de Google, y los famosos ChatGPT o Llama2 (o 3) son LLMs, mientras que [Stable Diffusion](https://stablediffusionweb.com/) o Bing Image Creator de Microsoft, basado en Dall-e 3, son AI Generativa pero producen imágenes, no son grandes modelos de lenguaje.

Algunos ejemplos de modelos de lenguaje grandes populares incluyen:

- **ChatGPT:** un chatbot de inteligencia artificial generativa desarrollado por OpenAI.
- **PaLM:** Pathways Language Model (PaLM) de Google, un modelo de lenguaje de transformadores capaz de realizar razonamientos aritméticos y de sentido común, explicar bromas, generar código y traducir.
- **BERT:** el modelo de lenguaje representación de codificador bidireccional de transformadores (BERT) también se desarrolló en Google. Es un modelo basado en transformadores que puede comprender el lenguaje natural y responder preguntas.
- **XLNet:** un modelo de lenguaje de permutación, XLNet generó predicciones de salida en un orden aleatorio, lo que lo distingue de BERT. Evalúa el patrón de tokens codificados y luego predice los tokens en orden aleatorio, en lugar de en un orden secuencial.
- **GPT:** los transformadores generativos pre entrenados son quizá los modelos de lenguaje grandes más conocidos. Desarrollados por OpenAI, GPT es un modelo fundacional popular cuyas iteraciones numeradas son mejoras de sus predecesores (GPT-3, GPT-4, etc.).

Además, de estos modelos de lenguaje también es preciso mencionar los conocidos como LLM de código abierto como ser:

[Llama2 (o 3)](https://llama.meta.com/) de Meta ( este a su vez posee una versión específica para la generación o corrección de código de programación llamada [CodeLlama](https://ai.meta.com/blog/code-llama-large-language-model-coding/)), [Gemma](https://ai.google.dev/gemma?hl=es-419) de Google ( este LLM también posee una versión específica para la generación y corrección de código de programación llamada [CodeGemma](https://ai.google.dev/gemma/docs/codegemma?hl=es-419)) o [Mistral](https://docs.mistral.ai/) de la compañía francesa del mismo nombre.

## Brevísima historia de los LLM

Los LLM existen desde hace algunas décadas, pero hace poco se volvieron lo suficientemente potentes y sofisticados como para que se los use en una amplia gama de tareas. El primer LLM se creó en la década de los sesenta con el primer chatbot, Eliza. Sin embargo, sus capacidades eran muy limitadas. No fue hasta la década de 2010 cuando los LLM maduraron hasta alcanzar un nivel de funcionalidad adecuado para modelos muy grandes y aplicaciones del mundo real.

Un momento crucial en el avance de LLM llegó con la introducción de la arquitectura [Transformer](https://aws.amazon.com/es/what-is/transformers-in-artificial-intelligence/) en 2017. El modelo de Transformer mejoró significativamente la comprensión de las relaciones de palabras dentro de oraciones, lo que dio como resultado una generación de texto que sea gramaticalmente correcta y semánticamente coherente.

En los últimos años, se pre entrenó a los LLM con amplios conjuntos de datos de cientos de miles de millones de textos y códigos, lo que ha permitido mejorar sustancialmente su rendimiento en diversas tareas. Por ejemplo, algunos LLM ahora pueden generar texto indistinguible del texto escrito por humanos.


![Historia_LLM](img/Historia_LLM.png)
# Consideraciones Iniciales

## Objetivo

El objetivo del presente trabajo es el desarrollo de un framework de comparación independiente para LLMs utilizando diversas herramientas del ambiente Open Source

## Consideraciones acerca de Frameworks de pruebas actuales

La evaluación de los LLM es un ámbito incipiente y abierto a experimentación y creación, dentro de este campo existen algunos frameworks/librerías para evaluar las respuestas de lo LLM, entre las principales podemos mencionar

- [Uptrain](https://github.com/uptrain-ai/uptrain)
- [Ragas](https://docs.ragas.io/en/stable/)
- [DeepEval](https://docs.confident-ai.com/)

En las evaluaciones previas, se verificó que estos frameworks de test, necesitan una Key para utilizar la plataforma de OpenAI (Excepto Uptrain) para utilizar el api abierta de esta compañía (la creadora de ChatGPT) y además están desarrolladas para evaluar un LLM contra el de la compañía OpenAI y obtener las métricas en base a ellos. (Podríamos detallar el uso de estos, pero sería tema de un paper al completo).

Por esta razón es que se decidió desarrollar una serie de métricas para realizar la evaluación de un LLM frente a otro, también es de mencionar, que para no largar el desarrollo del presente documento, no ahondaremos en los detalles teóricos que le dan sustento a cada uno de los indicadores seleccionados para realizar la comparativa.

## Selección de LLMs

Por esta razón es que se decidió desarrollar una serie de métricas para realizar la evaluación de un LLM frente a otro.

Se eligieron los LLM Open Source de dos de las compañías de tecnología más grandes e innovadoras Llama2 de Meta y Gema de Google, en ambos casos, para que la comparación/benchmark sea justo, se eligieron las versiones que fueron entrenadas con 7 billones de parámetros en cada caso; es decir la parametrización de entrenamiento de ambos modelos de LLM, a nivel numérico cuantitativo son idénticas (no tenemos certeza si son los mismos sets de parámetros a nivel cualitativo).

Se Omitió la versión más nueva del Modelo Llama, llama3, ya que este está entrenado con 8 billones de parámetros y la comparativa no sería matemáticamente correcta, ya que esta versión del modelo posee una ventaja de mil millones de parámetros sobre la versión de Google.

## Herramientas Utilizadas

En esta sección, antes de presentar los detalles y resultados del framework propuesto y de las pruebas realizadas, procederemos a mencionar las herramientas utilizadas:

- **Python:** Se eligió Python como lenguaje de programación, ya que hoy es el estándar de facto en el mundo de datos por sobre otros como Scala o R. Además de ser un lenguaje de programación Open Source y con una enorme comunidad y documentación accesible.
- **Ollama:** es una herramienta que nos permite ejecutar modelos de lenguaje en nuestros ordenadores de manera sencilla. Su principal propósito es facilitar el acceso a modelos de gran tamaño sin necesidad de utilizar la nube. Con Ollama, podemos descargar y ejecutar varios modelos, incluyendo LLaMA-2, Uncensored LLaMA, CodeLLaMA, Falcon y Mistral, entre otros.
- **SQLite:** es un sistema de gestión de bases de datos relacional compatible con ACID, contenida en una relativamente pequeña biblioteca escrita en C. SQLite es un proyecto de dominio público creado por D. Richard Hipp.
- **TextStat:** Paquete de Python para calcular estadísticas a partir de texto y determinar la legibilidad, complejidad y nivel de grado de un corpus específico.
- **TextBlob:** TextBlob es una biblioteca de Python para procesar datos textuales. Proporciona una API simple para realizar tareas comunes de procesamiento de lenguaje natural (PLN) como el etiquetado de partes del discurso, la extracción de sintagmas nominales, el análisis de sentimiento, la clasificación y más. Particularmente se utilizará para el análisis de sentimientos.
- **Langdetect:** Librería que permite la detección del lenguaje de un texto.
- **NLTK(Natural Language Toolkit):** Es una plataforma líder para construir programas de Python que trabajan con datos de lenguaje humano. Proporciona interfaces fáciles de usar para más de 50 corpus y recursos léxicos como WordNet, junto con un conjunto de bibliotecas de procesamiento de texto para clasificación, tokenización, derivación, etiquetado, análisis sintáctico y razonamiento semántico. También incluye envoltorios para bibliotecas de PNL de uso industrial.
- **Google Colab:** también conocido como Colaboratory, es un servicio gratuito de Jupyter Notebook alojado en la nube que te permite ejecutar código Python sin necesidad de configuración.
- **VsCode:** es un editor de código fuente gratuito y de código abierto desarrollado por Microsoft, altamente configurable, personalizable y extensible mediante plugin
- **Plotly Express**: es una biblioteca de Python para crear visualizaciones de datos interactivas de forma rápida y sencilla.
- **Ngrok:** es una herramienta que permite exponer un servidor local a Internet de forma rápida y sencilla. Funciona creando un túnel seguro entre tu computadora y los servidores de Ngrok, lo que te permite acceder a tu servidor desde cualquier lugar del mundo con una URL pública.

# Propuesta de Framework de Benchmark para LLMs

## Descripción del experimento

## Prompts de experimentación

## Respuestas a los Prompts de experimentación por parte de los LLM

## Indicadores seleccionados

## Comparaciones de indicadores aplicados

## Conclusiones

#

# Apéndice A: Detalles Técnicos del Entorno de Experimentación

# Referencias

<https://www.aprendemachinelearning.com/llm-que-son-los-grandes-modelos-de-lenguaje/>

<https://www.mongodb.com/es/resources/basics/large-language-models>

<https://aws.amazon.com/es/what-is/transformers-in-artificial-intelligence/>

<https://ai.meta.com/blog/code-llama-large-language-model-coding/>

<https://ai.google.dev/gemma/docs/codegemma?hl=es-419>

<https://ollama.com/>

<https://www.sqlite.org/>

<https://pypi.org>

<https://pypi.org/project/textstat/>

<https://pypi.org/project/textblob/>

<https://pypi.org/project/langdetect/>

<https://www.nltk.org/>

<https://plotly.com/python/plotly-express/>

<https://colab.research.google.com/>

<https://visualstudio.microsoft.com/es/#vscode-section>

<https://ngrok.com/>