#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the singly link list being passed.
 * Return: 0 if there is no cycle or 1 if there is one.
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
		return (0);

	fast = list;
	slow = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
