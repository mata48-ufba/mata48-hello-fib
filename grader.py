
import os

os.system("make clean")
os.system("make")

inputs = [0, 1, 19]
outputs = [0, 1, 4181]

success = True
for i in range(len(inputs)):
  try:
    out_str = os.popen("./a.out %d" % (inputs[i])).read().strip()
    exp_str = "fib(%d) = %d" % (inputs[i], outputs[i])
    if exp_str not in out_str:
      print("Expected '%s' but got '%s'" % (exp_str, out_str))
      success = False
  except:
    print("Failed to test input:", inputs[i])
    raise

if success:
  print("All tests passed.")