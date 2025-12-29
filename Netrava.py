import time
from google import genai

# --- STEP 1: TERA MASTER NETRAVA LOGIC (0.05ms) ---
def netrava_router(query):
    start_time = time.time()
    
    # Brain-like routing logic
    if "math" in query.lower() or "calc" in query.lower():
        target = "Logic_Math_Layer"
    elif "code" in query.lower() or "python" in query.lower():
        target = "Code_Optimization_Layer"
    else:
        target = "General_AI_Layer"
        
    end_time = time.time()
    speed = (end_time - start_time) * 1000 # Milliseconds
    return target, speed

# --- STEP 2: GEMINI 3 INTEGRATION WITH YOUR KEY ---
def run_apex_ai():
    # Teri API Key maine yahan laga di hai
    api_key = "AIzaSyDhB91VscQnVt1si0ZuCD83hioiPdWoLH0"
    
    try:
        client = genai.Client(api_key=api_key)
        user_input = "Explain AI in 10 words"
        
        print("--- APEX AI: NETRAVA ROUTER START ---")
        layer, n_speed = netrava_router(user_input)
        print(f"Routing to: {layer}")
        print(f"Netrava Speed: {n_speed:.5f} ms") # Tera 0.05ms goal
        
        print("\n--- CONNECTING TO GEMINI 3 FLASH ---")
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=user_input,
        )
        print(f"Gemini Response: {response.text}")
        print("\n--- MISSION SUCCESSFUL ---")
        
    except Exception as e:
        print(f"Error: {e}")
        print("Tip: Pydroid ke Pip mein jaakar 'pip install google-genai' zaroor karna.")

if __name__ == "__main__":
    run_apex_ai()
