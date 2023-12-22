#include <stdio.h>
#include <stdlib.h>

// Definition of the node
typedef struct node
{
  int number;
  struct node *next;
} node;

// Function prototypes
void reverse(node **head);
void printList(node *head);
void freeList(node *head);

void addNode(node **head, int number) {
  node *new_node = malloc(sizeof(node));
  new_node->number = number;
  new_node->next = *head;
  *head = new_node;
}

int main(void) {
  node *head = NULL;
  
  // Add nodes to the list
  addNode(&head, 3);
  addNode(&head, 2);
  addNode(&head, 1);
  
  // Print the original list
  printf("Original List:\n");
  printList(head);
  
  // Call the reverse function - Uncomment to check
  // reverse(&head);
  // printf("Reversed List:\n");  
  // printList(head);
  
  // Free the memory
  freeList(head);
  
  return 0;
}

void reverse(node **head) {
  // Your code here
}

void printList(node *head) {
  node *temp = head;
  while (temp != NULL) {
    printf("%d ", temp->number);
    temp = temp->next;
  }
  printf("\n");
}

void freeList(node *head) {
  node *temp;
  while (head != NULL) {
    temp = head;
    head = head->next;
    free(temp);
  }
}



