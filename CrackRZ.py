###################################
#####  Made by   Hous Unus   ######
###################################

print("""###################################
#####  Made by   Hous Unus   ######
###################################""")

import optparse
import zipfile
import rarfile
import Brute_force as BF

def crack_zip(file,tp,password):
        try :
            if(tp=="zip"):
                file.extractall(pwd= str.encode(password))
            else :
                file.extractall(pwd= password)
            print("Done")
            print("[+] Password Found " + password)
            return True
        except Exception as e:
                return False

def main():
    PG = BF.password_generator()
    parser = optparse.OptionParser("usage %programe " + "-t <fileformat> (zip or rar) -f <zipfileName> ")
    parser.add_option("-t",dest = "type",type="string",help = "'rar' or 'zip ")
    parser.add_option("-f",dest = "name",type="string",help = "Specify the file name ")
    (option ,arg)= parser.parse_args()
    if(option.name==None or option.type ==None):
        print(parser.usage)
        return 
    else:
        name = option.name
    if(option.type =="zip"):
        file = zipfile.ZipFile(name)
        
    elif(option.type == "rar"):
        file = file = rarfile.RarFile(name)
    else:
        print("Bad file Format")
        return
    print("[+] Cracking ...")
    while True :
        if(crack_zip(file,option.type,PG.GetPassword())):
            break

if __name__ == "__main__":
    main()
    
    
