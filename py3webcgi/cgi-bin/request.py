#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()

print('Content-type: text/html; charset=utf-8\n')

HTML = """
<html>
<head>
<style type="text/css">
    TABLE {
        width: 400px;
        border-collapse: collapse;
    }
    TD, TR {
        border: 1px solid black; 
    }
</style>
</head>
<body>
    <table>
        <tr><td colspan="2">Text</td></tr>
        <tr><td>%s</td><td>%s</td></tr>
    </table>
</body>
</html>
"""

def my_function(text1, text2):
    # some action

    print(HTML % (text1, text2))


text1 = form.getfirst('text1', 'no value')
text2 = form.getfirst('text2', 'no value')
my_function(text1, text2)

