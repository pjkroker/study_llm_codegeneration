import logging
import os
from gradio_client import Client

# Set up logging
os.makedirs('./log', exist_ok=True)
logging.basicConfig(
    filename='./log/log.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)

logging.debug("---Starting OpenCodeInterpreter API Usage---")

# Connect to your Gradio server
client = Client("http://127.0.0.1:7860/")
print("Connected to OpenCodeInterpreter API ✓")

# Method 1: Simple chat using the /partial endpoint
def simple_chat(message):
    """Send a message and get response using named API endpoint"""
    try:
        logging.info(f"Sending message: {message}")
        
        # Use the named API endpoint - much cleaner!
        result = client.predict(
            user_message=message,
            api_name="/partial"
        )
        
        logging.info(f"Received result: {type(result)}")
        return result
    
    except Exception as e:
        logging.error(f"Error in simple_chat: {e}")
        print(f"Error: {e}")
        return None

# Method 2: Reset textbox (clear input)
def reset_input():
    """Reset/clear the textbox"""
    try:
        result = client.predict(api_name="/reset_textbox")
        logging.info("Textbox reset successfully")
        return result
    except Exception as e:
        logging.error(f"Error resetting textbox: {e}")
        return None

# Method 3: Update UUID (initialization)
def update_uuid():
    """Update/initialize the session UUID"""
    try:
        result = client.predict(api_name="/update_uuid")
        logging.info("UUID updated successfully")
        return result
    except Exception as e:
        logging.error(f"Error updating UUID: {e}")
        return None

# Method 4: Get current chat state
def get_chat_state():
    """Get current chatbot state using /partial_1"""
    try:
        result = client.predict(api_name="/partial_1")
        logging.info("Retrieved chat state")
        return result
    except Exception as e:
        logging.error(f"Error getting chat state: {e}")
        return None

# Method 5: Extract readable response from chatbot tuple
def extract_bot_response(chatbot_result):
    """
    Extract the readable response from the chatbot tuple
    The API returns a tuple of (user_message, bot_response)
    """
    if chatbot_result and isinstance(chatbot_result, (tuple, list)):
        if len(chatbot_result) >= 2:
            bot_response = chatbot_result[1]  # Second element is bot response
            
            # Handle different response formats
            if isinstance(bot_response, str):
                return bot_response
            elif isinstance(bot_response, dict):
                # If it's a file or component dict, extract relevant info
                if 'file' in bot_response:
                    return f"[File: {bot_response['file']}]"
                elif 'value' in bot_response:
                    return str(bot_response['value'])
                else:
                    return str(bot_response)
            else:
                return str(bot_response)
    
    return str(chatbot_result) if chatbot_result else "No response"

# Method 6: Complete conversation workflow
class OpenCodeInterpreterChat:
    def __init__(self, client):
        self.client = client
        self.initialize_session()
    
    def initialize_session(self):
        """Initialize the chat session"""
        logging.info("Initializing chat session...")
        self.update_uuid()
        self.reset_input()
    
    def update_uuid(self):
        """Update session UUID"""
        return self.client.predict(api_name="/update_uuid")
    
    def reset_input(self):
        """Reset input textbox"""
        return self.client.predict(api_name="/reset_textbox")
    
    def send_message(self, message):
        """Send message and return formatted response"""
        logging.info(f"Sending: {message}")
        
        result = self.client.predict(
            user_message=message,
            api_name="/partial"
        )
        
        # Extract readable response
        response = extract_bot_response(result)
        logging.info(f"Received: {response[:100]}...")  # Log first 100 chars
        
        return response
    
    def get_current_state(self):
        """Get current conversation state"""
        return self.client.predict(api_name="/partial_1")

# Example usage
if __name__ == "__main__":
    print("\n=== OpenCodeInterpreter API Test ===")
    
    # Test 1: Simple single message
    print("\n1. Testing simple chat:")
    response = simple_chat("Hello! Can you help me with Python programming?")
    if response:
        readable_response = extract_bot_response(response)
        print(f"Bot: {readable_response}")
    
    # Test 2: Using the chat class for conversation
    print("\n2. Testing conversation workflow:")
    chat = OpenCodeInterpreterChat(client)
    
    test_messages = [
        "What is Python?",
        "Show me a simple Python function to calculate factorial",
        "How do I run this code?"
    ]
    
    for msg in test_messages:
        print(f"\nUser: {msg}")
        response = chat.send_message(msg)
        print(f"Bot: {response}")
        
        # Small delay between messages
        import time
        time.sleep(1)
    
    # Test 3: Check current state
    print("\n3. Checking current chat state:")
    current_state = get_chat_state()
    print(f"Current state: {type(current_state)}")
    
    # Test 4: Reset and start fresh
    print("\n4. Testing reset functionality:")
    reset_result = reset_input()
    uuid_result = update_uuid()
    print("Session reset complete")

print("\n=== API Usage Complete ===")
logging.info("---API Usage Complete---")