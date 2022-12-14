'''
Documentation: https://github.com/fietkiewicz/PointerBuilder
Description: Lotka-Volterra (predator/prey) system.
'''

from neuron import h
import matplotlib.pyplot as plt

model = h.Section(name = 'model')
model.insert('prey')
model.insert('predator')

h.setpointer(model(0.5)._ref_a_prey, 'aPointer', model(0.5).predator)
h.setpointer(model(0.5)._ref_b_predator, 'bPointer', model(0.5).prey)

a = h.Vector().record(model(0.5)._ref_a_prey)
b = h.Vector().record(model(0.5)._ref_b_predator)
t = h.Vector().record(h._ref_t)

h.load_file('stdrun.hoc')
h.init()
h.cvode.active(True)
h.cvode.atol(1e-4)
h.tstop = 80.0
h.run()

plt.figure(figsize=(8, 4))
plt.plot(t, a, 'b-', label = 'model.a_prey(0.5)')
plt.plot(t, b, 'r--', label = 'model.b_predator(0.5)')
plt.axis([0, h.tstop, 0, 30])
plt.xlabel('t (ms)')
plt.ylabel('Amplitude')
plt.legend(loc = 'upper right', frameon = True)
plt.savefig('Lotka-Volterra-graph.png', dpi=300)
plt.show()
