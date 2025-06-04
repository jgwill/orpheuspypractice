# 🔧 Advanced Workflows - Musical Production Pipelines

## What are Advanced Workflows?

**Advanced workflows** combine OrpheusPyPractice tools to create **complete musical production pipelines**:
- 🎼 **Multi-stage composition** - From idea to finished piece
- 🤖 **AI-assisted creation** - Generate, refine, and perfect
- 🔄 **Automated processing** - Batch convert, organize, and deploy
- 🎭 **Style-specific pipelines** - Jazz, Classical, Folk, etc.
- 📊 **Version control** - Track compositional evolution

**Perfect for:** Professional composers, music educators, production teams, and serious hobbyists.

---

## 🎯 Workflow 1: Complete Song Development

### Stage 1: Ideation with AI
```bash
# Start with AI brainstorming
olca init
olca

# Conversation:
You: "I want to write a Celtic ballad about lost love in Dm"
AI: "I'll create a foundation for your Celtic ballad..."

# AI generates initial structure
# Result: ballad_v1.abc
```

### Stage 2: Iterative Refinement
```bash
# Continue with AI assistance
You: "Make the A section more melancholy"
AI: [Generates ballad_v2.abc with modifications]

You: "Add ornamentation typical of Celtic music"  
AI: [Creates ballad_v3.abc with grace notes and turns]

You: "Create a contrasting B section that feels hopeful"
AI: [Develops ballad_v4.abc with major key shift]
```

### Stage 3: Production Pipeline
```bash
# Create production script
cat > produce_ballad.sh << 'EOF'
#!/bin/bash
VERSION="v4"
SONG="ballad_${VERSION}"

echo "🎼 Processing ${SONG}..."

# Convert to all formats
oabc ${SONG}.abc

# Create different arrangements
cp ${SONG}.abc ${SONG}_piano.abc
cp ${SONG}.abc ${SONG}_guitar.abc

# Generate lead sheet (without ornaments)
sed 's/{[^}]*}//g' ${SONG}.abc > ${SONG}_lead.abc
oabc ${SONG}_lead.abc

# Create practice tracks at different tempos
sed 's/Q:1\/4=[0-9]*/Q:1\/4=80/' ${SONG}.abc > ${SONG}_slow.abc
sed 's/Q:1\/4=[0-9]*/Q:1\/4=140/' ${SONG}.abc > ${SONG}_fast.abc

oabc ${SONG}_slow.abc
oabc ${SONG}_fast.abc

echo "✅ Production complete!"
ls -la ballad_*
EOF

chmod +x produce_ballad.sh
./produce_ballad.sh
```

### Stage 4: Portfolio Management
```bash
# Organize output
mkdir -p portfolio/celtic_ballads/${DATE}
mv ballad_* portfolio/celtic_ballads/${DATE}/

# Version control
git add portfolio/
git commit -m "Complete Celtic ballad composition - Lost Love in Dm"
git tag "ballad-lost-love-v1.0"
```

---

## 🎵 Workflow 2: Jazz Lead Sheet Factory

### Automated Jazz Generation
```bash
cat > jazz_factory.sh << 'EOF'
#!/bin/bash

# Jazz standards generator
PROGRESSIONS=(
    "Am7-D7-Gmaj7-Cmaj7"
    "Dm7-G7-Cmaj7-A7"
    "Em7-A7-Dm7-G7"
    "Cmaj7-Am7-Dm7-G7"
)

STYLES=("ballad" "swing" "bossa" "bebop")
KEYS=("C" "F" "Bb" "Eb" "G" "D")

for style in "${STYLES[@]}"; do
    for key in "${KEYS[@]}"; do
        # Generate with AI
        olca <<< "Create a ${style} jazz piece in ${key} major using ii-V-I progressions"
        
        # Rename output
        mv generated.abc jazz_${style}_${key}.abc
        
        # Convert to all formats
        oabc jazz_${style}_${key}.abc
        
        echo "✅ Created ${style} in ${key}"
    done
done
EOF

chmod +x jazz_factory.sh
./jazz_factory.sh
```

### Lead Sheet Optimization
```bash
# Create clean lead sheets
for file in jazz_*.abc; do
    # Extract melody and chords only
    grep -E '^[X|T|L|M|Q|K|"|\|]' "$file" > "${file%.abc}_lead.abc"
    
    # Generate clean sheet music
    oabc "${file%.abc}_lead.abc"
done
```

---

## 🎼 Workflow 3: Educational Content Pipeline

