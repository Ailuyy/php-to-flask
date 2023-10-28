def generate_table(size, color1, color2):
    table = '<table border align=center>'
    color = 'white'
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if i * j % 2 == 0:
                color = color1
            else:
                color = color2
            table += f"<td bgcolor={color}>{i * j}</td>"
        table += '</tr>'
    table += '</table>'
    return table