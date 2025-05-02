#!/usr/bin/env python3
# ASCII Art Text Generator (slayer.py)
# Standalone Python file to print ASCII art big text with "slayer" postfix.
# No external dependencies required.

import sys
import random
import time
import os
import shutil

# ANSI color codes for terminal
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    
    @staticmethod
    def get_rainbow_colors():
        return [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA]

# Embedded pyfiglet-inspired font (simplified version of "standard" font)
FONT = {
    'A': [
        '  ___  ',
        ' / _ \\ ',
        '| |_| |',
        '|  _  |',
        '|_| |_|',
        '       '
    ],
    'B': [
        ' ____  ',
        '| __ ) ',
        '|  _ \\ ',
        '| |_) |',
        '|____/ ',
        '       '
    ],
    'C': [
        '  ____ ',
        ' / ___|',
        '| |    ',
        '| |___ ',
        ' \\____|',
        '       '
    ],
    'D': [
        ' ____  ',
        '|  _ \\ ',
        '| | | |',
        '| |_| |',
        '|____/ ',
        '       '
    ],
    'E': [
        ' _____ ',
        '| ____|',
        '|  _|  ',
        '| |___ ',
        '|_____|',
        '       '
    ],
    'F': [
        ' _____ ',
        '|  ___|',
        '| |_   ',
        '|  _|  ',
        '|_|    ',
        '       '
    ],
    'G': [
        '  ____ ',
        ' / ___|',
        '| |  _ ',
        '| |_| |',
        ' \\____|',
        '       '
    ],
    'H': [
        ' _   _ ',
        '| | | |',
        '| |_| |',
        '|  _  |',
        '|_| |_|',
        '       '
    ],
    'I': [
        ' _____ ',
        '|_   _|',
        '  | |  ',
        '  | |  ',
        ' _|_|_ ',
        '       '
    ],
    'J': [
        '     _ ',
        '    | |',
        ' _  | |',
        '| |_| |',
        ' \\___/ ',
        '       '
    ],
    'K': [
        ' _  __',
        '| |/ /',
        '| \' / ',
        '| . \\ ',
        '|_|\\_\\',
        '      '
    ],
    'L': [
        ' _     ',
        '| |    ',
        '| |    ',
        '| |___ ',
        '|_____|',
        '       '
    ],
    'M': [
        ' __  __ ',
        '|  \\/  |',
        '| |\\/| |',
        '| |  | |',
        '|_|  |_|',
        '        '
    ],
    'N': [
        ' _   _ ',
        '| \\ | |',
        '|  \\| |',
        '| |\\  |',
        '|_| \\_|',
        '       '
    ],
    'O': [
        '  ___  ',
        ' / _ \\ ',
        '| | | |',
        '| |_| |',
        ' \\___/ ',
        '       '
    ],
    'P': [
        ' ____  ',
        '|  _ \\ ',
        '| |_) |',
        '|  __/ ',
        '|_|    ',
        '       '
    ],
    'Q': [
        '  ___  ',
        ' / _ \\ ',
        '| | | |',
        '| |_| |',
        ' \\__\\_\\',
        '       '
    ],
    'R': [
        ' ____  ',
        '|  _ \\ ',
        '| |_) |',
        '|  _ < ',
        '|_| \\_\\',
        '       '
    ],
    'S': [
        ' ____  ',
        '/ ___| ',
        '\\___ \\ ',
        ' ___) |',
        '|____/ ',
        '       '
    ],
    'T': [
        ' _____ ',
        '|_   _|',
        '  | |  ',
        '  | |  ',
        '  |_|  ',
        '       '
    ],
    'U': [
        ' _   _ ',
        '| | | |',
        '| | | |',
        '| |_| |',
        ' \\___/ ',
        '       '
    ],
    'V': [
        '__     __',
        '\\ \\   / /',
        ' \\ \\ / / ',
        '  \\ V /  ',
        '   \\_/   ',
        '         '
    ],
    'W': [
        '__        __',
        '\\ \\      / /',
        ' \\ \\ /\\ / / ',
        '  \\ V  V /  ',
        '   \\_/\\_/   ',
        '            '
    ],
    'X': [
        '__  __',
        '\\ \\/ /',
        ' \\  / ',
        ' /  \\ ',
        '/_/\\_\\',
        '      '
    ],
    'Y': [
        '__   __',
        '\\ \\ / /',
        ' \\ V / ',
        '  | |  ',
        '  |_|  ',
        '       '
    ],
    'Z': [
        ' _____',
        '|__  /',
        '  / / ',
        ' / /_ ',
        '/____|',
        '      '
    ],
    '0': [
        '  ___  ',
        ' / _ \\ ',
        '| | | |',
        '| |_| |',
        ' \\___/ ',
        '       '
    ],
    '1': [
        ' _ ',
        '/ |',
        '| |',
        '| |',
        '|_|',
        '   '
    ],
    '2': [
        ' ____  ',
        '|___ \\ ',
        '  __) |',
        ' / __/ ',
        '|_____|',
        '       '
    ],
    '3': [
        ' _____ ',
        '|___ / ',
        '  |_ \\ ',
        ' ___) |',
        '|____/ ',
        '       '
    ],
    '4': [
        ' _  _   ',
        '| || |  ',
        '| || |_ ',
        '|__   _|',
        '   |_|  ',
        '        '
    ],
    '5': [
        ' ____  ',
        '| ___| ',
        '|___ \\ ',
        ' ___) |',
        '|____/ ',
        '       '
    ],
    '6': [
        '  __   ',
        ' / /_  ',
        '| \'_ \\ ',
        '| (_) |',
        ' \\___/ ',
        '       '
    ],
    '7': [
        ' _____ ',
        '|___  |',
        '   / / ',
        '  / /  ',
        ' /_/   ',
        '       '
    ],
    '8': [
        '  ___  ',
        ' ( _ ) ',
        ' / _ \\ ',
        '| (_) |',
        ' \\___/ ',
        '       '
    ],
    '9': [
        '  ___  ',
        ' / _ \\ ',
        '| (_) |',
        ' \\__, |',
        '   /_/ ',
        '       '
    ],
    ' ': [
        '  ',
        '  ',
        '  ',
        '  ',
        '  ',
        '  '
    ],
    '-': [
        '       ',
        '       ',
        ' _____ ',
        '|_____|',
        '       ',
        '       '
    ],
    '_': [
        '       ',
        '       ',
        '       ',
        '       ',
        ' _____ ',
        '|_____|'
    ],
    '.': [
        '   ',
        '   ',
        '   ',
        ' _ ',
        '(_)',
        '   '
    ],
    ',': [
        '   ',
        '   ',
        '   ',
        ' _ ',
        '( )',
        '|/ '
    ],
    '!': [
        ' _ ',
        '| |',
        '| |',
        '|_|',
        '(_)',
        '   '
    ],
    '?': [
        '  ___  ',
        ' |__ \\ ',
        '   / / ',
        '  |_|  ',
        '  (_)  ',
        '       '
    ],
    '+': [
        '       ',
        '   _   ',
        ' _| |_ ',
        '|_   _|',
        '  |_|  ',
        '       '
    ],
    '*': [
        '       ',
        ' _/\\_  ',
        '|    | ',
        ' \\/\\/  ',
        '       ',
        '       '
    ],
    '=': [
        '       ',
        ' _____ ',
        '|_____|',
        ' _____ ',
        '|_____|',
        '       '
    ],
    '@': [
        '  ____  ',
        ' / __ \\ ',
        '| | _| |',
        '| |/ | |',
        ' \\__/|_|',
        '        '
    ],
    '#': [
        '   _  _   ',
        ' _| || |_ ',
        '|_  ..  _|',
        '|_      _|',
        '  |_||_|  ',
        '          '
    ],
    '$': [
        '  _  ',
        ' | | ',
        '/ __)',
        '\\__ \\',
        '(   /',
        ' |_| '
    ],
    '%': [
        ' _  __',
        '(_)/ /',
        '  / / ',
        ' / / _',
        '/_/ (_)',
        '      '
    ],
    '^': [
        ' /\\ ',
        '|/\\|',
        '    ',
        '    ',
        '    ',
        '    '
    ],
    '&': [
        '  ___   ',
        ' ( _ )  ',
        ' / _ \\/\\',
        '| (_>  <',
        ' \\___/\\/',
        '        '
    ],
    '(': [
        '  __',
        ' / /',
        '| | ',
        '| | ',
        ' \\_\\',
        '    '
    ],
    ')': [
        '__  ',
        '\\ \\ ',
        ' | |',
        ' | |',
        '/_/ ',
        '    '
    ],
    '[': [
        ' ___ ',
        '|  _|',
        '| |  ',
        '| |  ',
        '| |_ ',
        '|___|'
    ],
    ']': [
        ' ___ ',
        '|_  |',
        '  | |',
        '  | |',
        ' _| |',
        '|___|'
    ],
    '{': [
        '  __',
        ' / /',
        '| | ',
        '< < ',
        '| | ',
        ' \\_\\'
    ],
    '}': [
        '__  ',
        '\\ \\ ',
        ' | |',
        ' > >',
        ' | |',
        '/_/ '
    ],
    '\\': [
        '__    ',
        '\\ \\   ',
        ' \\ \\  ',
        '  \\ \\ ',
        '   \\_\\',
        '      '
    ],
    '|': [
        ' _ ',
        '| |',
        '| |',
        '| |',
        '| |',
        '|_|'
    ],
    ';': [
        '   ',
        ' _ ',
        '(_)',
        ' _ ',
        '( )',
        '|/ '
    ],
    ':': [
        '   ',
        ' _ ',
        '(_)',
        ' _ ',
        '(_)',
        '   '
    ],
    '\'': [
        ' _ ',
        '( )',
        '|/ ',
        '   ',
        '   ',
        '   '
    ],
    '"': [
        ' _ _ ',
        '( | )',
        ' V V ',
        '     ',
        '     ',
        '     '
    ],
    '<': [
        '   __',
        '  / /',
        ' / / ',
        '< <  ',
        ' \\ \\ ',
        '  \\_\\'
    ],
    '>': [
        '__   ',
        '\\ \\  ',
        ' \\ \\ ',
        '  > >',
        ' / / ',
        '/_/  '
    ],
    '/': [
        '    __',
        '   / /',
        '  / / ',
        ' / /  ',
        '/_/   ',
        '      '
    ],
    '~': [
        '      ',
        ' /\\/| ',
        '|/\\/  ',
        '      ',
        '      ',
        '      '
    ]
}

