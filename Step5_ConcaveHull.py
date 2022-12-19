from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull, convex_hull_plot_2d
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection, LineCollection
from scipy.spatial import Delaunay
from scipy.spatial import Delaunay
from scipy.spatial import cKDTree
from descartes import PolygonPatch
import numpy as np
import matplotlib.pyplot as plt
from f_alpha_shapes import Alpha_Shaper
from shapely.geometry import Point

from scipy.spatial import Delaunay
import numpy as np
from collections import defaultdict

def alpha_shape_3D(pos, alpha):
    """
    Compute the alpha shape (concave hull) of a set of 3D points.
    Parameters:
        pos - np.array of shape (n,3) points.
        alpha - alpha value.
    return
        outer surface vertex indices, edge indices, and triangle indices
    """

    tetra = Delaunay(pos)
    # Find radius of the circumsphere.
    # By definition, radius of the sphere fitting inside the tetrahedral needs
    # to be smaller than alpha value
    # http://mathworld.wolfram.com/Circumsphere.html
    tetrapos = np.take(pos,tetra.vertices,axis=0)
    normsq = np.sum(tetrapos**2,axis=2)[:,:,None]
    ones = np.ones((tetrapos.shape[0],tetrapos.shape[1],1))
    a = np.linalg.det(np.concatenate((tetrapos,ones),axis=2))
    Dx = np.linalg.det(np.concatenate((normsq,tetrapos[:,:,[1,2]],ones),axis=2))
    Dy = -np.linalg.det(np.concatenate((normsq,tetrapos[:,:,[0,2]],ones),axis=2))
    Dz = np.linalg.det(np.concatenate((normsq,tetrapos[:,:,[0,1]],ones),axis=2))
    c = np.linalg.det(np.concatenate((normsq,tetrapos),axis=2))
    r = np.sqrt(Dx**2+Dy**2+Dz**2-4*a*c)/(2*np.abs(a))

    # Find tetrahedrals
    tetras = tetra.vertices[r<alpha,:]
    # triangles
    TriComb = np.array([(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)])
    Triangles = tetras[:,TriComb].reshape(-1,3)
    Triangles = np.sort(Triangles,axis=1)
    # Remove triangles that occurs twice, because they are within shapes
    TrianglesDict = defaultdict(int)
    for tri in Triangles:TrianglesDict[tuple(tri)] += 1
    Triangles=np.array([tri for tri in TrianglesDict if TrianglesDict[tri] ==1])
    #edges
    EdgeComb=np.array([(0, 1), (0, 2), (1, 2)])
    Edges=Triangles[:,EdgeComb].reshape(-1,2)
    Edges=np.sort(Edges,axis=1)
    Edges=np.unique(Edges,axis=0)

    Vertices = np.unique(Edges)
    return Vertices,Edges,Triangles


def determineInsideAlphaShapes(excludePoints_xy, clusters_xy):
    # fig, (ax0, ax1) = plt.subplots(1, 2)
    # ax0.scatter(*zip(*clusters_xy), s=0.5)
    # ax0.set_title('data')
    # ax1.set_title("with normalization")
    # ax1.scatter(*zip(*clusters_xy), s=0.5)
    try:
        shaper = Alpha_Shaper(clusters_xy)
        alpha_shape = shaper.get_shape(alpha=5)
        # ax1.add_patch(PolygonPatch(alpha_shape, alpha=0.2, color='r'))
        # plot_polygon = True
    except:
        try:
            shaper = Alpha_Shaper(clusters_xy, normalize=True)
            alpha_opt, alpha_shape = shaper.optimize()
            # ax1.add_patch(PolygonPatch(alpha_shape, alpha=0.2, color='r'))
            plot_polygon = True
        except:
            plot_polygon = False
    # if plot_polygon:
    #     plt.show()
    #判断excludePoints_xy哪些点在polygon内部
    contains = np.vectorize(lambda p: alpha_shape.contains(Point(p)), signature='(n)->()')
    inside = contains(excludePoints_xy)
    # plt.plot(clusters_xy[:, 0], clusters_xy[:, 1], '.g', markersize=2)
    # plt.plot(excludePoints_xy[inside, 0], excludePoints_xy[inside, 1], '.r', markersize=2)
    # plt.plot(excludePoints_xy[~inside, 0], excludePoints_xy[~inside, 1], '.k', markersize=0.5)
    # plt.show()
    return inside



def searchInsidePoints(neighbor, optimalNeighbor):
    large_rows = neighbor.view([('', neighbor.dtype)] * neighbor.shape[1])  # 大范围
    small_rows = optimalNeighbor.view([('', optimalNeighbor.dtype)] * optimalNeighbor.shape[1])
    excludePoints = np.setdiff1d(large_rows, small_rows).view(neighbor.dtype).reshape(-1, neighbor.shape[1])
    try:
        inside = determineInsideAlphaShapes(excludePoints[:, 1:3], optimalNeighbor[:, 1:3])  # 建立AlphaShapes外轮廓
    except:
        inside = []
    if len(inside) != 0:
        insidePoints = excludePoints[inside, :]
        max_z = max(optimalNeighbor[:, 3])
        min_z = min(optimalNeighbor[:, 3])
        if max_z < 1:
            insidePointsRefine = insidePoints[np.where(insidePoints[:, 3] < max_z)]
        else:
            insidePointsRefine1 = insidePoints[np.where(insidePoints[:, 3] > min_z)]
            insidePointsRefine = insidePoints[np.where(insidePointsRefine1[:, 3] < max_z)]
        if len(insidePointsRefine) != 0:
            optimalNeighborRefine = np.vstack((optimalNeighbor, insidePointsRefine))
        else:
            optimalNeighborRefine = optimalNeighbor
    else:
        optimalNeighborRefine = optimalNeighbor
    return optimalNeighborRefine