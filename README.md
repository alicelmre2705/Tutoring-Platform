# Principe général de l'application Web: Tutorat en langue entre les élèves

Lorsqu'un élève arrive sur le site il doit se connecter, ou s'inscrire s'il n'est pas déjà dans la base de données. Ensuite, il peut consulter les langues disponibles, puis choisir le niveau de langue, puis le cours auquel il veut assister.

Un élève est caractérisé par un identifiant, un nom, un prénom, et une année/promotion.
Un cours est caractérisé par la langue enseignée, le niveau de langue, et l'horaire auquel a lieu le cours.

Un élève peut suivre plusieurs cours, et un cours peut être suivi par plusieurs personnes.


# Base de données :

- Cours (id, nom, date, horaire, durée, prix, #id_langue)
- Langues (id, nom, niveau)
- Elèves (id, nom, prénom, promotion, mail, #id_langue, #id_cours)
- Avis (?)

--> Ne pas hésiter à aller voir certains exercices du poly de SIP

# Organisation des pages du site :

- Page 1     : log in
- Page 1 bis : inscription
- Page 2     : langue
- Page 3     : cours
- Page 4     : nom du professeur

# Fonctionnalités à implémenter :

- Un élève se connecte ou s'inscrit sur le site 
- Un élève peut alors choisir un cours par étapes
- Fonctionnalité de paiement
- Laisser un avis


