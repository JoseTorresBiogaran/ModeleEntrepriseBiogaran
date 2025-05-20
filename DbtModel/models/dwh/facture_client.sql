{{
    config( materialized='table' )
}}
with facture_client as
(
    select
   cast(null as STRING) as officine, /* Relation to Etablissement.code_ebx */
   cast(null as DATE) as date,
   cast(null as STRING) as numero_facture /* Business key */
)
select *
from facture_client
