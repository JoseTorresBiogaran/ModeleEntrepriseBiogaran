{{
    config( materialized='table' )
}}
with societe_juridique as
(
    select
   cast(null as STRING) as tvaintra_communautaire,
   cast(null as STRING) as raison_sociale,
   cast(null as STRING) as siren /* Business key */
)
select *
from societe_juridique