### Batch Exercise Generator
```bash
cat > exercise_generator.sh << 'EOF'
#!/bin/bash

# Scale exercises for all keys
KEYS=("C" "G" "D" "A" "E" "B" "F#" "Db" "Ab" "Eb" "Bb" "F")
MODES=("major" "minor" "dorian" "mixolydian")

for key in "${KEYS[@]}"; do
    for mode in "${MODES[@]}"; do
        olca <<< "Create a ${mode} scale exercise in ${key}, 2 octaves, quarter notes"
        mv generated.abc scales_${key}_${mode}.abc
        oabc scales_${key}_${mode}.abc
    done
done

# Organize by difficulty
mkdir -p exercises/{beginner,intermediate,advanced}
mv scales_*_major.abc exercises/beginner/
mv scales_*_minor.abc exercises/beginner/
mv scales_*_dorian.abc exercises/intermediate/
mv scales_*_mixolydian.abc exercises/advanced/

# Convert all
find exercises/ -name "*.abc" -exec oabc {} \;
EOF

chmod +x exercise_generator.sh
./exercise_generator.sh
```

### Curriculum Builder
```bash
# Create lesson plans with embedded audio
cat > create_lesson.sh << 'EOF'
#!/bin/bash
LESSON_NAME="$1"
TOPIC="$2"

mkdir -p "lessons/${LESSON_NAME}"
cd "lessons/${LESSON_NAME}"

# Generate examples with AI
olca <<< "Create 5 progressive examples for teaching ${TOPIC}"

# Convert all examples
for i in {1..5}; do
    oabc example_${i}.abc
done

# Create lesson markdown
cat > lesson.md << EOF
# ${TOPIC} Lesson

## Examples

$(for i in {1..5}; do
    echo "### Example $i"
    echo "![Sheet Music](example_${i}.svg)"
    echo "[Listen (MP3)](example_${i}.mp3)"
    echo "[MIDI File](example_${i}.mid)"
    echo ""
done)
EOF

echo "✅ Lesson '${LESSON_NAME}' created!"
EOF

chmod +x create_lesson.sh

# Usage
./create_lesson.sh "chord-progressions" "Basic Chord Progressions"
./create_lesson.sh "counterpoint" "Introduction to Counterpoint"
```

---

## 🎭 Workflow 4: Style-Specific Production

### Baroque Counterpoint Pipeline
```bash
cat > baroque_workshop.sh << 'EOF'
#!/bin/bash

# Generate baroque-style compositions
FORMS=("invention" "fugue_subject" "chorale" "prelude")

for form in "${FORMS[@]}"; do
    echo "🎼 Creating ${form}..."
    
    # AI generation with specific instructions
    olca <<< "Create a ${form} in the style of J.S. Bach, use proper voice leading and counterpoint rules"
    
    # Rename and process
    mv generated.abc baroque_${form}.abc
    
    # Create different voicings
    if [ "$form" = "fugue_subject" ]; then
        # Create subject, answer, and full exposition
        cp baroque_${form}.abc baroque_${form}_subject.abc
        olca <<< "Create the tonal answer for this fugue subject: $(cat baroque_${form}.abc)"
        mv generated.abc baroque_${form}_answer.abc
        
        olca <<< "Create a full fugue exposition using this subject and answer"
        mv generated.abc baroque_${form}_exposition.abc
    fi
    
    # Convert all variations
    oabc baroque_${form}*.abc
done

# Create Bach-style collection
mkdir -p compositions/baroque_collection
mv baroque_* compositions/baroque_collection/
EOF

chmod +x baroque_workshop.sh
./baroque_workshop.sh
```

### Folk Song Collector
```bash
cat > folk_collector.sh << 'EOF'
#!/bin/bash

# Collect folk songs from different traditions
TRADITIONS=("irish" "scottish" "appalachian" "nordic" "eastern_european")
FORMS=("jig" "reel" "ballad" "hornpipe" "waltz")

for tradition in "${TRADITIONS[@]}"; do
    mkdir -p "folk_collection/${tradition}"
    
    for form in "${FORMS[@]}"; do
        echo "🎵 Creating ${tradition} ${form}..."
        
        olca <<< "Create an authentic ${tradition} ${form} with traditional characteristics and ornamentation"
        
        mv generated.abc "folk_collection/${tradition}/${tradition}_${form}.abc"
        
        # Create both ornamented and plain versions
        sed 's/{[^}]*}//g' "folk_collection/${tradition}/${tradition}_${form}.abc" > \
            "folk_collection/${tradition}/${tradition}_${form}_plain.abc"
    done
    
    # Convert all songs in this tradition
    find "folk_collection/${tradition}/" -name "*.abc" -exec oabc {} \;
done
EOF

chmod +x folk_collector.sh
./folk_collector.sh
```

---

## 🔄 Workflow 5: Automated Arrangement Pipeline

