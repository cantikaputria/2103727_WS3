# search.py
# ---------------
# Created by Yaya Wihardi (yayawihardi@upi.edu) on 15/03/2020

# Fungsi search harus me-return path.
# Path berupa list tuples dengan format (row, col)
# Path merupakan urutan states menuju goal.
# maze merupakan object dari Maze yang merepresentasikan keadaan lingkungan
# beberapa method dari maze yang dapat digunakan:

# getStart() : return tuple (row, col) -> mendapatkan initial state
# getObjectives() : return list of tuple [(row1, col1), (row2, col2) ...] -> mendapatkan list goal state
# getNeighbors(row, col) : input posisi, return list of tuple [(row1, col1), (row2, col2) ...]
#                          -> mendapatkan list tetangga yg mungkin (expand/sucessor functiom)
# isObjective(row, col) : return true/false -> goal test function

import queue

# bfs adding last node twice
def search(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    num_states_explored = 0  # jumlah state yang akan dikunjungi
    start = maze.getStart()  # start dimulai dari intial state yang merupakan kelas di file maze.py
    q = queue.Queue()  # membuat variabel fringe yaitu q dengan menggunakan bfs sehingga kodenya queue.Queue
    q.put(start)  # memasukkan node awal ke variabel q

    # membuat tiga variabel yang dibutuhkan
    visited = {}  # variabel penampung posisi yang pernah dikunjungi
    predecessors = {}  # parrent node
    predecessors[start] = None  # mengisi parent start dengan node

    while (not q.empty()):  # memproses dan menjalankan selama fringe tidak kosong

        num_states_explored += 1  # state yang pernah dikunjungi ditambah 1

        first = q.get()  # node saat ini
        current_pred = first  # membuat variabel current untuk menyimpan titik awal
        visited[first] = 1  # inisialisasi node saat ini menjadi true
        neighbors = maze.getNeighbors(first[0], first[1])

        for neighbor in neighbors:
            # jika tetangganya belum dikunjungi
            if (not neighbor in visited):  # koordinat tuple atau (x,y)
                # set parent dan childnya
                predecessors[neighbor] = current_pred
                visited[neighbor] = 1  # menandai state menjadi true
                q.put(neighbor)  # menginput neighbor ke fringe

    goal = maze.getObjectives()[0]  # untuk mendapatkan finish
    path = []  # membuat tuple untuk menyimpan rute yang benar
    path.append(goal)  # memasukkan goal yang diinginkan
    current = goal # posisi saat ini adalah goal

    # memproses dan menjalankan dari goal selama currentnya bukan start
    while (current != start):
        path.append(predecessors[current])
        current = predecessors[current]

    path.append(start)
    path.reverse()  # dikarenakan append nya dari goal, maka kita reverse
    print(path)  # print pathnya
    return path  # mengembalikan nilai path