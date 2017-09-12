## use find() and string slicing to extract the number, then
## convert the value to a float type.
str = "X-DSPAM-Confidence:    0.8475";

locate = str.find(':')
cut = str[locate+1:]
value = float(cut)
print(value)
