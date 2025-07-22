from haversine import haversine, Unit
import itertools
from heapq import heappush, heappop


class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, distance, vertex):
        self.distance = distance
        self.vertex = vertex


def get_distance(vertex_from: str, vertex_to: str, poi_l_and_l_data: dict):
    return round(haversine(poi_l_and_l_data[vertex_to], poi_l_and_l_data[vertex_from]),4)


def dijkstra(graph, start, end):
    previous = {v: None for v in graph.adjacency_list.keys()}
    visited = {v: False for v in graph.adjacency_list.keys()}
    distances = {v: float("inf") for v in graph.adjacency_list.keys()}
    distances[start] = 0
    queue = PriorityQueue()
    queue.add_task(0, start)
    path = []
    while queue:
        removed_distance, removed = queue.pop_task()
        visited[removed] = True

        # this piece of code is not part of the video, but it's useful to print the final path and distance
        if removed is end:
            while previous[removed]:
                path.append(removed.value)
                removed = previous[removed]
            path.append(start.value)
            print(f"shortest distance to {end.value}: ", distances[end])
            print(f"path to {end.value}: ", path[::-1])
            return

        for edge in graph.adjacency_list[removed]:
            if visited[edge.vertex]:
                continue
            new_distance = removed_distance + edge.distance
            if new_distance < distances[edge.vertex]:
                distances[edge.vertex] = new_distance
                previous[edge.vertex] = removed
                queue.add_task(new_distance, edge.vertex)
    return


# slightly modified heapq implementation from https://docs.python.org/3/library/heapq.html
class PriorityQueue:
    def __init__(self):
        self.pq = []  # list of entries arranged in a heap
        self.entry_finder = {}  # mapping of tasks to entries
        self.counter = itertools.count()  # unique sequence count

    def __len__(self):
        return len(self.pq)

    def add_task(self, priority, task):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.update_priority(priority, task)
            return self
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def update_priority(self, priority, task):
        'Update the priority of a task in place'
        entry = self.entry_finder[task]
        count = next(self.counter)
        entry[0], entry[1] = priority, count

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heappop(self.pq)
            del self.entry_finder[task]
            return priority, task
        raise KeyError('pop from an empty priority queue')


