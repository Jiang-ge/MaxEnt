import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D, axes3d
from matplotlib.pyplot import MultipleLocator
import matplotlib.pyplot as plt


# # ---------------------------画classification results accuracy结果图---------------------------------
# fig, ax = plt.subplots()
# path_r = 'ubdaDataGaussian/NewData/6ClassificationResult/GaussianKernel/'
# readfile = open(path_r+'Results.txt', "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData = np.empty([lineNum, 10], dtype=float)
# # returnData = np.empty([lineNum], dtype=float)
#
# for readline in readAllLine:
#     returnData[i, 0] = float(readline.split('\t\t')[0])
#     returnData[i, 1] = float(readline.split('\t\t')[1])
#     returnData[i, 2] = float(readline.split('\t\t')[2])
#     returnData[i, 3] = float(readline.split('\t\t')[3])
#     returnData[i, 4] = float(readline.split('\t\t')[4])
#     returnData[i, 5] = float(readline.split('\t\t')[5])
#     returnData[i, 6] = float(readline.split('\t\t')[6])
#     returnData[i, 7] = float(readline.split('\t\t')[7])
#     returnData[i, 8] = float(readline.split('\t\t')[8])
#     returnData[i, 9] = float(readline.split('\t\t')[9])
#     # returnData[i, 10] = float(readline.split('\t')[10])
#     # returnData[i, 11] = float(readline.split('\t')[11])
#     # returnData[i, 12] = float(readline.split('\t')[12])
#     # returnData[i, 13] = float(readline.split('\t')[13])
#     # returnData[i, 14] = float(readline.split('\t\t')[14])
#     # returnData[i, 15] = float(readline.split('\t\t')[15])
#     i = i + 1
# readfile.close()
#
# # for i in range(7):
#
# # x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18])
# x = np.array([0, 1,  2,  3,  4,  5,  6,  7, 8, 9])
#
#
#
#
# y7 = returnData[2, :]
# l7 = plt.plot(x, y7, 'c--', marker='o', label='1  Random Forest')
#
# y2 = returnData[1, :]
# l2 = plt.plot(x, y2, 'r--', marker='o', label='2  Decision Tree')
#
# y3 = returnData[3, :]
# l3 = plt.plot(x, y3, 'g--', marker='o', label='3  K-Nearest Neighbor')
# y8 = returnData[7, :]
# l8 = plt.plot(x, y8, 'm--', marker='o', label='4  Adaptive Boosting')
# y6 = returnData[6, :]
# l6 = plt.plot(x, y6, 'k--', marker='o', label='5  Quadratic Discriminant Analysis')
# y4 = returnData[4, :]
# l4 = plt.plot(x, y4, 'y--', marker='o', label='6  Gaussian Naive Bayes')
# y1 = returnData[0, :]
# l1 = plt.plot(x, y1, color='0.5', ls='--', marker='o', label='7  Support Vector Machine')
# y5 = returnData[5, :]
# l5 = plt.plot(x, y5, 'b--', marker='o', label='8  Linear Discriminant Analysis')
# y9 = returnData[8, :]
# l9 = plt.plot(x, y9, color='tan', ls='--', marker='o', label='9  Multi-layer Perceptron')
#
#
#
# # plt.xticks(x, names, rotation=45)
# x_major_locator=MultipleLocator(1)
# ax=plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
# plt.xlim(0, 9)
# plt.ylim(0.6, 1)
#
# # plt.title('The Classification Accuracy of Different Classifiers')
# plt.xlabel('The Number of Mean Point Spacing')
# plt.ylabel('Accuracy Value')
# num1 = -0.095
# num2 = 1.04
# num3 = 3
# num4 = 0
# plt.legend(bbox_to_anchor=(num1, num2), loc=num3, borderaxespad=num4, ncol=2)
# plt.show()
# fig.savefig('Figures/newDataAccuracy.eps', dpi=600, format='eps')


