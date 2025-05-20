{{
    config( materialized='table' )
}}
with etablissement as
(
    select
   cast(null as DATE) as date_fermeture,
   cast(null as STRING) as siret,
   cast(null as STRING) as code_ebx, /* Business key */
   cast(null as STRING) as type_etablissement, /* Relation to TypeEtablissement.code */
   cast(null as STRING) as etablissement_societe_juridique, /* Relation to SocieteJuridique.siren */
   cast(null as DATE) as date_ouverture
)
select *
from etablissement
