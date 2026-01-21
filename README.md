# CCAgno - Smart Architecture Diagram Creator

An intelligent architecture diagram creator powered by **Gemini AI** and **Agno Agentic SDK** with a beautiful **Streamlit** frontend.

## 🌟 Features

- **AI-Powered Architecture Analysis**: Uses Gemini 2.0 Flash model to analyze and understand system architectures
- **Intelligent Diagram Generation**: Automatically creates comprehensive architecture diagrams from text descriptions
- **Agno Agentic SDK**: Leverages advanced agentic AI capabilities for smarter diagram creation
- **Interactive Streamlit UI**: User-friendly interface with real-time generation
- **Quick Templates**: Pre-built templates for common architectures (E-commerce, Chat Apps, ML Pipelines)
- **Detailed Analysis**: Get comprehensive architecture breakdowns, component relationships, and best practices
- **Export Capabilities**: Download your architecture analysis and diagrams

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google API Key with Gemini API access

### Installation

1. Clone the repository:
```bash
git clone https://github.com/srinivasrowdur/CCAgno.git
cd CCAgno
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment:
```bash
cp .env.example .env
# Edit .env and add your Google API Key
```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 📖 Usage

1. **Enter API Key**: Provide your Google API key in the sidebar (or set it in `.env` file)
2. **Describe Your Architecture**: Write a description of the system you want to visualize
3. **Use Quick Templates** (Optional): Click on pre-built templates for common architectures
4. **Generate Diagram**: Click the "Generate Architecture Diagram" button
5. **Review Results**: View the AI-generated architecture analysis and diagram
6. **Download**: Export your architecture analysis for documentation

### Example Descriptions

**E-commerce Platform:**
```
A scalable e-commerce platform with microservices architecture including user authentication, 
product catalog, shopping cart, payment processing, order management, and notification services. 
Uses API gateway, load balancer, and cloud storage.
```

**Real-time Chat Application:**
```
A real-time chat application with WebSocket connections, message queue for async processing, 
user presence tracking, file sharing, and message history. Includes authentication, database 
for messages, and Redis for caching.
```

**ML Pipeline:**
```
A machine learning pipeline for image classification with data ingestion, preprocessing, 
model training, model serving API, monitoring, and feedback loop. Uses cloud storage, 
GPU instances, and model registry.
```

## 🏗️ Architecture

The application consists of three main components:

1. **diagram_agent.py**: Core agent logic using Agno Agentic SDK
   - Initializes Gemini 2.0 Flash model
   - Processes user input and generates architecture analysis
   - Creates optimized prompts for diagram generation

2. **app.py**: Streamlit frontend application
   - User interface for input and display
   - Handles API key configuration
   - Manages diagram generation workflow
   - Provides download and export features

3. **requirements.txt**: Python dependencies
   - Streamlit for UI
   - Agno SDK for agentic AI
   - Google Generative AI for Gemini integration
   - Supporting libraries

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Framework**: Agno Agentic SDK
- **AI Model**: Gemini 2.0 Flash (formerly Nanobanana)
- **Language**: Python 3.8+
- **Additional Libraries**: python-dotenv, Pillow

## 📝 API Key Setup

To get your Google API Key:

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key and add it to your `.env` file or enter it in the Streamlit sidebar

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **Gemini AI** by Google for powerful language and vision models
- **Agno Agentic SDK** for advanced agentic AI capabilities
- **Streamlit** for the amazing web app framework

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

Built with ❤️ using Gemini AI, Agno Agentic SDK, and Streamlit