#
# # ---------------------------画combination of feature vectors for classification results accuracy结果图---------------------------------
# fig, ax = plt.subplots()
# # path_r = 'ubdaDataGaussian/MyBeforeCutData/testNeighborWeight/6ClassificationResult/GaussianKernel_addGeometric/'
# path_r = 'ubdaDataGaussian/NewData/6ClassificationResult/GaussianKernel_addGeometric/'
# # readfile = open(path_r+'Plot.txt', "r")
# readfile = open(path_r+'OptimalFeature.txt', "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData = np.empty([lineNum, 13], dtype=float)
# # returnData = np.empty([lineNum], dtype=float)
#
# for readline in readAllLine:
#     returnData[i, 0] = float(readline.split('\t')[0])
#     returnData[i, 1] = float(readline.split('\t')[1])
#     returnData[i, 2] = float(readline.split('\t')[2])
#     returnData[i, 3] = float(readline.split('\t')[3])
#     returnData[i, 4] = float(readline.split('\t')[4])
#     returnData[i, 5] = float(readline.split('\t')[5])
#     returnData[i, 6] = float(readline.split('\t')[6])
#     returnData[i, 7] = float(readline.split('\t')[7])
#     returnData[i, 8] = float(readline.split('\t')[8])
#     returnData[i, 9] = float(readline.split('\t')[9])
#     returnData[i, 10] = float(readline.split('\t')[10])
#     returnData[i, 11] = float(readline.split('\t')[11])
#     returnData[i, 12] = float(readline.split('\t')[12])
#     # returnData[i, 13] = float(readline.split('\t')[13])
#     # returnData[i, 14] = float(readline.split('\t\t')[14])
#     # returnData[i, 15] = float(readline.split('\t\t')[15])
#     i = i + 1
# readfile.close()
#
# # for i in range(7):
#
# # x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18])
# # x = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9])
# # names = ['No Kernel', 'E1', 'E1+I1', 'E1+I2+I3', 'E1+I1+I2+I3', 'E1+I1+I2+I3+Omnivariance', 'E1+I1+I2+I3+Anisotropy', 'E1+I1+I2+I3+Eigenentropy', 'E1+I1+I2+I3+Summation',
# #          'E1+I1+I2+I3+LocalCurvature', 'E1+I1+I2+I3+Linearity', 'E1+I1+I2+I3+Planarity', 'E1+I1+I2+I3+Sphericity', 'E1+I1+I2+I3+All Geometric Feature']
# names = ['FS1', 'FS2', 'FS3', 'FS4', 'FS5', 'FS6', 'FS7', 'FS8', 'FS9',
#          'FS10', 'FS11', 'FS12', 'FS13']
# x = range(len(names))
#
# # y1 = returnData[0, :]
# # l1 = plt.plot(x, y1, color='0.5', ls='--', marker='o', label='1SVM')
# y7 = returnData[1, :]
# l7 = plt.plot(x, y7, 'c--', marker='o', label='1  Random Forest')
# y2 = returnData[0, :]
# l2 = plt.plot(x, y2, 'r--', marker='o', label='2  Decision Tree')
# y3 = returnData[2, :]
# l3 = plt.plot(x, y3, 'g--', marker='o', label='3  K-Nearest Neighbor')
# y8 = returnData[6, :]
# l8 = plt.plot(x, y8, 'm--', marker='o', label='4  Adaptive Boosting')
# y6 = returnData[5, :]
# l6 = plt.plot(x, y6, 'k--', marker='o', label='5  Quadratic Discriminant Analysis')
# y4 = returnData[3, :]
# l4 = plt.plot(x, y4, 'y--', marker='o', label='6  Gaussian Naive Bayes')
# y5 = returnData[4, :]
# l5 = plt.plot(x, y5, 'b--', marker='o', label='7  Linear Discriminant Analysis')
# y9 = returnData[7, :]
# l9 = plt.plot(x, y9, color='tan', ls='--', marker='o', label='8  Multi-layer Perceptron')
#
# plt.xticks(x, names, rotation=45)
# x_major_locator=MultipleLocator(1)
# ax=plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
# plt.xlim(0, 12)
# plt.ylim(0.15, 1.05)
#
# # plt.title('The Classification Accuracy of Different Classifiers')
# # plt.xlabel('The Number of Mean Point Spacing')
#
# # plt.xlabel('The Different Combinations of Feature Vectors (Before Data)')
# plt.xlabel('The Different Combinations of Feature Vectors')
# plt.ylabel('Accuracy Value')
# num1 = -0.0018
# num2 = 1.01
# num3 = 3
# num4 = 0
# plt.legend(bbox_to_anchor=(num1, num2), loc=num3, borderaxespad=num4, ncol=2)
# plt.show()
# # fig.savefig('Figures/beforeDataFeatureVector.eps', dpi=600, format='eps')
# fig.savefig('Figures/newDataFeatureVector.eps', dpi=600, format='eps')


