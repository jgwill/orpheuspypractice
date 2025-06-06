#!/usr/bin/env python3
"""
OABC-Pro - Orpheus ABC Pro Generator
A CLI Langchain Agent for musical and storytelling assistance

Goals:
- Process natural language requests for music generation
- Learn from user interactions and store knowledge
- Provide Python code interpretation and shell actions
- Support ABC notation processing and conversion
"""

import os
import sys
import json
import yaml
import click
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from datetime import datetime
from typing import Dict, List, Optional, Any

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from abc_processor import ABCProcessor
from knowledge_manager import KnowledgeManager
from llm_interface import LLMInterface

console = Console()

class OLCAAgent:
    """Main OLCA Agent class"""
    
    def __init__(self):
        self.config_file = Path("olca.conf")
        self.instructions_file = Path(".olca-instructions.md")
        self.db_file = Path(".olca-db.json")
        
        self.config = self.load_config()
        self.knowledge = KnowledgeManager(self.instructions_file, self.db_file)
        self.abc_processor = ABCProcessor()
        self.llm = LLMInterface(self.config.get('llm', {}))
        
        console.print(Panel.fit("🎵 OLCA - Orpheus Language Cognitive Agent", style="bold blue"))
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from olca.conf"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return yaml.safe_load(f)
            except Exception as e:
                console.print(f"[yellow]Warning: Could not load config: {e}[/yellow]")
        
        # Default configuration
        default_config = {
            'llm': {
                'provider': 'openai',
                'model': 'gpt-4',
                'api_key': os.getenv('OPENAI_API_KEY')
            },
            'music': {
                'default_key': 'C',
                'default_time': '4/4',
                'default_style': 'folk'
            },
            'learning': {
                'auto_save': True,
                'feedback_collection': True
            }
        }
        
        # Save default config
        self.save_config(default_config)
        return default_config
    
    def save_config(self, config: Dict[str, Any]):
        """Save configuration to olca.conf"""
        with open(self.config_file, 'w') as f:
            yaml.dump(config, f, default_flow_style=False)
    
    def process_request(self, request: str) -> str:
        """Process a natural language request"""
        console.print(f"[cyan]Processing: {request}[/cyan]")
        
        # Check if this is a musical request
        if any(keyword in request.lower() for keyword in ['melody', 'song', 'music', 'abc', 'chord', 'scale']):
            return self.handle_musical_request(request)
        
        # Check if this is a file processing request
        if any(keyword in request.lower() for keyword in ['convert', 'process', 'render', 'validate']):
            return self.handle_file_request(request)
        
        # Check if this is a learning request
        if any(keyword in request.lower() for keyword in ['learn', 'remember', 'save', 'knowledge']):
            return self.handle_learning_request(request)
        
        # General LLM request
        return self.llm.generate_response(request)
    
    def handle_musical_request(self, request: str) -> str:
        """Handle musical generation requests"""
        try:
            # Use LLM to generate ABC notation
            abc_prompt = f"""Generate ABC notation for: {request}
            
Please provide valid ABC notation with proper headers (X:, T:, M:, L:, K:) 
and musical content. Follow ABC notation standards."""
            
            abc_response = self.llm.generate_response(abc_prompt)
            
            # Extract ABC notation from response
            abc_notation = self.extract_abc_notation(abc_response)
            
            if abc_notation:
                # Validate the ABC notation
                is_valid, errors = self.abc_processor.validate(abc_notation)
                
                if is_valid:
                    console.print("[green]✓ Generated valid ABC notation[/green]")
                    
                    # Save to knowledge base
                    self.knowledge.add_entry('musical_generation', {
                        'request': request,
                        'abc_notation': abc_notation,
                        'timestamp': datetime.now().isoformat()
                    })
                    
                    return abc_notation
                else:
                    console.print(f"[yellow]⚠ ABC validation warnings: {errors}[/yellow]")
                    return abc_notation
            else:
                return "Could not extract valid ABC notation from LLM response."
                
        except Exception as e:
            console.print(f"[red]Error generating music: {e}[/red]")
            return f"Error: {e}"
    
    def handle_file_request(self, request: str) -> str:
        """Handle file processing requests"""
        # Simple file operation parsing
        words = request.lower().split()
        
        if 'convert' in words:
            return self.handle_conversion_request(request)
        elif 'validate' in words:
            return self.handle_validation_request(request)
        elif 'render' in words:
            return self.handle_render_request(request)
        else:
            return "File operation not recognized. Try: convert, validate, or render."
    
    def handle_conversion_request(self, request: str) -> str:
        """Handle file conversion requests"""
        # Extract file path and format from request
        words = request.split()
        file_path = None
        target_format = None
        
        for i, word in enumerate(words):
            if word.endswith('.abc'):
                file_path = word
            elif word in ['midi', 'wav', 'mp3'] and i > 0 and words[i-1] in ['to', 'format']:
                target_format = word
        
        if not file_path:
            return "Please specify an ABC file to convert."
        
        if not target_format:
            target_format = 'midi'  # Default
        
        try:
            result = self.abc_processor.convert(file_path, target_format)
            return f"Converted {file_path} to {target_format}: {result}"
        except Exception as e:
            return f"Conversion error: {e}"
    
    def handle_validation_request(self, request: str) -> str:
        """Handle ABC validation requests"""
        words = request.split()
        file_path = None
        
        for word in words:
            if word.endswith('.abc'):
                file_path = word
                break
        
        if not file_path:
            return "Please specify an ABC file to validate."
        
        try:
            if not Path(file_path).exists():
                return f"File not found: {file_path}"
            
            with open(file_path, 'r') as f:
                abc_content = f.read()
            
            is_valid, errors = self.abc_processor.validate(abc_content)
            
            if is_valid:
                return f"✓ {file_path} is valid ABC notation"
            else:
                return f"✗ {file_path} has validation errors: {errors}"
                
        except Exception as e:
            return f"Validation error: {e}"
    
    def handle_render_request(self, request: str) -> str:
        """Handle ABC rendering requests"""
        return "Rendering functionality not yet implemented."
    
    def handle_learning_request(self, request: str) -> str:
        """Handle learning and knowledge management requests"""
        if 'learn' in request.lower():
            # Extract what to learn
            learn_content = request.replace('learn', '').strip()
            self.knowledge.add_instruction(learn_content)
            return f"✓ Learned: {learn_content}"
        
        elif 'remember' in request.lower():
            # Store information
            info_content = request.replace('remember', '').strip()
            self.knowledge.add_entry('user_info', {
                'content': info_content,
                'timestamp': datetime.now().isoformat()
            })
            return f"✓ Remembered: {info_content}"
        
        else:
            return "Learning request not understood. Use 'learn' or 'remember'."
    
    def extract_abc_notation(self, text: str) -> Optional[str]:
        """Extract ABC notation from LLM response"""
        lines = text.split('\n')
        abc_lines = []
        in_abc = False
        
        for line in lines:
            line = line.strip()
            if line.startswith('X:'):
                in_abc = True
            if in_abc:
                abc_lines.append(line)
            # Stop at empty line after ABC content
            if in_abc and not line and abc_lines:
                break
        
        return '\n'.join(abc_lines) if abc_lines else None
    
    def interactive_mode(self):
        """Run in interactive mode"""
        console.print("[bold green]Entering interactive mode. Type 'exit' to quit.[/bold green]")
        
        while True:
            try:
                request = Prompt.ask("\n[bold cyan]OLCA[/bold cyan]")
                
                if request.lower() in ['exit', 'quit', 'bye']:
                    console.print("[yellow]Goodbye![/yellow]")
                    break
                
                if request.strip():
                    response = self.process_request(request)
                    console.print(f"[green]Response:[/green] {response}")
                
            except KeyboardInterrupt:
                console.print("\n[yellow]Goodbye![/yellow]")
                break
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")

@click.command()
@click.argument('request', required=False)
@click.option('--interactive', '-i', is_flag=True, help='Run in interactive mode')
@click.option('--config', help='Show current configuration')
@click.option('--knowledge', help='Show knowledge base')
def main(request, interactive, config, knowledge):
    """OLCA - Orpheus Language Cognitive Agent for musical and storytelling assistance"""
    
    agent = OLCAAgent()
    
    if config:
        console.print(Panel(yaml.dump(agent.config, default_flow_style=False), title="Configuration"))
        return
    
    if knowledge:
        kb_info = agent.knowledge.get_summary()
        console.print(Panel(json.dumps(kb_info, indent=2), title="Knowledge Base"))
        return
    
    if interactive:
        agent.interactive_mode()
    elif request:
        response = agent.process_request(request)
        console.print(response)
    else:
        console.print("Use --interactive for interactive mode or provide a request.")
        console.print("Example: python olca.py 'Generate a happy melody in C major'")

if __name__ == "__main__":
    main()
