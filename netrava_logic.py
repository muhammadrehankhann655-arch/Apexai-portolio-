import time

# Ye hai teri dimaag ki files (Abhi khali hain)
brain_layers = {
    "maths": "Layer_Math_Active",
    "vision": "Layer_Vision_Active",
    "other": "General_Layer"
}

def check_my_logic(user_input):
    print(f"\n[Analysing]: {user_input}")
    start = time.time()
    
    # Ye hai tera dimaag (The Router)
    # Ye sirf keywords pakadta hai jaise asli dimaag karta hai
    words = user_input.lower().split()
    
    if any(word in ["+", "-", "kitne", "maths", "hisab"] for word in words):
        decision = "maths"
    elif any(word in ["kya", "dekha", "nazar", "aankh"] for word in words):
        decision = "vision"
    else:
        decision = "other"
        
    end = time.time()
    speed = (end - start) * 1000
    
    print(f"🧠 Logic Decision: Send to '{brain_layers[decision]}'")
    print(f"⚡ Speed: {speed:.4f} ms")

# --- AB TU ISSE TEST KAR ---
# Kuch bhi naya likh kar dekh, code wahi layer chunega
check_my_logic("Bhai 5 aur 5 kitne honge?") 
check_my_logic("Maine ek botal dekhi hai")
