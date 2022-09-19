#include "lists.h"

/**
	* check_cycle - Checks for a loop in a linked list
	*
	* @list: Pointer to list
	* Return: 1 if there's a linked list 0 if there's none
	*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;
	int value = 0;

	while ((slow && fast) && fast->next)
	{		
		slow = slow->next;

		if (fast->next || fast->next->next)	
			fast = fast->next->next;
		else
			break;

		if (slow== fast)
		{
			value = 1;
			break;
		}
	}
	return (value);
}
