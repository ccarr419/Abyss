import os
import time
def main():
	while True:
		update()
		time.sleep(60*5)
	
def update():
	cmd = "git pull"
	os.system(cmd)

if __name__ == "__main__":
	main()