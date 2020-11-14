def destCity(paths):
    starts = [x[0] for x in paths]
    destinations = [x[1] for x in paths]
    
    # for destination in destinations:
    #     if destination not in starts:
    #         return destination

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

destCity(paths)