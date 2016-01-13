
def dijkstraAlgoForShortestCost(graph,source,destination,visitedOnes=None,dist=None,predec=None):
    
    if(visitedOnes==None):
        visitedOnes=[]
    if(dist==None):
        dist={}
    if(predec==None):
        predec={}
    
    if source not in graph:
        raise TypeError('root of the shortest path tree is not there in the graph')
    if destination not in graph:
        raise TypeError('target of the shortest path is not there in the graph')    
    
    if source == destination:
        
        outputFile=open('Q1.out','a')
        path=[]
        pred_1=destination
        while pred_1 != None:
            path.append(predec)
            pred_1=predec.get(pred_1,None)
        print('Shortest path is : '+str(path)+" And The Cost="+str(dist[destination]))
        outputFile.write(str(dist[destination]))
        outputFile.write('\n')
        outputFile.close()
    else :     
        
        if not visitedOnes: 
            dist[source]=0
        
        for neighbours in graph[source] :
            if neighbours not in visitedOnes:
                new_distance = dist[source] + graph[source][neighbours]
                if new_distance < dist.get(neighbours,float('inf')):
                    dist[neighbours] = new_distance
                    predec[neighbours] = source
        
        visitedOnes.append(source)
        
        unvisited={}
        for k in graph:
            if k not in visitedOnes:
                unvisited[k] = dist.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        dijkstraAlgoForShortestCost(graph,x,destination,visitedOnes,dist,predec)
        x=0
        destination=0
        visitedOnes=[]
        dist={}
        predec={}
        return 0
        





f = open('Q1.in')
line = f.readline()
numberOfCities = f.readline()
d={}
citiesList=[]
for i in xrange(int(numberOfCities)):
    city = f.readline()
    citiesList.append(city)
    neigh = int(f.readline())
    l1=[]
    l2=[]
    for i in xrange(neigh):
        neigh_data = f.readline()
        spl = neigh_data.split()
        l1.append((spl[0]))
        l2.append(int(spl[1]))

    a=dict(zip(l1, l2))
    d.update({city:a})
    

#print a
print d
print citiesList

for i in xrange(int(numberOfCities)):
    d[str(i+1)]=d.pop(citiesList[i])

print d

clearOutputFileContent = open('Q1.out','w').close()

how_many = int(f.readline())
for i in xrange(how_many):
    nextLine = f.readline()
    source_dest = nextLine.split()
    
    for i in xrange(0,int(numberOfCities)):
        if((source_dest[0])== (citiesList[i].rstrip('\n'))):
            source = str(i+1)
    for i in xrange(1,int(numberOfCities)):
        if((source_dest[1])== (citiesList[i].rstrip('\n'))):
            target = str(i+1)

    print source
    print target

    dijkstraAlgoForShortestCost(d, source, target)
#print d


f.close()
    
    




