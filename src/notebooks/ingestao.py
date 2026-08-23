# src/ingestao.py
from pyspark.sql.functions import current_timestamp, lit

print("Iniciando o job de ingestão via Asset Bundles...")

# Cria um dataframe de teste simulando a chegada de dados
df = spark.range(1, 100).withColumn("data_ingestao", current_timestamp())

# Exibe os dados no log do job
display(df)

print("Ingestão finalizada com sucesso!")