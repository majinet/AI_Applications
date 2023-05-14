import subprocess
if __name__ == '__main__':
#command line args along with error capture on failure with check true
      subprocess.run('coverage run -a -m behave',shell=True, check=True)
      subprocess.run('coverage xml',shell=True, check=True)
