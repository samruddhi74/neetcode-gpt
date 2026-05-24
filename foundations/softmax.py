import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        maxi = max(z)
        s = np.sum(np.exp(z-maxi))
        y = np.exp(z-maxi)/s
        return np.round(y,4)
