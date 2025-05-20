{{
    config( materialized='table' )
}}
with saison as
(
    select
   cast(null as STRING) as libelle,
   cast(null as STRING) as code /* Business key */
)
select *
from saison
