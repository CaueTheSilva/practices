for b in range(99, 0, -1):
    if b != 1:
        print("""{} bottles of beer on the wall, {} bottles of beer.
        Take one down and pass it around, {} bottles of beer on the wall.""".format(b, b, b - 1))
        print('\n')

    else:
        print("""1 bottle of beer on the wall, 1 bottle of beer.
        Take one down and pass it around, no more bottles of beer on the wall.

        No more bottles of beer on the wall, no more bottles of beer.
        Go to the store and buy some more, 99 bottles of beer on the wall.""")
        print('\n')
