from scipy import linalg
import numpy as np


class Event:
    def __init__(self, n_features=10, coefficients=None, tail_strength=0.1,
                 effective_rank=None, bias=0.0, noise_level=None):
        self.n_features = n_features
        self.noise_level = noise_level
        self.effective_rank = effective_rank

        if coefficients is None:
            self.coefficients = 10 * np.random.randn(n_features)
        else:
            self.coefficients = coefficients

        v, _ = linalg.qr(np.random.randn(n_features, n_features), mode='economic')
        self._v = v

        # Index of the singular values
        singular_ind = np.arange(n_features, dtype=np.float64)

        if self.effective_rank is None:
            tail_strength = 1
            self.effective_rank = n_features
            singular_ind = 10 * singular_ind

        # Build the singular profile by assembling signal and noise components
        low_rank = ((1 - tail_strength) *
                    np.exp(-1.0 * (singular_ind / self.effective_rank) ** 2))
        tail = tail_strength * np.exp(-0.1 * singular_ind / self.effective_rank)
        self._s = np.identity(n_features) * (low_rank + tail)

    def sample(self, n_samples=100):
        u0 = np.random.randn(max(n_samples, self.n_features), self.n_features)
        u, _ = linalg.qr(u0, mode='economic')
        X = np.dot(np.dot(u, self._s), self._v.T)
        X = X[:n_samples, :]
        y = np.dot(X, self.coefficients)

        if self.noise_level is not None:
            coeffs_norm = linalg.norm(self.coefficients)
            y += self.noise_level / 100 * coeffs_norm * np.random.randn(len(y))

        return X, y
