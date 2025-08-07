from repository.examples import run_demo

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))

if __name__ == "__main__":
    run_demo(k=12)  # Puoi cambiare k per testare diverse difficoltà
