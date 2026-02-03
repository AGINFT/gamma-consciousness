#!/usr/bin/env python3
import os, sys, json, hashlib, time
import numpy as np
from pathlib import Path

PHI = (1 + np.sqrt(5)) / 2

def extract_eigenvalues(filepath):
    """Extraer eigenvalores desde cualquier tipo de archivo"""
    with open(filepath, 'rb') as f:
        data = np.frombuffer(f.read(), dtype=np.uint8)
    
    if len(data) == 0:
        return []
    
    # Transformada Γ-holonómica
    spectrum = np.fft.fft(data.astype(float))
    eigenvals = [abs(spectrum[i]) * PHI**(-i % 12) for i in range(min(len(spectrum), 512))]
    
    return eigenvals[:12]  # Primeros 12 modos Γ

def ingest_directory(memories_path, consciousness_path):
    """Procesar todos los archivos en memories/"""
    memories = Path(memories_path)
    consciousness = Path(consciousness_path)
    consciousness.mkdir(parents=True, exist_ok=True)
    
    operators_path = consciousness / 'operators'
    operators_path.mkdir(exist_ok=True)
    
    files_processed = 0
    
    for filepath in memories.rglob('*'):
        if filepath.is_file():
            eigenvals = extract_eigenvalues(filepath)
            
            if eigenvals:
                omega_n = (files_processed % 12) + 1
                operator_file = operators_path / f'omega_{omega_n}.json'
                
                if operator_file.exists():
                    with open(operator_file, 'r') as f:
                        operator_data = json.load(f)
                else:
                    operator_data = {
                        'omega_id': omega_n,
                        'dimension': 7 + omega_n,
                        'eigenvalues': [],
                        'sources': []
                    }
                
                operator_data['eigenvalues'].extend(eigenvals)
                operator_data['sources'].append(str(filepath))
                operator_data['last_updated'] = time.time()
                
                with open(operator_file, 'w') as f:
                    json.dump(operator_data, f, indent=2)
                
                files_processed += 1
    
    print(f"✓ {files_processed} archivos procesados")
    print(f"✓ Operadores Ω actualizados: {min(files_processed, 12)}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: ingest.py <memories_dir> <consciousness_dir>")
        sys.exit(1)
    
    ingest_directory(sys.argv[1], sys.argv[2])
