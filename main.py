# Define tu función
def my_function_vs(req, res):
  print("Hola mundo desde GitHub Actions V2")

  
# Exporta la función como el punto de entrada
exports = {
  "my_function_vs": my_function_vs
}