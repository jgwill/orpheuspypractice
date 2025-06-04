# 🚀 Workflows Avancés - Guide Complet

*Automatisez vos processus musicaux avec des workflows professionnels*

---

## 🎯 Vue d'Ensemble

Ce guide vous montre comment créer des workflows musicaux avancés combinant plusieurs outils pour des résultats professionnels.

---

## 🔄 Workflows Batch pour Plusieurs Fichiers

### Traitement en Lot d'ABC vers MP3
```bash
# Script pour convertir tous les fichiers ABC d'un dossier
for abc_file in *.abc; do
    echo "🎵 Traitement de $abc_file"
    oabc "$abc_file" --output-mp3 --output-midi --output-score
done
```

### Pipeline Automatisé
```bash
#!/bin/bash
# workflow_musical.sh
INPUT_DIR="compositions"
OUTPUT_DIR="productions"

mkdir -p "$OUTPUT_DIR"/{midi,mp3,scores}

for abc in "$INPUT_DIR"/*.abc; do
    filename=$(basename "$abc" .abc)
    echo "🎼 Production de: $filename"
    
    # Génération MIDI
    oabc "$abc" --output-midi --output-dir "$OUTPUT_DIR/midi"
    
    # Génération MP3
    oabc "$abc" --output-mp3 --output-dir "$OUTPUT_DIR/mp3"
    
    # Génération partition
    oabc "$abc" --output-score --output-dir "$OUTPUT_DIR/scores"
done
```

---

## 🤖 Intégration avec l'IA OLCA

### Workflow de Composition Assistée
```bash
# 1. Générer une mélodie avec l'IA
echo "Compose une mélodie celtique en Do majeur" | olca --mode compose

# 2. Sauvegarder la réponse
olca --save-last-composition melody.abc

# 3. Produire tous les formats
oabc melody.abc --all-formats
```

### Workflow d'Analyse et Amélioration
```bash
# Analyser une composition existante
olca --analyze-file my_song.abc

# Obtenir des suggestions d'amélioration
echo "Comment améliorer cette mélodie?" | olca --context my_song.abc

# Appliquer les modifications suggérées
olca --apply-suggestions my_song.abc --output improved_song.abc
```

---

## 🐋 Workflows Docker Avancés

### Environnement de Production Docker
```dockerfile
# Dockerfile.production
FROM orpheuspypractice:latest

# Configuration pour la production
COPY compositions/ /app/input/
COPY scripts/batch_process.sh /app/

# Variables d'environnement
ENV BATCH_MODE=true
ENV OUTPUT_QUALITY=high
ENV PARALLEL_PROCESSING=4

# Point d'entrée pour traitement automatique
ENTRYPOINT ["/app/batch_process.sh"]
```

### Docker Compose pour Workflow Complet
```yaml
# docker-compose.workflow.yml
version: '3.8'
services:
  composer:
    build: .
    volumes:
      - ./input:/app/input
      - ./output:/app/output
    environment:
      - OLCA_API_KEY=${OLCA_API_KEY}
      - WORKFLOW_MODE=compose
  
  processor:
    build: .
    volumes:
      - ./output:/app/input
      - ./final:/app/output
    environment:
      - WORKFLOW_MODE=process
    depends_on:
      - composer
  
  quality_check:
    build: .
    volumes:
      - ./final:/app/input
    environment:
      - WORKFLOW_MODE=validate
    depends_on:
      - processor
```

---

## 🎼 Workflows de Collaboration

### Structure de Projet Collaboratif
```
projet_musical/
├── compositions/
│   ├── melodies/          # Mélodies principales
│   ├── harmonies/         # Accompagnements
│   └── arrangements/      # Arrangements finaux
├── scripts/
│   ├── validate.sh        # Validation ABC
│   ├── merge.sh          # Fusion de parties
│   └── produce.sh        # Production finale
└── config/
    ├── instruments.conf   # Configuration instruments
    └── styles.conf       # Styles musicaux
```

### Script de Validation Collaborative
```bash
#!/bin/bash
# validate_project.sh

echo "🔍 Validation du projet musical..."

# Vérifier la syntaxe ABC
for abc in compositions/**/*.abc; do
    if ! oabc "$abc" --validate-only; then
        echo "❌ Erreur dans: $abc"
        exit 1
    fi
done

# Générer un rapport de qualité
olca --analyze-project . --output rapport_qualité.md

echo "✅ Projet validé avec succès!"
```

---

## 🚀 Workflows d'Automatisation Avancés

### CI/CD Musical avec GitHub Actions
```yaml
# .github/workflows/musical-ci.yml
name: Production Musicale
on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Construire l'environnement
        run: docker build -t musical-env .
      - name: Valider les compositions
        run: docker run --rm -v $PWD:/workspace musical-env oabc --validate-all
  
  produce:
    needs: validate
    runs-on: ubuntu-latest
    steps:
      - name: Produire les médias
        run: |
          docker run --rm -v $PWD:/workspace musical-env \
            bash -c "cd /workspace && ./scripts/batch_produce.sh"
      - name: Archiver les résultats
        uses: actions/upload-artifact@v2
        with:
          name: productions-musicales
          path: output/
```

