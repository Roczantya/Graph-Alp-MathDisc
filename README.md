# Implementasi Graf dalam Python
Ini adalah implementasi graf terarah (DiGraph) menggunakan pustaka networkx dalam Python. Kelas Graf mendukung berbagai operasi graf seperti menambahkan node dan edge, memvisualisasikan graf, menghitung jalur terpendek dan terpanjang, serta mendeteksi siklus.

## Persyaratan
Untuk menjalankan kode ini, Anda perlu menginstal pustaka Python berikut:
* Python 3.x
* `networkx` (untuk pembuatan dan operasi graf)
* `matplotlib` (untuk visualisasi graf)
  
Instal pustaka yang diperlukan dengan pip:
```
pip install networkx matplotlib
```

## Gambaran Kelas
#### Kelas `Graf`
  Kelas Graf merepresentasikan graf terarah dengan berbagai metode untuk operasi graf. Kelas ini menggunakan networkx.DiGraph untuk representasi graf internal.

## Metode
* `add_node(node)`: Menambahkan node ke dalam graf.
* `add_edge(source, target, weight)`: Menambahkan edge terarah antara dua node dengan bobot tertentu.
* `visualize_graph()`: Memvisualisasikan keseluruhan graf.
* `shortest_path(start, end)`: Mengembalikan jalur terpendek antara dua node menggunakan algoritma Dijkstra.
* `visual_shortest_path(start, end)`: Memvisualisasikan jalur terpendek antara dua node dengan warna merah.
* `longest_path()`: Mengembalikan jalur terpanjang dalam Directed Acyclic Graph (DAG).
* `visual_longest_path()`: Memvisualisasikan jalur terpanjang dalam Directed Acyclic Graph.
* `node_degree(node)`: Mengembalikan derajat node (jumlah edge masuk dan keluar).
* `edge_weights()`: Mengembalikan dictionary yang berisi bobot semua edge dalam graf.
* `all_paths(start, end)`: Mengembalikan semua jalur sederhana antara dua node.
* `is_connected()`: Memeriksa apakah graf terhubung secara lemah.
* `connected_components()`: Mengembalikan komponen terhubung dalam graf.
* `graph_diameter()`: Mengembalikan diameter graf (hanya untuk graf yang terhubung kuat).
* `has_cycle()`: Memeriksa apakah graf mengandung siklus.
* `find_circuits()`: Mencari semua siklus sederhana (circuit) dalam graf.
* `length_of_circuits()`: Mengembalikan panjang setiap siklus dalam graf.
* `shortest_path_through_circuits()`: Mencari jalur terpendek yang melewati siklus.

## Contoh Penggunaan
Berikan contoh implementasinya dalam code python
```
# Membuat instance graf
graph = Graf()

# Menambahkan node
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)

# Menambahkan edge dengan bobot
graph.add_edge(1, 2, weight=4.5)
graph.add_edge(1, 3, weight=3.2)
graph.add_edge(2, 4, weight=2.7)
graph.add_edge(3, 4, weight=1.8)
graph.add_edge(1, 4, weight=6.7)
graph.add_edge(3, 5, weight=2.7)

# Memvisualisasikan graf
graph.visualize_graph()

# Mencari dan mencetak jalur terpendek dari node 1 ke node 5
print("Shortest Path:", graph.shortest_path(1, 5))
graph.visual_shortest_path(1, 5)

# Mencari dan mencetak jalur terpanjang dalam graf
print("Longest Path:", graph.longest_path())
graph.visual_longest_path()

# Operasi lainnya
print("Node Degree of 1:", graph.node_degree(1))
print("Edge Weights:", graph.edge_weights())
print("All Paths from 1 to 5:", graph.all_paths(1, 5))

# Konektivitas dan komponen graf
print("Is Graph Connected:", graph.is_connected())
print("Connected Components:", graph.connected_components())
print("Graph Diameter:", graph.graph_diameter())

# Memeriksa siklus dan mencari circuit
print("Has Cycle:", graph.has_cycle())
print("Circuits:", graph.find_circuits())
print("Length of Circuits:", graph.length_of_circuits())
print("Shortest Path Through Circuits:", graph.shortest_path_through_circuits())

```

## Visualisasi
Metode `visualize_graph`, `visual_shortest_path`, dan `visual_longest_path` menggunakan matplotlib untuk menampilkan representasi graf dan jalur-jalur yang relevan. Jalur terpendek akan ditampilkan dengan warna merah, sedangkan jalur terpanjang dengan warna biru.
