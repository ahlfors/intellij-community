f'{<error descr="Expression fragments inside f-strings cannot include line comments">#<error descr="'}' is expected"></error></error>'
<error descr="Missing closing quote [']">f'{<error descr="Expression fragments inside f-strings cannot include line comments">#<error descr="'}' is expected"></error></error></error>
f'{<error descr="Expression fragments inside f-strings cannot include line comments">#foo#</error>}'
f'{42:#}'
f'{42:{<error descr="Expression fragments inside f-strings cannot include line comments">#</error>}}'
f'{x <error descr="Expression fragments inside f-strings cannot include line comments">### foo</error>}'
f'{"###"}'