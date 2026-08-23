import dlt
from pyspark.sql.functions import col, upper

print("Inicializando pipeline DLT de roteirização...")

# 1. Tabela Bronze (Simulando a leitura de dados brutos)
@dlt.table(
    name="rotas_bronze",
    comment="Dados brutos de roteirização (ex: Roadnet/Greenmile)"
)
def rotas_bronze():
    # Em um cenário real, usaríamos spark.readStream
    return spark.sql("""
        SELECT 1 AS id_rota, 'Planejada' AS status, 'BR-SP' AS regiao 
        UNION ALL 
        SELECT 2, 'Em Rota', 'br-rj' 
        UNION ALL 
        SELECT 3, 'Concluída', NULL
    """)

# 2. Tabela Prata (Limpando e transformando os dados da Bronze)
@dlt.table(
    name="rotas_prata",
    comment="Dados padronizados e limpos"
)
# DLT Expectations: Regras de qualidade de dados (impede que dados ruins passem)
@dlt.expect_or_drop("regiao_valida", "regiao IS NOT NULL")
def rotas_prata():
    return (
        dlt.read("rotas_bronze")
        .withColumn("regiao_padronizada", upper(col("regiao")))
    )