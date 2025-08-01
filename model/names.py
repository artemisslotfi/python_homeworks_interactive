name_list=[]

while True:
    name=input("Enter your Name : ")

    if name=="exit":
        break

    name_list.append(name)
    more_than_5=list(filter(lambda x:len(x)>5,name_list))
    less_than_5=list(filter(lambda x:len(x)<5,name_list))

    print("اسامی بیشتر از 5 حرف:",more_than_5)
    print("اسامی کمتر از 5 حرف:", less_than_5)
    print("-" * 50)