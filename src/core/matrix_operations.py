import numpy as np

class MatrixOperations:
    @staticmethod
    def inverse(matrix):
        """Calculate the inverse of a matrix."""
        if not MatrixOperations.is_square(matrix):
            raise ValueError("Matrix must be square.")
        return np.linalg.inv(matrix)

    @staticmethod
    def diagonalize(matrix):
        """Diagonalize a matrix."""
        if not MatrixOperations.is_square(matrix):
            raise ValueError("Matrix must be square.")
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        return eigenvectors, np.diag(eigenvalues)

    @staticmethod
    def lu_decomposition(matrix):
        """Perform LU decomposition of a matrix."""
        if not MatrixOperations.is_square(matrix):
            raise ValueError("Matrix must be square.")
        from scipy.linalg import lu
        P, L, U = lu(matrix)
        return L, U

    @staticmethod
    def qr_decomposition(matrix):
        """Perform QR decomposition of a matrix."""
        Q, R = np.linalg.qr(matrix)
        return Q, R

    @staticmethod
    def svd(matrix):
        """Perform Singular Value Decomposition (SVD) of a matrix."""
        U, s, Vh = np.linalg.svd(matrix)
        return U, s, Vh

    @staticmethod
    def is_square(matrix):
        """Check if a matrix is square."""
        return matrix.shape[0] == matrix.shape[1]