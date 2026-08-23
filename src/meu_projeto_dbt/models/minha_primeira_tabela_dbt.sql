{{ config(materialized='table') }}

SELECT 
    'Teste executado com sucesso!' AS status,
    current_timestamp() AS data_execucao,
    'Rodando dbt via Databricks Asset Bundles' AS origem