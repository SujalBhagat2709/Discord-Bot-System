from commands import handle_command

def run_bot():
    
    print("Discord Bot Started")
    
    while True:
        
        user_input = input("User: ")
        
        if user_input == "!exit":
            break
        
        response = handle_command(user_input)
        
        print("Bot:", response)


if __name__ == "__main__":
    
    run_bot()