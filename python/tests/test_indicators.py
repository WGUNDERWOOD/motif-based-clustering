from motifcluster import indicators as mcin

import numpy as np
from scipy import sparse

def test_indicators():

  G_dense = np.array([0, 2, 0, 3, 0, 4, 0, 0, 0]).reshape((3, 3))
  G_sparse = sparse.csr_matrix(G_dense)

  G  = np.array([0, 2, 0, 3, 0, 4, 0, 0, 0]).reshape((3, 3))
  J  = np.array([0, 1, 0, 1, 0, 1, 0, 0, 0]).reshape((3, 3))
  Gs = np.array([0, 0, 0, 0, 0, 4, 0, 0, 0]).reshape((3, 3))
  Js = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0]).reshape((3, 3))
  Gd = np.array([0, 5, 0, 5, 0, 0, 0, 0, 0]).reshape((3, 3))
  Jd = np.array([0, 1, 0, 1, 0, 0, 0, 0, 0]).reshape((3, 3))
  J0 = np.array([0, 0, 1, 0, 0, 0, 1, 0, 0]).reshape((3, 3))
  Jn = np.array([0, 1, 1, 1, 0, 1, 1, 1, 0]).reshape((3, 3))
  Id = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1]).reshape((3, 3))
  Je = np.array([1, 1, 0, 1, 1, 1, 0, 1, 1]).reshape((3, 3))
  Gp = np.array([0, 6, 0, 6, 0, 0, 0, 0, 0]).reshape((3, 3))

  assert np.allclose(mcin._build_G(G_dense).toarray(), G)
  assert np.allclose(mcin._build_G(G_sparse).toarray(), G)

  assert np.allclose(mcin._build_J(G_dense).toarray(), J)
  assert np.allclose(mcin._build_J(G_sparse).toarray(), J)

  assert np.allclose(mcin._build_Gs(G_dense).toarray(), Gs)
  assert np.allclose(mcin._build_Gs(G_sparse).toarray(), Gs)

  assert np.allclose(mcin._build_Js(G_dense).toarray(), Js)
  assert np.allclose(mcin._build_Js(G_sparse).toarray(), Js)

  assert np.allclose(mcin._build_Gd(G_dense).toarray(), Gd)
  assert np.allclose(mcin._build_Gd(G_sparse).toarray(), Gd)

  assert np.allclose(mcin._build_Jd(G_dense).toarray(), Jd)
  assert np.allclose(mcin._build_Jd(G_sparse).toarray(), Jd)

  assert np.allclose(mcin._build_J0(G_dense).toarray(), J0)
  assert np.allclose(mcin._build_J0(G_sparse).toarray(), J0)

  assert np.allclose(mcin._build_Jn(G_dense).toarray(), Jn)
  assert np.allclose(mcin._build_Jn(G_sparse).toarray(), Jn)

  assert np.allclose(mcin._build_Id(G_dense).toarray(), Id)
  assert np.allclose(mcin._build_Id(G_sparse).toarray(), Id)

  assert np.allclose(mcin._build_Je(G_dense).toarray(), Je)
  assert np.allclose(mcin._build_Je(G_sparse).toarray(), Je)

  assert np.allclose(mcin._build_Gp(G_dense).toarray(), Gp)
  assert np.allclose(mcin._build_Gp(G_sparse).toarray(), Gp)
