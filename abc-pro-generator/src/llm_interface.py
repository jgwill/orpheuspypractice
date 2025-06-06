"""
LLM Interface - Handles communication with Language Learning Models
"""

import os
import json
from typing import Dict, Any, Optional
from datetime import datetime

try:
    import openai
except ImportError:
    openai = None

try:
    from langchain.llms import OpenAI as LangChainOpenAI
    from langchain.schema import HumanMessage, SystemMessage
except ImportError:
    LangChainOpenAI = None
    HumanMessage = None
    SystemMessage = None

class LLMInterface:
    """Interface for communicating with Large Language Models"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.provider = config.get('provider', 'openai')
        self.model = config.get('model', 'gpt-3.5-turbo')
        self.api_key = config.get('api_key') or os.getenv('OPENAI_API_KEY')
        
        self.client = None
        self.setup_client()
    
    def setup_client(self):
        """Setup the LLM client based on configuration"""
        if self.provider == 'openai' and openai and self.api_key:
            self.client = openai.OpenAI(api_key=self.api_key)
        else:
            print(f"Warning: LLM client not available. Provider: {self.provider}, API key: {'Yes' if self.api_key else 'No'}")
    
    def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate a response using the configured LLM"""
        if not self.client:
            return self.fallback_response(prompt)
        
        try:
            system_prompt = self.build_system_prompt(context)
            
            if self.provider == 'openai':
                return self.generate_openai_response(prompt, system_prompt)
            else:
                return self.fallback_response(prompt)
                
        except Exception as e:
            print(f"LLM Error: {e}")
            return self.fallback_response(prompt)
    
    def build_system_prompt(self, context: Optional[str] = None) -> str:
        """Build system prompt for ABC notation generation"""
        base_prompt = """You are OLCA (Orpheus Language Cognitive Agent), an expert in music composition and ABC notation.

Your role is to:
1. Generate high-quality ABC notation from natural language descriptions
2. Provide musical assistance and storytelling support
3. Help with ABC notation processing and conversion

ABC Notation Rules:
- Always include required headers: X: (number), T: (title), K: (key signature)
- Use proper note syntax: C D E F G A B (lower octave), c d e f g a b (higher octave)
- Include bar lines: | (single bar), || (double bar)
- Use correct rhythm notation: C2 (half note), C (quarter), C/2 (eighth), C/4 (sixteenth)
- Key signatures: C major, G major, Am minor, etc.
- Time signatures: M:4/4, M:3/4, M:6/8, etc.

When generating ABC notation:
- Ensure musical coherence and proper voice leading
- Match the requested style and mood
- Create memorable and singable melodies
- Use appropriate rhythm patterns for the style

Always provide complete, valid ABC notation that can be played."""

        if context:
            base_prompt += f"\n\nAdditional Context:\n{context}"
        
        return base_prompt
    
    def generate_openai_response(self, prompt: str, system_prompt: str) -> str:
        """Generate response using OpenAI API"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            raise Exception(f"OpenAI API error: {e}")
    
    def generate_abc_notation(self, musical_request: str, style: Optional[str] = None, 
                            key: Optional[str] = None, meter: Optional[str] = None) -> str:
        """Specialized method for generating ABC notation"""
        
        # Build a detailed prompt for ABC generation
        prompt_parts = [f"Generate ABC notation for: {musical_request}"]
        
        if style:
            prompt_parts.append(f"Style: {style}")
        if key:
            prompt_parts.append(f"Key: {key}")
        if meter:
            prompt_parts.append(f"Time signature: {meter}")
        
        prompt_parts.append("\nPlease provide only valid ABC notation with proper headers and musical content.")
        
        prompt = "\n".join(prompt_parts)
        
        return self.generate_response(prompt)
    
    def analyze_abc_notation(self, abc_content: str) -> Dict[str, Any]:
        """Analyze ABC notation and provide insights"""
        prompt = f"""Analyze this ABC notation and provide insights:

{abc_content}

Please analyze:
1. Musical style and characteristics
2. Key and harmonic structure
3. Rhythm patterns
4. Melodic contour and range
5. Overall musical quality
6. Suggestions for improvement

Provide your analysis in a clear, structured format."""

        response = self.generate_response(prompt)
        
        # Try to parse structured response
        try:
            # Look for JSON in response
            if '{' in response and '}' in response:
                json_start = response.find('{')
                json_end = response.rfind('}') + 1
                return json.loads(response[json_start:json_end])
        except:
            pass
        
        # Return as text analysis if JSON parsing fails
        return {
            'analysis': response,
            'timestamp': datetime.now().isoformat()
        }
    
    def suggest_improvements(self, abc_content: str, user_feedback: str) -> str:
        """Suggest improvements based on ABC content and user feedback"""
        prompt = f"""Given this ABC notation:

{abc_content}

And this user feedback: "{user_feedback}"

Please suggest specific improvements to the ABC notation to address the user's concerns. 
Provide the improved ABC notation with explanations of what was changed and why."""

        return self.generate_response(prompt)
    
    def fallback_response(self, prompt: str) -> str:
        """Provide fallback response when LLM is not available"""
        if any(keyword in prompt.lower() for keyword in ['melody', 'song', 'music', 'abc']):
            return self.generate_fallback_abc(prompt)
        else:
            return f"LLM not available. Received request: {prompt}"
    
    def generate_fallback_abc(self, prompt: str) -> str:
        """Generate simple ABC notation without LLM"""
        # Extract key if mentioned
        key = 'C'
        for k in ['C', 'G', 'D', 'A', 'E', 'B', 'F']:
            if k.lower() in prompt.lower():
                key = k
                break
        
        # Extract time signature if mentioned
        meter = '4/4'
        if '3/4' in prompt or 'waltz' in prompt.lower():
            meter = '3/4'
        elif '6/8' in prompt or 'jig' in prompt.lower():
            meter = '6/8'
        
        # Generate simple melody
        if meter == '3/4':
            melody = "C D E | F G A | B c B | A G F | E D C | C3 |"
        elif meter == '6/8':
            melody = "C D E F G A | B c B A G F | E F G A B c | c B A G F E |"
        else:
            melody = "C D E F | G A B c | c B A G | F E D C |"
        
        title = "Generated Song"
        if 'happy' in prompt.lower():
            title = "Happy Melody"
        elif 'sad' in prompt.lower():
            title = "Melancholy Tune"
        elif 'birthday' in prompt.lower():
            title = "Birthday Song"
        
        return f"""X:1
T:{title}
M:{meter}
L:1/4
K:{key}
{melody}"""
    
    def is_available(self) -> bool:
        """Check if LLM service is available"""
        return self.client is not None
    
    def get_model_info(self) -> Dict[str, str]:
        """Get information about the current model"""
        return {
            'provider': self.provider,
            'model': self.model,
            'available': str(self.is_available()),
            'api_key_configured': 'Yes' if self.api_key else 'No'
        }
