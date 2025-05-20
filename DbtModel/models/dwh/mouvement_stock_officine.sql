{{
    config( materialized='table' )
}}
with mouvement_stock_officine as
(
    select
   cast(null as STRING) as officine, /* Relation to Etablissement.code_ebx */
   cast(null as INT64) as stock_quantite,
   cast(null as DATE) as stock_date,
   cast(null as STRING) as identifiant, /* Business key */
   cast(null as STRING) as produit /* Relation to Produit.codeM */
)
select *
from mouvement_stock_officine