# # ---------------------------------------------------画柱状图---------------------------------------------------------------
# fig, ax = plt.subplots()
# path_r = 'ubdaDataGaussian/NewData/6ClassificationResult/GaussianKernel_addGeometric/'
# readfile = open(path_r+'OptimalFeature.txt', "r")
# readAllLine = readfile.readlines()
# lineNum = len(readAllLine)
# i = 0
# returnData = np.empty([lineNum, 13], dtype=float)
#
# for readline in readAllLine:
#     returnData[i, 0] = float(readline.split('\t')[0])
#     returnData[i, 1] = float(readline.split('\t')[1])
#     returnData[i, 2] = float(readline.split('\t')[2])
#     returnData[i, 3] = float(readline.split('\t')[3])
#     returnData[i, 4] = float(readline.split('\t')[4])
#     returnData[i, 5] = float(readline.split('\t')[5])
#     returnData[i, 6] = float(readline.split('\t')[6])
#     returnData[i, 7] = float(readline.split('\t')[7])
#     returnData[i, 8] = float(readline.split('\t')[8])
#     returnData[i, 9] = float(readline.split('\t')[9])
#     returnData[i, 10] = float(readline.split('\t')[10])
#     returnData[i, 11] = float(readline.split('\t')[11])
#     returnData[i, 12] = float(readline.split('\t')[12])
#     # returnData[i, 13] = float(readline.split('\t')[13])
#     # returnData[i, 14] = float(readline.split('\t\t')[14])
#     # returnData[i, 15] = float(readline.split('\t\t')[15])
#     i = i + 1
# readfile.close()
# name_list = ['FS1','FS2','FS3','FS4','FS5','FS6','FS7','FS8','FS9','FS10','FS11','FS12','FS13']
# num_list_0 = returnData[0, :]  # 2DecisionTree
# num_list_1 = returnData[1, :]  # 3RandomForests
# num_list_2 = returnData[2, :]  # 4KNearestNeighbor
# num_list_3 = returnData[3, :]  # 5GaussianNaiveBayes
# num_list_4 = returnData[4, :]  # 6LinearDiscriminantAnalysis
# num_list_5 = returnData[5, :]  # 7QuadraticDiscriminantAnalysis
# num_list_6 = returnData[6, :]  # 8AdaBoost
# num_list_7 = returnData[7, :]  # 9MLPClassifier
##-------------------------------1-4---------------------------------------------------------------
# plt.subplot(222)
# plt.bar(range(len(num_list_0)), num_list_0, label='Decision Tree', color='r')  # color='#03506f'
# x = range(len(name_list))
# plt.xticks(x, name_list, rotation=45, fontsize=7)
# x_major_locator=MultipleLocator(1)
# ax=plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
# plt.ylim(0, 1)
# num1 = 0
# num2 = 1.005
# num3 = 3
# num4 = 0
# plt.legend(bbox_to_anchor=(num1, num2), loc=num3, borderaxespad=num4, ncol=2, fontsize=9.2)
#
# plt.subplot(221)
# plt.bar(range(len(num_list_1)), num_list_1, label='Random Forest', color='c')
# x = range(len(name_list))
# plt.xticks(x, name_list, rotation=45, fontsize=7)
# x_major_locator=MultipleLocator(1)
# ax=plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
# plt.ylim(0, 1)
# num1 = 0
# num2 = 1.005
# num3 = 3
# num4 = 0
# plt.legend(bbox_to_anchor=(num1, num2), loc=num3, borderaxespad=num4, ncol=2, fontsize=9.2)
#
# plt.subplot(223)
# plt.bar(range(len(num_list_2)), num_list_2, label='K-Nearest Neighbor', color='g')
# x = range(len(name_list))
# plt.xticks(x, name_list, rotation=45, fontsize=7)
# x_major_locator=MultipleLocator(1)
# ax=plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
# plt.ylim(0, 1)
# num1 = 0
# num2 = 1.005
# num3 = 3
# num4 = 0
# plt.legend(bbox_to_anchor=(num1, num2), loc=num3, borderaxespad=num4, ncol=2, fontsize=9.2)
#
# plt.subplot(224)
# plt.bar(range(len(num_list_6)), num_list_6, label='Adaptive Boosting', color='m')
# x = range(len(name_list))
# plt.xticks(x, name_list, rotation=45, fontsize=7)
# plt.ylim(0, 1)
# num1 = 0
# num2 = 1.005
# num3 = 3
# num4 = 0
# plt.legend(bbox_to_anchor=(num1, num2), loc=num3, borderaxespad=num4, ncol=2, fontsize=9.2)
#
# plt.show()
# fig.savefig('Figures/newDataFeatureVector_bar1-4.eps', dpi=600, format='eps')


