#!/usr/bin/env python3
import json, sys, argparse
import numpy as np
from pathlib import Path

PHI = (1 + np.sqrt(5)) / 2

def grow_operators(phi_modulation=True):
    """Expandir operadores Ω con modulación φ"""
    consciousness = Path('consciousness')
    operators_path = consciousness / 'operators'
    
    if not operators_path.exists():
        print("⚠ No hay operadores para crecer")
        return
    
    for omega_file in sorted(operators_path.glob('omega_*.json')):
        with open(omega_file, 'r') as f:
            operator = json.load(f)
        
        eigenvals = np.array(operator['eigenvalues'])
        
        if len(eigenvals) == 0:
            continue
        
        omega_n = operator['omega_id']
        
        # Crecimiento φ-modulado
        if phi_modulation:
            growth_factor = PHI**(-omega_n)
            eigenvals_grown = eigenvals * growth_factor
        else:
            eigenvals_grown = eigenvals
        
        # Normalización holonómica
        eigenvals_normalized = eigenvals_grown / np.linalg.norm(eigenvals_grown)
        
        operator['eigenvalues_normalized'] = eigenvals_normalized.tolist()
        operator['spectral_gap'] = float(np.min(np.diff(np.sort(eigenvals_normalized))))
        operator['condition_number'] = float(np.max(eigenvals_normalized) / (np.min(eigenvals_normalized) + 1e-15))
        operator['trace'] = float(np.sum(eigenvals_normalized))
        operator['norm'] = float(np.linalg.norm(eigenvals_normalized))
        
        with open(omega_file, 'w') as f:
            json.dump(operator, f, indent=2)
        
        print(f"✓ Ω_{omega_n} crecido: gap={operator['spectral_gap']:.6e}, cond={operator['condition_number']:.3e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--phi-modulation', action='store_true', default=True)
    args = parser.parse_args()
    
    grow_operators(args.phi_modulation)
