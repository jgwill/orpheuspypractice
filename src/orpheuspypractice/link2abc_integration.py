"""
🎵 Link2ABC Integration with HuggingFace ChatMusician Pipeline
=============================================================

This module provides the integration between Link2ABC and orpheuspypractice,
enabling professional AI music enhancement through HuggingFace ChatMusician.

🧠 Mia: Recursive DevOps pattern - each block transforms and enhances the musical recursion
🌸 Miette: This is where the magic happens - web content becomes professional music!
"""

import json
import os
import time
import yaml
import tempfile
import subprocess
from typing import Dict, List, Optional, Tuple, Any
from pathlib import Path

# Import from existing orpheuspypractice modules  
from jgcmlib.jgcmhelper import (
    postprocess_abc, 
    extract_abc_from_text,
    generate_markdown_output,
    save_as_json_to_filename
)
from jghfmanager.cminferencer import main as hf_inference_main
from jghfmanager.jgthfdata import JgHfConfig, JgHfMusicalPieces


class CostBudgetManager:
    """Manages HuggingFace cost budgets and usage tracking"""
    
    def __init__(self, budget_file: str = ".orpheus_budget.json"):
        self.budget_file = budget_file
        self.session_budget = 0.0
        self.daily_budget = 0.0
        self.current_session_cost = 0.0
        self.current_daily_cost = 0.0
        self.load_budget_state()
    
    def load_budget_state(self):
        """Load existing budget state from file"""
        if os.path.exists(self.budget_file):
            with open(self.budget_file, 'r') as f:
                data = json.load(f)
                self.daily_budget = data.get('daily_budget', 0.0)
                self.current_daily_cost = data.get('daily_cost', 0.0)
                last_date = data.get('last_date', '')
                
                # Reset daily cost if it's a new day
                today = time.strftime('%Y-%m-%d')
                if last_date != today:
                    self.current_daily_cost = 0.0
    
    def set_session_budget(self, budget: float):
        """Set budget for current session"""
        self.session_budget = budget
        
    def set_daily_budget(self, budget: float):
        """Set daily spending limit"""
        self.daily_budget = budget
    
    def can_spend(self, estimated_cost: float) -> bool:
        """Check if we can afford the estimated cost"""
        if self.session_budget > 0 and (self.current_session_cost + estimated_cost) > self.session_budget:
            return False
        if self.daily_budget > 0 and (self.current_daily_cost + estimated_cost) > self.daily_budget:
            return False
        return True
    
    def record_cost(self, actual_cost: float):
        """Record actual cost incurred"""
        self.current_session_cost += actual_cost
        self.current_daily_cost += actual_cost
        self.save_budget_state()
    
    def save_budget_state(self):
        """Save current budget state to file"""
        data = {
            'daily_budget': self.daily_budget,
            'daily_cost': self.current_daily_cost,
            'last_date': time.strftime('%Y-%m-%d')
        }
        with open(self.budget_file, 'w') as f:
            json.dump(data, f, indent=2)


class HFEndpointManager:
    """Manages HuggingFace endpoint lifecycle with cost optimization"""
    
    def __init__(self, config_file: str = "orpheus-config.yml"):
        self.config_file = config_file
        self.config = None
        self.endpoint = None
        self.keep_alive_until = 0
        self.boot_time = 0
        self.load_config()
    
    def load_config(self):
        """Load HuggingFace configuration"""
        if not os.path.exists(self.config_file):
            config_file = os.path.join(os.getenv("HOME", "."), self.config_file)
        else:
            config_file = self.config_file
            
        if os.path.exists(config_file):
            self.config = JgHfConfig(config_file)
        else:
            raise FileNotFoundError(f"HuggingFace config not found: {self.config_file}")
    
    def start_endpoint(self):
        """Start HuggingFace endpoint and measure boot time"""
        print("🧠 Mia: Booting HuggingFace ChatMusician endpoint...")
        start_time = time.time()
        
        # Use existing cminferencer logic but capture endpoint reference
        from huggingface_hub import HfApi, InferenceEndpoint
        
        api = HfApi()
        token_env = self.config.huggingface.get('token_env_var', 'HUGGINGFACE_API_KEY')
        token = os.getenv(token_env)
        
        name = self.config.huggingface['name']
        namespace = self.config.huggingface['namespace']
        
        self.endpoint = api.get_inference_endpoint(name=name, namespace=namespace, token=token)
        self.endpoint.resume()
        
        # Wait for endpoint to be running
        while self.endpoint.status != 'running':
            self.endpoint = api.get_inference_endpoint(name=name, namespace=namespace, token=token)
            print(".", end="", flush=True)
            time.sleep(3)
        
        self.boot_time = time.time() - start_time
        print(f"\n🌸 Miette: Endpoint is alive! Boot time: {self.boot_time:.1f}s")
        return self.endpoint
    
    def set_keep_alive(self, seconds: int):
        """Set how long to keep endpoint alive for batching"""
        self.keep_alive_until = time.time() + seconds
        print(f"🧠 Mia: Keeping endpoint alive for {seconds}s for batch processing")
    
    def should_shutdown(self) -> bool:
        """Check if endpoint should be shut down"""
        return time.time() > self.keep_alive_until
    
    def shutdown_endpoint(self):
        """Shutdown HuggingFace endpoint"""
        if self.endpoint:
            print("🌸 Miette: Shutting down endpoint to save costs...")
            self.endpoint.pause()
            self.endpoint = None