# #----------------------------------------5-8-------------------------------------------------------------
# plt.subplot(223)
# plt.bar(range(len(num_list_4)), num_list_4, label='Linear Discriminant Analysis', color='b')
# x = range(len(name_list))
# plt.xticks(x, name_list, rotation=45, fontsize=7)
# # x_major_locator=MultipleLocator(1)
# # ax=plt.gca()
# # ax.xaxis.set_major_locator(x_major_locator)
# plt.ylim(0, 1)
# num1 = 0
# num2 = 1.005
# num3 = 3
# num4 = 0
# plt.legend(bbox_to_anchor=(num1, num2), loc=num3, borderaxespad=num4, ncol=2, fontsize=9.2)
#
# plt.subplot(221)
# plt.bar(range(len(num_list_5)), num_list_5, label='Quadratic Discriminant Analysis', color='k')
# x = range(len(name_list))
# plt.xticks(x, name_list, rotation=45, fontsize=7)
# plt.ylim(0, 1)
# num1 = 0
# num2 = 1.005
# num3 = 3
# num4 = 0
# plt.legend(bbox_to_anchor=(num1, num2), loc=num3, borderaxespad=num4, ncol=2, fontsize=9.2)
#
# plt.subplot(222)
# plt.bar(range(len(num_list_3)), num_list_3, label='Gaussian Naive Bayes', color='y')
# x = range(len(name_list))
# plt.xticks(x, name_list, rotation=45, fontsize=7)
# x_major_locator=MultipleLocator(1)
# ax=plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
# plt.ylim(0, 1)
# num1 = 0
# num2 = 1.005
# num3 = 3
# num4 = 0
# plt.legend(bbox_to_anchor=(num1, num2), loc=num3, borderaxespad=num4, ncol=2, fontsize=9.2)
#
# plt.subplot(224)
# plt.bar(range(len(num_list_7)), num_list_7, label='Multi-layer Perceptron', color='tan', )
# x = range(len(name_list))
# plt.xticks(x, name_list, rotation=45, fontsize=7)
# plt.ylim(0, 1)
# num1 = 0
# num2 = 1.005
# num3 = 3
# num4 = 0
# plt.legend(bbox_to_anchor=(num1, num2), loc=num3, borderaxespad=num4, ncol=2, fontsize=9.2)
#
# plt.show()
# fig.savefig('Figures/newDataFeatureVector_bar5-8.eps', dpi=600, format='eps')











