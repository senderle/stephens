from linkedlist import LinkedList

def make_loop(ll, loop_ix):
    i = 0
    target_node = ll.sentinel.next_node
    while i < loop_ix:
        target_node = target_node.next_node
        i += 1

    tail_node = target_node
    while tail_node.next_node is not None:
        tail_node = tail_node.next_node

    tail_node.next_node = target_node

def tortoise_hare(ll):
    if (ll.sentinel.next_node is None or
            ll.sentinel.next_node.next_node is None or
            ll.sentinel.next_node.next_node.next_node is None):
        print('No loop!')
        return

    tort = ll.sentinel.next_node.next_node  # index 1
    hare = ll.sentinel.next_node.next_node.next_node  # index 2

    while tort is not hare:
        if hare is None:
            print('No loop!')
            return
        tort = tort.next_node
        hare = hare.next_node.next_node

    tort = ll.sentinel.next_node  # index 0
    i = 0
    while tort is not hare:
        tort = tort.next_node
        hare = hare.next_node
        i += 1

    print('Index of loop: {}'.format(i))

    loop_size = 1
    tort = tort.next_node
    while tort is not hare:
        tort = tort.next_node
        loop_size += 1

    print('Size of loop: {}'.format(loop_size))
    print('Total size {}:'.format(loop_size + i))

def test0():
    ll = LinkedList()
    for x in range(10):
        ll.push_first(x)

    ll.print_list()

def test1(ll_len=10, ll_loop=5):
    ll = LinkedList()
    for x in range(ll_len):
        ll.push_first(x)

    make_loop(ll, ll_loop)

    print('ll_len = {}'.format(ll_len))
    print('ll_loop = {}'.format(ll_loop))

    tortoise_hare(ll)

    print()
    print('Testing loopless list...')

    ll = LinkedList()
    for x in range(ll_len):
        ll.push_first(x)

    tortoise_hare(ll)

if __name__ == '__main__':
    x = 1
    for y in range(x):
        test1(x, y)
        print()

    print()
    print('Testing empty list...')
    ll = LinkedList()
    tortoise_hare(ll)
