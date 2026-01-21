"""
Test script for the Smart Architecture Diagram Creator
This script tests the core functionality without requiring a live Streamlit session
"""
import os
import sys

# Mock environment for testing
os.environ["GOOGLE_API_KEY"] = "test_key_placeholder"

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    try:
        import streamlit as st
        print("✓ Streamlit imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import Streamlit: {e}")
        return False
    
    try:
        from agno.agent import Agent
        print("✓ Agno Agent imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import Agno Agent: {e}")
        return False
    
    try:
        from agno.models.google import Gemini
        print("✓ Agno Gemini model imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import Gemini model: {e}")
        return False
    
    try:
        from google import genai
        print("✓ Google GenAI imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import Google GenAI: {e}")
        return False
    
    return True

def test_diagram_agent_creation():
    """Test that the diagram agent can be instantiated"""
    print("\nTesting diagram agent creation...")
    try:
        # This will fail without a real API key, but we're just testing the structure
        from diagram_agent import ArchitectureDiagramAgent
        print("✓ ArchitectureDiagramAgent class can be imported")
        return True
    except Exception as e:
        print(f"✗ Failed to import ArchitectureDiagramAgent: {e}")
        return False

def test_app_structure():
    """Test that the app.py file is properly structured"""
    print("\nTesting app structure...")
    try:
        import app
        print("✓ app.py can be imported")
        
        # Check for key functions
        if hasattr(app, 'initialize_session_state'):
            print("✓ initialize_session_state function exists")
        else:
            print("✗ initialize_session_state function not found")
            return False
        
        if hasattr(app, 'generate_diagram_with_imagen'):
            print("✓ generate_diagram_with_imagen function exists")
        else:
            print("✗ generate_diagram_with_imagen function not found")
            return False
        
        if hasattr(app, 'main'):
            print("✓ main function exists")
        else:
            print("✗ main function not found")
            return False
        
        return True
    except Exception as e:
        print(f"✗ Failed to test app structure: {e}")
        return False

def test_file_structure():
    """Test that all required files exist"""
    print("\nTesting file structure...")
    required_files = [
        'app.py',
        'diagram_agent.py',
        'requirements.txt',
        'README.md',
        '.gitignore',
        '.env.example',
        'EXAMPLES.md'
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} not found")
            all_exist = False
    
    return all_exist

def main():
    """Run all tests"""
    print("=" * 60)
    print("Smart Architecture Diagram Creator - Test Suite")
    print("=" * 60)
    
    results = []
    
    results.append(("File Structure", test_file_structure()))
    results.append(("Imports", test_imports()))
    results.append(("Diagram Agent", test_diagram_agent_creation()))
    results.append(("App Structure", test_app_structure()))
    
    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)
    
    for test_name, result in results:
        status = "PASS" if result else "FAIL"
        symbol = "✓" if result else "✗"
        print(f"{symbol} {test_name}: {status}")
    
    all_passed = all(result for _, result in results)
    
    print("=" * 60)
    if all_passed:
        print("All tests passed! ✓")
        return 0
    else:
        print("Some tests failed. ✗")
        return 1

if __name__ == "__main__":
    sys.exit(main())
