#!/bin/bash

# Function to animate text
animate_text() {
    text="$1"
    for ((i = 0; i < ${#text}; i++)); do
        echo -ne "\e[38;2;0;255;0m${text:$i:1}" # Set color to RGB(0, 255, 0) which is equivalent to #00ff00
        sleep 0.09
    done
    echo -ne " \e[38;2;0;255;0m\e[0m<< "
}

# Function to display the menu
display_menu() {
    clear
    echo -e "\e[38;2;0;255;0m" # Set color to RGB(0, 255, 0) which is equivalent to #00ff00
    echo " _____ _           ____                     "
    echo "|_   _| |__   ___ / ___|_ __ ___  ___ _ __  "
    echo "  | | | '_ \ / _ \ |  _| '__/ _ \/ _ \ '_ \ "
    echo "  | | | | | |  __/ |_| | | |  __/  __/ | | |"
    echo "  |_| |_| |_|\___|\____|_|  \___|\___|_| |_|"
    echo -e "\e[0m"
    echo -n "Made by >> "
    animate_text "TheGreenH4ck3r"
    echo -e "\e[38;2;0;255;0m"
    echo " "
    echo "[*] Select a number..."
    echo "[1] Facebook login form."
    echo "[0] Exit"
}

# Function to handle user input
handle_input() {
   read -p $'\e[38;2;0;255;0mTheGreen☠️ H4ck3r ~# \e[0m' choice
    case $choice in
        1)
            python3 Tool/runScript.py
            ;;
        0)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a valid option."
            handle_input
            ;;
    esac
}

# Main function
main() {
    while true; do
        display_menu
        handle_input
    done
}

# Execute the main function
main