### Multi-Instrument Arrangements
```bash
cat > arrangement_pipeline.sh << 'EOF'
#!/bin/bash
SONG="$1"  # Input ABC file

if [ ! -f "$SONG" ]; then
    echo "Usage: $0 song.abc"
    exit 1
fi

BASE="${SONG%.abc}"

echo "🎼 Creating arrangements for ${BASE}..."

# Create different instrument arrangements
INSTRUMENTS=(
    "piano:C_major:treble_bass"
    "guitar:tabs:standard_tuning"
    "violin:C_major:treble"
    "flute:C_major:treble"
    "trumpet:Bb_major:treble"
    "sax_alto:Eb_major:treble"
)

for inst_config in "${INSTRUMENTS[@]}"; do
    IFS=':' read -r instrument key clef <<< "$inst_config"
    
    echo "Creating ${instrument} arrangement..."
    
    # Use AI to create arrangement
    olca <<< "Arrange this piece for ${instrument} in ${key}, optimize for ${clef} clef: $(cat ${SONG})"
    
    mv generated.abc "${BASE}_${instrument}.abc"
    oabc "${BASE}_${instrument}.abc"
done

# Create ensemble score
olca <<< "Create a chamber ensemble arrangement (violin, viola, cello, piano) for: $(cat ${SONG})"
mv generated.abc "${BASE}_chamber_ensemble.abc"
oabc "${BASE}_chamber_ensemble.abc"

# Create fake book lead sheet
olca <<< "Create a jazz fake book lead sheet with melody and chord symbols: $(cat ${SONG})"
mv generated.abc "${BASE}_lead_sheet.abc"
oabc "${BASE}_lead_sheet.abc"

echo "✅ All arrangements complete!"
ls -la ${BASE}_*
EOF

chmod +x arrangement_pipeline.sh

# Usage
./arrangement_pipeline.sh my_song.abc
```

---

## 📊 Workflow 6: Analytics and Version Control

### Composition Analytics
```bash
cat > analyze_compositions.sh << 'EOF'
#!/bin/bash

# Analyze musical content of ABC files
echo "🎼 Musical Analytics Report"
echo "=========================="

# Count compositions by key
echo "## Key Distribution"
find . -name "*.abc" -exec grep "^K:" {} \; | sort | uniq -c | sort -nr

# Count time signatures
echo -e "\n## Time Signatures"
find . -name "*.abc" -exec grep "^M:" {} \; | sort | uniq -c | sort -nr

# Count tempos
echo -e "\n## Tempo Markings"
find . -name "*.abc" -exec grep "^Q:" {} \; | sort | uniq -c | sort -nr

# Analyze by style (based on filename)
echo -e "\n## Style Distribution"
find . -name "*.abc" | sed 's/.*\///' | cut -d'_' -f1 | sort | uniq -c | sort -nr

# File statistics
echo -e "\n## Collection Statistics"
echo "Total compositions: $(find . -name "*.abc" | wc -l)"
echo "Generated MIDI files: $(find . -name "*.mid" | wc -l)"
echo "Generated audio files: $(find . -name "*.mp3" | wc -l)"
echo "Generated sheet music: $(find . -name "*.svg" | wc -l)"
EOF

chmod +x analyze_compositions.sh
./analyze_compositions.sh > analytics_report.md
```

### Advanced Git Workflow
```bash
cat > musical_git_workflow.sh << 'EOF'
#!/bin/bash

# Musical version control workflow
OPERATION="$1"

case "$OPERATION" in
    "start-piece")
        PIECE_NAME="$2"
        git checkout -b "compose/${PIECE_NAME}"
        mkdir -p "compositions/${PIECE_NAME}/versions"
        echo "Started composition: ${PIECE_NAME}"
        ;;
        
    "version")
        # Save current version with timestamp
        TIMESTAMP=$(date +%Y%m%d_%H%M%S)
        CURRENT_BRANCH=$(git branch --show-current)
        PIECE_NAME=$(echo $CURRENT_BRANCH | cut -d'/' -f2)
        
        cp *.abc "compositions/${PIECE_NAME}/versions/${PIECE_NAME}_${TIMESTAMP}.abc"
        git add "compositions/${PIECE_NAME}/versions/"
        git commit -m "Version ${TIMESTAMP} of ${PIECE_NAME}"
        ;;
        
    "finalize")
        PIECE_NAME="$2"
        # Convert final version
        oabc "compositions/${PIECE_NAME}/${PIECE_NAME}.abc"
        
        # Move to main
        git add .
        git commit -m "Finalize ${PIECE_NAME}"
        git checkout main
        git merge "compose/${PIECE_NAME}"
        git tag "release/${PIECE_NAME}-v1.0"
        
        echo "✅ ${PIECE_NAME} finalized and tagged!"
        ;;
        
    "release")
        # Create release package
        VERSION=$(git describe --tags --abbrev=0)
        mkdir -p "releases/${VERSION}"
        
        # Copy all generated files
        find . -name "*.abc" -o -name "*.mid" -o -name "*.mp3" -o -name "*.svg" | \
            xargs -I {} cp {} "releases/${VERSION}/"
        
        # Create release notes
        git log --oneline $(git describe --tags --abbrev=0 HEAD~1)..HEAD > "releases/${VERSION}/CHANGELOG.md"
        
        echo "📦 Release ${VERSION} packaged!"
        ;;
esac
EOF

chmod +x musical_git_workflow.sh

# Usage examples:
# ./musical_git_workflow.sh start-piece "autumn-waltz"
# ./musical_git_workflow.sh version
# ./musical_git_workflow.sh finalize "autumn-waltz" 
# ./musical_git_workflow.sh release
```

