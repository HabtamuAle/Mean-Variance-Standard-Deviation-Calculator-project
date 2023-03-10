import numpy as np


def calculate(list):
  arr = np.array(list)
  if arr.shape != (9, ):
    raise ValueError('List must contain nine numbers.')

  mat = arr.reshape(3, 3)

  calculations = {
    'mean': [mat.mean(axis=0).tolist(),
             mat.mean(axis=1).tolist(),
             mat.mean()],
    'variance':
    [mat.var(axis=0).tolist(),
     mat.var(axis=1).tolist(),
     mat.var()],
    'standard deviation':
    [mat.std(axis=0).tolist(),
     mat.std(axis=1).tolist(),
     mat.std()],
    'max': [mat.max(axis=0).tolist(),
            mat.max(axis=1).tolist(),
            mat.max()],
    'min': [mat.min(axis=0).tolist(),
            mat.min(axis=1).tolist(),
            mat.min()],
    'sum': [mat.sum(axis=0).tolist(),
            mat.sum(axis=1).tolist(),
            mat.sum()],
  }
  return calculations
