import subprocess
if __name__ == '__main__':
#command line args along with error capture on failure with check true
      s = subprocess.run('behave --no-capture',shell=True, check=True)