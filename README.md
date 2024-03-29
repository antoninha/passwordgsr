# Passwordgsr

## 1. Polymorphisme

## 2. Ecapsulation

### Utilisation

J'utilise l'encapsulation dans ma classe 'Date', dans cette classe j'ai mes méthodes en protected et j'ai une méthode get  'getDate' permettant d'accéder aux données depuis d'autres classes

### Définition

L'encapsulation est l'un des principes fondamentaux de la programmation orientée objet (POO). Il s'agit de regrouper les données et les méthodes qui les manipulent au sein d'une même entité appelée classe. L'objectif principal de l'encapsulation est de cacher les détails internes de la classe et de fournir une interface publique pour interagir avec les objets de cette classe.
En POO, l'encapsulation est mise en œuvre en définissant des attributs privés et des méthodes publiques dans une classe. Les attributs privés ne sont pas accessibles directement en dehors de la classe, ils sont donc protégés contre les modifications non autorisées. Les méthodes publiques, également appelées méthodes d'accès ou d'interface, permettent d'interagir avec les attributs privés de la classe.

## 3. Composition

### Utilisation

J'utilise la composition dans ma classe 'Merge', dans celle-ci j'utilise les méthodes 'getDate' et 'getWord' de mes objets 'Date' et 'Word' afin d'acceder aux données de ces objets dans ma classe 'Merge'

### Définition

La composition est un concept clé de la programmation orientée objet (POO) qui permet de créer des relations entre les objets en les combinant pour former des structures plus complexes. La composition se base sur l'idée qu'un objet peut être composé d'autres objets.

En utilisant la composition, un objet peut avoir une référence vers un ou plusieurs autres objets et utiliser leurs fonctionnalités pour accomplir ses propres tâches. La composition est souvent considérée comme une relation "partie-tout", où un objet est constitué de plusieurs autres objets.

## 4. Héritage 

### Utilisation

J'utilise de l'héritage dans ma classe 'ToL33t', celle-ci hérite de la classe 'Word' afin de permettre d'isoler la partie l33t de la partie Word, et de pouvoir réutiliser les méthodes de la classe 'Word' dans une autre autre classe sans avoir la méthode de 'ToL33t' 

### Définition

L'héritage en programmation orientée objet (POO) est un concept clé qui permet de créer une relation de parenté entre les classes. Une classe héritant d'une autre classe est appelée une classe dérivée ou sous-classe, tandis que la classe dont elle hérite est appelée la classe de base ou superclasse.

## 5. Interface

### Utilisation

Je n'utilise pas d'interface car le python ne le permet pas.

### Définition

En programmation orientée objet (POO), une interface est un contrat qui spécifie les méthodes qu'une classe doit implémenter. Elle définit les signatures des méthodes, mais ne fournit pas d'implémentation concrète. Une interface permet de définir un ensemble de comportements attendus sans se soucier des détails d'implémentation de chaque classe.

## 6. Méthodes et attributs d'objets

### Utilisation

J'utilise des méthodes et attributs d'objets dans ma classe 'Merge', je créer une instance de la classe 'Word' avec des attributs 'word' et 'args' et j'utilise la méthode 'getWord' de la classe Word afin d'obtenir des données de cette instance.

### Définition

Méthodes d'objets : Les méthodes sont des fonctions définies à l'intérieur d'une classe et associées à des objets créés à partir de cette classe. Elles permettent de définir le comportement des objets et d'effectuer des opérations spécifiques. Les méthodes d'objets sont généralement appelées en utilisant la notation pointée, c'est-à-dire en utilisant l'objet suivi du nom de la méthode, comme par exemple objet.methode(). Les méthodes d'objets peuvent accéder aux attributs de l'objet sur lequel elles sont appelées.

Attributs d'objets : Les attributs sont des variables définies à l'intérieur d'une classe et associées à des objets créés à partir de cette classe. Ils représentent les caractéristiques ou les données spécifiques à chaque objet. Les attributs d'objets peuvent être de deux types : les attributs de données (ou variables d'instance) qui stockent des valeurs uniques pour chaque objet, et les attributs de classe (ou variables de classe) qui sont partagés par tous les objets d'une classe. Les attributs d'objets peuvent être accédés et modifiés à l'aide de la notation pointée, comme par exemple objet.attribut.

En utilisant les méthodes et attributs d'objets, vous pouvez définir le comportement des objets, encapsuler les données, effectuer des opérations spécifiques sur les objets et interagir avec d'autres objets.

## 7. Méthodes et attributs statiques

### Utilisation

J'utilise une méthode statique 'get_specials_characters()' dans ma classe 'Specials_characters', celle-ci n'est pas influée si la classe 'Specials_characters' est instanciée (ce qui n'est pas possible parce qu'elle est abstraite).

### Définition

Méthodes statiques : Les méthodes statiques sont des méthodes définies dans une classe qui n'ont pas besoin d'accéder à l'instance de la classe ou à ses attributs. Elles sont généralement utilisées pour effectuer des opérations qui sont liées à la classe dans son ensemble, mais qui ne nécessitent pas de manipuler des attributs spécifiques de l'objet. Les méthodes statiques sont décorées avec le décorateur @staticmethod et elles peuvent être appelées directement sur la classe sans avoir besoin d'instancier un objet. Elles sont utiles pour regrouper des fonctionnalités connexes qui sont spécifiques à la classe.

Attributs statiques : Les attributs statiques sont des variables définies dans une classe qui sont partagées par tous les objets de cette classe. Contrairement aux attributs de données normaux, les attributs statiques n'appartiennent pas à un objet spécifique, mais à la classe elle-même. Ils sont définis à l'intérieur de la classe, en dehors de toute méthode, et ils sont généralement utilisés pour stocker des données qui sont communes à tous les objets de la classe. Les attributs statiques peuvent être accédés en utilisant la notation pointée sur la classe elle-même, plutôt que sur une instance de la classe.

## 8. Méthodes et attributs de classe

### Utilisation

J'utilise un attribut de classe 'compteur' dans ma classe 'Date', et j'utilise la méthode de classe 'number_date', cet attribut et cette méthodes permettent de connaitre le nombre d'instance de date qui ont été créer.

### Définition

Les méthodes et attributs de classe sont des éléments qui appartiennent à la classe elle-même plutôt qu'à une instance spécifique de la classe. Ils sont définis au niveau de la classe et partagés par toutes les instances de cette classe. Les méthodes de classe agissent sur les attributs de classe et ne peuvent pas accéder aux attributs spécifiques à une instance, tandis que les attributs de classe sont des variables partagées par toutes les instances de la classe.