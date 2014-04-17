from __future__ import print_function


class Tower(object):
    def __init__(self, index):
        self.disks = []
        self.index = index

    def push(self, disk):
        """Add a disk"""
        self.disks.append(disk)

    def pop(self):
        """Remove the top disk"""
        return self.disks.pop()

    def move_top_to(self, tower):
        disk = self.pop()
        tower.push(disk)
        msg = 'Move disk "%d" from Tower %d to Tower %d'
        print(msg % (disk, self.index, tower.index))

    def move_disks(self, n, dest_tower, aux_tower):
        """Move the top n disks to `desk_tower` using `aux_tower`"""
        if n > 0:
            self.move_disks(n - 1, aux_tower, dest_tower)
            self.move_top_to(dest_tower)
            aux_tower.move_disks(n - 1, dest_tower, self)


def _test():
    t1 = Tower(1)
    t2 = Tower(2)
    t3 = Tower(3)
    n = 3
    disks = range(1, n + 1)
    disks.reverse()
    for d in disks:
        t1.push(d)
    t1.move_disks(n, t3, t2)
    print(t1.disks)
    print(t2.disks)
    print(t3.disks)


def _print():
    pass


if __name__ == '__main__':
    _test()
    _print()