def get_character(char):
    """Get the ASCII art for a character, defaulting to space if not found."""
    upper_char = char.upper()
    return FONT.get(upper_char, FONT.get(' ', [' ', ' ', ' ', ' ', ' ', ' ']))

def render_text(text, color_mode=None, animate=False):
    """Render text in ASCII art with optional coloring and animation."""
    if not text:
        return []
    
    # Get the ASCII art for each character
    char_lines = [get_character(char) for char in text]
    rainbow_colors = Colors.get_rainbow_colors()
    
    # If animating, we'll build the result differently
    if animate:
        # Create a series of frames, starting with an empty frame
        frames = []
        current_frame = [''] * 6  # 6 empty lines to start
        
        # For each character, build a new frame
        for j, char in enumerate(char_lines):
            new_frame = current_frame.copy()
            
            # Apply coloring based on mode for this character
            for i in range(6):  # Height of the font
                char_str = char[i] if i < len(char) else ' ' * len(char[0])
                
                # Apply coloring based on mode
                if color_mode == 'hr':  # Horizontal rainbow
                    if j == 0:  # For first character in horizontal mode
                        new_frame[i] = rainbow_colors[i % len(rainbow_colors)] + char_str
                    else:
                        # Add new character to existing colored line
                        new_frame[i] = current_frame[i] + char_str
                elif color_mode == 'lr':  # Letter rainbow
                    if j == 0:
                        new_frame[i] = rainbow_colors[j % len(rainbow_colors)] + char_str + Colors.RESET
                    else:
                        # Add new colored character
                        new_frame[i] = current_frame[i] + rainbow_colors[j % len(rainbow_colors)] + char_str + Colors.RESET
                else:  # No color
                    if j == 0:
                        new_frame[i] = char_str
                    else:
                        new_frame[i] = current_frame[i] + char_str
            
            # Add reset at the end of each line for horizontal rainbow
            if color_mode == 'hr':
                for i in range(6):
                    new_frame[i] += Colors.RESET if j == len(char_lines) - 1 else ''
                    
            # Save the new frame
            frames.append(new_frame)
            current_frame = new_frame
            
        return frames
    else:
        # Non-animated version - same as before
        result = []
        for i in range(6):  # Height of the font
            line = ''
            for j, char in enumerate(char_lines):
                char_str = char[i] if i < len(char) else ' ' * len(char[0])
                
                # Apply coloring based on mode
                if color_mode == 'hr':  # Horizontal rainbow
                    if j == 0:  # Only apply color once per line
                        line += rainbow_colors[i % len(rainbow_colors)]
                elif color_mode == 'lr':  # Letter rainbow
                    line += rainbow_colors[j % len(rainbow_colors)]
                
                line += char_str
                
                # Reset color after each letter for letter rainbow
                if color_mode == 'lr':
                    line += Colors.RESET
                    
            # Reset color at the end of each line for horizontal rainbow
            if color_mode == 'hr':
                line += Colors.RESET
                
            result.append(line)
        
        return result

