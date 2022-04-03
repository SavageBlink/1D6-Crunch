import drawingUtils
import mainUtils


mainUtils.computeConsumption("exmple_consommation.txt", "exmple_consommation_avec.txt")

optimisedPath = mainUtils.getOptimisedPath(1,2,"exmple_consommation_avec.txt")
print("opt",optimisedPath)

drawingUtils.drawMap(optimisedPath[0],optimisedPath[1],30,70)
