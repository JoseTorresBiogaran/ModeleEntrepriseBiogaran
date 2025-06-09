{{
    config( materialized='table' )
}}
with officine as
(
    select
   cast(null as DATE) as date_fermeture,
   cast(null as STRING) as cip, /* Business key */
   cast(null as DATE) as date_ouverture
)
select *
from officine
