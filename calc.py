def calculator_app(a,b):
  try:
    arr = []
    result = a+b
    arr.append(result)
    result = a-b
    arr.append(result)
    result = a*b
    arr.append(result)
    try:
      result = a/b
    except ZeroDivisionError:
      arr.append("zero div error")
      return arr
    arr.append(result)
    return arr
  except TypeError:
    arr.append("either a or b is not a num")
    return arr