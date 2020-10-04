import os 
import sys
import shutil

y= "caminhos dos arquivos que deseja mover"
x = os.listdir(y)
lista = os.listdir('Caminho de onde estão as pastas dos arquivos')

#loop para ver cada arquivo se ja existe uma pasta corespondente a seu tipo e mover ele e se não existe criar uma e depois mover ele
for i in x:
	if os.path.isdir(y+i) == False:
		local = i.rfind(".")

		if i[local+1:] in lista :
				shutil.move(y+i,y+i[local+1:])
		else:
				os.mkdir(y+i[local+1:])
				shutil.move(y+i,y+i[local+1:])
				lista.append(i[local+1:])
	else:
		continue
