#include<stdio.h>
#include<stdlib.h>
typedef struct{
	int b;
	struct note * p;
}note;
 note*creture(int a){
	note*pe=(note*)malloc(sizeof(note));
	pe->b=a;
	pe->p=NULL;
	return pe;}
/*int main(){
	note*p1=creture(1);
	note*p2=creture(2);
	note*p3=creture(3);
	note*p4=creture(4);
	p1->p=p2;
	p2->p=p3;
	p3->p=p4;
	note*p5=p1;*/
/*void pon(note**p,int d){
	note*pc=creture(d);
	if(*p==NULL) {*p=pc;
	printf("0");}
	else {pc->p=*p;
	*p=pc;
	printf("1");}}
	void text(){
		note*pa=NULL;
	pon(&pa,1);
	pon(&pa,2);
	pon(&pa,3);
	while(pa!=NULL){
		printf("%d",pa->b);
		pa=pa->p;}
	}*/
	void pon(note**p,int d){
		note*pc=creture(d);
		if(*p==NULL) *p=pc;
		else {
			note*pd;
			pd=*p;
			while(pd->p!=NULL){
				pd=pd->p;
			}pd->p=pc;
		}
	}
	void text1(){
		note*pa=NULL;
		pon(&pa,1); 
		pon(&pa,2);
		pon(&pa,3);
		while(pa!=NULL){
		printf("%d",pa->b);
		pa=pa->p;}
	}
/*void pons(note**p){
	note*pc=*p;
	note*pd=NULL; 
	if(pc->b!=2){
		pd=pc;
		pc=pc->p;
	}pd->p=pc->p;
	free(pc);}*/
void pons(note**p){
	note*pc=*p;
	note*pd=NULL;
	if(pc->b!=2){
		pd=pc;
		pc=pc->p;
	}pd->p=pc->p;}//pd->p==pc?
void text2(){
	note*pa=NULL;
		pon(&pa,1); 
		pon(&pa,2);
		pon(&pa,3);
		/*while(pa!=NULL){
		printf("%d",pa->b);
		pa=pa->p;}*/	
		pons(&pa);
		while(pa!=NULL){
		printf("%d",pa->b);
		pa=pa->p;}
}
int main(){
//	text();
//	text1(); 
text2(); 
	return 0;	 
}