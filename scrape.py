import sys		
import xml.dom.minidom					
document = xml.dom.minidom.parse(sys.argv[1])		
tableElements = document.getElementsByTagName('table')	
rowCounter=0
# WORK ON ELEMENTS OF THE THIRD TABLE OF THE DOCUMENT
for tr in tableElements[2].getElementsByTagName('tr'):	
	data = []	
	#IF FIRST ROW IS BEING OBSERVED					
	if rowCounter == 0:	
		data.append("exchange")
		data.append("symbol")
		data.append("company")	
		data.append("volume")	
		data.append("price")
		data.append("change")
		print(', '.join(data))
		rowCounter=rowCounter+1
		continue			
	length = tr.getElementsByTagName('td').length
	#DON'T TAKE RATING AND %CHANGE INTO ACCOUNT		
	for i in range(1, length-1):											
		for td in tr.getElementsByTagName('td')[i].childNodes:
			#IF WE FOUND STOCK NAME "meaning <td> tag contains <a> inside it"
			if td.hasChildNodes():
				if td.childNodes[0].nodeType == td.childNodes[0].TEXT_NODE:	
					if td.childNodes[0].nodeValue != '\n':
						compName=td.childNodes[0].nodeValue.replace('\n','')
						#GET THE SYMBOL OF THE COMPANY "find values between ()"
						symbol = compName[compName.find("(")+1:compName.find(")")]	
						#GET THE COMPANY NAME WITHOUT THE SYMBOL
						updatedCompanyName=compName[:compName.find("(")-1]
						#APPEND NASDAQ STOCK MARKET NAME TO THE TABLE		
						data.append("Nasdaq")		
						#APPEND THE SYMBOL				
						data.append(symbol)		
						#APPEND THE COMPANY NAME				
						data.append(updatedCompanyName)					
			#IF THE NODE HAS NO CHILD "meaning <td> tag has no child"	
			elif not td.hasChildNodes():						
				if td.nodeType == td.TEXT_NODE:
					if td.nodeValue != '\n':
						value = td.nodeValue.replace(',','')
						data.append(value)
	print(', '.join(data))
