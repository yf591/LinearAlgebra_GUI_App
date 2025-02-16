import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import scipy.linalg

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Linear Algebra GUI")
        self.master.geometry("800x800")
        
        # 行列のサイズ設定用の変数
        self.matrix_size = tk.IntVar(value=3)
        self.matrix_entries = []
        
        self.create_widgets()

    def create_widgets(self):
        # メインフレームの作成
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 行列サイズ選択
        size_frame = ttk.LabelFrame(main_frame, text="行列サイズ", padding="5")
        size_frame.grid(row=0, column=0, columnspan=2, pady=5, sticky=tk.W)
        
        sizes = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i, size in enumerate(sizes):
            ttk.Radiobutton(size_frame, text=f"{size}x{size}", 
                          variable=self.matrix_size, value=size,
                          command=self.update_matrix_input).grid(row=i//5, column=i%5, padx=5)

        # 行列入力エリア
        matrix_frame = ttk.LabelFrame(main_frame, text="行列入力", padding="5")
        matrix_frame.grid(row=1, column=0, pady=5, sticky=tk.W)
        self.setup_matrix_input(matrix_frame)

        # 操作ボタン
        operations_frame = ttk.LabelFrame(main_frame, text="行列演算", padding="5")
        operations_frame.grid(row=1, column=1, padx=10, pady=5, sticky=tk.N)
        
        operations = [
            ("行列式", self.compute_determinant),
            ("逆行列", self.compute_inverse),
            ("対角化", self.compute_diagonalization),
            ("LU分解", self.compute_lu),
            ("QR分解", self.compute_qr),
            ("特異値分解", self.compute_svd)
        ]
        
        for i, (text, command) in enumerate(operations):
            ttk.Button(operations_frame, text=text, command=command).grid(
                row=i, column=0, pady=2, padx=5, sticky=tk.W+tk.E)

        # 結果表示エリア
        result_frame = ttk.LabelFrame(main_frame, text="計算結果", padding="5")
        result_frame.grid(row=2, column=0, columnspan=2, pady=5, sticky=tk.W+tk.E)
        
        self.result_text = tk.Text(result_frame, height=30, width=100)
        self.result_text.grid(row=0, column=0, padx=5, pady=5)

    def setup_matrix_input(self, frame):
        size = self.matrix_size.get()
        self.matrix_entries = []
        
        for i in range(size):
            row_entries = []
            for j in range(size):
                entry = ttk.Entry(frame, width=8)
                entry.grid(row=i, column=j, padx=2, pady=2)
                entry.insert(0, "0")
                row_entries.append(entry)
            self.matrix_entries.append(row_entries)

    def update_matrix_input(self):
        for widget in self.matrix_entries:
            for entry in widget:
                entry.destroy()
        self.matrix_entries.clear()
        
        matrix_frame = self.master.winfo_children()[0].winfo_children()[1]
        self.setup_matrix_input(matrix_frame)

    def get_matrix(self):
        size = self.matrix_size.get()
        matrix = np.zeros((size, size))
        
        for i in range(size):
            for j in range(size):
                try:
                    matrix[i][j] = float(self.matrix_entries[i][j].get())
                except ValueError:
                    messagebox.showerror("エラー", "有効な数値を入力してください")
                    return None
        return matrix

    def display_result(self, result):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    def compute_inverse(self):
        matrix = self.get_matrix()
        if matrix is None:
            return
        
        try:
            inverse = np.linalg.inv(matrix)
            explanation = """
逆行列とは:
- 元の行列に掛けると単位行列になる行列です
- 連立方程式の解法や行列方程式の解法に使用されます
- 行列式が0でない場合のみ存在します
"""
            self.display_result(f"逆行列:\n{inverse}\n\n{explanation}")
        except np.linalg.LinAlgError:
            messagebox.showerror("エラー", "この行列は逆行列を持ちません")

    def compute_diagonalization(self):
        matrix = self.get_matrix()
        if matrix is None:
            return
        
        try:
            eigenvalues, eigenvectors = np.linalg.eig(matrix)
            explanation = """
対角化とは:
- 行列を P⁻¹AP = D の形に変換する操作です
- D は対角行列（固有値を対角に並べた行列）
- P は固有ベクトルを列に並べた行列

固有値とは:
- Ax = λx を満たすスカラー値 λ
- 行列の特性を表す重要な値

固有ベクトルとは:
- 行列による変換で方向が変化しないベクトル
- 各固有値に対応するベクトル

応用例:
- 連立微分方程式の解法
- 主成分分析（PCA）
- 振動解析
- 量子力学の計算
"""
            result = f"固有値:\n{eigenvalues}\n\n固有ベクトル:\n{eigenvectors}\n\n{explanation}"
            self.display_result(result)
        except np.linalg.LinAlgError:
            messagebox.showerror("エラー", "対角化に失敗しました")

    def compute_lu(self):
        matrix = self.get_matrix()
        if matrix is None:
            return
        
        try:
            P, L, U = scipy.linalg.lu(matrix)
            explanation = """
LU分解とは:
- 行列を下三角行列(L)と上三角行列(U)の積に分解
- P は行の入れ替えを表す置換行列
- A = PLU の形式で表現

L（下三角行列）:
- 対角成分より下のみに非ゼロ要素を持つ
- 対角成分は1

U（上三角行列）:
- 対角成分より上のみに非ゼロ要素を持つ

応用例:
- 連立方程式の効率的な解法
- 行列式の計算
- 数値シミュレーション
- 回路解析
"""
            result = f"P行列:\n{P}\n\nL行列:\n{L}\n\nU行列:\n{U}\n\n{explanation}"
            self.display_result(result)
        except:
            messagebox.showerror("エラー", "LU分解に失敗しました")

    def compute_qr(self):
        matrix = self.get_matrix()
        if matrix is None:
            return
        
        try:
            Q, R = np.linalg.qr(matrix)
            explanation = """
QR分解とは:
- 行列を直交行列(Q)と上三角行列(R)の積に分解
- A = QR の形式で表現

Q（直交行列）:
- 列ベクトルが互いに直交
- Q^T Q = I（単位行列）
- 長さが1に正規化された基底ベクトル

R（上三角行列）:
- 対角成分より上のみに非ゼロ要素を持つ

応用例:
- 最小二乗法による曲線フィッティング
- 固有値計算のQR法
- 信号処理
- データ圧縮
"""
            result = f"Q行列:\n{Q}\n\nR行列:\n{R}\n\n{explanation}"
            self.display_result(result)
        except:
            messagebox.showerror("エラー", "QR分解に失敗しました")

    def compute_svd(self):
        matrix = self.get_matrix()
        if matrix is None:
            return
        
        try:
            U, S, Vh = np.linalg.svd(matrix)
            explanation = """
特異値分解（SVD）の解説:
特異値分解は行列を U・Σ・V^H の積に分解する手法です。

U行列（左特異ベクトル）:
- 入力空間の正規直交基底を表します
- 列ベクトルは互いに直交し、長さが1です

特異値:
- 行列の「強さ」を表す非負の実数です
- 大きい順に並んでおり、行列の重要な特徴を示します

V^H行列（右特異ベクトルの共役転置）:
- 出力空間の正規直交基底を表します
- 行ベクトルは互いに直交し、長さが1です

応用例:
- データ圧縮
- ノイズ除去
- 画像処理
- 推薦システム
"""
            result = f"U行列:\n{U}\n\n特異値:\n{S}\n\nV^H行列:\n{Vh}\n\n{explanation}"
            self.display_result(result)
        except:
            messagebox.showerror("エラー", "特異値分解に失敗しました")

    def compute_determinant(self):
        matrix = self.get_matrix()
        if matrix is None:
            return
        
        try:
            det = np.linalg.det(matrix)
            explanation = """
行列式とは、正方行列から計算される特別な数値です。
- 行列が可逆かどうかの判定（行列式≠0なら可逆）
- 線形変換による面積・体積の変化率
- 連立方程式の解の存在判定
などに使用されます。
"""
            self.display_result(f"行列式の値: {det}\n\n{explanation}")
        except:
            messagebox.showerror("エラー", "行列式の計算に失敗しました")