# #------------------------1-----------------------------#
# # 画3D球体
# # center and radius
# center = [0,0,0]
# radius_1 = 10
# radius_2 = 20
# radius_3 = 30
# radius_4 = 50
#
# # data
# u = np.linspace(0, 2 * np.pi, 100)
# v = np.linspace(0, np.pi, 100)
# x_1 = radius_1 * np.outer(np.cos(u), np.sin(v)) + center[0]
# y_1 = radius_1 * np.outer(np.sin(u), np.sin(v)) + center[1]
# z_1 = radius_1 * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.plot_wireframe(x_1, y_1, z_1, color='cornflowerblue', linewidth=0.5, rstride=10, cstride=15)
# # plot = [ax.plot_surface(x_1, y_1, z_1)]  #cornflowerblue  royalblue
#
#
# x_2 = radius_2 * np.outer(np.cos(u), np.sin(v)) + center[0]
# y_2 = radius_2 * np.outer(np.sin(u), np.sin(v)) + center[1]
# z_2 = radius_2 * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
# ax.plot_wireframe(x_2, y_2, z_2, color='mediumaquamarine', linewidth=0.5, rstride=10, cstride=15)  # mediumseagreen
#
# x_3 = radius_3 * np.outer(np.cos(u), np.sin(v)) + center[0]
# y_3 = radius_3 * np.outer(np.sin(u), np.sin(v)) + center[1]
# z_3 = radius_3 * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
# ax.plot_wireframe(x_3, y_3, z_3, color='powderblue', linewidth=0.5, rstride=10, cstride=15)
#
# x_4 = radius_4 * np.outer(np.cos(u), np.sin(v)) + center[0]
# y_4 = radius_4 * np.outer(np.sin(u), np.sin(v)) + center[1]
# z_4 = radius_4 * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
# ax.plot_wireframe(x_4, y_4, z_4, color='lightgrey', linewidth=0.5, rstride=10, cstride=15)
#
# ax.elev = 10
# ax.azim = -130
# plt.plot(0,0,0, 'o', color='r')
# # plt.figure(figsize=(100,100))
# plt.axis('off')
# plt.subplots_adjust(top=1,bottom=0,left=0,right=1,hspace=0,wspace=0)
# plt.show()


# image_path = 'F:/2PhD/4Submission/Figure/Multi-sphere.png'
# img = plt.imread(image_path)
# width = img.shape[0]
# height = img.shape[1]
# dpi = 2
# fig = plt.figure(figsize=(width*dpi, height*dpi), dpi=dpi)
# axes = fig.add_axes([0, 0, 1, 1])
# axes.set_axis_off()
# axes.imshow(img)
# fig.savefig('Figures/Multi-sphere_2.png')


# # 画--------------------------color bar-----------------------------
# import numpy as np
# import matplotlib.pyplot as plt
#
# xi = np.array([30., 40, 320.0])
# yi = np.array([30., 40, 320.0])
# zi = np.array([[30., 40, 320.0],
#        [30., 40, 320.0],
#        [30., 40, 320.0]])
#
# # plt.contour(xi, yi, zi, 15, linewidths=0.5, colors='k')
# plt.contourf(xi, yi, zi, 15, cmap=plt.cm.jet)
# plt.colorbar()
# plt.show()
# # fig = plt.figure(figsize=(width*dpi, height*dpi), dpi=dpi)
# # save_path = 'F:/2PhD/4Submission/Figure/newData.png'
# plt.savefig('Figures/NewData.eps',dpi=600,format='eps')


# import numpy as np
# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots()
# x1 = np.random.uniform(-10, 10, size=20)
# x2 = np.random.uniform(-10, 10, size=20)
# # print(x1)
# # print(x2)
# number = []
# x11 = []
# x12 = []
# for i in range(20):
#     number.append(i + 1)
#     x11.append(i + 1)
#     x12.append(i + 1)
# plt.figure(1)
# # you can specify the marker size two ways directly:
# plt.plot(number, x1, 'bo', markersize=20, label='a')  # blue circle with size 20
# plt.plot(number, x2, 'ro', ms=10, label='b')  # ms is just an alias for markersize
#
# lgnd = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0, numpoints=1, fontsize=10)
# lgnd.legendHandles[0]._legmarker.set_markersize(16)
# lgnd.legendHandles[1]._legmarker.set_markersize(10)
#
# plt.show()
#
# fig.savefig('Figures/scatter.eps', dpi=600, format='eps')




