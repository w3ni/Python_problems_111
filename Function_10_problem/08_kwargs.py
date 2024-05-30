# **kwargs example

def kwargs(**kwargs):
    # print("Name :",name,"Power :", power)

    for key,value in kwargs.items():
        print(f'{key}: {value}')


kwargs(name = "Spiderman", power="spider")