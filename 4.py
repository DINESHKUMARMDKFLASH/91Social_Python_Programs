data_input = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
          {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

print("Original dictionary : ", data_input, "\n")
print("Sorted Dictionary : ", sorted(data_input, key=lambda sortby: sortby['color']))
