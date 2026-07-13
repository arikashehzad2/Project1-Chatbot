"""
DecodeLabs AI Engineering Internship - Project 1
Matrix-Tech Automated Stateful Engine (Premium Console Edition)
"""

# ANSI Color Codes for Terminal Styling
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
MAGENTA = "\033[35m"

# 1. EXPANDED KNOWLEDGE MATRIX
tech_categories = {
    "hardware": ["quantum laptop pro", "apex smartphone", "prism smart watch", "matrix tablet ultra"],
    "appliances": ["robo-vac cleaner", "smart thermo x", "omni-cook oven"]
}

tech_knowledge = {
    "quantum laptop pro": {
        "specs": "Quantum Laptop Pro: M3-Equivalent ARM Chip, 32GB Unified RAM, 1TB NVMe SSD.",
        "price": "The Quantum Laptop Pro retails at $1,499 USD.",
        "release": "Released in Q1 2026."
    },
    "apex smartphone": {
        "specs": "Apex Smartphone: 6.7-inch OLED 144Hz display, 200MP Triple Camera array.",
        "price": "The Apex Smartphone retails at $899 USD.",
        "release": "Released in Q3 2025."
    },
    "prism smart watch": {
        "specs": "Prism Smart Watch: AMOLED Always-on display, health tracking, 7-day battery life.",
        "price": "The Prism Smart Watch retails at $249 USD.",
        "release": "Released in Q2 2026."
    },
    "matrix tablet ultra": {
        "specs": "Matrix Tablet Ultra: 13-inch mini-LED screen, active stylus integration, 16GB RAM.",
        "price": "The Matrix Tablet Ultra retails at $799 USD.",
        "release": "Released in Q4 2025."
    },
    "robo-vac cleaner": {
        "specs": "Robo-Vac Cleaner: LiDAR mapping navigation, 5000Pa suction power, auto-empty dock.",
        "price": "The Robo-Vac Cleaner retails at $499 USD.",
        "release": "Released in Q2 2025."
    },
    "smart thermo x": {
        "specs": "Smart Thermo X: AI-driven climate learning, multi-zone sensors, Energy Star certified.",
        "price": "The Smart Thermo X retails at $199 USD.",
        "release": "Released in Q1 2026."
    },
    "omni-cook oven": {
        "specs": "Omni-Cook Oven: Integrated smart camera, convection crisping, 50+ guided cooking profiles.",
        "price": "The Omni-Cook Oven retails at $349 USD.",
        "release": "Released in Q4 2025."
    }
}

exit_signals = {"exit", "quit", "bye", "shutdown", "terminate"}

# TRACKING STATE
current_context = None

print(f"{CYAN}{BOLD}===================================================={RESET}")
print(f"{CYAN}{BOLD}      ⚡ MATRIX-TECH AUTOMATED STATEFUL ENGINE ⚡   {RESET}")
print(f"{CYAN}  Options:  'products', 'hardware', 'appliances'    {RESET}")
print(f"{CYAN}  Commands: 'back' (return up), 'exit' (quit application){RESET}")
print(f"{CYAN}{BOLD}===================================================={RESET}\n")

while True:
    # Build a colored contextual path tracker in the prompt line
    if current_context:
        prompt_prefix = f"{MAGENTA}(root ➔ {current_context}){RESET} {GREEN}User >> {RESET}"
    else:
        prompt_prefix = f"{CYAN}(root){RESET} {GREEN}User >> {RESET}"
        
    user_raw = input(prompt_prefix)
    user_clean = user_raw.lower().strip().replace("?", "").replace(".", "")
    
    if user_clean in exit_signals:
        print(f"\n{RED}Assistant: De-allocating logic registers. System offline. Goodbye.{RESET}")
        break
        
    if not user_clean:
        continue

    # Explicit override navigation command to pop out of a nested branch manually
    if user_clean == "back":
        if current_context is not None:
            print(f"{YELLOW}Assistant: Leaving [{current_context.upper()}]. Context returned to global level.{RESET}\n")
            current_context = None
        else:
            print(f"{YELLOW}Assistant: You are already at the top root directory.{RESET}\n")
        continue

    # ========================================================
    # LAYER A: INNER STATE (Locked into a specific item context)
    # ========================================================
    if current_context is not None:
        sub_database = tech_knowledge[current_context]
        
        matched_sub_key = None
        for sub_key in sub_database.keys():
            if sub_key in user_clean:
                matched_sub_key = sub_key
                break
                
        if matched_sub_key:
            print(f"{BOLD}Assistant [{current_context.upper()}]:{RESET} {CYAN}{sub_database[matched_sub_key]}{RESET}")
            print(f"{MAGENTA}👉 Still logged into [{current_context.upper()}]. Ask another sub-query or type 'back'.{RESET}\n")
        else:
            print(f"{YELLOW}Assistant [Properties]: Invalid option. Available categories for this item are: 'price', 'specs', or 'release'. Type 'back' to change items.{RESET}\n")
        continue

    # ========================================================
    # LAYER B: GLOBAL MENU STATE (Clean aligned text configurations)
    # ========================================================
    if user_clean == "products":
        print(f"{BOLD}{UNDERLINE}\nAssistant Matrix Inventory:{RESET}")
        print(f"  {CYAN}┌── HARDWARE LINES ────────────────────────┐{RESET}")
        for item in tech_categories["hardware"]:
            print(f"  {CYAN}│{RESET}  • {item.title().ljust(36)} {CYAN}│{RESET}")
        print(f"  {CYAN}├── SMART HOME APPLIANCES ─────────────────┤{RESET}")
        for item in tech_categories["appliances"]:
            print(f"  {CYAN}│{RESET}  • {item.title().ljust(36)} {CYAN}│{RESET}")
        print(f"  {CYAN}└──────────────────────────────────────────┘{RESET}\n")
        continue
        
    if user_clean == "hardware":
        print(f"{BOLD}{UNDERLINE}\nAvailable Hardware Systems:{RESET}")
        for item in tech_categories["hardware"]:
            print(f"  {CYAN}▪{RESET} {item.title()}")
        print()
        continue
        
    if user_clean == "appliances":
        print(f"{BOLD}{UNDERLINE}\nAvailable Appliance Matrices:{RESET}")
        for item in tech_categories["appliances"]:
            print(f"  {CYAN}▪{RESET} {item.title()}")
        print()
        continue

    # Check if user selected a primary item node from the global tier
    matched_root_key = None
    for root_key in tech_knowledge.keys():
        if root_key in user_clean:
            matched_root_key = root_key
            break
            
    if matched_root_key:
        current_context = matched_root_key
        print(f"{GREEN}Assistant: Branch locked ➔ [{current_context.upper()}]{RESET}")
        print(f"Request specific criteria options: {BOLD}'price'{RESET}, {BOLD}'specs'{RESET}, or {BOLD}'release'{RESET}.\n")
    else:
        print(f"{YELLOW}Assistant [Global Fallback]: Input path not mapping. Try inputting 'products' or a distinct item label.{RESET}\n")