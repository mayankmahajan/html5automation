import glob

test_file_strings = glob.glob('../Site_Interaction/test_*.py')
module_strings = [str.split('/')[1] + "." + str.split('/')[2].split('.')[0] for str in test_file_strings]
[__import__(str) for str in module_strings]