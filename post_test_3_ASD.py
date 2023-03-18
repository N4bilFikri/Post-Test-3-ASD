class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_task(self, task):
        new_node = Node(task)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node
            
    def delete_task(self, task):
        curr_node = self.head
        if curr_node is not None and curr_node.data == task:
            self.head = curr_node.next
            curr_node = None
            return
        prev_node = None
        while curr_node is not None and curr_node.data != task:
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        prev_node.next = curr_node.next
        curr_node = None
        
    def mark_as_done(self, task):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == task:
                curr_node.data = 'DONE: ' + task
                return
            curr_node = curr_node.next
        
    def print_tasks(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

# contoh penggunaan LinkedList
my_list = LinkedList()

my_list.add_task('Membuat laporan keuangan')
my_list.add_task('Beli bahan makanan')
my_list.add_task('Ambil paket di kantor pos')
my_list.add_task('Kirim email ke klien')

print("Daftar tugas awal:")
my_list.print_tasks()

my_list.delete_task('Beli bahan makanan')
my_list.mark_as_done('Kirim email ke klien')

print("\nDaftar tugas setelah dihapus dan ditandai selesai:")
my_list.print_tasks()
