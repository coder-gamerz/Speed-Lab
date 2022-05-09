import speed-lab

while True:
    text = input('speed-lab ~ >')
    result, error = loon.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)