class MusicalPromptManager:
    """Manages dynamic musical.yml generation for ChatMusician prompts"""
    
    @staticmethod
    def create_enhancement_prompt(abc_content: str, custom_prompt: str = None) -> str:
        """Create enhancement prompt for existing ABC notation"""
        base_prompt = f"""Please enhance this ABC music notation with professional arranging and creative harmonization:

{abc_content}

Enhancement instructions:
- Keep the original melodic structure but add sophisticated harmonies
- Add dynamic markings and articulations for expressive performance
- Ensure all ABC notation syntax is correct and complete
- Make it sound more professional and engaging
"""
        
        if custom_prompt:
            base_prompt += f"\nAdditional requirements: {custom_prompt}"
        
        return base_prompt
    
    def generate_musical_yml(self, abc_content: str, creation_name: str, 
                           custom_prompts: List[str] = None) -> str:
        """Generate musical.yml file for HuggingFace inference"""
        
        if not custom_prompts:
            custom_prompts = [self.create_enhancement_prompt(abc_content)]
        
        musical_config = {
            'musical': {
                'name': creation_name,
                'sname': 'enhanced',
                'prompts': {}
            }
        }
        
        for i, prompt in enumerate(custom_prompts, 1):
            musical_config['musical']['prompts'][f'enhancement_{i}'] = prompt
        
        yaml_filename = f"{creation_name}_musical_enhanced.yml"
        with open(yaml_filename, 'w') as f:
            yaml.dump(musical_config, f, default_flow_style=False)
        
        return yaml_filename