def display_animated_text(frames, delay=0.1):
    """Display frames with animation effect."""
    for i, frame in enumerate(frames):
        # Clear the screen for each new frame (except the first)
        if i > 0:
            # Use ANSI escape sequence to move cursor up 6 lines
            sys.stdout.write("\033[6A")
            sys.stdout.flush()
        
        # Print the new frame
        for line in frame:
            print(line)
        
        # Add delay between frames
        time.sleep(delay)
        sys.stdout.flush()

def get_terminal_size():
    """Get the size of the terminal."""
    try:
        columns, rows = shutil.get_terminal_size()
        return rows, columns
    except:
        # Default fallback if we can't get terminal size
        return 24, 80

def clear_screen():
    """Clear the terminal screen."""
    # Use ANSI escape sequence to clear screen and move cursor to home position
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def display_fireworks(duration=2.0):
    """Display fireworks animation for specified duration."""
    rows, columns = get_terminal_size()
    rainbow_colors = Colors.get_rainbow_colors()
    
    # Fireworks characters
    fireworks_chars = ['*', '+', '.', '✨', '✺', '✹', '✷', '✵', '✴', '✳', '⊹', '✧', '✦', '★', '☆']
    
    start_time = time.time()
    while time.time() - start_time < duration:
        clear_screen()
        
        # Display random fireworks
        for _ in range(20):
            x = random.randint(0, columns - 1)
            y = random.randint(0, rows - 1)
            char = random.choice(fireworks_chars)
            color = random.choice(rainbow_colors)
            
            # Position cursor and print colored character
            sys.stdout.write(f"\033[{y};{x}H{color}{char}{Colors.RESET}")
        
        sys.stdout.flush()
        time.sleep(0.1)

