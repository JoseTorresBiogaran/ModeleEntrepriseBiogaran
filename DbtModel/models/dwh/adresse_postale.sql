{{
    config( materialized='table' )
}}
with adresse_postale as
(
    select
   cast(null as DATE) as date_fermeture,
   cast(null as STRING) as adresse_postale_etablissement, /* Relation to Etablissement.code_ebx */
   cast(null as STRING) as cip, /* Business key */
   cast(null as DATE) as date_ouverture
)
select *
from adresse_postale
