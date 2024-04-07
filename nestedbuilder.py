def makeindex(directory_name):
    print(".")
    os.chdir(directory_name)
    List = os.listdir() 
    omit = ['LICENSE', 'README.md', '.git', 'default.html', 'builder.py', 'nestedbuilder.py', 'index.html']
    List = [ i for i in List if i not in omit ]
    ListDir = [i for i in List if os.path.isdir(i)]
    Location = os.getcwd()
    Location = Location[17:]

    with open("index.html","w") as index :
        goback=f"<a href='../'>go back</a>\n"
        titleblock = f"<title> {Location} </title>\n"
        breadcrumb =f"<i> {Location} </i>\n</br>\n"
        heading = (Location.split("/"))[-1]
        headingblock = f"<h1>{heading}</h1>\n</br>\n"
        Hyperlinks = []
        for f in List :
            Hyperlinks.append(f"<a href='{f}' style='font-size: 1.25rem; line-height: 1.75rem; '>{f}</a>\n</br>\n")
        index.writelines(l+"\n" for l in lines[:5])
        index.writelines(titleblock)
        index.writelines(breadcrumb)
        index.writelines(goback)
        index.writelines(headingblock)
        index.writelines(l+"\n" for l in lines[5:7])
        index.writelines(Hyperlinks)
        index.writelines(l+"\n" for l in lines[7:])
        
        if len(ListDir) == 0 :
            os.chdir("../")
            return

        for i in ListDir :
            makeindex(i)
        os.chdir("../")
    return 

import os
print("Welcome to the Web Builder! \n Author: Prayag Yadav\n")
rootdirname = ((os.getcwd()).split("/"))[-1]

with open("default.html", "r") as template :
        lines = []
        for line in template :
            lines.append(line.strip())

os.chdir("../")
print("\n Building the index.html files.")
makeindex(rootdirname)
print("Completed building the index.html")