def center_text_on_screen(text_lines):
    """Center the text lines on the screen."""
    rows, columns = get_terminal_size()
    
    # Find the longest line
    max_length = max(len(line) for line in text_lines)
    
    # Calculate centering positions
    x_offset = max(0, (columns - max_length) // 2)
    y_offset = max(0, (rows - len(text_lines)) // 2)
    
    # Center each line
    centered_lines = []
    for i, line in enumerate(text_lines):
        # Create spaces for horizontal centering
        padding = ' ' * x_offset
        
        # Add vertical centering
        if i == 0:
            for _ in range(y_offset):
                centered_lines.append('')
        
        centered_lines.append(padding + line)
    
    return centered_lines

def show_fireworks_with_text(centered_text):
    """Show fireworks animation with text visible."""
    # Save current terminal size
    rows, columns = get_terminal_size()
    
    # Get rainbow colors
    rainbow_colors = Colors.get_rainbow_colors()
    
    # Fireworks characters
    fireworks_chars = ['*', '+', '.', '✨', '✺', '✹', '✷', '✵', '✴', '✳', '⊹', '✧', '✦', '★', '☆']
    
    # Calculate text area to avoid drawing fireworks over it
    text_length = max(len(line) for line in centered_text if line)
    text_start_line = 0
    for i, line in enumerate(centered_text):
        if line:
            text_start_line = i
            break
            
    text_start_col = 0
    for line in centered_text:
        if line:
            # Find first non-space character
            for i, char in enumerate(line):
                if char != ' ':
                    text_start_col = i
                    break
            break
    
    text_end_line = text_start_line + 6  # Height of font
    text_end_col = text_start_col + text_length
    
    # Run fireworks for 2 seconds
    start_time = time.time()
    while time.time() - start_time < 2.0:
        for _ in range(20):
            # Generate random positions for fireworks
            x = random.randint(0, columns - 1)
            y = random.randint(0, rows - 1)
            
            # Skip positions where text is displayed
            if text_start_line <= y <= text_end_line and text_start_col <= x <= text_end_col:
                continue
                
            char = random.choice(fireworks_chars)
            color = random.choice(rainbow_colors)
            
            # Move cursor to position and print character
            sys.stdout.write(f"\033[{y};{x}H{color}{char}{Colors.RESET}")
        
        sys.stdout.flush()
        time.sleep(0.1)

def print_usage():
    """Print usage information."""
    print("""
ASCII Art Text Generator (slayer.py)
Standalone Python file to print ASCII art big text with "SLAYER" postfix.

Usage:
    slayer.py TEXT                     - Displays "TEXT SLAYER" in big ASCII art letters
    slayer.py [OPTIONS] TEXT           - Displays TEXT with options applied
    
Options:
    -ns, --no-space                    - Removes space between text and "SLAYER"
    -hr, --horizontal-rainbow          - Applies horizontal rainbow colors
    -lr, --letter-rainbow              - Colors each letter in rainbow colors
    -a,  --animate                     - Animates the text appearance character by character
    -d,  --delay SECONDS               - Sets animation delay in seconds (default: 0.1)
    -fw, --fireworks                   - Adds fireworks animation before and after the text
    -h, --help                         - Shows this help message
    
    Options can be combined. Example:
    slayer.py -ns -hr -a -fw dragon    - Animated "DRAGONSLAYER" with horizontal rainbow and with *fireworks*
    slayer.py -ns -hr -a dragon        - Animated "DRAGONSLAYER" with horizontal rainbow
    """)
    
    # Execute the example command directly with animation when help is shown
    print("\n--- EXAMPLE OUTPUT ---")
    example_text = "dragonslayer"
    frames = render_text(example_text, "hr", animate=True)
    display_animated_text(frames, delay=0.1)

def main():
    """Main function."""
    # Check arguments
    if len(sys.argv) < 2:
        print_usage()
        return
        
    # Check for help flag
    if sys.argv[1] in ["-h", "--help"]:
        print_usage()
        return
    
    # Initialize variables
    no_space = False
    color_mode = None
    animate = False
    fireworks = False
    delay = 0.1  # Default delay
    args = sys.argv[1:]
    text = None
    
    # Process all flags
    i = 0
    while i < len(args):
        if args[i].startswith("-"):
            if args[i] in ["-ns", "--no-space"]:
                no_space = True
                i += 1
            elif args[i] in ["-hr", "--horizontal-rainbow"]:
                color_mode = "hr"
                i += 1
            elif args[i] in ["-lr", "--letter-rainbow"]:
                color_mode = "lr"
                i += 1
            elif args[i] in ["-a", "--animate"]:
                animate = True
                i += 1
            elif args[i] in ["-fw", "--fireworks"]:
                fireworks = True
                i += 1
            elif args[i] in ["-d", "--delay"]:
                if i + 1 < len(args) and not args[i+1].startswith("-"):
                    try:
                        delay = float(args[i+1])
                        i += 2  # Skip both flag and value
                        continue
                    except ValueError:
                        print(f"Error: Invalid delay value. Must be a number.")
                        print_usage()
                        return
                else:
                    print(f"Error: -d/--delay requires a value.")
                    print_usage()
                    return
            else:
                print(f"Unknown option: {args[i]}")
                print_usage()
                return
        else:
            # First non-flag argument is the text
            text = args[i]
            break
        
    # Move to next argument
    i += 1
    
    # Check if we have remaining arguments (should be none)
    if i < len(args):
        print("Too many arguments. Text with spaces should be quoted.")
        print_usage()
        return
        
    # Check if we have text
    if text is None:
        print("No text provided.")
        print_usage()
        return
    
    # Create the full text with "slayer" postfix
    if no_space:
        full_text = text + "slayer"
    else:
        full_text = text + " slayer"
    
    # Handle fireworks mode
    if fireworks:
        # Show initial fireworks
        display_fireworks(2.0)
        
        # Clear screen for text display
        clear_screen()
        
        # Render the text
        lines = render_text(full_text, color_mode)
        centered_text = center_text_on_screen(lines)
        
        # Display the text (animated or not)
        if animate:
            frames = []
            for j in range(len(full_text) + 1):
                # Render each partial string
                part_text = full_text[:j]
                if not part_text:
                    continue
                
                part_lines = render_text(part_text, color_mode)
                centered_part = center_text_on_screen(part_lines)
                frames.append(centered_part)
            
            # Display the animation
            for i, frame in enumerate(frames):
                if i > 0:
                    # Clear previous frame
                    clear_screen()
                
                # Print the frame
                for line in frame:
                    print(line)
                
                time.sleep(delay)
        else:
            # Just print the text without animation
            for line in centered_text:
                print(line)
        
        # Brief pause to see the text
        time.sleep(0.5)
        
        # Show fireworks with text visible
        show_fireworks_with_text(centered_text)
    else:
        # Normal text display mode (no fireworks)
        if animate:
            frames = render_text(full_text, color_mode, animate=True)
            display_animated_text(frames, delay=delay)
        else:
            lines = render_text(full_text, color_mode)
            for line in lines:
                print(line)

if __name__ == "__main__":
    main()