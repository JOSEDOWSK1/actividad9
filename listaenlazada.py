#include <iostream>

using namespace std;

class Node
{
  public:
  int data;
  Node* next;
  Node(){
    data=0;
    next=NULL;
  }
  Node(int d){
    data = d;
    next = NULL;
  }
  void print(){
    cout<<data;
    cout<<",";
  }
};
class List
{ public:
  Node* head;
  Node* end;
  List(){
    head = NULL;
    end = NULL;
  }
  ~List(){
    Node* n;
    while(head){
      n = head->next;
      delete head;
      head = n;
    }
  }
  void add(int d){
    Node* new_node = new Node(d);
    if(!head)
      head = new_node;
    else
      end->next = new_node;
    end = new_node;
  }
  void print(){
    for(Node* p=head;p;p = p->next)
      p->print();
    cout<<"\n";
  }
  void swap(Node* & ant,Node* & q){
    Node* temp = q->next;
    if (q == head){
      head = temp;
      q->next = temp->next;
      temp->next = q;
      q = head;}
    else{
	    ant->next = temp;
      q->next = temp->next;
      temp->next = q;
      q = temp;}
  }
};

int mayorque(int a, int b){
  if(a>b) return 1;
  return 0;
}
int menorque(int a, int b){
  if(a<b) return 1;
  return 0;
}
int comparar(int a, int b,int(*p)(int,int)){
  return p(a,b);
}
int absoluto(int a, int b,int(*p)(int,int)){
  a = abs(a);
  b = abs(b);
  return p(a,b);
}
void BubbleSort(List* A,int n, int(*p)(int,int,int(*)(int,int)),int(pComp)(int,int)){
  Node* ant = NULL;
  for(int i=0;i<n;i++){
    for(Node* q=A->head;q->next;q = q->next){
      if(q == A->head->next)//Segundo elemento
        ant = A->head;
      if(p(q->data,q->next->data,pComp))
        A->swap(ant,q);
      if(ant)
        ant=ant->next;
    }
  }
}
typedef int(*PF1)(int,int,int(*)(int,int));
typedef int(*PF2)(int,int);
int main() {
  const int dim1=2;const int dim2=5;
  List A;
  A.add(3);
  A.add(4);
  A.add(-9);
  A.add(12);
  A.add(-7);
  List B;
  B.add(5);
  B.add(7);
  B.add(9);
  B.add(2);
  B.add(4);
  List* vectores[dim1] ={&A,&B};
  List **pvectores = vectores;
  PF1 comparadores[2] = {comparar,absoluto};
  PF2 comparaciones[2] = {mayorque,menorque};
  PF1* ppff1 = comparadores;
  PF2* ppff2 = comparaciones;
  int op1[dim1]= {1,0};
  int op2[dim1]= {0,1};
  int* pop1 = op1; 
  int* pop2 = op2;  
  
  std::cout <<"Vectores Desordenados\n";
  for(List** p=vectores;p<vectores+dim1;p++){
    (*p)->print();
  }  
  for(int i =0; i <dim1; i++)
  { 
    BubbleSort(*pvectores,dim2, *(ppff1+*pop1),*(ppff2+*pop2));
    pop1++;
    pop2++;
    pvectores++;
  }
  std::cout <<"Vectores Ordenados\n";
  for(List** p=vectores;p<vectores+dim1;p++){
    (*p)->print();
  }
}