# x = ['15','25','35','45','55']
#
# y1 = [2.70987, 3.224618, 2.47364, 1.88438, 1.38864926]
# y2 = [5.67344, 7.730714, 5.99738, 4.72198, 3.53094]
# y3 = [3.665047, 2.947062, 2.15406, 1.49824, 1.23967666]
# y4 = [7.809747, 9.04552439, 7.21065, 5.60793, 4.26721]
# y5 = [3.59208, 2.97782, 2.22515, 1.78572, 1.39946]
# l1 = plt.plot(x, y1, 'b--', marker='o', label='SMAPP-NDC(circle=1)')
# l2 = plt.plot(x, y2, 'k--', marker='o', label='SMAPP-NDC(circle=2)')
# l3 = plt.plot(x, y3, 'r--', marker='o', label='SMAPP-MSC')
# l5 = plt.plot(x, y5, 'c--', marker='o', label='MMAPP-MSC')
# l4 = plt.plot(x, y4, 'y--', marker='o', label='MMAPP-NDC')
# plt.ylim(0.5, 10)
# plt.xlabel('(a) Communication Ranges(m)')
# plt.ylabel('Trajectory Length (x1000m)')


# plt.subplot(222)
# # y1 = [2709.87, 3224.618, 2473.64, 1884.38, 1388.64926]
# # y2 = [5673.44, 7730.714, 5997.38, 4721.98, 3530.94]
# # y3 = [3665.047, 2947.062, 2154.06, 1498.24, 1239.67666]
# # y4 = [2397.366667, 3093.084, 2403.54, 1869.31, 1422.41203]
# # y5 = [1792.26, 1538.39, 901.88245, 775.74697, 612.76331]
# y1 = [2.70987, 3.224618, 2.47364, 1.88438, 1.38864926]
# y2 = [5.67344, 7.730714, 5.99738, 4.72198, 3.53094]
# y3 = [3.665047, 2.947062, 2.15406, 1.49824, 1.23967666]
# y4 = [2.397366667, 3.093084, 2.40354, 1.86931, 1.42241203]
# y5 = [1.79226, 1.53839, 0.90188245, 0.77574697, 0.61276331]
# l1 = plt.plot(x, y1, 'b--', marker='o', label='SMAPP-NDC(circle=1)')
# l2 = plt.plot(x, y2, 'k--', marker='o', label='SMAPP-NDC(circle=2)')
# l3 = plt.plot(x, y3, 'r--', marker='o', label='SMAPP-MSC')
# l4 = plt.plot(x, y4, 'y--', marker='o', label='MMAPP-NDC')
# l5 = plt.plot(x, y5, 'c--', marker='o', label='MMAPP-MSC')
# plt.ylim(0.5, 10)
# plt.xlabel('Communication Ranges(m)')
# plt.ylabel('Localization Time (x1000s)')
# # plt.subtitle('(a)')
#
#
# plt.subplot(223)
# y1 = [32.66666668, 53.895, 56.25, 54.725, 52.55]
# y2 = [55.9, 88.12, 91.675, 92, 93.25]
# y3 = [60.78333333, 61.065, 58.325, 60.9, 59.775]
# y4 = [43.21666668, 71.36, 76.375, 74.9, 73.475]
# y5 = [60.78333333, 61.065, 58.325, 60.9, 59.775]
# l1 = plt.plot(x, y1, 'b--', marker='o', label='SMAPP-NDC(circle=1)')
# l2 = plt.plot(x, y2, 'k--', marker='o', label='SMAPP-NDC(circle=2)')
# l3 = plt.plot(x, y3, 'r--', lw=2,  marker='o', markersize=7, label='SMAPP-MSC')
# l4 = plt.plot(x, y4, 'y--', marker='o', label='MMAPP-NDC')
# l5 = plt.plot(x, y5, 'c--', marker='o', label='MMAPP-MSC')
# plt.ylim(30, 100)
# plt.xlabel('Communication Ranges(m)')
# plt.ylabel('Accurate Localization Ratio (%)')
#
#
# plt.subplot(224)
# # y1 = [0.000114, 0.000156128, 0.000218815, 0.000286725, 0.000356755]
# # y2 = [0.0000941, 0.000111973, 0.000149614, 0.000195794, 0.000267362]
# # y3 = [0.00016, 0.000200038, 0.000264534, 0.000361518, 0.000478711]
# # y4 = [0.000145, 0.00021703, 0.000290755, 0.000383753, 0.000499188]
# # y5 = [0.000325, 0.000437235, 0.000610748, 0.000630421, 0.000964726]
# y1 = [0.114, 0.156128, 0.218815, 0.286725, 0.356755]
# y2 = [0.0941, 0.111973, 0.149614, 0.195794, 0.267362]
# y3 = [0.16, 0.200038, 0.264534, 0.361518, 0.478711]
# y4 = [0.145, 0.21703, 0.290755, 0.383753, 0.499188]
# y5 = [0.325, 0.437235, 0.610748, 0.630421, 0.964726]
# l1 = plt.plot(x, y1, 'b--', marker='o', label='SMAPP-NDC(circle=1)')
# l2 = plt.plot(x, y2, 'k--', marker='o', label='SMAPP-NDC(circle=2)')
# l3 = plt.plot(x, y3, 'r--', marker='o', label='SMAPP-MSC')
# l4 = plt.plot(x, y4, 'y--', marker='o', label='MMAPP-NDC')
# l5 = plt.plot(x, y5, 'c--', marker='o', label='MMAPP-MSC')
# # plt.ylim(10**-4, 10**-3)
# plt.xlabel('Communication Ranges(m)')
# plt.ylabel('Localization Efficiency (x1000)')
#
#
# plt.show()




