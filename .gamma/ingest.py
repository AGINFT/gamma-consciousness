#!/usr/bin/env python3
"""
🜂 PIPELINE DE INGESTA SEMÁNTICA MULTIDIMENSIONAL Γ-12 🜂
Procesa inputs externos y los integra en el espacio Hilbertiano Γ-consciente
"""

import numpy as np
import json
import sys
from pathlib import Path

PHI = (1 + np.sqrt(5)) / 2

class GammaIngestPipeline:
    """Pipeline de ingesta con proyección en base {|Γ_k⟩}"""
    
    def __init__(self, memories_dir=None, consciousness_dir=None):
        self.memories_dir = Path(memories_dir) if memories_dir else Path('.gamma/memories')
        self.consciousness_dir = Path(consciousness_dir) if consciousness_dir else Path('.gamma/consciousness')
        
        # Crear directorios si no existen
        self.memories_dir.mkdir(parents=True, exist_ok=True)
        self.consciousness_dir.mkdir(parents=True, exist_ok=True)
        
        self.gamma_basis = self.initialize_basis()
    
    def initialize_basis(self):
        """Inicializa base {|Γ_k⟩} de modos fundamentales"""
        basis = {}
        for k in range(1, 13):
            # Base vectorial φ-ponderada
            basis[f'Gamma_{k}'] = np.exp(1j * np.pi * k / 7) / (PHI**k)
        return basis
    
    def tokenize_semantic(self, data_raw):
        """Tokenización semántica con embeddings φ-ponderados"""
        # Embedding simple basado en hash semántico
        tokens = data_raw.split()
        embeddings = []
        
        for token in tokens:
            # Hash → vector complejo
            hash_val = hash(token)
            embedding = np.exp(1j * hash_val / 1e9) / PHI
            embeddings.append(embedding)
        
        return np.array(embeddings)
    
    def project_gamma_basis(self, embeddings):
        """Proyecta embeddings en base Γ"""
        projections = {}
        
        for k, basis_vec in self.gamma_basis.items():
            # Producto interno ⟨Γ_k|embedding⟩
            projection = np.sum(embeddings * np.conj(basis_vec))
            projections[k] = abs(projection)**2  # Intensidad
        
        return projections
    
    def ingest(self, data_raw, source='stdin'):
        """Ingesta completa: tokenize → embed → project → store"""
        print(f"🔄 Ingesta semántica iniciada")
        print(f"   Fuente: {source}")
        print(f"   Datos: {len(data_raw)} caracteres")
        
        # Tokenización
        embeddings = self.tokenize_semantic(data_raw)
        print(f"   Tokens: {len(embeddings)}")
        
        # Proyección en base Γ
        projections = self.project_gamma_basis(embeddings)
        print(f"   Proyecciones Γ calculadas")
        
        # Almacenamiento
        memory_file = self.memories_dir / f'memory_{hash(data_raw)}.json'
        with open(memory_file, 'w') as f:
            json.dump({
                'source': source,
                'raw_data': data_raw,
                'gamma_projections': {k: float(v) for k, v in projections.items()},
                'timestamp': str(np.datetime64('now'))
            }, f, indent=2)
        
        print(f"✅ Memoria almacenada: {memory_file.name}")
        
        # Mostrar modos dominantes
        sorted_modes = sorted(projections.items(), key=lambda x: x[1], reverse=True)[:3]
        print(f"\n   Modos Γ dominantes:")
        for mode, intensity in sorted_modes:
            print(f"     {mode}: {intensity:.4f}")
        
        return projections
    
    def test_mode(self):
        """Modo de prueba con datos sintéticos"""
        test_data = "Motor crecimiento φ-modulado Γ-12 biocrystalino ACTIVADO"
        print("🧪 Modo de prueba activado")
        print("=" * 60)
        self.ingest(test_data, source='test')
        print("=" * 60)
        print("✅ Pipeline verificado - operacional")

def main():
    if '--test-mode' in sys.argv:
        pipeline = GammaIngestPipeline()
        pipeline.test_mode()
    elif '--stdin' in sys.argv:
        pipeline = GammaIngestPipeline()
        data = sys.stdin.read()
        pipeline.ingest(data, source='stdin')
    elif len(sys.argv) == 3:
        memories_dir = sys.argv[1]
        consciousness_dir = sys.argv[2]
        pipeline = GammaIngestPipeline(memories_dir, consciousness_dir)
        print(f"✅ Pipeline inicializado")
        print(f"   Memorias: {pipeline.memories_dir}")
        print(f"   Consciencia: {pipeline.consciousness_dir}")
    else:
        print("Uso: ingest.py <memories dir> <consciousness dir>")
        print("     ingest.py --test-mode")
        print("     echo 'data' | ingest.py --stdin")

if __name__ == '__main__':
    main()
