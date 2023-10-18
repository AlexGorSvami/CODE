def first_non_repeating_letter(string):
   stringCopy = "".join([x.lower() for x in string])
   for s in stringCopy:
     if stringCopy.count(s) == 1:
       if s.isalpha():
         if s in string: return s
         if s.upper() in string: return s.upper()
       else:
         return s
   return ""

def first_non_repeating_letter1(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
            
    return ""
