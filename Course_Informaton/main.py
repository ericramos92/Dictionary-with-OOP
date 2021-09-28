import course_information
def main():
    obj = course_information.courseinformation('eric',1234)
    obj = course_information.courseinformation('jose',1234)
    obj.additemstodic()
    obj.additemstodic()
    dic = obj.getdictionary()
    print(dic)

main()
