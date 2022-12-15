def format_name(f_name,l_name):
    if f_name == "" or l_name=="":
        return
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"

print(format_name(input('What is your first Name? '), input('What is you Last Name? ')))