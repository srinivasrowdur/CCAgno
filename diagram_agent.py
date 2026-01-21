"""
Smart Architecture Diagram Creator Agent using Agno Agentic SDK
"""
import os
from agno import Agno
from agno.models.google import Gemini


class ArchitectureDiagramAgent:
    """Agent for creating architecture diagrams using Gemini Nanobanana model"""
    
    def __init__(self, api_key: str = None):
        """Initialize the architecture diagram agent"""
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("Google API key is required. Set GOOGLE_API_KEY environment variable.")
        
        # Initialize Agno agent with Gemini Nanobanana model
        self.agent = Agno(
            model=Gemini(id="gemini-2.0-flash-exp", api_key=self.api_key),
            description="An intelligent agent that creates architecture diagrams based on text descriptions",
            instructions=[
                "You are an expert system architect and diagram creator.",
                "When given a description of a system or architecture, you create clear and comprehensive diagrams.",
                "You provide detailed explanations of the architecture components and their relationships.",
                "You suggest best practices and improvements for the proposed architecture.",
            ],
            markdown=True,
        )
    
    def create_diagram_description(self, user_input: str) -> str:
        """
        Generate a detailed architecture diagram description based on user input
        
        Args:
            user_input: User's description of the system/architecture
            
        Returns:
            Detailed diagram description and architecture analysis
        """
        prompt = f"""
Based on the following system description, create a comprehensive architecture diagram description:

System Description: {user_input}

Please provide:
1. A detailed textual description of the architecture diagram that should be created
2. List all components/services that should be included
3. Describe the connections and data flows between components
4. Suggest the best architecture pattern for this system
5. Provide recommendations for scalability, security, and reliability

Format your response in a clear, structured way that can be used to generate a visual diagram.
"""
        
        # Run the agent to generate the diagram description
        response = self.agent.run(prompt)
        return response.content
    
    def generate_diagram_prompt(self, user_input: str) -> str:
        """
        Generate an optimized prompt for image generation
        
        Args:
            user_input: User's description of the system/architecture
            
        Returns:
            Optimized prompt for diagram generation
        """
        # Get the detailed architecture description
        architecture_desc = self.create_diagram_description(user_input)
        
        # Create a prompt optimized for image generation
        image_prompt = f"""
Create a professional, clean architecture diagram showing:

{architecture_desc}

Style requirements:
- Use standard architecture diagram symbols and icons
- Clear labels for all components
- Arrows showing data flow and connections
- Professional color scheme (blues, grays, whites)
- Clean, modern design
- High contrast for readability
"""
        
        return image_prompt, architecture_desc


def create_architecture_agent(api_key: str = None) -> ArchitectureDiagramAgent:
    """Factory function to create an architecture diagram agent"""
    return ArchitectureDiagramAgent(api_key=api_key)
