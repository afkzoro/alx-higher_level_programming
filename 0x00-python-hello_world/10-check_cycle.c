#include "lists.h"

/**
 * check_cycle - Checks for a loop in a linked list
 *
 * @list: Pointer to list
 * Return: 1 if there's a linked list 0 if there's none
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
