# 🤖 OLCA - Votre Assistant IA de Composition Musicale

## Qu'est-ce qu'OLCA ?

**OLCA** (Orpheus Langchain CLI Assistant) est votre **compositeur IA personnel** qui peut :
- 🎼 **Créer de la musique** en notation ABC
- 🔧 **Exécuter des commandes** pour convertir automatiquement
- 💡 **Analyser et améliorer** vos compositions
- 🎵 **Générer des arrangements** dans différents styles
- 📝 **Apprendre de vos préférences** au fil du temps

**C'est comme avoir un maître compositeur IA dans votre terminal !**

---

## 🚀 Configuration Rapide

### 1. Initialiser OLCA
```bash
# Configuration automatique
olca init -y

# Ou configuration interactive
olca init
```

### 2. Configurer Votre Clé API
```bash
# Définir votre clé OpenAI
export OPENAI_API_KEY_olca="votre-clé-api-ici"

# Ou l'ajouter à .env
echo "OPENAI_API_KEY_olca=votre-clé-api-ici" >> .env
```

### 3. Commencer à Composer !
```bash
# Démarrer l'assistant IA
olca
```

---

## 🎯 Exemples de Composition Musicale

### Exemple 1 : Générer une Chanson Folk
```
Vous : "Créer un air folk irlandais simple en Ré majeur, temps 6/8"

OLCA : Je vais créer un air folk irlandais pour vous...
[Crée automatiquement un fichier ABC]

X:1
T:Air Folk Irlandais
L:1/8
M:6/8
Q:3/8=120
K:D
|: A | d2 f e2 d | A2 F D2 E | F2 A A2 B | A3 A2 :|
|: f | a2 f d2 f | e2 c A2 c | d2 f e2 c | d3 d2 :|
```

### Exemple 2 : Analyser et Améliorer
```
Vous : "Analyser cet ABC et suggérer des améliorations : [coller votre ABC]"

OLCA : En regardant votre composition, je remarque :
- La mélodie pourrait utiliser plus de variation aux mesures 3-4
- Considérez ajouter des symboles d'accords pour l'accompagnement
- La fin pourrait être plus forte

Voici une version améliorée : [génère ABC amélioré]
```

### Exemple 3 : Workflow Complet
```
Vous : "Créer une ballade jazz et la convertir en tous formats"

OLCA : Je vais créer une ballade jazz et la convertir pour vous...
[Génère ABC, puis exécute :]
oabc ballade_jazz.abc

Résultat : ballade_jazz.mid, ballade_jazz.mp3, ballade_jazz.svg créés !
```

---

## 🔧 Modes et Options

### Mode Humain (Interactif)
```bash
# Démarrer avec interaction humaine
olca -H

# L'IA vous demandera confirmation avant actions importantes
```

### Mode Mathématique
```bash
# Activer outils mathématiques pour théorie musicale
olca -M

# Utile pour : calculs d'intervalles, analyse harmonique
```

### Mode Débogage
```bash
# Activer traçage pour développement
olca -T

# Voir toutes les étapes de raisonnement de l'IA
```

### Configuration Personnalisée
Éditez `olca.yml` :
```yaml
api_keyname: OPENAI_API_KEY_olca
model_name: gpt-4o-mini
recursion_limit: 50
temperature: 0.0
human: true
tracing: false
system_instructions: "Vous êtes un assistant de composition musicale expert."
```

---

## 🎼 Capacités Musicales Avancées

### Génération par Style
```
"Créer une fugue baroque dans le style de Bach"
"Générer un riff de blues en Mi"
"Composer une valse viennoise classique"
"Écrire une progression jazz ii-V-I"
```

### Analyse Musicale
```
"Analyser la structure harmonique de ce morceau"
"Identifier la gamme utilisée dans cette mélodie"
"Suggérer réharmonisation pour cette progression"
```

### Arrangements
```
"Arranger cette mélodie pour quatuor à cordes"
"Créer version piano de cet air folk"
"Adapter ce jazz standard pour guitare"
```

---

## 🛠️ Intégration Shell

OLCA peut exécuter des commandes pour créer workflows complets :

### Conversion Automatique
```
Vous : "Créer une progression blues et convertir en audio"

OLCA exécute :
1. Génère notation ABC blues
2. Sauvegarde comme blues.abc
3. Exécute : oabc blues.abc
4. Rapporte : "Créé blues.mid, blues.mp3, blues.svg"
```

### Traitement par Lots
```
Vous : "Convertir tous les fichiers ABC du dossier samples/"

OLCA exécute :
for file in samples/*.abc; do
    oabc "$file"
done
```

### Intégration Git
```
Vous : "Sauvegarder ma composition dans git avec message de commit approprié"

OLCA exécute :
git add ma_chanson.abc
git commit -m "Ajouter nouvelle composition ballade celtique"
```

---

## 🎵 Cas d'Usage Créatifs

### 1. Éducation Musicale
```
"Créer exercices de gammes pour débutant"
"Générer exemples de cadences classiques"
"Faire dictée musicale avec ABC"
```

### 2. Composition Collaborative
```
"Continuer cette mélodie que j'ai commencée"
"Ajouter contre-mélodie à ce thème"
"Harmoniser cette ligne de basse"
```

### 3. Exploration Stylistique
```
"Transformer ce thème classique en style jazz"
"Créer variation folk de cette mélodie"
"Adapter ce morceau pour différents instruments"
```

---

## 🔥 Fonctionnalités Spéciales

### Apprentissage Adaptatif
- OLCA se souvient de vos préférences
- Améliore suggestions au fil du temps
- Adapte son style à vos besoins

### Instructions Personnalisées
```bash
# Ajouter instructions spécifiques dans olca.yml
system_instructions: "Créer toujours en notation ABC. Privilégier style folk celtique. Utiliser tonalités simples."
```

### Intégration Workflow
- Création automatique de dossiers
- Génération de rapports
- Sauvegarde versionnée des créations

---

## 🛠️ Dépannage

### "Configuration OLCA manquante"
```bash
# Réinitialiser configuration
rm -f olca.yml
olca init -y
```

### "Clé API introuvable"
```bash
# Vérifier variable d'environnement
echo $OPENAI_API_KEY_olca

# Définir temporairement
export OPENAI_API_KEY_olca="votre-clé"
```

### "Limite de récursion atteinte"
```bash
# Augmenter limite dans olca.yml
sed -i 's/recursion_limit: [0-9]*/recursion_limit: 100/' olca.yml
```

### OLCA se bloque
```bash
# Arrêter avec Ctrl+C
# Redémarrer avec requête plus simple
olca
# "Créer mélodie simple de 8 mesures"
```

---

## 🎼 Intégration avec Autres Outils

### Avec Docker
```bash
# Utiliser OLCA dans environnement conteneurisé
(cd bin/testapp && dkrun)
# Dans le conteneur :
olca
```

### Avec Contrôle de Version
```bash
# OLCA peut aider avec workflows git
# Vous : "Créer nouvelle composition et la commiter proprement"
# L'IA gère tout le processus
```

### Avec Pipeline OABC
```bash
# Intégration transparente
# OLCA crée ABC → convertit automatiquement avec OABC
# Pipeline complet de l'idée à l'audio/partition
```

---

## 📚 Prochaines Étapes

1. **🐳 Configuration Docker** → `05-configuration-docker.md`
2. **🔧 Workflows avancés** → `06-workflows-avances.md`
3. **📖 Narration IA** → `07-narration-ia.md`

---

*🤖 OLCA transforme votre terminal en studio de composition IA - laissez l'intelligence artificielle amplifier votre créativité musicale !*
