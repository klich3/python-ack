"""
█▀ █▄█ █▀▀ █░█ █▀▀ █░█
▄█ ░█░ █▄▄ █▀█ ██▄ ▀▄▀

Author: <Anton Sychev> (anton at sychev dot xyz) 
__init__.py (c) 2024 
Created:  2024-01-02 17:37:05 
Desc: Inilization of RocketStore
"""

from .ack import ack

def main():
    my_ack_instance = ack()
    # Realiza otras operaciones con la instancia de la clase ack

if __name__ == "__main__":
    main()