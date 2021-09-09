#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: Address of the head
 * @number: where the new node should be added
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *new;

	new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);

	tmp = *head;
	new->n = number;
	/*Create space for node and assign the int value before anything*/
	if (tmp == NULL)
	{
		/*if the head don't exist make the new, the head*/
		new->next = tmp;
		*head = new;
		return (new);
	}

	while (tmp && tmp->next && tmp->next->n < number)
	{
		/**
		 * Mientras el node existe y el valor es menos que
		 * el number, move to the next node
		 */
		tmp = tmp->next;
	}
	/* When it reaches the number, "insert" the node*/
	new->next = tmp->next;
	tmp->next = new;
	return (new);
}
