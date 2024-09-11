import sys

def main():
    options = {
        "/name": "My name is Ryan Langlie",
        "/why": "I chose computer science as my field because I really like computers and their potential future functionality",
        "/what": "Im not entirely sure what I want to do out of college. I think I may want to try to master in either math or CS but im not at sure which school. I really want to do research though, something that could potentially help people.",
        "/fact": "I enjoy repairing electronics and soldering",
    }

    if len(sys.argv) < 2:
        print("Usage: python script.py [option]\nAvailable options:\n/name\t/why\n/what\t/fact")
        sys.exit()

    selection = sys.argv[1].lower()
    if selection in options:
        print(options[selection])
    else:
        print("-- Invalid Option\nAvailable options:\n/name\t/why\n/what\t/fact")
        sys.exit()
       
if __name__ == "__main__":
    main()