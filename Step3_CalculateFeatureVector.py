from sklearn.neighbors import KDTree
import numpy as np
import MyFileOperator
import math
from scipy.spatial import cKDTree

'''
3D Feature
# omnivariance anisotropy eigenentropy summation localCurvature linearity planarity sphericity
omnivariance = pow(lambda_1*lambda_2*lambda_3, 1/3) 各向同性   ###
anisotropy = (lambda_1-lambda_3)/lambda_1 各向异性  
eigenentropy = -(lambda_1 * math.log(lambda_1) + lambda_2 * math.log(lambda_2) + lambda_3 * math.log(lambda_3)) 特征熵   ###
summation = lambda_1 + lambda_2 + lambda_3 特征值和
localCurvature / change of curvature = lambda_3/summation 曲率变化   ###
linearity = (lambda_1-lambda_2)/lambda_1 线性指数
planarity = (lambda_2 - lambda_3)/lambda_1 面状指数
sphericity / Scattering = lambda_3/lambda_1 发散状指数

S = l[0] + l[1] + l[2] #Sum of eigenvalues
e = [l[0]/S,l[1]/S,l[2]/S] #normalised eigenvalues
L = (e[0]-e[1])/e[0] #Linearity
P = (e[1]-e[2])/e[0] #Planarity
S = e[2]/e[0] #Scattering
O = (e[0]*e[1]*e[2])**(1.0/3.0) #Omnivariance
A = (e[0]-e[2])/e[0] #Anisotropy
E = -(l[0]*log(l[0])+l[1]*log(l[1])+l[2]*log(l[2])) #Eigenentropy
C = l[2]/S #Change of curvature
'''

path = 'Data/'  # 'F:\\2PhD\\Technology\\MyCode\\UBDA\\SphericalConvolution\\Data\\'
meanPointSpacing_L1C1 = 0.592
meanPointSpacing_L1C2 = 0.547
meanPointSpacing_L1C3 = 0.511
meanPointSpacing = meanPointSpacing_L1C2
radius = 5 * meanPointSpacing   #修改3     #要先确定需要几个mean point spacing的范围内的点来计算geometric feature

ID_Pos = 0
x_Pos = 1
y_Pos = 2
z_Pos = 3
intensity_Pos = 4  # intensity数据在FeatureData文件中位置



def calculateGeometricFeature(eigen_vals):
    lambda_1 = eigen_vals[0] / (eigen_vals[0] + eigen_vals[1] + eigen_vals[2])  # normalization
    lambda_2 = eigen_vals[1] / (eigen_vals[0] + eigen_vals[1] + eigen_vals[2])
    lambda_3 = eigen_vals[2] / (eigen_vals[0] + eigen_vals[1] + eigen_vals[2])

    try:
        omnivariance = pow(lambda_1*lambda_2*lambda_3, 1/3)
    except:
        omnivariance = 0
    try:
        anisotropy = (lambda_1-lambda_3)/lambda_1
    except:
        anisotropy = 0
    try:
        eigenentropy = -(lambda_1 * math.log(lambda_1) + lambda_2 * math.log(lambda_2) + lambda_3 * math.log(lambda_3))
    except:
        eigenentropy = 0
    try:
        summation = eigen_vals[0] + eigen_vals[1] + eigen_vals[2]
    except:
        summation = 0
    try:
        # localCurvature = lambda_3/summation  #
        localCurvature = lambda_3
    except:
        localCurvature = 0
    try:
        linearity = (lambda_1-lambda_2)/lambda_1
    except:
        linearity = 0
    try:
        planarity = (lambda_2 - lambda_3)/lambda_1
    except:
        planarity = 0
    try:
        sphericity = lambda_3/lambda_1
    except:
        sphericity = 0

    if math.isinf(omnivariance) or math.isnan(omnivariance):
        omnivariance = 0
    if math.isinf(anisotropy) or math.isnan(anisotropy):
        anisotropy = 0
    if math.isinf(eigenentropy) or math.isnan(eigenentropy):
        eigenentropy = 0
    if math.isinf(summation) or math.isnan(summation):
        summation = 0
    if math.isinf(omnivariance) or math.isnan(omnivariance):
        omnivariance = 0
    if math.isinf(localCurvature) or math.isnan(localCurvature):
        localCurvature = 0
    if math.isinf(linearity) or math.isnan(linearity):
        linearity = 0
    if math.isinf(planarity) or math.isnan(planarity):
        planarity = 0
    if math.isinf(sphericity) or math.isnan(sphericity):
        sphericity = 0
    geometricFeature = np.array([omnivariance, anisotropy, eigenentropy, summation, localCurvature, linearity, planarity, sphericity])
    return geometricFeature

def calculateGeoFeatureVector(optimalNeighbor, centerPoint):
    try:
        NeighborPointXYZ = optimalNeighbor[1:len(optimalNeighbor), 1:4]
    except:
        stop = 0
    centerPointMatrix = np.tile(centerPoint[0, 1:4], (len(NeighborPointXYZ), 1))
    try:
        covMatrix = ((NeighborPointXYZ - centerPointMatrix).T).dot((NeighborPointXYZ - centerPointMatrix)) / len(NeighborPointXYZ)
        eigen_vals, eigen_vecs = np.linalg.eig(covMatrix)
        eigen_vals = sorted(eigen_vals, reverse=True)
        if isinstance(eigen_vals[0], complex) or isinstance(eigen_vals[1], complex) or isinstance(eigen_vals[2], complex):
            geometricFeature = np.array([0, 0, 0, 0, 0, 0, 0, 0])
        else:
            geometricFeature = calculateGeometricFeature(eigen_vals)
    except:
        geometricFeature = np.array([0, 0, 0, 0, 0, 0, 0, 0])
    geometricFeatureVector = np.array([centerPoint[0, 0], geometricFeature[0], geometricFeature[1], geometricFeature[2], geometricFeature[3], \
                              geometricFeature[4], geometricFeature[5], geometricFeature[6], geometricFeature[7]])
    return geometricFeatureVector



def calculateEleRadFeatureVector(optimalNeighbor):
    mean_ele = np.mean(optimalNeighbor[:, 3].T)
    var_ele = np.var(optimalNeighbor[:, 3].T)

    mean_ch2 = np.mean(optimalNeighbor[:, 4].T)
    var_ch2 = np.var(optimalNeighbor[:, 4].T)

    mean_ch1 = np.mean(optimalNeighbor[:, 7].T)
    var_ch1 = np.var(optimalNeighbor[:, 7].T)

    mean_ch3 = np.mean(optimalNeighbor[:, 9].T)
    var_ch3 = np.var(optimalNeighbor[:, 9].T)
    EleRadFeatureVector = np.array([mean_ele, var_ele, mean_ch2, var_ch2, mean_ch1, var_ch1, mean_ch3, var_ch3])
    return EleRadFeatureVector



def calculateFeatureVector(optimalNeighbor, centerPoint):
    geoFeature = calculateGeoFeatureVector(optimalNeighbor, centerPoint)
    eleRadFeature = calculateEleRadFeatureVector(optimalNeighbor)
    featureVector = np.concatenate([geoFeature, eleRadFeature])
    return featureVector




