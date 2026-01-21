"""
Smart Architecture Diagram Creator - Streamlit UI
"""
import streamlit as st
import os
from dotenv import load_dotenv
from diagram_agent import create_architecture_agent
import google.generativeai as genai
from PIL import Image
import io

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Smart Architecture Diagram Creator",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1E88E5;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E88E5;
        color: white;
        font-size: 1.1rem;
        padding: 0.5rem;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables"""
    if 'diagram_description' not in st.session_state:
        st.session_state.diagram_description = None
    if 'generated_image' not in st.session_state:
        st.session_state.generated_image = None
    if 'architecture_analysis' not in st.session_state:
        st.session_state.architecture_analysis = None

def generate_diagram_with_imagen(prompt: str, api_key: str) -> Image:
    """
    Generate diagram using Gemini's image generation capabilities
    Note: Using text-based diagram representation as Imagen API has specific requirements
    """
    try:
        # Configure Gemini
        genai.configure(api_key=api_key)
        
        # Using Gemini to create a detailed text-based diagram representation
        # In production, this would call Imagen API for actual image generation
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        diagram_prompt = f"""
Create a detailed ASCII/text-based architecture diagram for:

{prompt}

Use boxes, arrows, and clear labels to show the system architecture.
Make it visual and easy to understand.
"""
        
        response = model.generate_content(diagram_prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating diagram: {str(e)}")
        return None

def main():
    """Main application function"""
    initialize_session_state()
    
    # Header
    st.markdown('<div class="main-header">🏗️ Smart Architecture Diagram Creator</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Powered by Gemini AI & Agno Agentic SDK</div>', unsafe_allow_html=True)
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # API Key input
        api_key = st.text_input(
            "Google API Key",
            type="password",
            value=os.getenv("GOOGLE_API_KEY", ""),
            help="Enter your Google API key for Gemini"
        )
        
        st.markdown("---")
        
        st.markdown("""
        ### 📖 How to Use
        1. Enter your Google API key (or set GOOGLE_API_KEY env variable)
        2. Describe your system architecture in the text area
        3. Click 'Generate Architecture Diagram'
        4. Review the AI-generated analysis and diagram
        
        ### 🎯 Example Inputs
        - "E-commerce platform with microservices"
        - "Real-time chat application with WebSockets"
        - "ML pipeline for image classification"
        - "Serverless data processing system"
        """)
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📝 System Description")
        
        # Input area
        user_input = st.text_area(
            "Describe the system or architecture you want to visualize:",
            height=200,
            placeholder="E.g., A microservices-based e-commerce platform with user service, product catalog, shopping cart, payment gateway, and notification service. Users interact through a web and mobile app...",
            help="Provide a detailed description of your system architecture"
        )
        
        # Example templates
        st.subheader("💡 Quick Templates")
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("🛒 E-commerce"):
                user_input = "A scalable e-commerce platform with microservices architecture including user authentication, product catalog, shopping cart, payment processing, order management, and notification services. Uses API gateway, load balancer, and cloud storage."
                
        with col_b:
            if st.button("💬 Chat App"):
                user_input = "A real-time chat application with WebSocket connections, message queue for async processing, user presence tracking, file sharing, and message history. Includes authentication, database for messages, and Redis for caching."
                
        with col_c:
            if st.button("🤖 ML Pipeline"):
                user_input = "A machine learning pipeline for image classification with data ingestion, preprocessing, model training, model serving API, monitoring, and feedback loop. Uses cloud storage, GPU instances, and model registry."
        
        # Generate button
        if st.button("🚀 Generate Architecture Diagram", type="primary"):
            if not api_key:
                st.error("⚠️ Please provide a Google API key in the sidebar")
            elif not user_input:
                st.error("⚠️ Please describe the system architecture")
            else:
                with st.spinner("🔄 Analyzing architecture and generating diagram..."):
                    try:
                        # Create agent
                        agent = create_architecture_agent(api_key=api_key)
                        
                        # Generate diagram description
                        image_prompt, architecture_desc = agent.generate_diagram_prompt(user_input)
                        
                        # Store in session state
                        st.session_state.architecture_analysis = architecture_desc
                        st.session_state.diagram_description = image_prompt
                        
                        # Generate the diagram
                        diagram_result = generate_diagram_with_imagen(image_prompt, api_key)
                        st.session_state.generated_image = diagram_result
                        
                        st.success("✅ Diagram generated successfully!")
                        st.rerun()
                        
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
    
    with col2:
        st.header("🎨 Generated Architecture")
        
        if st.session_state.architecture_analysis:
            st.subheader("📊 Architecture Analysis")
            with st.expander("View Detailed Analysis", expanded=True):
                st.markdown(st.session_state.architecture_analysis)
        
        if st.session_state.generated_image:
            st.subheader("🖼️ Architecture Diagram")
            
            # Display the text-based diagram in a code block for better formatting
            st.code(st.session_state.generated_image, language="text")
            
            # Download options
            st.download_button(
                label="📥 Download Analysis",
                data=st.session_state.architecture_analysis,
                file_name="architecture_analysis.txt",
                mime="text/plain"
            )
        else:
            st.info("👈 Enter a system description and click 'Generate' to create an architecture diagram")
    
    # Footer
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: #666;'>
            <p>Built with ❤️ using Streamlit, Agno Agentic SDK, and Gemini AI</p>
            <p>🏗️ Smart Architecture Diagram Creator | Version 1.0</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
