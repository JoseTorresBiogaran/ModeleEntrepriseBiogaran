{{
    config( materialized='table' )
}}
with famille_produit as
(
    select
   cast(null as STRING) as libelle,
   cast(null as STRING) as code /* Business key */
)
select *
from famille_produit
