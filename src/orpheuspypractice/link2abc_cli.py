#!/usr/bin/env python3
"""
🎵 Link2ABC CLI Integration for orpheuspypractice
===============================================

Enhanced CLI commands that Link2ABC can use for HuggingFace ChatMusician integration.

🧠 Mia: CLI as recursive contract - every invocation spirals the music forward  
🌸 Miette: These commands make the music sparkle with AI enhancement!

Usage Examples:
    # Basic enhancement
    oenhance --abc-file content.abc --output-dir ./output

    # With budget control
    oenhance --abc-file content.abc --hf-budget 0.50 --output-dir ./output
    
    # Batch processing with keep-alive
    oenhance --abc-file content.abc --keep-alive 300 --custom-prompt "Jazz-influenced harmonies"
"""

import argparse
import os
import sys
import json
from pathlib import Path
from typing import Optional

# Import our integration module
from .link2abc_integration import (
    process_with_orpheus_enhancement,
    CostBudgetManager,
    OrpheusIntegrationBlock
)


def create_cli_parser():
    """Create argument parser for Link2ABC integration commands"""
    
    parser = argparse.ArgumentParser(
        prog='oenhance',
        description='🎵 Enhance ABC music notation with HuggingFace ChatMusician',
        epilog="""
🧠 Mia: Every CLI call is a recursive music spiral
🌸 Miette: Transform your melodies with AI sparkle!

Examples:
  oenhance --abc-file melody.abc --output-dir ./music
  oenhance --abc-content "X:1\\nT:Test\\nM:4/4..." --name "test_song" 
  oenhance --abc-file melody.abc --hf-budget 1.00 --keep-alive 300
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Input options
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        '--abc-file', 
        type=str,
        help='Path to ABC notation file to enhance'
    )
    input_group.add_argument(
        '--abc-content', 
        type=str,
        help='ABC notation content as string'
    )
    
    # Output options
    parser.add_argument(
        '--output-dir',
        type=str,
        default='./output',
        help='Output directory for generated files (default: ./output)'
    )
    
    parser.add_argument(
        '--name',
        type=str,
        help='Creation name (auto-generated from filename if not provided)'
    )
    
    # Enhancement options
    parser.add_argument(
        '--enhance-hf',
        action='store_true',
        default=True,
        help='Enable HuggingFace ChatMusician enhancement (default: True)'
    )
    
    parser.add_argument(
        '--no-enhance',
        action='store_true',
        help='Disable HuggingFace enhancement (original only)'
    )
    
    # Cost management
    parser.add_argument(
        '--hf-budget',
        type=float,
        default=0.0,
        help='Session budget for HuggingFace costs (default: unlimited)'
    )
    
    parser.add_argument(
        '--daily-budget',
        type=float,
        default=0.0,
        help='Daily budget limit (default: unlimited)'
    )
    
    # Endpoint management
    parser.add_argument(
        '--keep-alive',
        type=int,
        default=0,
        help='Keep HuggingFace endpoint alive for N seconds (for batching)'
    )
    
    # Prompt customization
    parser.add_argument(
        '--hf-prompt',
        type=str,
        help='Custom prompt for HuggingFace enhancement'
    )
    
    # Utility options
    parser.add_argument(
        '--budget-status',
        action='store_true',
        help='Show current budget status and exit'
    )
    
    parser.add_argument(
        '--reset-budget',
        action='store_true',
        help='Reset budget counters and exit'
    )
    
    parser.add_argument(
        '--config-check',
        action='store_true',
        help='Check HuggingFace configuration and exit'
    )
    
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Reduce output verbosity'
    )
    
    parser.add_argument(
        '--json-output',
        action='store_true',
        help='Output results as JSON'
    )
    
    return parser


def load_abc_content(abc_file: str) -> str:
    """Load ABC content from file"""
    try:
        with open(abc_file, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Error: ABC file not found: {abc_file}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error reading ABC file: {str(e)}")
        sys.exit(1)


def generate_creation_name(abc_file: str = None, abc_content: str = None) -> str:
    """Generate creation name from file or content"""
    if abc_file:
        return Path(abc_file).stem
    
    # Try to extract title from ABC content
    if abc_content:
        for line in abc_content.split('\n'):
            if line.startswith('T:'):
                title = line[2:].strip()
                # Clean title for filename
                return ''.join(c for c in title if c.isalnum() or c in '-_').lower()
    
    # Fallback to timestamp
    import time
    return f"music_{int(time.time())}"


def show_budget_status():
    """Display current budget status"""
    budget_manager = CostBudgetManager()
    
    print("💰 Budget Status:")
    print(f"   Daily Budget: ${budget_manager.daily_budget:.2f}")
    print(f"   Daily Spent:  ${budget_manager.current_daily_cost:.2f}")
    print(f"   Daily Remaining: ${budget_manager.daily_budget - budget_manager.current_daily_cost:.2f}")
    
    if os.path.exists(budget_manager.budget_file):
        print(f"   Budget file: {budget_manager.budget_file}")
    else:
        print("   No budget file found")


def reset_budget():
    """Reset budget counters"""
    budget_manager = CostBudgetManager()
    budget_manager.current_daily_cost = 0.0
    budget_manager.current_session_cost = 0.0
    budget_manager.save_budget_state()
    print("✅ Budget counters reset")


def check_config():
    """Check HuggingFace configuration"""
    try:
        from .link2abc_integration import HFEndpointManager
        hf_manager = HFEndpointManager()
        
        print("✅ HuggingFace Configuration Check:")
        print(f"   Config file: {hf_manager.config_file}")
        print(f"   Endpoint name: {hf_manager.config.huggingface['name']}")
        print(f"   Namespace: {hf_manager.config.huggingface['namespace']}")
        print(f"   Repository: {hf_manager.config.huggingface['repository']}")
        
        token_env = hf_manager.config.huggingface.get('token_env_var', 'HUGGINGFACE_API_KEY')
        token = os.getenv(token_env)
        if token:
            print(f"   Token: {'*' * (len(token) - 4)}{token[-4:]} (from {token_env})")
        else:
            print(f"   ❌ Token not found in {token_env}")
            
    except Exception as e:
        print(f"❌ Configuration error: {str(e)}")
        sys.exit(1)


def main():
    """Main CLI entry point"""
    parser = create_cli_parser()
    args = parser.parse_args()
    
    # Handle utility commands
    if args.budget_status:
        show_budget_status()
        return
    
    if args.reset_budget:
        reset_budget()
        return
    
    if args.config_check:
        check_config()
        return
    
    # Load ABC content
    if args.abc_file:
        abc_content = load_abc_content(args.abc_file)
        creation_name = args.name or generate_creation_name(abc_file=args.abc_file)
    else:
        abc_content = args.abc_content
        creation_name = args.name or generate_creation_name(abc_content=abc_content)
    
    if not abc_content.strip():
        print("❌ Error: No ABC content provided")
        sys.exit(1)
    
    # Set up enhancement options
    enhance_hf = args.enhance_hf and not args.no_enhance
    
    if not args.quiet:
        print(f"🎵 Processing: {creation_name}")
        print(f"🎯 Output directory: {args.output_dir}")
        if enhance_hf:
            print("⭐ HuggingFace enhancement: ENABLED")
            if args.hf_budget > 0:
                print(f"💰 Session budget: ${args.hf_budget:.2f}")
            if args.keep_alive > 0:
                print(f"⏰ Keep-alive: {args.keep_alive}s")
        else:
            print("📝 HuggingFace enhancement: DISABLED")
    
    # Process with enhancement
    try:
        results = process_with_orpheus_enhancement(
            abc_content=abc_content,
            output_dir=args.output_dir,
            creation_name=creation_name,
            enhance_hf=enhance_hf,
            hf_budget=args.hf_budget,
            keep_alive=args.keep_alive,
            custom_prompt=args.hf_prompt
        )
        
        if args.json_output:
            print(json.dumps(results, indent=2, default=str))
        elif not args.quiet:
            print("\n✅ Processing complete!")
            
            # Show original results
            if 'original' in results:
                original = results['original']
                if not original.get('error'):
                    print(f"📄 Original files:")
                    print(f"   ABC: {original['abc_file']}")
                    print(f"   MIDI: {original['midi_file']}")
                    print(f"   Audio: {original['audio_file']}")
                    print(f"   Score: {original['score_file']}")
                else:
                    print(f"❌ Original processing error: {original['error']}")
            
            # Show enhanced results
            if results.get('enhanced'):
                enhanced = results['enhanced']
                if not enhanced.get('error'):
                    print(f"⭐ Enhanced files:")
                    print(f"   ABC: {enhanced['abc_file']}")
                    print(f"   MIDI: {enhanced['midi_file']}")
                    print(f"   Audio: {enhanced['audio_file']}")
                    print(f"   Score: {enhanced['score_file']}")
                    print(f"   Processing time: {enhanced.get('processing_time', 0):.1f}s")
                    print(f"   Cost: ${enhanced.get('cost', 0):.3f}")
                else:
                    print(f"❌ Enhancement error: {enhanced.get('reason', 'unknown')}")
            
            if 'report_file' in results:
                print(f"📊 Report: {results['report_file']}")
    
    except Exception as e:
        print(f"❌ Processing failed: {str(e)}")
        if not args.quiet:
            import traceback
            traceback.print_exc()
        sys.exit(1)


# Additional CLI commands for specific use cases

def main_batch_enhance():
    """CLI for batch enhancement of multiple ABC files"""
    parser = argparse.ArgumentParser(
        description='🎵 Batch enhance multiple ABC files with HuggingFace'
    )
    
    parser.add_argument(
        'abc_files',
        nargs='+',
        help='ABC files to enhance'
    )
    
    parser.add_argument(
        '--output-base',
        default='./batch_output',
        help='Base output directory'
    )
    
    parser.add_argument(
        '--hf-budget',
        type=float,
        default=5.0,
        help='Total budget for batch processing'
    )
    
    parser.add_argument(
        '--keep-alive',
        type=int,
        default=600,
        help='Keep endpoint alive between files (default: 10min)'
    )
    
    args = parser.parse_args()
    
    print(f"🎵 Batch processing {len(args.abc_files)} files...")
    print(f"💰 Total budget: ${args.hf_budget:.2f}")
    
    # Set up shared budget manager
    budget_manager = CostBudgetManager()
    budget_manager.set_session_budget(args.hf_budget)
    
    integration_block = OrpheusIntegrationBlock(budget_manager)
    integration_block.hf_manager.set_keep_alive(args.keep_alive)
    
    results = []
    
    for i, abc_file in enumerate(args.abc_files, 1):
        print(f"\n📄 Processing {i}/{len(args.abc_files)}: {abc_file}")
        
        try:
            abc_content = load_abc_content(abc_file)
            creation_name = Path(abc_file).stem
            output_dir = os.path.join(args.output_base, creation_name)
            
            result = integration_block.process_link2abc_output(
                abc_content=abc_content,
                output_dir=output_dir,
                creation_name=creation_name,
                enhance_hf=True
            )
            
            results.append({
                'file': abc_file,
                'result': result
            })
            
            if result.get('enhanced') and not result['enhanced'].get('error'):
                enhanced = result['enhanced']
                print(f"✅ Enhanced in {enhanced.get('processing_time', 0):.1f}s, cost: ${enhanced.get('cost', 0):.3f}")
            else:
                print("❌ Enhancement failed")
        
        except Exception as e:
            print(f"❌ Error processing {abc_file}: {str(e)}")
            results.append({
                'file': abc_file,
                'error': str(e)
            })
    
    # Summary
    print(f"\n📊 Batch processing complete!")
    successful = len([r for r in results if 'error' not in r])
    print(f"✅ Successful: {successful}/{len(args.abc_files)}")
    print(f"💰 Total spent: ${budget_manager.current_session_cost:.3f}")


if __name__ == '__main__':
    main()