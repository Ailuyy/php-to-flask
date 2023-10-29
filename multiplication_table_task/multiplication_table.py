def generate_table(size, color1, color2, with_border):
    table = f"<table{' border' if with_border else ''} align='center'>"
    colors = [color1, color2]
    for i in range(1, size + 1):
        table += '<tr>'
        for j in range(1, size + 1):
            color_index = (i * j) % 2
            table += f'<td bgcolor={colors[color_index]}>{i * j}</td>'
        table += '</tr>'
    table += '</table>'
    return table