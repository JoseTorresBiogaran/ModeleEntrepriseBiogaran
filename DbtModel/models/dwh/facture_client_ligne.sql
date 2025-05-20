{{
    config( materialized='table' )
}}
with facture_client_ligne as
(
    select
   cast(null as STRING) as numero_ligne, /* Business key */
   cast(null as INT64) as quantite,
   cast(null as STRING) as facture_client, /* Relation to FactureClient.numeroFacture */
   cast(null as STRING) as produit /* Relation to Produit.codeM */
)
select *
from facture_client_ligne
