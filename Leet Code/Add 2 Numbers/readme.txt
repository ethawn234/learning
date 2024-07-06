Pre-reqs:

1. Understand the Number system (base 10, binary, etc)

    - Understanding the number system (decimal or base 10 for AddTwoNumbers)
        leads to a better understanding of how to construct the carry over 
        amount after summing the total values at both linked list nodes (l1.val + l2.val).

        - 


2. Understanding the problem statement constraints:

    - Limiting node values to 0-9 indicates I am working with base10 number system
    
    - the maximum number of nodes - this would be an edge case thing to account for like
        will I run into OOM errors with my implementation?

    - Node values come in reverse-order which makes constructing the output linked list easier
    since I'm starting with the right-most significant digit.

        - Why does this make it easier? It makes it easier to calculate the carry over amount


3. Understand Linked Lists:

    - Linked Lists are traversed a bit differently than lists and dicts because of their structure.

        - The data structure allows constant time or o1 time insertion/deletion. This is due
        to the fact that nodes in a linked list are connected by the next field, which is defined
        as part of the schema.

            - This also means location in memory does not matter. Data in a linked list need not be
                contiguous.

        - By knowing the above details about linked lists, I can construct a while loop that iterates
            until the given linked list(s) `next` field is None.


4. Chunk the problem:

    - Chunking in this case will entail breaking down the problem by new concepts:

        1. Linked Lists - not really new to me but good to refresh
        2. Building applicable logical statements
            - for when/where/how long to iterate the given linked lists
                1. when: l1 and l2 are not None
                2. where:
                    - Function Input: starting from l1[0] and l2[0]
                    - Function Output: starting from a head node's `next`
                        - I think this part is due to variable scoping. I cannot keep a tracking variable
                            inside the while loop.
                3. how: by accounting for all constraints.

        3. Floor Division - I was more concerned with not how the floor division works, but how it applies
            to this problem. Once I understood how the carry over value worked, the reason for floor division
            became clear.

            - Floor Division can be done `Math.floor()` or `//`. This returns the number of times the divisor
                can go into the dividend.

                    9 // 10 = 0: 10 cannot go into 9 any times, so returns 0
                    11 // 10 = 1: 10 can go into 11 once, so returns 1

                - Floor Division returns the value that cannot be added to the current node's total due to
                    our Number system constraint, which is that all nodes are 0-9.

                    This value represents how much to add to the next place in the base10 system.

                    Since we get the linked list in reverse order, we start on the right-most sig digits,
                    which makes calculating the carry over easier.

             