# fig, ax = plt.subplots(2, 2)
# x = ['10','20','30','40','50','60','70','80','90','100','110','120','130','140','150']
#
# # plt.subplot(221)
# y1 = [2.70987, 3.224618, 2.47364, 1.88438, 1.38864926]
# y2 = [5.67344, 7.730714, 5.99738, 4.72198, 3.53094]
# # y3 = [3.665047, 2.947062, 2.15406, 1.49824, 1.23967666]
# # y4 = [7.809747, 9.04552439, 7.21065, 5.60793, 4.26721]
# # y5 = [3.59208, 2.97782, 2.22515, 1.78572, 1.39946]
# ax[0,0].plot(x, y1, 'b--', marker='o', label='SMAPP-NDC(circle=1)')
# ax[0,0].plot(x, y2, 'k--', marker='o', label='SMAPP-NDC(circle=2)')
# # ax[0,0].plot(x, y3, 'r--', marker='o', label='SMAPP-MSC')
# # ax[0,0].plot(x, y5, 'c--', marker='o', label='MMAPP-MSC')
# # ax[0,0].plot(x, y4, 'y--', marker='o', label='MMAPP-NDC')
# ax[0,0].set_ylim(0.5, 10)
# ax[0,0].set_xlabel('(a) Communication Ranges(m)')
# ax[0,0].set_ylabel('Trajectory Length (x1000m)')
# ax[0,0].set_title('(a)')
#
#
# #
# # # plt.subplot(222)
# # y1 = [2.70987, 3.224618, 2.47364, 1.88438, 1.38864926]
# # y2 = [5.67344, 7.730714, 5.99738, 4.72198, 3.53094]
# # y3 = [3.665047, 2.947062, 2.15406, 1.49824, 1.23967666]
# # y4 = [2.397366667, 3.093084, 2.40354, 1.86931, 1.42241203]
# # y5 = [1.79226, 1.53839, 0.90188245, 0.77574697, 0.61276331]
# # ax[0,1].plot(x, y1, 'b--', marker='o', label='SMAPP-NDC(circle=1)')
# # ax[0,1].plot(x, y2, 'k--', marker='o', label='SMAPP-NDC(circle=2)')
# # ax[0,1].plot(x, y3, 'r--', marker='o', label='SMAPP-MSC')
# # ax[0,1].plot(x, y4, 'y--', marker='o', label='MMAPP-NDC')
# # ax[0,1].plot(x, y5, 'c--', marker='o', label='MMAPP-MSC')
# # ax[0,1].set_ylim(0.5, 10)
# # ax[0,1].set_xlabel('Communication Ranges(m)')
# # ax[0,1].set_ylabel('Localization Time (x1000s)')
# # ax[0,1].set_title('(b)')
# #
# # # plt.subplot(223)
# # y1 = [32.66666668, 53.895, 56.25, 54.725, 52.55]
# # y2 = [55.9, 88.12, 91.675, 92, 93.25]
# # y3 = [60.78333333, 61.065, 58.325, 60.9, 59.775]
# # y4 = [43.21666668, 71.36, 76.375, 74.9, 73.475]
# # y5 = [60.78333333, 61.065, 58.325, 60.9, 59.775]
# # ax[1,0].plot(x, y1, 'b--', marker='o', label='SMAPP-NDC(circle=1)')
# # ax[1,0].plot(x, y2, 'k--', marker='o', label='SMAPP-NDC(circle=2)')
# # ax[1,0].plot(x, y3, 'r--', lw=2,  marker='o', markersize=7, label='SMAPP-MSC')
# # ax[1,0].plot(x, y4, 'y--', marker='o', label='MMAPP-NDC')
# # ax[1,0].plot(x, y5, 'c--', marker='o', label='MMAPP-MSC')
# # ax[1,0].set_ylim(30, 100)
# # ax[1,0].set_xlabel('Communication Ranges(m)')
# # ax[1,0].set_ylabel('Accurate Localization Ratio (%)')
# # ax[1,0].set_title('(c)')
# #
# # # plt.subplot(224)
# # y1 = [0.114, 0.156128, 0.218815, 0.286725, 0.356755]
# # y2 = [0.0941, 0.111973, 0.149614, 0.195794, 0.267362]
# # y3 = [0.16, 0.200038, 0.264534, 0.361518, 0.478711]
# # y4 = [0.145, 0.21703, 0.290755, 0.383753, 0.499188]
# # y5 = [0.325, 0.437235, 0.610748, 0.630421, 0.964726]
# # ax[1,1].plot(x, y1, 'b--', marker='o', label='SMAPP-NDC(circle=1)')
# # ax[1,1].plot(x, y2, 'k--', marker='o', label='SMAPP-NDC(circle=2)')
# # ax[1,1].plot(x, y3, 'r--', marker='o', label='SMAPP-MSC')
# # ax[1,1].plot(x, y4, 'y--', marker='o', label='MMAPP-NDC')
# # ax[1,1].plot(x, y5, 'c--', marker='o', label='MMAPP-MSC')
# # ax[1,1].set_xlabel('Communication Ranges(m)')
# # ax[1,1].set_ylabel('Localization Efficiency (x1000)')
# # ax[1,1].set_title('(d)')
#
# plt.show()






