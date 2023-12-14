text = "X-DSPM-Confidence: 0.8475"

colon_position = text.find(":")
piece = text[colon_position+2:]
value = float(piece)
print(value)
