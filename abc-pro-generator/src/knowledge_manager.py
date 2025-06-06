"""
Knowledge Manager - Handles learning and knowledge storage for OLCA
"""

import json
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

class KnowledgeManager:
    """Manages OLCA's learning system and knowledge base"""
    
    def __init__(self, instructions_file: Path, db_file: Path):
        self.instructions_file = instructions_file
        self.db_file = db_file
        self.instructions = self.load_instructions()
        self.db = self.load_database()
    
    def load_instructions(self) -> List[str]:
        """Load instructions from .olca-instructions.md"""
        if self.instructions_file.exists():
            try:
                with open(self.instructions_file, 'r') as f:
                    content = f.read()
                
                # Extract instructions from markdown
                instructions = []
                for line in content.split('\n'):
                    if line.startswith('- ') or line.startswith('* '):
                        instructions.append(line[2:].strip())
                
                return instructions
            except Exception as e:
                print(f"Warning: Could not load instructions: {e}")
        
        return []
    
    def load_database(self) -> Dict[str, Any]:
        """Load knowledge database from .olca-db.json"""
        if self.db_file.exists():
            try:
                with open(self.db_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Warning: Could not load database: {e}")
        
        return {
            'created': datetime.now().isoformat(),
            'entries': {},
            'user_preferences': {},
            'musical_patterns': [],
            'learned_styles': {},
            'statistics': {
                'total_requests': 0,
                'successful_generations': 0,
                'user_feedback_count': 0
            }
        }
    
    def save_instructions(self):
        """Save instructions to .olca-instructions.md"""
        content = f"""# OLCA Learned Instructions
*Auto-generated file - stores learned behaviors and instructions*

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Instructions

"""
        for instruction in self.instructions:
            content += f"- {instruction}\n"
        
        content += """
## Usage Notes

This file contains instructions that OLCA has learned from user interactions.
You can manually edit this file to teach OLCA new behaviors.
"""
        
        with open(self.instructions_file, 'w') as f:
            f.write(content)
    
    def save_database(self):
        """Save knowledge database to .olca-db.json"""
        self.db['last_updated'] = datetime.now().isoformat()
        
        with open(self.db_file, 'w') as f:
            json.dump(self.db, f, indent=2)
    
    def add_instruction(self, instruction: str):
        """Add a new learned instruction"""
        if instruction not in self.instructions:
            self.instructions.append(instruction)
            self.save_instructions()
            
            # Also log to database
            self.add_entry('learned_instructions', {
                'instruction': instruction,
                'timestamp': datetime.now().isoformat()
            })
    
    def add_entry(self, category: str, data: Dict[str, Any]):
        """Add an entry to the knowledge database"""
        if category not in self.db['entries']:
            self.db['entries'][category] = []
        
        entry = {
            'id': len(self.db['entries'][category]) + 1,
            'timestamp': datetime.now().isoformat(),
            **data
        }
        
        self.db['entries'][category].append(entry)
        self.save_database()
    
    def get_entries(self, category: str) -> List[Dict[str, Any]]:
        """Get all entries from a category"""
        return self.db['entries'].get(category, [])
    
    def update_statistics(self, stat_name: str, increment: int = 1):
        """Update a statistic in the database"""
        if stat_name in self.db['statistics']:
            self.db['statistics'][stat_name] += increment
        else:
            self.db['statistics'][stat_name] = increment
        
        self.save_database()
    
    def add_user_preference(self, key: str, value: Any):
        """Add or update a user preference"""
        self.db['user_preferences'][key] = {
            'value': value,
            'updated': datetime.now().isoformat()
        }
        self.save_database()
    
    def get_user_preference(self, key: str, default: Any = None) -> Any:
        """Get a user preference"""
        if key in self.db['user_preferences']:
            return self.db['user_preferences'][key]['value']
        return default
    
    def add_musical_pattern(self, pattern: Dict[str, Any]):
        """Add a recognized musical pattern"""
        pattern['learned_at'] = datetime.now().isoformat()
        self.db['musical_patterns'].append(pattern)
        self.save_database()
    
    def get_musical_patterns(self, style: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get musical patterns, optionally filtered by style"""
        patterns = self.db['musical_patterns']
        
        if style:
            patterns = [p for p in patterns if p.get('style', '').lower() == style.lower()]
        
        return patterns
    
    def learn_style_preference(self, request: str, generated_abc: str, user_feedback: str):
        """Learn from user feedback about generated music"""
        style_key = self.extract_style_from_request(request)
        
        if style_key not in self.db['learned_styles']:
            self.db['learned_styles'][style_key] = {
                'examples': [],
                'preferences': {},
                'feedback_history': []
            }
        
        # Add example
        example = {
            'request': request,
            'abc_notation': generated_abc,
            'user_feedback': user_feedback,
            'timestamp': datetime.now().isoformat()
        }
        
        self.db['learned_styles'][style_key]['examples'].append(example)
        
        # Update preferences based on feedback
        if 'good' in user_feedback.lower() or 'great' in user_feedback.lower():
            self.update_style_preferences(style_key, generated_abc, positive=True)
        elif 'bad' in user_feedback.lower() or 'wrong' in user_feedback.lower():
            self.update_style_preferences(style_key, generated_abc, positive=False)
        
        self.save_database()
        self.update_statistics('user_feedback_count')
    
    def extract_style_from_request(self, request: str) -> str:
        """Extract musical style from request"""
        request_lower = request.lower()
        
        # Common musical styles
        styles = ['folk', 'classical', 'jazz', 'blues', 'country', 'irish', 'scottish', 
                 'celtic', 'baroque', 'waltz', 'march', 'ballad']
        
        for style in styles:
            if style in request_lower:
                return style
        
        return 'general'
    
    def update_style_preferences(self, style: str, abc_notation: str, positive: bool):
        """Update preferences for a musical style based on feedback"""
        # Analyze the ABC notation for patterns
        # This is simplified - in a real implementation, you'd do more sophisticated analysis
        
        patterns = self.analyze_abc_patterns(abc_notation)
        
        if positive:
            # Reinforce these patterns for this style
            for pattern, value in patterns.items():
                if pattern not in self.db['learned_styles'][style]['preferences']:
                    self.db['learned_styles'][style]['preferences'][pattern] = 0
                self.db['learned_styles'][style]['preferences'][pattern] += value
        else:
            # Discourage these patterns for this style
            for pattern, value in patterns.items():
                if pattern not in self.db['learned_styles'][style]['preferences']:
                    self.db['learned_styles'][style]['preferences'][pattern] = 0
                self.db['learned_styles'][style]['preferences'][pattern] -= value
    
    def analyze_abc_patterns(self, abc_notation: str) -> Dict[str, float]:
        """Analyze ABC notation for musical patterns"""
        patterns = {}
        
        # Extract key signature
        for line in abc_notation.split('\n'):
            if line.startswith('K:'):
                key = line[2:].strip()
                patterns[f'key_{key}'] = 1.0
            elif line.startswith('M:'):
                meter = line[2:].strip()
                patterns[f'meter_{meter}'] = 1.0
        
        # Count note patterns (simplified)
        notes = ''.join([c for c in abc_notation if c in 'CDEFGABcdefgab'])
        if notes:
            patterns['note_density'] = len(notes) / len(abc_notation.replace('\n', ''))
        
        return patterns
    
    def get_style_recommendations(self, style: str) -> Dict[str, Any]:
        """Get recommendations for generating music in a specific style"""
        if style in self.db['learned_styles']:
            return self.db['learned_styles'][style]['preferences']
        return {}
    
    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of the knowledge base"""
        return {
            'instructions_count': len(self.instructions),
            'database_entries': {k: len(v) for k, v in self.db['entries'].items()},
            'user_preferences_count': len(self.db['user_preferences']),
            'musical_patterns_count': len(self.db['musical_patterns']),
            'learned_styles': list(self.db['learned_styles'].keys()),
            'statistics': self.db['statistics'],
            'last_updated': self.db.get('last_updated', 'Never')
        }