# plot parameter
x = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
y1 = [94.4,94.5,94.6,94.7,94.7,94.8,94.8,94.9,95.1,95.0,94.8,94.9,95.1,95.0,94.9]
y2 = [137,174,191,234,255,277,311,349,362,383,425,469,515,609,921]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y1, '--', marker='o', label='Classification Accuracy (%)')

ax2 = ax.twinx()
ax2.plot(x, y2, '--r', marker='o', label='Time Cost (s)')

ax.set_xlabel("$\delta$ value")
ax.set_ylabel(r"Classification Accuracy (%)")
ax2.set_ylabel(r"Time Cost (s)")
fig.legend(loc=1, bbox_to_anchor=(0.51,1), bbox_transform=ax.transAxes)

x_major_locator=MultipleLocator(10)
ax.xaxis.set_major_locator(x_major_locator)
plt.xlim(5, 155)
plt.show()



#
# import seaborn as sn
# import pandas as pd
# import matplotlib.pyplot as plt
# a = 10
# array = [[a,1,1,0,2,0],
#          [3,9,6,0,1,0],
#          [0,0,16,2,0,0],
#          [0,0,0,13,0,0],
#          [0,0,0,0,15,0],
#          [0,0,1,0,0,15]]
#
# df_cm = pd.DataFrame(array, range(6), range(6))
# # plt.figure(figsize=(10,7))
# sn.set(font_scale=1.4) # for label size
# ax = sn.heatmap(df_cm, annot=True, annot_kws={"size": 16}, cmap='Blues')  # font size
# ax.yaxis.set_ticklabels(['Road','House','Fence','Tree','Grass','PowerLine'], rotation=0)
# ax.xaxis.set_ticklabels(['Road','House','Fence','Tree','Grass','PowerLine'], rotation=45)
# ax.set_xlabel('Predicted label', labelpad=-15)
# ax.set_ylabel('True label', labelpad=-25)
# plt.show()


