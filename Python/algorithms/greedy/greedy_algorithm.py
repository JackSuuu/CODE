

# 首先，创建一个集合，其中包含要覆盖的州。
states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
# 可供选择的广播台清单
stations = {}
stations["one"] = {"id", "nv", "ut"}
stations["two"] = {"wa", "id", "mt"}
stations["three"] = {"or", "nv", "ca"}
stations["four"] = {"nv", "ut"}
stations["five"] = {"ca", "az"}

final_stations = set()


def cover(stations: dict):
    global states_needed, final_stations

    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        states_needed -= states_covered
        final_stations.add(best_station)
    return final_stations


print(cover(stations))

