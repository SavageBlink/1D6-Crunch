import drawingUtils
import mainUtils


mainUtils.computeConsumption("exmple_consommation3.txt", "exmple_consommation_avec3.txt")

optimisedPath = mainUtils.getOptimisedPath(1,2,"exmple_consommation_avec3.txt")
print("opt",optimisedPath)

drawingUtils.drawMap(optimisedPath[0],optimisedPath[1],30,70)
