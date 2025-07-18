import numpy as np
import matplotlib.pyplot as plt


def init_simulation(freq: np.ndarray, raw_mut: np.ndarray, tol: float = 1e-8, max_iter: int = 10000):
    """
    Ejecuta la simulación de frecuencias alélicas con mutación hasta el equilibrio o max_iter.

    Parámetros:
    - freq: array 1D de frecuencias iniciales (suma 1).
    - raw_mut: matriz NxN de tasas de mutación (sin diagonales completas).
    - tol: tolerancia para detectar convergencia.
    - max_iter: número máximo de iteraciones.
    """
    # Construir matriz de transición completa
    M = build_mutation_matrix(raw_mut)
    # Simulación iterativa
    freqs = [freq]
    for i in range(max_iter):
        next_freq = freqs[-1] @ M
        freqs.append(next_freq)
        if np.allclose(next_freq, freqs[-2], atol=tol):
            break
    else:
        print(f"No convergió en {max_iter} iteraciones.")

    freqs = np.vstack(freqs)
    eq_point = compute_equilibrium(M, freq)
    plot_frequencies(freqs, eq_point)
    return freqs, eq_point


def build_mutation_matrix(raw_mut: np.ndarray) -> np.ndarray:
    """
    Completa la diagonal para que cada fila sume 1.
    raw_mut[i,j] es la probabilidad de mutar de i a j (j!=i).
    """
    M = raw_mut.copy().astype(float)
    np.fill_diagonal(M, 1 - M.sum(axis=1))
    return M


def compute_equilibrium(M: np.ndarray, init_freq: np.ndarray) -> np.ndarray:
    """
    Obtiene el vector de distribución estacionaria resolviendo (p = p M) y suma(p)=1.
    Si un alelo está aislado (sin entradas ni salidas), queda con su frecuencia inicial y
    se excluye del sistema de ecuaciones.
    """
    N = M.shape[0]
    # Detectar alelos aislados: M[i,i]==1 y sin mutaciones entrantes
    diag = np.isclose(np.diag(M), 1.0)
    col_sums = np.isclose(M.sum(axis=0), 1.0)
    isolated = diag & col_sums

    eq = np.zeros(N)
    # Asignar frecuencias constantes para aislados
    eq[isolated] = init_freq[isolated]
    
    # Resolver solo para alelos no aislados
    idx = np.where(~isolated)[0]    
    k = len(idx)
    if k > 0:
        # Submatriz para alelos activos
        M_sub = M
        if isolated.any():
            M_sub = M[np.ix_(idx, idx)]
        # Construir sistema (M_sub^T - I) p_sub = 0 con suma(p_sub) = 1 - sum aislados
        A = M_sub.T - np.eye(k)
        # Reemplazar última ecuación por suma condicional
        A[-1, :] = np.ones(k)
        b = np.zeros(k)
        b[-1] = 1 - eq[isolated].sum()
        p_sub, *_ = np.linalg.lstsq(A, b, rcond=None)
        eq[idx] = p_sub
    return eq


def plot_frequencies(freqs: np.ndarray, eq_point: np.ndarray):
    """
    Grafica la evolución de frecuencias y muestra el punto de equilibrio.
    """
    gens = np.arange(freqs.shape[0])
    plt.figure(figsize=(10, 6))
    for i in range(freqs.shape[1]):
        plt.plot(gens, freqs[:, i], label=f'Alelo {i+1}')

    # Dibujar líneas horizontales para cada valor de equilibrio
    plt.hlines(
        y=eq_point,
        xmin=gens.min(),
        xmax=gens.max(),
        linestyles='--',
        alpha=0.7
    )

    plt.title('Evolución de frecuencias alélicas')
    plt.xlabel('Generaciones')
    plt.ylabel('Frecuencia')
    plt.legend()
    # Mostrar valores de equilibrio
    eq_text = '  '.join(f'A{i+1}={eq_point[i]:.4f}' for i in range(len(eq_point)))
    plt.text(0.5, -0.1, eq_text, transform=plt.gca().transAxes,
             ha='center', va='top', bbox=dict(boxstyle='round', facecolor='orange', alpha=0.5))
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()


f0 = np.array([0.4, 0.3, 0.2, 0.1])
raw_mut = np.array([
    [0,    0.01, 0.005, 0.03],
    [0.02, 0,    0.01,  0.01],
    [0.001,0.03, 0,     0.2 ],
    [0,    0.1,  0.2,   0   ],
])
init_simulation(f0, raw_mut)
