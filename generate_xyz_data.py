import numpy as np
from matplotlib.mlab import  bivariate_normal

def generate_xyz_data(delta=0.05, minRange=-3.0, maxRange=3.0, nDistributions=0, variances=[], means=[], signs=[], ranges=()):
    x = y = np.arange(minRange, maxRange, delta)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros(X.shape)
    
    for n in range(nDistributions):
        sigma = variances[n]
        sigmax = sigma[0]
        sigmay = sigma[1]
        mu = means[n]
        mux = mu[0]
        muy = mu[1]
        newZ = signs[n] * bivariate_normal(X, Y, sigmax, sigmay, mux, muy)
        Z = Z + newZ
    
    X = X * ranges[0]
    Y = Y * ranges[1]
    Z = Z * ranges[2]
    
    return X, Y, Z