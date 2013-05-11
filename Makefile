test:
	rm test.log
	#now=$(date +"%m_%d_%Y")

	java -Xmx1000M -jar ISSVis.jar -exec "python test.py" -resolution 800 -show_power -show_longerons -rendering -view_beta 70 > result.log
	sh rename.sh	
	#-rendering
cleanlog:
	rm test.log