def run_dijkstra(poi_hs_table: object, user_input_from: str, user_input_to: str) -> object:
    """ from user option to view menu descriptions """ 

    # Data
    poi_list = {    
        "Cardiff Castle": ["St John the Baptist Church","Animal Wall","Wales National War Memorial","Bute Park"],
        "Animal Wall": ["Cardiff Castle","St John the Baptist Church","Wales National War Memorial","Cardiff City Stadium"],
        "St John the Baptist Church": ["Cardiff Castle","Animal Wall","Bute Park"],
        "City Hall": ["Bute Park","Crowd Building (Old)","Principality Stadium Tours"],
        "Pierhead Building": ["Norwegian Church Arts Centre","Wales Millennium Centre"],
        "St Davids Hall": ["Principality Stadium Tours","Tommy Cooper Statue","Iantos Shrine"],
        "Iantos Shrine": ["St Davids Metropolitan Cathedral","Principality Stadium Tours","St Davids Hall","Wales Millennium Centre"],
        "Wales Millennium Centre": ["Techniquest (Science Centre)","Pierhead Building","Iantos Shrine","St Davids Metropolitan Cathedral"],
        "Norwegian Church Arts Centre": ["Cardiff Bay Barrage","Techniquest (Science Centre)","Pierhead Building"],
        "Principality Stadium": ["Iantos Shrine","St Davids Hall","City Hall","Victoria Park"],
        "Cardiff City Stadium": ["Animal Wall","National Museum Cardiff","Old Bishops Palace"],
        "Cardiff Bay Yacht Club": ["St. Lythans Burial Chamber","Cardiff Bay Wetlands Reserve","Cardiff Bay Barrage"],
        "Techniquest (Science Centre)": ["Cardiff Bay Barrage","Norwegian Church Arts Centre","Wales Millennium Centre"],
        "Principality Stadium Tours": ["Victoria Park","Iantos Shrine","St Davids Hall","City Hall"],
        "National Museum Cardiff": ["Cardiff City Stadium","Old Bishops Palace","Roath Park"],
        "St Fagans Castle": ["Insole Court","Victoria Park","Tinkinswood Burial Chamber","St. Lythans Burial Chamber"],
        "Castell Coch": ["Llandaff Cathedral","Insole Court","Nantgarw China Works & Museum"],
        "Caerphilly Castle": ["Nantgarw China Works & Museum","Cefn Onn Park"],
        "Llandaff Cathedral": ["Castell Coch","Victoria Park","Insole Court"],
        "St Davids Metropolitan Cathedral": ["Wales Millennium Centre","Iantos Shrine","Tommy Cooper Statue"],
        "Bute Park": ["City Hall","Wales National War Memorial","Cardiff Castle","St John the Baptist Church"],
        "Roath Park": ["Old Bishops Palace","National Museum Cardiff","Cefn Onn Park"],
        "Victoria Park": ["St Fagans Castle","Insole Court","Llandaff Cathedral","Principality Stadium Tours"],
        "Cefn Onn Park": ["Roath Park","Caerphilly Castle","Nantgarw China Works & Museum"],
        "Cardiff Bay Wetlands Reserve": ["Cardiff Bay Yacht Club","Cardiff Bay Barrage"],
        "Cardiff Bay Barrage": ["Cardiff Bay Yacht Club","Cardiff Bay Wetlands Reserve","Techniquest (Science Centre)","Norwegian Church Arts Centre"],
        "Wales National War Memorial": ["Crowd Building (Old)","Bute Park","Cardiff Castle","Animal Wall"],
        "Crowd Building (Old)": ["Wales National War Memorial","City Hall","Tommy Cooper Statue"],
        "St. Lythans Burial Chamber": ["Cardiff Bay Yacht Club","St Fagans Castle","Barry Castle","Tinkinswood Burial Chamber"],
        "Tinkinswood Burial Chamber": ["St. Lythans Burial Chamber","St Fagans Castle","Barry Castle"],
        "Nantgarw China Works & Museum": ["Castell Coch","Caerphilly Castle","Cefn Onn Park"],
        "Tommy Cooper Statue": ["St Davids Hall","St Davids Metropolitan Cathedral","Crowd Building (Old)"],
        "Old Bishops Palace": ["Cardiff City Stadium","National Museum Cardiff","Roath Park"],
        "Insole Court": ["St Fagans Castle","Victoria Park","Llandaff Cathedral","Castell Coch"],
        "Barry Castle": ["St. Lythans Burial Chamber","Tinkinswood Burial Chamber"]
    }

    poi_l_and_l_data = {
        "Cardiff_Castle":  [51.482208, -3.181301],
        "Animal_Wall":  [51.4825, -3.1820],
        "St_John_the_Baptist_Church":  [51.4820, -3.1815],
        "City_Hall":  [51.4810, -3.1790],
        "Pierhead_Building":  [51.4680, -3.1680],
        "St_Davids_Hall":  [51.4807, -3.1780],
        "Iantos_Shrine":  [51.4795, -3.1760],
        "Wales_Millennium_Centre":  [51.4686, -3.1727],
        "Norwegian_Church_Arts_Centre":  [51.4678, -3.1688],
        "Principality_Stadium":  [51.478146, -3.183414],
        "Cardiff_City_Stadium":  [51.4845, -3.1820],
        "Cardiff_Bay_Yacht_Club":  [51.448265, -3.175035],
        "Techniquest_Science_Centre":  [51.4670, -3.1720],
        "Principality_Stadium_Tours":  [51.478146, -3.183414],
        "National_Museum_Cardiff":  [51.4870, -3.1780],
        "St_Fagans_Castle":  [51.4864, -3.2688],
        "Castell_Coch":  [51.5190, -3.2960],
        "Caerphilly_Castle":  [51.5790, -3.2220],
        "Llandaff_Cathedral":  [51.4905, -3.2190],
        "St_Davids_Metropolitan_Cathedral":  [51.4785, -3.1735],
        "Bute_Park":  [51.4815, -3.1800],
        "Roath_Park":  [51.5070, -3.1540],
        "Victoria_Park":  [51.4825, -3.2050],
        "Cefn_Onn_Park":  [51.5360, -3.1660],
        "Cardiff_Bay_Wetlands_Reserve":  [51.4540, -3.1660],
        "Cardiff_Bay_Barrage":  [51.4640, -3.1670],
        "Wales_National_War_Memorial":  [51.4822, -3.1791],
        "Crowd_Building_Old":  [51.4820, -3.1780],
        "St_Lythans_Burial_Chamber":  [51.4220, -3.2530],
        "Tinkinswood_Burial_Chamber":  [51.4420, -3.2700],
        "Nantgarw_China_Works__Museum":  [51.5680, -3.2670],
        "Tommy_Cooper_Statue":  [51.4800, -3.1760],
        "Old_Bishops_Palace":  [51.4900, -3.1790],
        "Insole_Court":  [51.4820, -3.2140],
        "Barry_Castle":  [51.3990, -3.2760]
    }

    vertices = [
        Vertex("Cardiff_Castle"),
        Vertex("Animal_Wall"),
        Vertex("St_John_the_Baptist_Church"),
        Vertex("City_Hall"),
        Vertex("Pierhead_Building"),
        Vertex("St_Davids_Hall"),
        Vertex("Iantos_Shrine"),
        Vertex("Wales_Millennium_Centre"),
        Vertex("Norwegian_Church_Arts_Centre"),
        Vertex("Principality_Stadium"),
        Vertex("Cardiff_City_Stadium"),
        Vertex("Cardiff_Bay_Yacht_Club"),
        Vertex("Techniquest_Science_Centre"),
        Vertex("Principality_Stadium_Tours"),
        Vertex("National_Museum_Cardiff"),
        Vertex("St_Fagans_Castle"),
        Vertex("Castell_Coch"),
        Vertex("Caerphilly_Castle"),
        Vertex("Llandaff_Cathedral"),
        Vertex("St_Davids_Metropolitan_Cathedral"),
        Vertex("Bute_Park"),
        Vertex("Roath_Park"),
        Vertex("Victoria_Park"),
        Vertex("Cefn_Onn_Park"),
        Vertex("Cardiff_Bay_Wetlands_Reserve"),
        Vertex("Cardiff_Bay_Barrage"),
        Vertex("Wales_National_War_Memorial"),
        Vertex("Crowd_Building_Old"),
        Vertex("St_Lythans_Burial_Chamber"),
        Vertex("Tinkinswood_Burial_Chamber"),
        Vertex("Nantgarw_China_Works__Museum"),
        Vertex("Tommy_Cooper_Statue"),
        Vertex("Old_Bishops_Palace"),
        Vertex("Insole_Court"),
        Vertex("Barry_Castle")
    ]

    #vertices
    Cardiff_Castle,Animal_Wall,St_John_the_Baptist_Church,City_Hall,Pierhead_Building,St_Davids_Hall,Iantos_Shrine,Wales_Millennium_Centre,Norwegian_Church_Arts_Centre,Principality_Stadium,Cardiff_City_Stadium,Cardiff_Bay_Yacht_Club,Techniquest_Science_Centre,Principality_Stadium_Tours,National_Museum_Cardiff,St_Fagans_Castle,Castell_Coch,Caerphilly_Castle,Llandaff_Cathedral,St_Davids_Metropolitan_Cathedral,Bute_Park,Roath_Park,Victoria_Park,Cefn_Onn_Park,Cardiff_Bay_Wetlands_Reserve,Cardiff_Bay_Barrage,Wales_National_War_Memorial,Crowd_Building_Old,St_Lythans_Burial_Chamber,Tinkinswood_Burial_Chamber,Nantgarw_China_Works__Museum,Tommy_Cooper_Statue,Old_Bishops_Palace,Insole_Court,Barry_Castle  = vertices

    #graph poi links
    adj_list = {

        Cardiff_Castle: [Edge(get_distance("Cardiff_Castle","St_John_the_Baptist_Church",poi_l_and_l_data), St_John_the_Baptist_Church), Edge(get_distance("Cardiff_Castle","Animal_Wall",poi_l_and_l_data), Animal_Wall), Edge(get_distance("Cardiff_Castle","Wales_National_War_Memorial",poi_l_and_l_data), Wales_National_War_Memorial), Edge(get_distance("Cardiff_Castle","Bute_Park",poi_l_and_l_data), Bute_Park)],
        Animal_Wall: [Edge(get_distance("Animal_Wall","Cardiff_Castle",poi_l_and_l_data), Cardiff_Castle), Edge(get_distance("Animal_Wall","St_John_the_Baptist_Church",poi_l_and_l_data), St_John_the_Baptist_Church), Edge(get_distance("Animal_Wall","Wales_National_War_Memorial",poi_l_and_l_data), Wales_National_War_Memorial), Edge(get_distance("Animal_Wall","Cardiff_City_Stadium",poi_l_and_l_data), Cardiff_City_Stadium)],
        St_John_the_Baptist_Church: [Edge(get_distance("St_John_the_Baptist_Church","Cardiff_Castle",poi_l_and_l_data), Cardiff_Castle), Edge(get_distance("St_John_the_Baptist_Church","Animal_Wall",poi_l_and_l_data), Animal_Wall), Edge(get_distance("St_John_the_Baptist_Church","Bute_Park",poi_l_and_l_data), Bute_Park)],
        City_Hall: [Edge(get_distance("City_Hall","Bute_Park",poi_l_and_l_data), Bute_Park), Edge(get_distance("City_Hall","Crowd_Building_Old",poi_l_and_l_data), Crowd_Building_Old), Edge(get_distance("City_Hall","Principality_Stadium_Tours",poi_l_and_l_data), Principality_Stadium_Tours)],
        Pierhead_Building: [Edge(get_distance("Pierhead_Building","Norwegian_Church_Arts_Centre",poi_l_and_l_data), Norwegian_Church_Arts_Centre), Edge(get_distance("Pierhead_Building","Wales_Millennium_Centre",poi_l_and_l_data), Wales_Millennium_Centre)],
        St_Davids_Hall: [Edge(get_distance("St_Davids_Hall","Principality_Stadium_Tours",poi_l_and_l_data), Principality_Stadium_Tours), Edge(get_distance("St_Davids_Hall","Tommy_Cooper_Statue",poi_l_and_l_data), Tommy_Cooper_Statue), Edge(get_distance("St_Davids_Hall","Iantos_Shrine",poi_l_and_l_data), Iantos_Shrine)],
        Iantos_Shrine: [Edge(get_distance("Iantos_Shrine","St_Davids_Metropolitan_Cathedral",poi_l_and_l_data), St_Davids_Metropolitan_Cathedral), Edge(get_distance("Iantos_Shrine","Principality_Stadium_Tours",poi_l_and_l_data), Principality_Stadium_Tours), Edge(get_distance("Iantos_Shrine","St_Davids_Hall",poi_l_and_l_data), St_Davids_Hall), Edge(get_distance("Iantos_Shrine","Wales_Millennium_Centre",poi_l_and_l_data), Wales_Millennium_Centre)],
        Wales_Millennium_Centre: [Edge(get_distance("Wales_Millennium_Centre","Techniquest_Science_Centre",poi_l_and_l_data), Techniquest_Science_Centre), Edge(get_distance("Wales_Millennium_Centre","Pierhead_Building",poi_l_and_l_data), Pierhead_Building), Edge(get_distance("Wales_Millennium_Centre","Iantos_Shrine",poi_l_and_l_data), Iantos_Shrine), Edge(get_distance("Wales_Millennium_Centre","St_Davids_Metropolitan_Cathedral",poi_l_and_l_data), St_Davids_Metropolitan_Cathedral)],
        Norwegian_Church_Arts_Centre: [Edge(get_distance("Norwegian_Church_Arts_Centre","Cardiff_Bay_Barrage",poi_l_and_l_data), Cardiff_Bay_Barrage), Edge(get_distance("Norwegian_Church_Arts_Centre","Techniquest_Science_Centre",poi_l_and_l_data), Techniquest_Science_Centre), Edge(get_distance("Norwegian_Church_Arts_Centre","Pierhead_Building",poi_l_and_l_data), Pierhead_Building)],
        Principality_Stadium: [Edge(get_distance("Principality_Stadium","Iantos_Shrine",poi_l_and_l_data), Iantos_Shrine), Edge(get_distance("Principality_Stadium","St_Davids_Hall",poi_l_and_l_data), St_Davids_Hall), Edge(get_distance("Principality_Stadium","City_Hall",poi_l_and_l_data), City_Hall), Edge(get_distance("Principality_Stadium","Victoria_Park",poi_l_and_l_data), Victoria_Park)],
        Cardiff_City_Stadium: [Edge(get_distance("Cardiff_City_Stadium","Animal_Wall",poi_l_and_l_data), Animal_Wall), Edge(get_distance("Cardiff_City_Stadium","National_Museum_Cardiff",poi_l_and_l_data), National_Museum_Cardiff), Edge(get_distance("Cardiff_City_Stadium","Old_Bishops_Palace",poi_l_and_l_data), Old_Bishops_Palace)],
        Cardiff_Bay_Yacht_Club: [Edge(get_distance("Cardiff_Bay_Yacht_Club","St_Lythans_Burial_Chamber",poi_l_and_l_data), St_Lythans_Burial_Chamber), Edge(get_distance("Cardiff_Bay_Yacht_Club","Cardiff_Bay_Wetlands_Reserve",poi_l_and_l_data), Cardiff_Bay_Wetlands_Reserve), Edge(get_distance("Cardiff_Bay_Yacht_Club","Cardiff_Bay_Barrage",poi_l_and_l_data), Cardiff_Bay_Barrage)],
        Techniquest_Science_Centre: [Edge(get_distance("Techniquest_Science_Centre","Cardiff_Bay_Barrage",poi_l_and_l_data), Cardiff_Bay_Barrage), Edge(get_distance("Techniquest_Science_Centre","Norwegian_Church_Arts_Centre",poi_l_and_l_data), Norwegian_Church_Arts_Centre), Edge(get_distance("Techniquest_Science_Centre","Wales_Millennium_Centre",poi_l_and_l_data), Wales_Millennium_Centre)],
        Principality_Stadium_Tours: [Edge(get_distance("Principality_Stadium_Tours","Victoria_Park",poi_l_and_l_data), Victoria_Park), Edge(get_distance("Principality_Stadium_Tours","Iantos_Shrine",poi_l_and_l_data), Iantos_Shrine), Edge(get_distance("Principality_Stadium_Tours","St_Davids_Hall",poi_l_and_l_data), St_Davids_Hall), Edge(get_distance("Principality_Stadium_Tours","City_Hall",poi_l_and_l_data), City_Hall)],
        National_Museum_Cardiff: [Edge(get_distance("National_Museum_Cardiff","Cardiff_City_Stadium",poi_l_and_l_data), Cardiff_City_Stadium), Edge(get_distance("National_Museum_Cardiff","Old_Bishops_Palace",poi_l_and_l_data), Old_Bishops_Palace), Edge(get_distance("National_Museum_Cardiff","Roath_Park",poi_l_and_l_data), Roath_Park)],
        St_Fagans_Castle: [Edge(get_distance("St_Fagans_Castle","Insole_Court",poi_l_and_l_data), Insole_Court), Edge(get_distance("St_Fagans_Castle","Victoria_Park",poi_l_and_l_data), Victoria_Park), Edge(get_distance("St_Fagans_Castle","Tinkinswood_Burial_Chamber",poi_l_and_l_data), Tinkinswood_Burial_Chamber), Edge(get_distance("St_Fagans_Castle","St_Lythans_Burial_Chamber",poi_l_and_l_data), St_Lythans_Burial_Chamber)],
        Castell_Coch: [Edge(get_distance("Castell_Coch","Llandaff_Cathedral",poi_l_and_l_data), Llandaff_Cathedral), Edge(get_distance("Castell_Coch","Insole_Court",poi_l_and_l_data), Insole_Court), Edge(get_distance("Castell_Coch","Nantgarw_China_Works__Museum",poi_l_and_l_data), Nantgarw_China_Works__Museum)],
        Caerphilly_Castle: [Edge(get_distance("Caerphilly_Castle","Nantgarw_China_Works__Museum",poi_l_and_l_data), Nantgarw_China_Works__Museum), Edge(get_distance("Caerphilly_Castle","Cefn_Onn_Park",poi_l_and_l_data), Cefn_Onn_Park)],
        Llandaff_Cathedral: [Edge(get_distance("Llandaff_Cathedral","Castell_Coch",poi_l_and_l_data), Castell_Coch), Edge(get_distance("Llandaff_Cathedral","Victoria_Park",poi_l_and_l_data), Victoria_Park), Edge(get_distance("Llandaff_Cathedral","Insole_Court",poi_l_and_l_data), Insole_Court)],
        St_Davids_Metropolitan_Cathedral: [Edge(get_distance("St_Davids_Metropolitan_Cathedral","Wales_Millennium_Centre",poi_l_and_l_data), Wales_Millennium_Centre), Edge(get_distance("St_Davids_Metropolitan_Cathedral","Iantos_Shrine",poi_l_and_l_data), Iantos_Shrine), Edge(get_distance("St_Davids_Metropolitan_Cathedral","Tommy_Cooper_Statue",poi_l_and_l_data), Tommy_Cooper_Statue)],
        Bute_Park: [Edge(get_distance("Bute_Park","City_Hall",poi_l_and_l_data), City_Hall), Edge(get_distance("Bute_Park","Wales_National_War_Memorial",poi_l_and_l_data), Wales_National_War_Memorial), Edge(get_distance("Bute_Park","Cardiff_Castle",poi_l_and_l_data), Cardiff_Castle), Edge(get_distance("Bute_Park","St_John_the_Baptist_Church",poi_l_and_l_data), St_John_the_Baptist_Church)],
        Roath_Park: [Edge(get_distance("Roath_Park","Old_Bishops_Palace",poi_l_and_l_data), Old_Bishops_Palace), Edge(get_distance("Roath_Park","National_Museum_Cardiff",poi_l_and_l_data), National_Museum_Cardiff), Edge(get_distance("Roath_Park","Cefn_Onn_Park",poi_l_and_l_data), Cefn_Onn_Park)],
        Victoria_Park: [Edge(get_distance("Victoria_Park","St_Fagans_Castle",poi_l_and_l_data), St_Fagans_Castle), Edge(get_distance("Victoria_Park","Insole_Court",poi_l_and_l_data), Insole_Court), Edge(get_distance("Victoria_Park","Llandaff_Cathedral",poi_l_and_l_data), Llandaff_Cathedral), Edge(get_distance("Victoria_Park","Principality_Stadium_Tours",poi_l_and_l_data), Principality_Stadium_Tours)],
        Cefn_Onn_Park: [Edge(get_distance("Cefn_Onn_Park","Roath_Park",poi_l_and_l_data), Roath_Park), Edge(get_distance("Cefn_Onn_Park","Caerphilly_Castle",poi_l_and_l_data), Caerphilly_Castle), Edge(get_distance("Cefn_Onn_Park","Nantgarw_China_Works__Museum",poi_l_and_l_data), Nantgarw_China_Works__Museum)],
        Cardiff_Bay_Wetlands_Reserve: [Edge(get_distance("Cardiff_Bay_Wetlands_Reserve","Cardiff_Bay_Yacht_Club",poi_l_and_l_data), Cardiff_Bay_Yacht_Club), Edge(get_distance("Cardiff_Bay_Wetlands_Reserve","Cardiff_Bay_Barrage",poi_l_and_l_data), Cardiff_Bay_Barrage)],
        Cardiff_Bay_Barrage: [Edge(get_distance("Cardiff_Bay_Barrage","Cardiff_Bay_Yacht_Club",poi_l_and_l_data), Cardiff_Bay_Yacht_Club), Edge(get_distance("Cardiff_Bay_Barrage","Cardiff_Bay_Wetlands_Reserve",poi_l_and_l_data), Cardiff_Bay_Wetlands_Reserve), Edge(get_distance("Cardiff_Bay_Barrage","Techniquest_Science_Centre",poi_l_and_l_data), Techniquest_Science_Centre), Edge(get_distance("Cardiff_Bay_Barrage","Norwegian_Church_Arts_Centre",poi_l_and_l_data), Norwegian_Church_Arts_Centre)],
        Wales_National_War_Memorial: [Edge(get_distance("Wales_National_War_Memorial","Crowd_Building_Old",poi_l_and_l_data), Crowd_Building_Old), Edge(get_distance("Wales_National_War_Memorial","Bute_Park",poi_l_and_l_data), Bute_Park), Edge(get_distance("Wales_National_War_Memorial","Cardiff_Castle",poi_l_and_l_data), Cardiff_Castle), Edge(get_distance("Wales_National_War_Memorial","Animal_Wall",poi_l_and_l_data), Animal_Wall)],
        Crowd_Building_Old: [Edge(get_distance("Crowd_Building_Old","Wales_National_War_Memorial",poi_l_and_l_data), Wales_National_War_Memorial), Edge(get_distance("Crowd_Building_Old","City_Hall",poi_l_and_l_data), City_Hall), Edge(get_distance("Crowd_Building_Old","Tommy_Cooper_Statue",poi_l_and_l_data), Tommy_Cooper_Statue)],
        St_Lythans_Burial_Chamber: [Edge(get_distance("St_Lythans_Burial_Chamber","Cardiff_Bay_Yacht_Club",poi_l_and_l_data), Cardiff_Bay_Yacht_Club), Edge(get_distance("St_Lythans_Burial_Chamber","St_Fagans_Castle",poi_l_and_l_data), St_Fagans_Castle), Edge(get_distance("St_Lythans_Burial_Chamber","Barry_Castle",poi_l_and_l_data), Barry_Castle), Edge(get_distance("St_Lythans_Burial_Chamber","Tinkinswood_Burial_Chamber",poi_l_and_l_data), Tinkinswood_Burial_Chamber)],
        Tinkinswood_Burial_Chamber: [Edge(get_distance("Tinkinswood_Burial_Chamber","St_Lythans_Burial_Chamber",poi_l_and_l_data), St_Lythans_Burial_Chamber), Edge(get_distance("Tinkinswood_Burial_Chamber","St_Fagans_Castle",poi_l_and_l_data), St_Fagans_Castle), Edge(get_distance("Tinkinswood_Burial_Chamber","Barry_Castle",poi_l_and_l_data), Barry_Castle)],
        Nantgarw_China_Works__Museum: [Edge(get_distance("Nantgarw_China_Works__Museum","Castell_Coch",poi_l_and_l_data), Castell_Coch), Edge(get_distance("Nantgarw_China_Works__Museum","Caerphilly_Castle",poi_l_and_l_data), Caerphilly_Castle), Edge(get_distance("Nantgarw_China_Works__Museum","Cefn_Onn_Park",poi_l_and_l_data), Cefn_Onn_Park)],
        Tommy_Cooper_Statue: [Edge(get_distance("Tommy_Cooper_Statue","St_Davids_Hall",poi_l_and_l_data), St_Davids_Hall), Edge(get_distance("Tommy_Cooper_Statue","St_Davids_Metropolitan_Cathedral",poi_l_and_l_data), St_Davids_Metropolitan_Cathedral), Edge(get_distance("Tommy_Cooper_Statue","Crowd_Building_Old",poi_l_and_l_data), Crowd_Building_Old)],
        Old_Bishops_Palace: [Edge(get_distance("Old_Bishops_Palace","Cardiff_City_Stadium",poi_l_and_l_data), Cardiff_City_Stadium), Edge(get_distance("Old_Bishops_Palace","National_Museum_Cardiff",poi_l_and_l_data), National_Museum_Cardiff), Edge(get_distance("Old_Bishops_Palace","Roath_Park",poi_l_and_l_data), Roath_Park)],
        Insole_Court: [Edge(get_distance("Insole_Court","St_Fagans_Castle",poi_l_and_l_data), St_Fagans_Castle), Edge(get_distance("Insole_Court","Victoria_Park",poi_l_and_l_data), Victoria_Park), Edge(get_distance("Insole_Court","Llandaff_Cathedral",poi_l_and_l_data), Llandaff_Cathedral), Edge(get_distance("Insole_Court","Castell_Coch",poi_l_and_l_data), Castell_Coch)],
        Barry_Castle: [Edge(get_distance("Barry_Castle","St_Lythans_Burial_Chamber",poi_l_and_l_data), St_Lythans_Burial_Chamber), Edge(get_distance("Barry_Castle","Tinkinswood_Burial_Chamber",poi_l_and_l_data), Tinkinswood_Burial_Chamber)]

    }


    print(user_input_from, user_input_to)
    

    my_graph = Graph(adj_list)
    dijkstra(my_graph, start=user_input_from, end=user_input_to)
    #dijkstra(my_graph, start="Principality_Stadium", end="Animal_Wall")

    return poi_hs_table