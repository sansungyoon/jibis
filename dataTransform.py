#f=open("/home/sansungyoon/0108/0108_test.txt",'r')
f=open("C:\Users\ITLab_pc\Desktop\0113_svm,mfcc\0113_svm_mfcc\0113_svm_mfcc\\0113_mfcc.txt",'r')
data=f.read().split(",")
data=map(float,data)
f.close()
x=[]
X=[]
y=[]

for i in range(len(data)):
	if (i%17==16):
		y.append(data[i])
	else:
		x.append(data[i])

X=zip(x[0::16],x[1::16],x[2::16],x[3::16],x[4::16],x[5::16],x[6::16],x[7::16],x[8::16],x[9::16],x[10::16],x[11::16],x[12::16],x[13::16],x[14::16],x[15::16])
y=map(int,y)

print X
print y

