from textx import metamodel_from_file

# validate metamodel
metamodel = metamodel_from_file('drone.tx')

print ('Metamodel is valid')

# validate model based on metamodel
model = metamodel.model_from_file('example.dr')

print("Model is valid")
