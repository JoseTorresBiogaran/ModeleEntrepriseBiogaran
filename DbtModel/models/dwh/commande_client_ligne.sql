{{
    config( materialized='table' )
}}
with commande_client_ligne as
(
    select
   cast(null as STRING) as numero_ligne, /* Business key */
   cast(null as INT64) as quantite,
   cast(null as STRING) as commande_client, /* Relation to CommandeClient.numeroCommande */
   cast(null as STRING) as produit /* Relation to Produit.codeM */
)
select *
from commande_client_ligne
