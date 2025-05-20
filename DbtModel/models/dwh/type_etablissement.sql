{{
    config( materialized='table' )
}}
with type_etablissement as
(
    select
   cast(null as STRING) as libelle,
   cast(null as STRING) as code /* Business key */
)
select *
from type_etablissement
