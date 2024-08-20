from flask import Flask, render_template, request
import numpy as np
from MatrixCalculator import matrix_addition, matrix_subtraction, matrix_multiplication, matrix_determinant, matrix_inverse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error_message = None
    show_matrix2 = True  # Control whether to show the second matrix input

    if request.method == 'POST':
        try:
            matrix1 = request.form.get('matrix1')
            matrix2 = request.form.get('matrix2')
            operation = request.form.get('operation')

            A = np.array(eval(matrix1))
            B = np.array(eval(matrix2)) if matrix2 else None

            if operation == 'addition' and B is not None:
                if A.shape == B.shape:
                    result_matrix = matrix_addition(A, B).tolist()
                    result = f"Result: {result_matrix}"
                else:
                    error_message = "Matrices must have the same dimensions for addition."
            elif operation == 'subtraction' and B is not None:
                if A.shape == B.shape:
                    result_matrix = matrix_subtraction(A, B).tolist()
                    result = f"Result: {result_matrix}"
                else:
                    error_message = "Matrices must have the same dimensions for subtraction."
            elif operation == 'multiplication' and B is not None:
                try:
                    result_matrix = matrix_multiplication(A, B).tolist()
                    result = f"Result: {result_matrix}"
                except ValueError as e:
                    error_message = str(e)
            elif operation == 'determinant':
                if A.shape[0] == A.shape[1]:
                    result_value = matrix_determinant(A)
                    result = f"Determinant: {result_value:.2f}"
                    show_matrix2 = False
                else:
                    error_message = "Matrix must be square to compute the determinant."
            elif operation == 'inverse':
                if A.shape[0] == A.shape[1]:
                    result_matrix = matrix_inverse(A).tolist()
                    result = f"Inverse: {result_matrix}"
                    show_matrix2 = False
                else:
                    error_message = "Matrix must be square to compute the inverse."
            else:
                error_message = "Invalid operation or missing second matrix."

        except Exception as e:
            error_message = f"An error occurred: {e}"

    return render_template('index.html', result=result, error_message=error_message, show_matrix2=show_matrix2)

if __name__ == '__main__':
    app.run(debug=True)
