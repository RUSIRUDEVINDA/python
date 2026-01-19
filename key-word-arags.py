def my_form(*values, **params):
  print(values)
  if "name" not in params:
    print("Error")
  else:
    print("Hello! ", params["name"])

my_form(1,78, height=199, city="colombo")
my_form(name="rusiru", height=188, city="piliyandala")

