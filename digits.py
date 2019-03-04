
digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']

translations = {}
i = len(digits)
for i in range(len(digits)):
    translations[digits[i]] = { 'french': fr[i], 'english': en[i]}
print(translations)




# translations =
# {
#   '1': {'french': 'un', 'english': 'one'},
#   '2': {'french': 'deux', 'english': 'two'},
#   '3': {'french': 'trois', 'english': 'three'},
#   ...
#   '9': {'french': 'neuf', 'english': 'nine'}
# }