---

## 🎯 Workflow 7: Production Deployment

### Web Publishing Pipeline
```bash
cat > web_publisher.sh << 'EOF'
#!/bin/bash

# Generate web-ready musical content
OUTPUT_DIR="web_output"
mkdir -p "$OUTPUT_DIR"/{audio,sheets,midi}

echo "🌐 Preparing web content..."

# Convert all ABC to web formats
for abc_file in *.abc; do
    if [ -f "$abc_file" ]; then
        base="${abc_file%.abc}"
        
        # Generate all formats
        oabc "$abc_file"
        
        # Copy to web directories
        [ -f "${base}.mp3" ] && cp "${base}.mp3" "$OUTPUT_DIR/audio/"
        [ -f "${base}.svg" ] && cp "${base}.svg" "$OUTPUT_DIR/sheets/"
        [ -f "${base}.mid" ] && cp "${base}.mid" "$OUTPUT_DIR/midi/"
    fi
done

# Generate index.html
cat > "$OUTPUT_DIR/index.html" << 'HTML'
<!DOCTYPE html>
<html>
<head>
    <title>Musical Collection</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .piece { margin: 20px 0; padding: 20px; border: 1px solid #ddd; }
        audio { width: 100%; margin: 10px 0; }
        img { max-width: 100%; }
    </style>
</head>
<body>
    <h1>🎵 Musical Collection</h1>
HTML

# Add each piece to index
for abc_file in *.abc; do
    if [ -f "$abc_file" ]; then
        base="${abc_file%.abc}"
        title=$(grep "^T:" "$abc_file" | head -1 | cut -d':' -f2- | tr -d ' ')
        
        cat >> "$OUTPUT_DIR/index.html" << HTML
    <div class="piece">
        <h2>${title}</h2>
        <audio controls>
            <source src="audio/${base}.mp3" type="audio/mpeg">
        </audio>
        <br>
        <img src="sheets/${base}.svg" alt="Sheet Music">
        <br>
        <a href="midi/${base}.mid">Download MIDI</a>
    </div>
HTML
    fi
done

echo "</body></html>" >> "$OUTPUT_DIR/index.html"

echo "✅ Web content ready in $OUTPUT_DIR/"
echo "Open $OUTPUT_DIR/index.html in browser to view"
EOF

chmod +x web_publisher.sh
./web_publisher.sh
```

---

## 🔥 Pro Workflow Tips

### 1. Automation Templates
```bash
# Create workflow templates
mkdir -p ~/.orpheus/workflows
cp *.sh ~/.orpheus/workflows/

# Make global command
echo 'export PATH="$HOME/.orpheus/workflows:$PATH"' >> ~/.bashrc
```

### 2. Parallel Processing
```bash
# Process multiple files in parallel
find . -name "*.abc" | xargs -P 4 -I {} oabc {}

# Parallel AI generation
for style in jazz classical folk; do
    (olca <<< "Create ${style} piece" &)
done
wait
```

### 3. Quality Control
```bash
# Validate all ABC files
for abc in *.abc; do
    abc2midi "$abc" -o /dev/null && echo "✅ $abc" || echo "❌ $abc"
done
```

### 4. Backup Strategies
```bash
# Automated backups
rsync -av compositions/ backup/compositions_$(date +%Y%m%d)/
tar czf "musical_backup_$(date +%Y%m%d).tar.gz" compositions/
```

---

## 📚 Next Steps

1. **🎭 Musical storytelling** → `07-ai-storytelling.md`
2. **🆘 Troubleshooting** → `08-troubleshooting.md`
3. **🔄 Return to basics** → `01-quick-start.md`

---

*🔧 Advanced workflows transform OrpheusPyPractice from a tool into a complete musical production system!*
