from qiskit import Aer, QuantumCircuit, transpile, assemble, execute
from qiskit.visualization import plot_histogram

# Création du circuit
qc = QuantumCircuit(3, 3)

# Supposons que le joueur choisit la porte 0. On met donc un état |1> sur cette porte.
qc.x(0)

# On ajoute une superposition à la porte choisie.
qc.h(0)

# Supposons que Monty (l'hôte) ouvre la porte 1.
# Monty ouvre la porte 1 seulement si le trésor est derrière la porte 0 ou 2.
# Nous pouvons utiliser une porte Toffoli pour simuler cette action.
qc.ccx(0, 2, 1)

# Si le joueur décide de changer son choix après que Monty ait ouvert une porte,
# nous créons une superposition à nouveau.
qc.h(0)

# Mesurer le résultat
qc.measure([0, 1, 2], [0, 1, 2])

qc.draw('mpl')

# Exécution du circuit
backend = Aer.get_backend('qasm_simulator')
t_qc = transpile(qc, backend)
qobj = assemble(t_qc)
result = execute(qc, backend).result()
counts = result.get_counts()

# Affichage des résultats
print(plot_histogram(counts))
