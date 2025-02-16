def is_positive_integer(value):
    """Check if the value is a positive integer."""
    try:
        ivalue = int(value)
        return ivalue > 0
    except ValueError:
        return False

def is_valid_matrix_entry(value):
    """Check if the value is a valid number (integer or float)."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def validate_matrix_size(size: int) -> bool:
    """
    行列のサイズが有効かどうかを検証する
    
    Args:
        size (int): 検証する行列のサイズ
        
    Returns:
        bool: サイズが有効な場合True、そうでない場合False
    """
    return isinstance(size, int) and 2 <= size <= 10

def validate_matrix_values(matrix: list) -> bool:
    """
    行列の値が有効かどうかを検証する
    
    Args:
        matrix (list): 検証する行列（2次元リスト）
        
    Returns:
        bool: 値が有効な場合True、そうでない場合False
    """
    if not matrix or not isinstance(matrix, list):
        return False
        
    try:
        rows = len(matrix)
        cols = len(matrix[0])
        
        # 行列が正方形であることを確認
        if rows != cols:
            return False
            
        # すべての要素が数値であることを確認
        return all(
            isinstance(val, (int, float)) 
            for row in matrix 
            for val in row
        )
    except (TypeError, AttributeError):
        return False