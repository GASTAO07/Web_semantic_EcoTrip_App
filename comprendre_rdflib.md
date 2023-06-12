
## Utilisation de la bibliothèque RDFlib en Python

Pour commencer, vous devez installer la bibliothèque `rdflib` en exécutant la commande suivante avec pip :

```bash
pip install rdflib
```

Une fois installée, vous pouvez importer `rdflib` dans votre script Python ou votre session interactive à l'aide de l'instruction suivante :

```python
import rdflib
```

Voici quelques concepts clés et fonctionnalités de `rdflib` :

1. **Graph** : La structure de données centrale dans `rdflib` est la classe `Graph`, qui représente un graphe RDF. Elle vous permet d'ajouter, de supprimer et de consulter des triplets RDF.

2. **URIRef** : La bibliothèque `rdflib` fournit la classe `URIRef` pour représenter les URIs (Uniform Resource Identifiers). Elle est couramment utilisée pour représenter les ressources dans les déclarations RDF.

3. **Literal** : La bibliothèque `rdflib` fournit la classe `Literal` pour représenter les valeurs littérales dans les déclarations RDF, telles que les chaînes de caractères, les nombres et les dates.

4. **Namespace** : `rdflib` vous permet de définir et d'utiliser des espaces de noms pour faciliter l'utilisation des URIs. La classe `Namespace` peut être utilisée pour définir des préfixes pour les URIs.

Voici un exemple simple qui montre comment créer un graphe RDF de base à l'aide de `rdflib` :

```python
import rdflib

# Créer un nouveau graphe RDF
g = rdflib.Graph()

# Définir quelques espaces de noms
ns = rdflib.Namespace("http://example.org/")
foaf = rdflib.Namespace("http://xmlns.com/foaf/0.1/")

# Ajouter un triplet au graphe
subject = ns["person1"]
predicate = foaf["name"]
object = rdflib.Literal("John Doe")
g.add((subject, predicate, object))

# Interroger le graphe
for triple in g:
    print(triple)
```

Cet exemple crée un nouveau graphe RDF, définit deux espaces de noms (`ns` et `foaf`), ajoute un triplet représentant le nom d'une personne dans le graphe, puis itère sur les triplets et les affiche.

Ceci est juste une introduction de base à `rdflib`. La bibliothèque offre de nombreuses autres fonctionnalités, notamment l'analyse et la sérialisation des données RDF dans différents formats (par exemple, RDF/XML, Turtle, JSON-LD), des capacités de requête avancées (par exemple, SPARQL) et une intégration avec des magasins de triplets et des bases de données externes.

Vous pouvez trouver des informations et des exemples plus détaillés dans la documentation de `rdflib` : https://rdflib.readthedocs.io/
