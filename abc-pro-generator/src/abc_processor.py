"""
ABC Processor - Core ABC notation processing functionality
"""

import re
import mido
from pathlib import Path
from typing import Tuple, List, Optional, Dict, Any

class ABCProcessor:
    """Handles ABC notation parsing, validation, and conversion"""
    
    def __init__(self):
        self.abc_headers = ['X:', 'T:', 'M:', 'L:', 'K:']
    
    def validate(self, abc_content: str) -> Tuple[bool, List[str]]:
        """Validate ABC notation syntax"""
        errors = []
        warnings = []
        
        lines = abc_content.strip().split('\n')
        
        # Check for required headers
        has_x = any(line.startswith('X:') for line in lines)
        has_k = any(line.startswith('K:') for line in lines)
        
        if not has_x:
            errors.append("Missing X: (reference number) header")
        if not has_k:
            errors.append("Missing K: (key signature) header")
        
        # Check for musical content (notes or bars)
        has_music = any('|' in line or any(note in line for note in 'CDEFGABcdefgab') 
                       for line in lines if not line.startswith(tuple(self.abc_headers)))
        
        if not has_music:
            warnings.append("No musical content found")
        
        # Basic syntax checks
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue
                
            # Check for invalid characters in music lines
            if not line.startswith(tuple(self.abc_headers + ['%', 'w:'])):
                invalid_chars = re.findall(r'[^A-Ga-g0-9/|:.\-_\s"()^=,\'<>\\[\]{}#b]', line)
                if invalid_chars:
                    warnings.append(f"Line {i}: Potentially invalid characters: {set(invalid_chars)}")
        
        all_issues = errors + warnings
        return len(errors) == 0, all_issues
    
    def parse_metadata(self, abc_content: str) -> Dict[str, str]:
        """Extract metadata from ABC notation"""
        metadata = {}
        
        for line in abc_content.split('\n'):
            line = line.strip()
            if ':' in line and any(line.startswith(header) for header in self.abc_headers + ['C:', 'A:', 'O:', 'R:', 'S:']):
                key, value = line.split(':', 1)
                metadata[key] = value.strip()
        
        return metadata
    
    def convert(self, input_file: str, target_format: str) -> str:
        """Convert ABC file to other formats"""
        input_path = Path(input_file)
        
        if not input_path.exists():
            raise FileNotFoundError(f"File not found: {input_file}")
        
        if target_format == 'midi':
            return self.convert_to_midi(input_path)
        elif target_format in ['wav', 'mp3']:
            # For now, just convert to MIDI and note that audio conversion needs additional tools
            midi_file = self.convert_to_midi(input_path)
            return f"{midi_file} (Note: Audio conversion requires additional tools like timidity++ or fluidsynth)"
        else:
            raise ValueError(f"Unsupported format: {target_format}")
    
    def convert_to_midi(self, abc_file: Path) -> str:
        """Convert ABC to MIDI (basic implementation)"""
        # This is a simplified conversion - in a real implementation,
        # you'd use a proper ABC to MIDI converter
        
        output_file = abc_file.with_suffix('.mid')
        
        # Read ABC content
        with open(abc_file, 'r') as f:
            abc_content = f.read()
        
        # Extract basic info
        metadata = self.parse_metadata(abc_content)
        
        # Create a simple MIDI file
        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)
        
        # Add basic tempo
        track.append(mido.MetaMessage('set_tempo', tempo=500000, time=0))
        
        # Simple note extraction (very basic)
        notes = self.extract_notes(abc_content)
        
        for note in notes:
            # Convert ABC note to MIDI note number
            midi_note = self.abc_note_to_midi(note)
            if midi_note:
                track.append(mido.Message('note_on', channel=0, note=midi_note, velocity=64, time=0))
                track.append(mido.Message('note_off', channel=0, note=midi_note, velocity=64, time=480))
        
        # Save MIDI file
        mid.save(output_file)
        
        return str(output_file)
    
    def extract_notes(self, abc_content: str) -> List[str]:
        """Extract notes from ABC content (basic implementation)"""
        notes = []
        
        for line in abc_content.split('\n'):
            line = line.strip()
            # Skip header lines and comments
            if line.startswith(tuple(self.abc_headers + ['%', 'w:'])) or not line:
                continue
            
            # Extract notes (simplified)
            note_pattern = r'[A-Ga-g][#b]?[0-9/]*'
            found_notes = re.findall(note_pattern, line)
            notes.extend(found_notes)
        
        return notes
    
    def abc_note_to_midi(self, abc_note: str) -> Optional[int]:
        """Convert ABC note to MIDI note number"""
        # Remove ornaments and length indicators
        clean_note = re.sub(r'[0-9/]+$', '', abc_note)
        
        # Basic note mapping (C4 = 60)
        note_map = {
            'C': 60, 'D': 62, 'E': 64, 'F': 65, 'G': 67, 'A': 69, 'B': 71,
            'c': 72, 'd': 74, 'e': 76, 'f': 77, 'g': 79, 'a': 81, 'b': 83
        }
        
        base_note = clean_note[0]
        if base_note in note_map:
            midi_note = note_map[base_note]
            
            # Handle sharps and flats
            if '#' in clean_note:
                midi_note += 1
            elif 'b' in clean_note:
                midi_note -= 1
            
            return midi_note
        
        return None
    
    def generate_sample_abc(self, title: str = "Sample Song", key: str = "C") -> str:
        """Generate a simple sample ABC notation"""
        return f"""X:1
T:{title}
M:4/4
L:1/4
K:{key}
C D E F | G A B c | c B A G | F E D C |"""
