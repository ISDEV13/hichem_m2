# Analyse RGPD des variables

Selon les principes du RGPD et les recommandations de la CNIL, les données peuvent être classées selon leur niveau de sensibilité et de risque de discrimination.

## Classification des variables

- **Nom** : Identifiant direct — permet d'identifier immédiatement une personne physique.
- **Prénom** : Identifiant direct — permet d'identifier immédiatement une personne physique.
- **Âge** : Donnée personnelle — peut être fortement discriminante selon les cas d'usage (ex : crédit, emploi).
- **Taille** : Donnée de santé indirecte — liée à l'état physique d'un individu ; peut être considérée comme sensible selon le contexte (RGPD art. 9).
- **Poids** : Donnée de santé indirecte — même justification que la taille, liée à l'état physique.
- **Sexe** : Donnée personnelle à risque élevé de discrimination — souvent utilisée dans des biais décisionnels.
- **Sport_licence** : Donnée non sensible a priori — mais pouvant être corrélée à l'état de santé ou au mode de vie.
- **Niveau_etude** : Donnée socio-économique — risque de discrimination indirecte (origine sociale, accès à l'emploi).
- **Région** : Donnée personnelle — peut indirectement révéler l'origine ou le niveau socio-économique.
- **Smoker** : Donnée de santé — considérée comme donnée sensible (RGPD art. 9), car liée au comportement de santé.
- **Nationalité_française** : Donnée personnelle — peut révéler l'origine ethnique ou nationale, donc sensible indirectement.
- **Revenu_estime_mois** : Donnée socio-économique — fortement discriminante, utilisée dans de nombreuses décisions (crédit, logement).
- **Situation_familiale** : Donnée personnelle — peut entraîner des discriminations (ex : célibataire vs marié).
- **Historique_credits** : Donnée financière — risque élevé, impact direct sur les décisions de crédit.
- **Date_creation_compte** : Donnée personnelle — risque faible, mais peut contribuer au profilage.
- **Score_credit** : Donnée financière — risque très élevé, souvent utilisée dans des décisions automatisées.
- **Loyer_mensuel** : Donnée financière — peut révéler le niveau de vie et entraîner une discrimination socio-économique.

## Conclusion

Toutes les données peuvent potentiellement être discriminantes, soit de manière directe, soit indirecte.  
Cependant, pour construire un modèle prédictif performant (par exemple pour estimer un montant de prêt), il est souvent nécessaire d'utiliser un maximum de variables pertinentes.  

👉 Il est important de souligner que la sensibilité et le caractère discriminant d'une donnée dépendent fortement du contexte d'utilisation.  

Dans le cadre d'un modèle visant à prédire un montant de prêt remboursable, certaines variables peuvent être considérées comme légitimes et justifiées, notamment :

- le revenu estimé mensuel
- l'historique de crédits
- le score de crédit
- l'âge
- le loyer mensuel
- la situation familiale

Ces variables permettent d'évaluer la capacité de remboursement et sont donc cohérentes avec l'objectif du modèle. Leur utilisation peut être justifiée au regard du principe de pertinence et de minimisation des données du RGPD, à condition qu'elles soient strictement nécessaires à la finalité poursuivie.  

Il est donc primordial de réfléchir à l'usage du modèle.

## Traitement des données technique

- Suppression des outliers sur les colonnes poids et taille
- Conservation des outliers sur les revenus estimés car ces outliers font partie de la distribution « normale » et doivent être intégrés au modèle
- Suppression de la colonne nationalité car biais statistique trop forte concentration autour de la nationalité fr en plus d'être hautement discriminante
- Suppression des colonnes score crédit et historique crédit car + de 50% des valeurs manquantes

## Traitement des données éthique

- Transformation des variables les plus sensibles pour limiter les biais
- Suppression des variables nom et prénom (non pertinentes et directement identifiantes)
- Stratégie de réduction des risques (Les transformations réduisent le risque discriminant mais ne le suppriment pas)
  - Regrouper les âges en tranches
  - Transformer taille et poids en IMC (catégories : faible, moyen, élevé)

## Réflexion éthique sur l'usage du modèle

L'usage du modèle est un point central car toutes les données peuvent être discriminantes :

- ❌ Décision automatisée (ex : refus de crédit) → risque élevé de discrimination
- ⚠️ Aide à la décision → risque toujours présent
- ✅ Analyse statistique (ex : identifier des inégalités) → usage plus éthique

Le choix des variables et du modèle doit donc être aligné avec l'objectif poursuivi.

## Choix retenus pour ce projet

Je choisis de supprimer les colonnes avec des valeurs manquantes trop importantes, avec une concentration autour d'une valeur non pertinente trop importante.  
Je transforme les colonnes sensible
Je garde toutes les autres colonnes pour avoir le modèle le plus performant possible.  
Il est cependant nécessaire de :

- Mettre en place un consentement explicite RGPD lors de la collecte des données
- Informer les utilisateurs de l'usage de leurs données

[https://www.cnil.fr/fr/rgpd-points-de-vigilance](https://www.cnil.fr/fr/rgpd-points-de-vigilance)  
[https://cnil.fr/fr/definition/donnee-sensible](https://cnil.fr/fr/definition/donnee-sensible)  
[https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/legal-grounds-processing-data/sensitive-data/what-personal-data-considered-sensitive_fr](https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/legal-grounds-processing-data/sensitive-data/what-personal-data-considered-sensitive_fr) 
