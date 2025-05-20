{{
    config( materialized='table' )
}}
with commande_client as
(
    select
   cast(null as STRING) as officine, /* Relation to Etablissement.code_ebx */
   cast(null as STRING) as date,
   cast(null as STRING) as numero_commande /* Business key */
)
select *
from commande_client
