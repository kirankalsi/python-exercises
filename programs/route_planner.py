'''
peaks = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
route = ""
counter = 0
num_of_peaks = len(peaks) - 1
while counter < num_of_peaks:
    if peaks[counter] < peaks[counter + 1]:
        route = route + str(peaks[counter]) + " "
    counter += 1

print("Best Route:", route)
'''
'''
peaks = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
route = []
counter = 0
num_of_peaks = len(peaks) - 1
while counter < num_of_peaks:
'''

def route_planner(peaks):
    peaks_list = peaks.split(" ")
    best_route = [peaks[0]]
    for peak in peaks_list:            
        if int(peak) > int(best_route[len(best_route) - 1]):
            best_route.append(peak)
    return best_route

print(route_planner("0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15"))