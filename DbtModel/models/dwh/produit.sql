{{
    config( materialized='table' )
}}
with produit as
(
    select
   cast(null as STRING) as code_m, /* Business key */
   cast(null as STRING) as famille_produit, /* Relation to FamilleProduit.code */
   cast(null as STRING) as libelle,
   cast(null as STRING) as saisonnalite, /* Relation to Saison.code */
   cast(null as STRING) as cip13
)
select *
from produit
