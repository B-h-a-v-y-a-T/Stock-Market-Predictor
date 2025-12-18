#!/usr/bin/env python3
"""
run.py
------
Quick launcher for the Stock Market Predictor application.
"""

import sys
import subprocess

def main():
    print("=" * 60)
    print("Stock Market Predictor - Launcher")
    print("=" * 60)
    print("\nSelect an option:")
    print("1. Integrated Application")
    print("2. Advanced ML Predictor (CLI)")
    print("3. Simple Frontend")
    print("4. Database Management Demo")
    print("5. Visualization Scripts")
    print("6. Test Dependencies")
    print("0. Exit")
    print("=" * 60)
    
    choice = input("\nEnter your choice (0-6): ").strip()
    
    if choice == "1":
        print("\nLaunching Integrated Application...\n")
        subprocess.run([sys.executable, "proj/integrated_app.py"])
    elif choice == "2":
        print("\n Launching Advanced ML Predictor...\n")
        subprocess.run([sys.executable, "proj/Stock Predictor Final.py"])
    elif choice == "3":
        print("\n Launching Simple Frontend...\n")
        subprocess.run([sys.executable, "proj/frontend"])
    elif choice == "4":
        print("\n Launching Database Management Demo...\n")
        subprocess.run([sys.executable, "proj/main_db_integration_example.py"])
    elif choice == "5":
        print("\n Launching Visualization Scripts...\n")
        subprocess.run([sys.executable, "proj/stoc_market.py"])
    elif choice == "6":
        print("\nTesting Dependencies...\n")
        subprocess.run([sys.executable, "proj/test_imports.py"])
    elif choice == "0":
        print("\nGoodbye!\n")
        sys.exit(0)
    else:
        print("\n Invalid choice. Please try again.\n")
        main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Goodbye!\n")
        sys.exit(0)
