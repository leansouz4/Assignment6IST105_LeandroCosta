import sys
import cgi

def process_data(values):
    try:
        numbers = [float(value) for value in values]
    except ValueError:
        return "<p>Error: All inputs must be numeric.</p>"
    
    if any(num < 0 for num in numbers):
        return "<p>Warning: Some values are negative.</p>"
    
    average = sum(numbers) / len(numbers)
    
    positive_count = sum(1 for num in numbers if num > 0)
    is_even = "even" if positive_count % 2 == 0 else "odd"
    
    greater_than_10 = sorted([num for num in numbers if num > 10])
    
    return f"""
    <h2>Results:</h2>
    <p>Original Values: {', '.join(map(str, numbers))}</p>
    <p>Sorted Values (greater than 10): {', '.join(map(str, greater_than_10))}</p>
    <p>Average: {average}</p>
    <p>Positive count is {is_even}</p>
    """


form = cgi.FieldStorage()
values = [form.getvalue(param, "") for param in ["a", "b", "c", "d", "e"]]
print("Content-type: text/html\n")
print(process_data(values))
