{{
    config( materialized='table' )
}}
with vente_officine as
(
    select
   cast(null as STRING) as officine, /* Relation to Etablissement.code_ebx */
   cast(null as INT64) as quantite_vendue,
   cast(null as STRING) as identifiant, /* Business key */
   cast(null as STRING) as produit, /* Relation to Produit.codeM */
   cast(null as DATE) as date_de_vente
)
select *
from vente_officine