class OrpheusIntegrationBlock:
    """
    🎵 Main integration component that bridges Link2ABC with HuggingFace ChatMusician
    
    This block processes ABC notation through HuggingFace enhancement and creates
    both original and enhanced outputs with comprehensive format conversion.
    """
    
    def __init__(self, budget_manager: CostBudgetManager = None):
        self.budget_manager = budget_manager or CostBudgetManager()
        self.hf_manager = HFEndpointManager()
        self.prompt_manager = MusicalPromptManager()
        self.original_cwd = os.getcwd()
        
    def enhance_abc_content(self, abc_content: str, creation_name: str,
                          custom_prompt: str = None, estimated_cost: float = 0.10) -> Dict[str, Any]:
        """
        Enhance ABC content using HuggingFace ChatMusician
        
        Args:
            abc_content: Original ABC notation
            creation_name: Name for the musical creation
            custom_prompt: Optional custom enhancement instructions
            estimated_cost: Estimated cost for this operation
            
        Returns:
            Dictionary with enhancement results
        """
        
        # Budget check
        if not self.budget_manager.can_spend(estimated_cost):
            print("🌸 Miette: Budget exceeded! Falling back to original generation...")
            return {'enhanced': False, 'reason': 'budget_exceeded'}
        
        try:
            # Create temporary working directory
            with tempfile.TemporaryDirectory() as temp_dir:
                os.chdir(temp_dir)
                
                # Generate musical.yml for HuggingFace
                prompts = [self.prompt_manager.create_enhancement_prompt(abc_content, custom_prompt)]
                musical_yml = self.prompt_manager.generate_musical_yml(
                    abc_content, creation_name, prompts
                )
                
                # Start HuggingFace endpoint
                endpoint = self.hf_manager.start_endpoint()
                
                # Run HuggingFace inference (reuse existing cminferencer logic)
                start_time = time.time()
                hf_inference_main()  # This uses the musical.yml we created
                processing_time = time.time() - start_time
                
                # Find generated JSON files
                json_files = [f for f in os.listdir('.') if f.endswith('.json') and creation_name in f]
                
                if not json_files:
                    return {'enhanced': False, 'reason': 'no_output_generated'}
                
                # Process the first JSON result
                enhanced_json = json_files[0]
                enhanced_results = []
                
                with open(enhanced_json, 'r') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        generated_text = data[0].get('generated_text', '')
                    else:
                        generated_text = data.get('generated_text', '')
                
                # Extract enhanced ABC notation
                enhanced_abc_list = extract_abc_from_text(generated_text)
                
                if not enhanced_abc_list:
                    return {'enhanced': False, 'reason': 'no_abc_extracted'}
                
                enhanced_abc = enhanced_abc_list[0]
                
                # Copy results back to original directory
                os.chdir(self.original_cwd)
                
                # Record actual cost (simplified estimation)
                actual_cost = min(estimated_cost, estimated_cost * (processing_time / 30.0))
                self.budget_manager.record_cost(actual_cost)
                
                return {
                    'enhanced': True,
                    'enhanced_abc': enhanced_abc,
                    'original_abc': abc_content,
                    'processing_time': processing_time,
                    'cost': actual_cost
                }
                
        except Exception as e:
            os.chdir(self.original_cwd)
            print(f"🌸 Miette: Enhancement failed: {str(e)}")
            return {'enhanced': False, 'reason': f'error: {str(e)}'}
        
        finally:
            # Shutdown endpoint if not keeping alive
            if self.hf_manager.should_shutdown():
                self.hf_manager.shutdown_endpoint()
    
    def process_link2abc_output(self, abc_content: str, output_dir: str,
                              creation_name: str, enhance_hf: bool = False,
                              custom_prompt: str = None, hf_budget: float = 0.0,
                              keep_alive: int = 0) -> Dict[str, Any]:
        """
        Process Link2ABC output with optional HuggingFace enhancement
        
        This creates the dual output structure:
        output/
        ├── original/
        │   ├── content.abc, content.mid, content.mp3, content.svg
        └── enhanced/  (if enhance_hf=True)
            ├── content_enhanced.abc, content_enhanced.mid, etc.
        """
        
        results = {
            'original': {},
            'enhanced': None,
            'enhanced_enabled': enhance_hf
        }
        
        # Set up budget and keep-alive
        if hf_budget > 0:
            self.budget_manager.set_session_budget(hf_budget)
        
        if keep_alive > 0:
            self.hf_manager.set_keep_alive(keep_alive)
        
        # Create output directories
        original_dir = os.path.join(output_dir, 'original')
        os.makedirs(original_dir, exist_ok=True)
        
        # Process original ABC
        abc_file = os.path.join(original_dir, f"{creation_name}.abc")
        with open(abc_file, 'w') as f:
            f.write(abc_content)
        
        # Convert original to all formats
        try:
            from jgcmlib.jgabcli import pto_post_just_an_abc_file
            score_path, audio_path, midi_path = pto_post_just_an_abc_file(abc_file, score_ext="svg")
            
            results['original'] = {
                'abc_file': abc_file,
                'midi_file': midi_path,
                'audio_file': audio_path,
                'score_file': score_path
            }
        except Exception as e:
            print(f"🌸 Miette: Original processing failed: {str(e)}")
            results['original']['error'] = str(e)
        
        # Process enhanced version if requested
        if enhance_hf:
            enhanced_dir = os.path.join(output_dir, 'enhanced')
            os.makedirs(enhanced_dir, exist_ok=True)
            
            enhancement_result = self.enhance_abc_content(
                abc_content, creation_name, custom_prompt
            )
            
            if enhancement_result.get('enhanced'):
                enhanced_abc = enhancement_result['enhanced_abc']
                enhanced_abc_file = os.path.join(enhanced_dir, f"{creation_name}_enhanced.abc")
                
                with open(enhanced_abc_file, 'w') as f:
                    f.write(enhanced_abc)
                
                # Convert enhanced to all formats
                try:
                    enhanced_score, enhanced_audio, enhanced_midi = pto_post_just_an_abc_file(
                        enhanced_abc_file, score_ext="svg"
                    )
                    
                    results['enhanced'] = {
                        'abc_file': enhanced_abc_file,
                        'midi_file': enhanced_midi,
                        'audio_file': enhanced_audio,
                        'score_file': enhanced_score,
                        'processing_time': enhancement_result['processing_time'],
                        'cost': enhancement_result['cost']
                    }
                except Exception as e:
                    print(f"🌸 Miette: Enhanced processing failed: {str(e)}")
                    results['enhanced'] = {'error': str(e)}
            else:
                results['enhanced'] = enhancement_result
        
        return results


