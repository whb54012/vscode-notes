
        let arr1=[1,2,3];
        let arr2=Array(1,2,3);
        let arr3=new Array(1,2,3);
//若内部元素只有一个，就用第一个，第二格和第三个有歧义，会将它输入的元素默认为此数组长度
//如let arr1=Array[1]会将它理解为长度为一的数组;
document.write(arr1);
//当输出直接写数组本身时，他是直接输出所有元素