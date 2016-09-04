/*
Problem: Infix notation to post fix notation(Reverse polish notation) and evaluate the post fix notation arithmetic.
Aglo:

1. start
2. scan the expression from left to right 
3. if it is an operand push it to the stack
4. if it is an operator pop the operand from the stack and perform operation
5. Store the output of step 4 back to the stack
6. Scan the expression untill all operands are consumed.
7. pop the stack and perform operation.
*/

# include <stdio.h>
# include <string.h>

// char stack
char stack[25];
int top = -1;

void push(char item){
	stack[++top] = item;
}
char pop(){
	return stack[top--];
}

// return precedence of operator
int precedence(char symbol){
	switch(symbol){
		case '+':
		case '-':
			return 2;
			break;
		case '*':
		case '/':
			return 3;
			break;
		case '^':
			return 4;
			break;
		case '(':
		case ')':
		case '#':
			return 1;
			break;
	}
}

// check whether the symbol is an operator?

int isOperator(char symbol){
	switch(symbol){
		case '+':
		case '-':
		case '*':
		case '/':
		case '(':
		case ')':
		case '^':
		case '#':
			return 1;
			break;
		default:
			return 0;
	}
}

// convert infix to postfix
void convert(char infix[], char postfix[]){
	int symbol, i , j =0;
	stack[++top] = '#';
	for(i=0;i<strlen(infix);i++){
		symbol = infix[i];
		if(isOperator(symbol) == 0){
			postfix[j] = symbol;
			j++;
		}else{
			if(symbol == '('){
				push(symbol);
			}else{
				if(symbol == ')'){
					while(stack[top]!='('){
						postfix[j] = pop();
						j++;
					}
					pop() ; // get the '(' out.
				}else{
					if(precedence(symbol) > precedence(stack[top])){
						push(symbol);

					}else{
						while(precedence(symbol)<=precedence(stack[top])) {
                     		postfix[j] = pop(); 
                     		j++; 
                  		}
                  		push(symbol);
					}
				}
			}
		}
	}
	while(stack[top] != '#') {
      postfix[j] = pop(); 
      j++; 
   	} 
	
   postfix[j]='\0';//null terminate string. 
}

// int stack

int stack_int[25];
int top_int  = -1;

void push_int(int item){
	stack_int[++top_int]= item;
}
int pop_int(){
	return stack_int[top_int--];
}

// evaluate post fix notation.

int evaluate(char *postfix){

   char ch;
   int i = 0,operand1,operand2;

   while( (ch = postfix[i++]) != '\0') {
	
      if(isdigit(ch)) {
	     push_int(ch-'0'); // Push the operand 
      }else {
         //Operator,pop two  operands 
         operand2 = pop_int();
         operand1 = pop_int();
			
         switch(ch) {
            case '+':
               push_int(operand1+operand2);
               break;
            case '-':
               push_int(operand1-operand2);
               break;
            case '*':
               push_int(operand1*operand2);
               break;
            case '/':
               push_int(operand1/operand2);
               break;
         }
      }
   }
	
   return stack_int[top_int];
}


int main(){
	char infix[25] = "1*(2+3)",postfix[25]; 
   	convert(infix,postfix); 
	
   	printf("Infix expression is: %s\n" , infix);
   	printf("Postfix expression is: %s\n" , postfix);
   	printf("Evaluated expression is: %d\n" , evaluate(postfix));

}