def create_enhanced_format_converter():
    """Factory function for enhanced format conversion"""
    
    class EnhancedFormatConverter:
        """Handles dual output management for original vs enhanced music"""
        
        @staticmethod
        def generate_comparison_report(results: Dict[str, Any], output_dir: str):
            """Generate markdown report comparing original vs enhanced"""
            
            report_content = """# 🎵 Music Generation Report

## Original Version
"""
            
            if 'original' in results and not results['original'].get('error'):
                original = results['original']
                report_content += f"""
- **ABC Source**: [{os.path.basename(original['abc_file'])}]({original['abc_file']})
- **MIDI File**: [{os.path.basename(original['midi_file'])}]({original['midi_file']})
- **Audio File**: [{os.path.basename(original['audio_file'])}]({original['audio_file']})

![Original Score]({original['score_file']})
"""
            else:
                report_content += "\n❌ Original generation failed\n"
            
            if results.get('enhanced_enabled') and results.get('enhanced'):
                enhanced = results['enhanced']
                if not enhanced.get('error'):
                    report_content += f"""
## 🌟 Enhanced Version (HuggingFace ChatMusician)

- **Processing Time**: {enhanced.get('processing_time', 0):.1f}s
- **Cost**: ${enhanced.get('cost', 0):.3f}
- **ABC Source**: [{os.path.basename(enhanced['abc_file'])}]({enhanced['abc_file']})
- **MIDI File**: [{os.path.basename(enhanced['midi_file'])}]({enhanced['midi_file']})
- **Audio File**: [{os.path.basename(enhanced['audio_file'])}]({enhanced['audio_file']})

![Enhanced Score]({enhanced['score_file']})

🧠 **Mia**: Professional AI enhancement applied with recursive musical intelligence
🌸 **Miette**: The enhanced version sparkles with AI creativity!
"""
                else:
                    report_content += f"""
## ❌ Enhancement Failed
Reason: {enhanced.get('reason', 'unknown')}
"""
            
            report_file = os.path.join(output_dir, 'generation_report.md')
            with open(report_file, 'w') as f:
                f.write(report_content)
            
            return report_file
    
    return EnhancedFormatConverter()


# CLI Integration Functions for Link2ABC
def integrate_with_link2abc_cli():
    """
    Integration functions that Link2ABC can call to add HuggingFace enhancement
    
    Usage in Link2ABC:
    ```python
    from orpheuspypractice.link2abc_integration import process_with_orpheus_enhancement
    
    # In Link2ABC pipeline
    if args.enhance_hf:
        enhanced_results = process_with_orpheus_enhancement(
            abc_content, output_dir, creation_name, 
            enhance_hf=True, hf_budget=args.hf_budget, 
            keep_alive=args.keep_alive, custom_prompt=args.hf_prompt
        )
    ```
    """
    pass


def process_with_orpheus_enhancement(abc_content: str, output_dir: str, creation_name: str,
                                   enhance_hf: bool = False, hf_budget: float = 0.0,
                                   keep_alive: int = 0, custom_prompt: str = None) -> Dict[str, Any]:
    """
    Main integration function for Link2ABC to call
    
    🧠 Mia: This is the recursive bridge that connects web content to professional music
    🌸 Miette: The magic transformation happens here!
    """
    
    budget_manager = CostBudgetManager()
    integration_block = OrpheusIntegrationBlock(budget_manager)
    
    results = integration_block.process_link2abc_output(
        abc_content=abc_content,
        output_dir=output_dir,
        creation_name=creation_name,
        enhance_hf=enhance_hf,
        custom_prompt=custom_prompt,
        hf_budget=hf_budget,
        keep_alive=keep_alive
    )
    
    # Generate comparison report
    converter = create_enhanced_format_converter()
    report_file = converter.generate_comparison_report(results, output_dir)
    results['report_file'] = report_file
    
    print(f"\n🎵 Music generation complete!")
    print(f"📊 Report: {report_file}")
    
    if results.get('enhanced'):
        enhanced = results['enhanced']
        if not enhanced.get('error'):
            print(f"⭐ Enhanced version created in {enhanced.get('processing_time', 0):.1f}s")
            print(f"💰 Cost: ${enhanced.get('cost', 0):.3f}")
    
    return results


if __name__ == "__main__":
    # Test/demo usage
    test_abc = """X:1
T:Test Melody
M:4/4
L:1/4
K:C
C D E F | G A B c |"""
    
    results = process_with_orpheus_enhancement(
        test_abc, "./test_output", "test_melody", 
        enhance_hf=True, hf_budget=1.0
    )
    print(json.dumps(results, indent=2, default=str))