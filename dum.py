import os
import sys
import tty
import termios
import select

class TerminalCharacterMover:
    def __init__(self):
        self.position = 10  # Starting position
        self.character = '@'  # Character to move
        self.terminal_width = os.get_terminal_size().columns
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def get_key(self):
        """Get a single key press without pressing Enter"""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            # Check if input is available
            if select.select([sys.stdin], [], [], 0.1)[0]:
                key = sys.stdin.read(1)
                return key
            return None
        finally:
            termios.tcsetattr(fd, termios.TCSETATTR, old_settings)
    
    def draw_character(self):
        """Draw the character at its current position"""
        self.clear_screen()
        print("Use 'a' to move left, 'd' to move right, 'q' to quit")
        print("-" * self.terminal_width)
        
        # Create a line with the character at the specified position
        line = [' '] * self.terminal_width
        if 0 <= self.position < self.terminal_width:
            line[self.position] = self.character
        
        print(''.join(line))
        print("-" * self.terminal_width)
        print(f"Position: {self.position}")
    
    def move_left(self):
        """Move character left"""
        if self.position > 0:
            self.position -= 1
    
    def move_right(self):
        """Move character right"""
        if self.position < self.terminal_width - 1:
            self.position += 1
    
    def run(self):
        """Main game loop"""
        print("Terminal Character Mover")
        print("Controls: 'a' = left, 'd' = right, 'q' = quit")
        input("Press Enter to start...")
        
        try:
            while True:
                self.draw_character()
                key = self.get_key()
                
                if key:
                    if key.lower() == 'a':
                        self.move_left()
                    elif key.lower() == 'd':
                        self.move_right()
                    elif key.lower() == 'q':
                        break
                        
        except KeyboardInterrupt:
            pass
        finally:
            self.clear_screen()
            print("Thanks for playing!")

# Alternative simpler version using input() (requires pressing Enter)
class SimpleCharacterMover:
    def __init__(self):
        self.position = 10
        self.character = '@'
        self.width = 40  # Fixed width for simplicity
    
    def draw(self):
        """Draw the character"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print("Simple Character Mover (press Enter after each command)")
        print("Commands: 'a' = left, 'd' = right, 'q' = quit")
        print("-" * self.width)
        
        line = [' '] * self.width
        if 0 <= self.position < self.width:
            line[self.position] = self.character
        print(''.join(line))
        print("-" * self.width)
        print(f"Position: {self.position}")
    
    def run(self):
        """Main loop for simple version"""
        while True:
            self.draw()
            command = input("Enter command (a/d/q): ").lower()
            
            if command == 'a' and self.position > 0:
                self.position -= 1
            elif command == 'd' and self.position < self.width - 1:
                self.position += 1
            elif command == 'q':
                break
        
        print("Thanks for playing!")

if __name__ == "__main__":
    print("Choose version:")
    print("1. Real-time movement (no Enter required)")
    print("2. Simple movement (press Enter after each command)")
    
    choice = input("Enter choice (1 or 2): ")
    
    if choice == "1":
        # Check if we're on a Unix-like system for real-time input
        if os.name == 'posix':
            game = TerminalCharacterMover()
            game.run()
        else:
            print("Real-time input not supported on Windows. Using simple version.")
            game = SimpleCharacterMover()
            game.run()
    else:
        game = SimpleCharacterMover()
        game.run()