import drawingUtils
import mainUtils



optimisedPath = mainUtils.getOptimisedPath(1,200)

drawingUtils.drawMap(optimisedPath[0],optimisedPath[1],30,70)