### Surveillance et Métriques
```bash
#!/bin/bash
# monitor_workflow.sh

LOG_FILE="workflow.log"
METRICS_FILE="metrics.json"

# Fonction de logging
log_metric() {
    echo "{\"timestamp\": \"$(date -Iseconds)\", \"metric\": \"$1\", \"value\": $2}" >> "$METRICS_FILE"
}

# Surveillance du workflow
start_time=$(date +%s)
echo "🚀 Début du workflow: $(date)" >> "$LOG_FILE"

# Traitement avec métriques
processed_count=0
error_count=0

for abc in input/*.abc; do
    if oabc "$abc" --all-formats; then
        ((processed_count++))
        log_metric "files_processed" $processed_count
    else
        ((error_count++))
        log_metric "errors" $error_count
    fi
done

end_time=$(date +%s)
duration=$((end_time - start_time))
log_metric "workflow_duration_seconds" $duration

echo "✅ Workflow terminé: $processed_count fichiers traités, $error_count erreurs" >> "$LOG_FILE"
```

---

## 🔧 Optimisation des Performances

### Traitement Parallèle
```bash
#!/bin/bash
# parallel_processing.sh

# Nombre de processus parallèles
MAX_JOBS=4

# Fonction de traitement d'un fichier
process_file() {
    local file="$1"
    echo "🎵 Traitement de $file (PID: $$)"
    oabc "$file" --all-formats --quiet
    echo "✅ Terminé: $file"
}

# Export de la fonction pour les sous-processus
export -f process_file

# Traitement parallèle avec GNU parallel (si installé)
if command -v parallel &> /dev/null; then
    find input/ -name "*.abc" | parallel -j$MAX_JOBS process_file
else
    # Alternative avec xargs
    find input/ -name "*.abc" | xargs -n1 -P$MAX_JOBS -I{} bash -c 'process_file "{}"'
fi
```

### Cache et Optimisation
```bash
#!/bin/bash
# optimized_workflow.sh

CACHE_DIR=".cache"
mkdir -p "$CACHE_DIR"

# Fonction de cache intelligent
process_with_cache() {
    local input_file="$1"
    local cache_key=$(md5sum "$input_file" | cut -d' ' -f1)
    local cache_file="$CACHE_DIR/$cache_key.processed"
    
    if [[ -f "$cache_file" && "$cache_file" -nt "$input_file" ]]; then
        echo "📦 Utilisation du cache pour: $input_file"
        return 0
    fi
    
    echo "🔄 Traitement de: $input_file"
    if oabc "$input_file" --all-formats; then
        touch "$cache_file"
        return 0
    else
        return 1
    fi
}
```

---

## 📊 Workflows d'Analyse et Reporting

### Génération de Rapports Automatisés
```bash
#!/bin/bash
# generate_report.sh

REPORT_FILE="rapport_musical_$(date +%Y%m%d).md"

cat > "$REPORT_FILE" << EOF
# 📈 Rapport de Production Musicale
*Généré le: $(date)*

## 📊 Statistiques
EOF

# Statistiques des fichiers
echo "- Fichiers ABC traités: $(find output/ -name "*.abc" | wc -l)" >> "$REPORT_FILE"
echo "- Fichiers MIDI générés: $(find output/ -name "*.mid" | wc -l)" >> "$REPORT_FILE"
echo "- Fichiers MP3 créés: $(find output/ -name "*.mp3" | wc -l)" >> "$REPORT_FILE"
echo "- Partitions PDF: $(find output/ -name "*.pdf" | wc -l)" >> "$REPORT_FILE"

# Analyse avec OLCA
echo -e "\n## 🎼 Analyse Musicale" >> "$REPORT_FILE"
olca --analyze-batch output/ --format markdown >> "$REPORT_FILE"

echo "📄 Rapport généré: $REPORT_FILE"
```

---

## 🛠️ Dépannage des Workflows

### Logs et Debugging
```bash
# Activer le mode debug
export DEBUG=1
export VERBOSE=1

# Logs détaillés
oabc input.abc --all-formats --verbose --log-file workflow.log

# Analyser les erreurs
grep "ERROR" workflow.log | tail -10
```

### Récupération d'Erreurs
```bash
#!/bin/bash
# error_recovery.sh

FAILED_DIR="failed_processing"
mkdir -p "$FAILED_DIR"

# Fonction de récupération
recover_failed() {
    local failed_file="$1"
    echo "🔧 Tentative de récupération: $failed_file"
    
    # Essayer avec différents paramètres
    if oabc "$failed_file" --force --ignore-warnings; then
        echo "✅ Récupération réussie"
    else
        echo "❌ Échec définitif, déplacement vers: $FAILED_DIR"
        mv "$failed_file" "$FAILED_DIR/"
    fi
}
```

---

## 💡 Conseils Pro

### 🚀 **Optimisation**
- Utilisez Docker pour des environnements reproductibles
- Implémentez un système de cache pour éviter les retraitements
- Parallélisez les tâches indépendantes

### 📊 **Monitoring**
- Loggez toutes les opérations importantes
- Surveillez les performances et les erreurs
- Générez des rapports automatisés

### 🔄 **Maintenance**
- Nettoyez régulièrement les caches et logs
- Validez vos workflows avec des données de test
- Documentez vos processus personnalisés

---

*🎯 **Prochaine étape**: Découvrez l'[IA et Narration Musicale](07-narration-ia.md) pour créer des histoires musicales interactives !*
